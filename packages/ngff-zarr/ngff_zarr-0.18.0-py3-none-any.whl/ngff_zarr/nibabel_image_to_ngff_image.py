# SPDX-FileCopyrightText: Copyright (c) Fideus Labs LLC
# SPDX-License-Identifier: MIT
from typing import Dict, Tuple
import numpy as np

from .ngff_image import NgffImage
from .rfc4 import AnatomicalOrientation, AnatomicalOrientationValues


def decompose_affine_with_shear(affine):
    """Decompose affine transformation matrix into translation, scale, shear, and orientation."""
    # Affine top-left 3x3: linear (rotation, scale, shear), last column: translation
    matrix = affine[:3, :3]
    translation = affine[:3, 3]

    # Extract scale: norm of each column (preserves axis order)
    scale = np.linalg.norm(matrix, axis=0)

    # Normalize columns to remove scale for shear/orientation steps
    normed_matrix = matrix / scale

    # Shear extraction (per scipy/ITK/transforms3d conventions)
    shear_xy = np.dot(normed_matrix[:, 0], normed_matrix[:, 1])
    y_orth = normed_matrix[:, 1] - shear_xy * normed_matrix[:, 0]
    shear_y = np.linalg.norm(y_orth)
    shear_xz = np.dot(normed_matrix[:, 0], normed_matrix[:, 2])
    shear_yz = np.dot(normed_matrix[:, 1], normed_matrix[:, 2])
    z_orth = normed_matrix[:, 2] - shear_xz * normed_matrix[:, 0] - shear_yz * normed_matrix[:, 1]
    shear_z = np.linalg.norm(z_orth)

    shear = np.array([shear_xy, shear_xz, shear_yz])

    # Orthonormal rotation/orientation: Gram-Schmidt
    x = normed_matrix[:, 0]
    y = y_orth / shear_y
    z = z_orth / shear_z
    orientation = np.stack([x, y, z], axis=1)

    # Compose explicit scale and shear matrices
    scale_matrix = np.diag(scale)
    shear_matrix = np.array([[1, shear_xy, shear_xz],
                             [0,     1,   shear_yz],
                             [0,     0,      1    ]])

    # The "remaining affine" is shear * orientation
    remaining_affine_matrix = orientation @ shear_matrix

    return {
        "translation": translation,
        "scale": scale,                # pixel spacing in x,y,z order
        "shear": shear,                # [shear_xy, shear_xz, shear_yz]
        "orientation": orientation,    # rotation (orthonormal, columns x y z)
        "remaining_affine": remaining_affine_matrix
    }


def extract_spatial_metadata(img) -> Tuple[Dict[str, float], Dict[str, float], np.ndarray]:
    """Extract translation, scale, and orientation from NIfTI spatial metadata."""
    # Get the affine transformation matrix
    affine = img.affine

    # Use axis-preserving decomposition
    decomposition = decompose_affine_with_shear(affine)

    # Get image dimensions
    shape = img.shape

    # Create scale and translation dictionaries for spatial dimensions
    if len(shape) >= 3:
        # NIfTI uses RAS+ coordinate system, but array indexing is in reverse order
        # The affine maps from voxel coordinates (i,j,k) to world coordinates (x,y,z)
        # Array dimensions are typically (z,y,x) or (t,z,y,x)
        spatial_dims = ['x', 'y', 'z']  # World coordinate order
        scale_dict = {dim: float(decomposition["scale"][i]) for i, dim in enumerate(spatial_dims)}
        translation_dict = {dim: float(decomposition["translation"][i]) for i, dim in enumerate(spatial_dims)}

        # Add time dimension if 4D
        if len(shape) == 4:
            scale_dict['t'] = 1.0
            translation_dict['t'] = 0.0
        elif len(shape) == 5:
            scale_dict['c'] = 1.0
            translation_dict['c'] = 0.0
    else:
        raise ValueError(f"Image must have at least 3 dimensions, got {len(shape)}")

    return scale_dict, translation_dict, affine


def nibabel_image_to_ngff_image(
    nibabel_image,
    add_anatomical_orientation: bool = True,
) -> NgffImage:
    """Convert a nibabel image to an NgffImage, preserving spatial metadata.

    This function optimizes memory usage by checking the NIfTI scaling parameters:
    - If scl_slope=1.0 and scl_inter=0.0 (identity scaling), uses the raw dataobj
      to preserve the original data type and minimize memory usage
    - If scaling is required, uses get_fdata(dtype=np.float32) to balance
      memory usage and precision

    Args:
        nibabel_image: A nibabel image object
        add_anatomical_orientation: Whether to add anatomical orientation metadata.
                                   Only added if orientation matrix is identity
                                   (no rotation/shear).

    Returns:
        NgffImage with spatial metadata from the NIfTI file

    Note:
        The data is returned as a numpy array (not Dask) to maintain compatibility
        with the original implementation requirements.
    """
    # Get image data as numpy array (not Dask) with optimized memory usage
    # Check NIfTI scaling parameters for memory efficiency
    header = nibabel_image.header

    # Get scaling parameters using nibabel's methods which handle defaults correctly
    scl_slope = header.get('scl_slope')
    scl_inter = header.get('scl_inter')

    # nibabel treats slope of 0 or None as 1.0, and inter of None as 0.0
    if scl_slope is None or scl_slope == 0 or np.isnan(scl_slope):
        scl_slope = 1.0
    else:
        scl_slope = float(scl_slope)

    if scl_inter is None or np.isnan(scl_inter):
        scl_inter = 0.0
    else:
        scl_inter = float(scl_inter)

    # Use raw data if no scaling is needed (identity scaling)
    if scl_slope == 1.0 and scl_inter == 0.0:
        # No scaling needed, use raw data to preserve original dtype and memory
        data = np.asanyarray(nibabel_image.dataobj)
    else:
        # Scaling is needed, use float32 to balance memory and precision
        data = nibabel_image.get_fdata(dtype=np.float32)

    # Extract spatial metadata
    scale_dict, translation_dict, affine = extract_spatial_metadata(nibabel_image)

    # Determine dimension names based on image shape
    if len(data.shape) == 3:
        dims = ['x', 'y', 'z']
    elif len(data.shape) == 4:
        dims = ['x', 'y', 'z', 't']
    elif len(data.shape) == 5:
        dims = ['x', 'y', 'z', 't', 'c']
    else:
        raise ValueError(f"Unsupported number of dimensions: {len(data.shape)}")

    # Create anatomical orientations for spatial dimensions (RAS) only if matrices are identity
    axes_orientations = None
    if add_anatomical_orientation:
        from nibabel.orientations import io_orientation, ornt2axcodes
        labels = (
        (AnatomicalOrientationValues.right_to_left, AnatomicalOrientationValues.left_to_right),
        (AnatomicalOrientationValues.anterior_to_posterior, AnatomicalOrientationValues.posterior_to_anterior),
        (AnatomicalOrientationValues.superior_to_inferior, AnatomicalOrientationValues.inferior_to_superior),
        )
        orientation = ornt2axcodes(io_orientation(affine), labels)
        orientation = {dim: ornt for  dim, ornt in zip(['x', 'y', 'z'], orientation)}

        spatial_dims = [dim for dim in dims if dim in ['x', 'y', 'z']]
        axes_orientations = {dim: orientation[dim] for dim in spatial_dims}

    # Create NgffImage
    ngff_img = NgffImage(
        data=data,  # Keep as numpy array
        dims=dims,
        scale=scale_dict,
        translation=translation_dict,
        name="nibabel_converted_image",
        axes_orientations=axes_orientations
    )

    return ngff_img


def extract_omero_metadata_from_nibabel(nibabel_image):
    """Extract OMERO windowing metadata from a nibabel image's cal_min/cal_max headers.

    Args:
        nibabel_image: A nibabel image object

    Returns:
        Omero metadata if cal_min and cal_max are available and valid, None otherwise

    Note:
        This function creates OMERO windowing metadata from NIfTI cal_min and cal_max
        header values when both are not 0.0 and neither is NaN. The windowing applies
        to all channels in the image.
    """
    from .v04.zarr_metadata import Omero, OmeroChannel, OmeroWindow

    header = nibabel_image.header

    # Get calibration min/max values
    cal_min = header.get('cal_min')
    cal_max = header.get('cal_max')

    # Convert to float and handle None values
    if cal_min is None:
        cal_min = 0.0
    else:
        cal_min = float(cal_min)

    if cal_max is None:
        cal_max = 0.0
    else:
        cal_max = float(cal_max)

    # Check if both are not 0.0 and neither is NaN
    if not (cal_min == 0.0 and cal_max == 0.0) and not (np.isnan(cal_min) or np.isnan(cal_max)):
        # Determine data range for min/max values
        data_min = float(np.min(nibabel_image.dataobj))
        data_max = float(np.max(nibabel_image.dataobj))

        # Create OMERO windowing metadata
        # For simplicity, create one channel - users can extend this for multi-channel images
        omero_window = OmeroWindow(
            min=data_min,
            max=data_max,
            start=cal_min,
            end=cal_max
        )

        omero_channel = OmeroChannel(
            color="FFFFFF",  # Default to white
            window=omero_window,
            label=""  # Empty label by default
        )

        return Omero(channels=[omero_channel])

    return None
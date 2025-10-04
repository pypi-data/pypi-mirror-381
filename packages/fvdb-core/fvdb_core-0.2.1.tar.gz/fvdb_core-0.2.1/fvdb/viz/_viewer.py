# Copyright Contributors to the OpenVDB Project
# SPDX-License-Identifier: Apache-2.0
#
from typing import Sequence

import numpy as np
import torch

from .._Cpp import CameraView as CameraViewCpp
from .._Cpp import GaussianSplat3d as GaussianSplat3dCpp
from .._Cpp import GaussianSplat3dView as GaussianSplat3dViewCpp
from .._Cpp import Viewer as ViewerCpp
from ..gaussian_splatting import GaussianSplat3d
from ..types import NumericMaxRank1, NumericMaxRank3, to_Mat44fBatch, to_Vec3f
from ._camera_view import CameraView
from ._gaussian_splat_3d_view import GaussianSplat3dView


class Viewer:
    def __init__(self, ip_address: str = "127.0.0.1", port: int = 8888, verbose: bool = False):
        """
        Create a new `Viewer` running a server at the specified IP address and port.

        If there is already a viewer server running at the specified address and port,
        this will throw an Exception.

        Args:
            ip_address (str): The IP address to bind the viewer server to. Default is "127.0.0.1"
            port (int): The port to bind the viewer server to. Default is 8888.
        """
        if not isinstance(port, int) or port < 0 or port > 65535:
            raise ValueError(f"Port must be an integer between 0 and 65535, got {port}")

        self._impl = ViewerCpp(ip_address=ip_address, port=port, verbose=verbose)

    def add_gaussian_splat_3d(
        self,
        name: str,
        gaussian_splat_3d: GaussianSplat3d,
        tile_size: int = 16,
        min_radius_2d: float = 0.0,
        eps_2d: float = 0.3,
        antialias: bool = False,
        sh_degree_to_use: int = -1,
    ) -> GaussianSplat3dView:
        """
        Add a `GaussianSplat3d` to the viewer and return a view for it.

        Args:
            name (str): The name of the Gaussian splat 3D scene. This must be unique among all
                scenes added to the viewer.
            gaussian_splat_3d (GaussianSplat3d): The Gaussian splat 3D scene to add.
            tile_size (int): The tile size to use for rendering. Default is 16.
            min_radius_2d (float): The minimum radius in pixels to use when rendering splats. Default is 0.0.
            eps_2d (float): The epsilon value to use when rendering splats. Default is 0.3.
            antialias (bool): Whether to use antialiasing when rendering splats. Default is False.
            sh_degree_to_use (int): The degree of spherical harmonics to use when rendering colors.
                If -1, the maximum degree supported by the Gaussian splat 3D scene is used. Default is -1.

        Returns:
            GaussianSplat3dView: A view for the added Gaussian splat 3D scene.
        """
        gs_impl: GaussianSplat3dCpp = gaussian_splat_3d._impl
        view: GaussianSplat3dViewCpp = self._impl.add_gaussian_splat_3d(name=name, gaussian_splat_3d=gs_impl)
        view.tile_size = tile_size
        view.min_radius_2d = min_radius_2d
        view.eps_2d = eps_2d
        view.antialias = antialias
        if sh_degree_to_use >= 0:
            sh_degree_to_use = max(0, min(gaussian_splat_3d.sh_degree, sh_degree_to_use))
        else:
            sh_degree_to_use = gaussian_splat_3d.sh_degree
        view.sh_degree_to_use = sh_degree_to_use
        return GaussianSplat3dView(view, GaussianSplat3dView.__PRIVATE__)

    def add_camera_view(
        self,
        name: str,
        cam_to_world_matrices: NumericMaxRank3,
        projection_matrices: torch.Tensor | None = None,
        axis_length: float = 0.3,
        axis_thickness: float = 2.0,
        frustum_line_width: float = 2.0,
        frustum_scale: float = 1.0,
        frustum_color: Sequence[float] | np.ndarray = (0.5, 0.8, 0.3),
        frustum_near_plane: float = 0,
        frustum_far_plane: float = 0.5,
        enabled: bool = True,
    ) -> CameraView:
        """
        Add CameraView to the viewer and return a view.

        Args:
            name (str): The name of the camera view.
            cam_to_world_matrix (NumericMaxRank3): The 4x4 camera to world transformation matrix.
            projection_matrix (torch.Tensor | None): The 3x3 projection matrix.
            axis_length (float): The length of the axis lines in the camera frustum view.
            axis_thickness (float): The thickness (in world coordinates) of the axis lines in the camera frustum view.
            frustum_line_width (float): The width (in pixels) of the frustum lines in the camera frustum view.
            frstum_scale (float): The scale factor for the frustum size in the camera frustum view.
            frustum_color (Sequence[float] | np.ndarray): The color of the frustum lines as a sequence of three floats (R, G, B) in the range [0, 1].
            frustum_near_plane (float): The near clipping plane distance for the frustum in the camera frustum view.
            frustum_far_plane (float): The far clipping plane distance for the frustum in the camera frustum view.
            enabled (bool): If True, the camera view UI is enabled and the cameras will be rendered.
                If False, the camera view UI is disabled and the cameras will not be rendered.
        """

        if cam_to_world_matrices is None or projection_matrices is None:
            raise ValueError("Both camera_to_world_matrices and projection_matrices must be provided.")
        if len(frustum_color) != 3 or any(c < 0.0 or c > 1.0 for c in frustum_color):
            raise ValueError(f"Frustum color must be a sequence of three floats in [0, 1], got {frustum_color}")

        cam_to_world_matrices = to_Mat44fBatch(cam_to_world_matrices)

        view: CameraViewCpp = self._impl.add_camera_view(
            name, cam_to_world_matrices, projection_matrices, frustum_near_plane, frustum_far_plane
        )
        view.visible = enabled
        view.axis_length = axis_length
        view.axis_thickness = axis_thickness
        view.frustum_line_width = frustum_line_width
        view.frustum_scale = frustum_scale
        view.frustum_color = (float(frustum_color[0]), float(frustum_color[1]), float(frustum_color[2]))
        return CameraView(view, CameraView.__PRIVATE__)

    @property
    def camera_orbit_center(self) -> torch.Tensor:
        """
        Return center of the camera orbit in world coordinates.

        Returns:
            torch.Tensor: A tensor of shape (3,) representing the camera orbit center in world coordinates.
        """
        ox, oy, oz = self._impl.camera_orbit_center()
        return torch.tensor([ox, oy, oz], dtype=torch.float32)

    @camera_orbit_center.setter
    def camera_orbit_center(self, center: NumericMaxRank1):
        """
        Set the center of the camera orbit in world coordinates.

        Args:
            center (NumericMaxRank1): A tensor-like object of shape (3,) representing the camera orbit center in world coordinates.
        """
        center_vec3f = to_Vec3f(center).cpu().numpy().tolist()
        self._impl.set_camera_orbit_center(*center_vec3f)

    @property
    def camera_orbit_radius(self) -> float:
        """
        Return the radius of the camera orbit.

        Returns:
            float: The radius of the camera orbit.
        """
        return self._impl.camera_orbit_radius()

    @camera_orbit_radius.setter
    def camera_orbit_radius(self, radius: float):
        """
        Set the radius of the camera orbit.

        Args:
            radius (float): The radius of the camera orbit.
        """
        if radius <= 0.0:
            raise ValueError(f"Radius must be positive, got {radius}")
        self._impl.set_camera_orbit_radius(radius)

    @property
    def camera_orbit_direction(self) -> torch.Tensor:
        """
        Return the direction pointing from the orbit center to the camera position.

        Note: The camera itself is positioned at:
            camera_position = orbit_center + orbit_radius * orbit_direction

        Returns:
            torch.Tensor: A tensor of shape (3,) representing the direction pointing from the orbit
                center to the camera position.
        """
        dx, dy, dz = self._impl.camera_view_direction()
        return torch.tensor([dx, dy, dz], dtype=torch.float32)

    @camera_orbit_direction.setter
    def camera_orbit_direction(self, direction: NumericMaxRank1):
        """
        Set the direction pointing from the orbit center to the camera position.

        Note: The camera itself is positioned at:
            camera_position = orbit_center + orbit_radius * orbit_direction

        Args:
            direction (NumericMaxRank1): A tensor-like object of shape (3,) representing the direction pointing from the orbit
                center to the camera position.
        """
        dir_vec3f = to_Vec3f(direction).cpu().numpy()
        if np.linalg.norm(dir_vec3f) < 1e-6:
            raise ValueError("Camera orbit direction cannot be a zero vector.")
        dir_vec3f /= np.linalg.norm(dir_vec3f)
        self._impl.set_camera_view_direction(*dir_vec3f)

    @property
    def camera_up_direction(self) -> torch.Tensor:
        """
        Return the up vector of the camera. _i.e._ the direction that is considered 'up' in the camera's view.

        Returns:
            torch.Tensor: A tensor of shape (3,) representing the up vector of the camera.
        """
        ux, uy, uz = self._impl.camera_up_direction()
        return torch.tensor([ux, uy, uz], dtype=torch.float32)

    @camera_up_direction.setter
    def camera_up_direction(self, up: NumericMaxRank1):
        """
        Set the up vector of the camera. _i.e._ the direction that is considered 'up' in the camera's view.

        Args:
            up (NumericMaxRank1): A tensor-like object of shape (3,) representing the up vector of the camera.
        """
        up_vec3f = to_Vec3f(up).cpu().numpy()
        if np.linalg.norm(up_vec3f) < 1e-6:
            raise ValueError("Camera up direction cannot be a zero vector.")
        up_vec3f /= np.linalg.norm(up_vec3f)
        self._impl.set_camera_up_direction(*up_vec3f)

    @property
    def camera_near(self) -> float:
        """
        Get the near clipping plane distance for rendering. Splats closer to the camera than this distance
        will not be rendered.

        Returns:
            float: The near clipping plane distance.
        """
        return self._impl.camera_near()

    @camera_near.setter
    def camera_near(self, near: float):
        """
        Sets the near clipping plane distance for rendering. Splats closer to the camera than this distance
        will not be rendered.

        Args:
            near (float): The near clipping plane distance.
        """
        if near <= 0.0:
            raise ValueError(f"Near clipping plane distance must be positive, got {near}")
        self._impl.set_camera_near(near)

    @property
    def camera_far(self) -> float:
        """
        Get the far clipping plane distance for rendering. Splats farther from the camera than this distance
        will not be rendered.

        Returns:
            float: The far clipping plane distance.
        """
        return self._impl.camera_far()

    @camera_far.setter
    def camera_far(self, far: float):
        """
        Set the far clipping plane distance for rendering. Splats farther from the camera than this distance
        will not be rendered.

        Args:
            far (float): The far clipping plane distance.
        """
        if far <= 0.0:
            raise ValueError(f"Far clipping plane distance must be positive, got {far}")
        self._impl.set_camera_far(far)

    def set_camera_lookat(
        self,
        camera_origin: NumericMaxRank1,
        lookat_point: NumericMaxRank1,
        up_direction: NumericMaxRank1 = [0.0, 1.0, 0.0],
    ):
        """
        Set the camera pose from a camera origin, a lookat point, and an up direction.

        Args:
            camera_origin (NumericMaxRank1): A tensor-like object of shape (3,) representing the camera position in world coordinates.
            lookat_point (NumericMaxRank1): A tensor-like object of shape (3,) representing the point the camera is looking at.
            up_direction (NumericMaxRank1): A tensor-like object of shape (3,) representing the up direction of the camera.
        """
        camera_origin_vec3f = to_Vec3f(camera_origin).cpu().numpy()
        lookat_point_vec3f = to_Vec3f(lookat_point).cpu().numpy()
        up_direction_vec3f = to_Vec3f(up_direction).cpu().numpy()
        view_direction_vec3f = lookat_point_vec3f - camera_origin_vec3f
        orbit_radius = float(np.linalg.norm(view_direction_vec3f))

        if orbit_radius < 1e-6:
            raise ValueError("Camera origin and lookat point cannot be the same.")
        if np.linalg.norm(view_direction_vec3f) < 1e-6:
            raise ValueError("Camera origin and lookat point cannot be the same.")
        if np.linalg.norm(up_direction_vec3f) < 1e-6:
            raise ValueError("Up direction cannot be a zero vector.")

        view_direction_vec3f /= np.linalg.norm(view_direction_vec3f)
        up_direction_vec3f /= np.linalg.norm(up_direction_vec3f)

        # Check that the view direction is not parallel to the up direction
        dot_product = np.dot(view_direction_vec3f, up_direction_vec3f)
        if abs(dot_product) > 0.999:
            raise ValueError("View direction and up direction cannot be parallel or anti-parallel.")

        self._impl.set_camera_orbit_center(*lookat_point_vec3f)
        self._impl.set_camera_view_direction(*view_direction_vec3f)
        self._impl.set_camera_orbit_radius(orbit_radius)
        self._impl.set_camera_up_direction(*up_direction_vec3f)

"""Type definitions for Blender MCP addon and server."""

from typing import Any, Literal, TypedDict

try:
    from typing import NotRequired
except ImportError:  # pragma: no cover
    from typing_extensions import NotRequired


# ============================================================================
# Blender Object/Scene Types
# ============================================================================


class Vec3(TypedDict):
    """3D vector/coordinate."""

    x: float
    y: float
    z: float


class AABB(TypedDict):
    """Axis-aligned bounding box."""

    min: list[float]
    max: list[float]


class MaterialInfo(TypedDict):
    """Information about a Blender material."""

    name: str
    has_nodes: bool
    node_count: int
    texture_nodes: list[str]


class MeshInfo(TypedDict):
    """Information about mesh geometry."""

    vertices: int
    edges: int
    faces: int


class ObjectInfo(TypedDict):
    """Complete information about a Blender object."""

    name: str
    type: str
    location: list[float]
    rotation: NotRequired[list[float]]
    scale: NotRequired[list[float]]
    visible: NotRequired[bool]
    materials: NotRequired[list[str]]
    mesh: NotRequired[MeshInfo]
    world_bounding_box: NotRequired[list[list[float]]]


class SceneInfo(TypedDict):
    """Information about the active Blender scene."""

    name: str
    object_count: int
    objects: list[ObjectInfo]
    materials_count: int


# ============================================================================
# Command/Response Types
# ============================================================================


class CommandResult(TypedDict, total=False):
    """Generic command execution result."""

    status: str
    result: dict[str, Any] | list[Any] | str | int | float | bool | None
    message: str
    error: str
    data: Any


class ExecuteCodeResult(TypedDict, total=False):
    """Result of executing Python code in Blender."""

    status: Literal["success", "error"]
    output: str
    result: Any
    error: str
    traceback: str


class ViewportScreenshot(TypedDict):
    """Viewport screenshot data."""

    status: str
    filepath: str
    format: str
    max_size: int


# ============================================================================
# Asset Types - PolyHaven
# ============================================================================


class PolyhavenAsset(TypedDict):
    """Asset from Poly Haven API."""

    name: str
    type: int
    categories: list[str]
    download_count: int


class PolyhavenCategory(TypedDict):
    """Category from Poly Haven."""

    name: str
    description: str
    assetCount: int


class PolyhavenResponse(TypedDict):
    """Response from Poly Haven API."""

    results: list[PolyhavenAsset]
    next: NotRequired[str]


class TextureMap(TypedDict):
    """Downloaded texture map information."""

    type: str
    path: str
    resolution: str


class TextureDownload(TypedDict):
    """Texture download with all maps."""

    name: str
    maps: list[TextureMap]
    format: str


# ============================================================================
# Asset Types - Sketchfab
# ============================================================================


class SketchfabUser(TypedDict):
    """Sketchfab user info."""

    username: str
    url: str


class SketchfabLicense(TypedDict):
    """Sketchfab license info."""

    name: str
    url: str


class SketchfabModel(TypedDict):
    """Model from Sketchfab API."""

    name: str
    uid: str
    user: SketchfabUser
    license: SketchfabLicense
    faceCount: int
    isDownloadable: bool


class SketchfabSearchResult(TypedDict):
    """Search results from Sketchfab."""

    results: list[SketchfabModel]
    count: int
    next: NotRequired[str]


# ============================================================================
# Asset Types - 3D Generation (Rodin, Hunyuan3D)
# ============================================================================


class GenerationJobParams(TypedDict, total=False):
    """Parameters for asset generation job."""

    name: str
    prompt: str
    style: NotRequired[str]
    quality: NotRequired[str]
    negative_prompt: NotRequired[str]


class GenerationJobStatus(TypedDict, total=False):
    """Status of a generation job."""

    task_uuid: str
    status: str
    progress: NotRequired[int]
    result_url: NotRequired[str]
    error: NotRequired[str]


class GeneratedAssetImport(TypedDict):
    """Generated asset import info."""

    filepath: str
    name: str
    import_success: bool
    mesh_name: str


# ============================================================================
# Server/Connection Types
# ============================================================================


class BlenderCommandRequest(TypedDict, total=False):
    """Command request to Blender."""

    type: str
    command: str
    params: dict[str, Any]


class BlenderCommandResponse(TypedDict, total=False):
    """Response from Blender command."""

    type: str
    status: str
    result: Any
    error: str
    message: str


# ============================================================================
# Configuration/Status Types
# ============================================================================


class AddonStatus(TypedDict, total=False):
    """Status information about the addon."""

    addon_version: str
    blender_version: str
    server_running: bool
    connected: bool


class PolyhavStatusInfo(TypedDict):
    """PolyHaven feature status."""

    enabled: bool
    has_api_key: bool
    cache_directory: str


class Hyper3DStatusInfo(TypedDict):
    """Hyper3D generation status."""

    enabled: bool
    service: Literal["local", "main_site", "fal_ai"]
    api_key_configured: bool


class SketchfabStatusInfo(TypedDict):
    """Sketchfab feature status."""

    enabled: bool
    api_key_configured: bool


class RodinStatusInfo(TypedDict):
    """Rodin feature status."""

    enabled: bool
    api_key_configured: bool
    service: Literal["main_site", "fal_ai"]


class HunyuanStatusInfo(TypedDict):
    """Hunyuan3D feature status."""

    enabled: bool
    api_key_configured: bool
    service: Literal["local", "main_site"]


# ============================================================================
# Tool Response Wrapper Types (for MCP tools)
# ============================================================================


class ToolTextContent(TypedDict):
    """Text content for MCP tool response."""

    type: Literal["text"]
    text: str


class ToolImageContent(TypedDict):
    """Image content for MCP tool response."""

    type: Literal["image"]
    data: str
    mime_type: str


ToolContent = ToolTextContent | ToolImageContent


class ToolResponse(TypedDict, total=False):
    """MCP tool response format."""

    type: str
    content: list[ToolContent]
    isError: bool

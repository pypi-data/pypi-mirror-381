import asyncio
from enum import Enum

from hishel import AsyncCacheClient
from pydantic import BaseModel, ConfigDict, Field

from uv_secure.package_info.dependency_file_parser import Dependency
from uv_secure.package_utils import canonicalize_name


class ProjectState(str, Enum):
    ACTIVE = "active"
    ARCHIVED = "archived"
    DEPRECATED = "deprecated"
    QUARANTINED = "quarantined"


class ProjectStatus(BaseModel):
    model_config = ConfigDict(extra="ignore")

    status: ProjectState = ProjectState.ACTIVE
    reason: str | None = None


class PackageIndex(BaseModel):
    model_config = ConfigDict(extra="ignore")

    name: str = Field(min_length=1)
    project_status: ProjectStatus = Field(
        default_factory=lambda: ProjectStatus(status=ProjectState.ACTIVE),
        alias="project-status",
    )

    @property
    def status(self) -> ProjectState:
        """Convenience accessor for the enum status."""
        return self.project_status.status


async def _download_package_index(
    http_client: AsyncCacheClient, dependency: Dependency, disable_cache: bool
) -> PackageIndex:
    """Queries the PyPi Simple JSON API for the status of a dependency"""
    canonical_name = canonicalize_name(dependency.name)
    url = f"https://pypi.org/simple/{canonical_name}/"
    response = await http_client.get(
        url,
        extensions={"cache_disabled": True} if disable_cache else None,
        headers={"Accept": "application/vnd.pypi.simple.v1+json"},
    )
    response.raise_for_status()
    return PackageIndex.model_validate_json(response.content)


async def download_package_indexes(
    dependencies: list[Dependency], http_client: AsyncCacheClient, disable_cache: bool
) -> list[PackageIndex | BaseException]:
    """Fetch vulnerabilities for all dependencies concurrently."""
    tasks = [
        _download_package_index(http_client, dep, disable_cache) for dep in dependencies
    ]
    return await asyncio.gather(*tasks, return_exceptions=True)

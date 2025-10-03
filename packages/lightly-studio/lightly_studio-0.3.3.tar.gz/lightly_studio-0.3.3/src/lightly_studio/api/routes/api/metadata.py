"""This module contains the API routes for managing datasets."""

from __future__ import annotations

from typing import List
from uuid import UUID

from fastapi import APIRouter, Path
from typing_extensions import Annotated

from lightly_studio.db_manager import SessionDep
from lightly_studio.models.metadata import MetadataInfoView
from lightly_studio.resolvers.metadata_resolver.sample.get_metadata_info import (
    get_all_metadata_keys_and_schema,
)

metadata_router = APIRouter(prefix="/datasets/{dataset_id}", tags=["metadata"])


@metadata_router.get("/metadata/info", response_model=List[MetadataInfoView])
def get_metadata_info(
    session: SessionDep,
    dataset_id: Annotated[UUID, Path(title="Dataset Id")],
) -> list[MetadataInfoView]:
    """Get all metadata keys and their schema for a dataset.

    Args:
        session: The database session.
        dataset_id: The ID of the dataset.

    Returns:
        List of metadata info objects with name, type, and optionally min/max values
        for numerical metadata types.
    """
    return get_all_metadata_keys_and_schema(session=session, dataset_id=dataset_id)

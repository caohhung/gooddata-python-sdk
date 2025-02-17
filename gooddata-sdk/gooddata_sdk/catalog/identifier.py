# (C) 2022 GoodData Corporation
from __future__ import annotations

from typing import Type

import attr

from gooddata_metadata_client.model.assignee_identifier import AssigneeIdentifier
from gooddata_metadata_client.model.grain_identifier import GrainIdentifier
from gooddata_metadata_client.model.reference_identifier import ReferenceIdentifier
from gooddata_metadata_client.model.user_group_identifier import UserGroupIdentifier
from gooddata_metadata_client.model.workspace_identifier import WorkspaceIdentifier
from gooddata_sdk.catalog.base import Base


@attr.s(auto_attribs=True, kw_only=True)
class CatalogWorkspaceIdentifier(Base):
    id: str

    @staticmethod
    def client_class() -> Type[WorkspaceIdentifier]:
        return WorkspaceIdentifier


@attr.s(auto_attribs=True, kw_only=True)
class CatalogReferenceIdentifier(Base):
    id: str

    @staticmethod
    def client_class() -> Type[ReferenceIdentifier]:
        return ReferenceIdentifier


@attr.s(auto_attribs=True, kw_only=True)
class CatalogGrainIdentifier(Base):
    id: str
    type: str

    @staticmethod
    def client_class() -> Type[GrainIdentifier]:
        return GrainIdentifier


@attr.s(auto_attribs=True, kw_only=True)
class CatalogAssigneeIdentifier(Base):
    id: str
    type: str

    @staticmethod
    def client_class() -> Type[AssigneeIdentifier]:
        return AssigneeIdentifier


@attr.s(auto_attribs=True, kw_only=True)
class CatalogUserGroupIdentifier(Base):
    id: str
    type: str = "userGroup"

    @staticmethod
    def client_class() -> Type[UserGroupIdentifier]:
        return UserGroupIdentifier

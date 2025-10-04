"""Imbi project management system API models.

Defines Pydantic models for Imbi API responses including projects, project
types, environments, links, facts, and other project metadata used for
workflow targeting and context enrichment.
"""

import typing

import pydantic

from . import base


class ImbiEnvironment(base.BaseModel):
    """Imbi environment with metadata."""

    name: str
    icon_class: str
    description: str | None = None


class ImbiProjectLink(base.BaseModel):
    """External link associated with an Imbi project.

    Represents links to external systems like GitHub, PagerDuty, etc.
    """

    id: int | None = None
    project_id: int
    link_type_id: int
    created_by: str
    last_modified_by: str | None = None
    url: str


class ImbiProject(base.BaseModel):
    """Imbi project with metadata and external system integrations.

    Complete project definition including dependencies, facts, identifiers
    for external systems, and links to related services.
    """

    id: int
    dependencies: list[int] | None
    description: str | None
    environments: list[str] | None
    facts: dict[str, typing.Any] | None
    identifiers: dict[str, typing.Any] | None
    links: dict[str, str] | None
    name: str
    namespace: str
    namespace_slug: str
    project_score: str | None
    project_type: str
    project_type_slug: str
    slug: str
    urls: dict[str, str] | None
    imbi_url: str


class ImbiProjectFact(base.BaseModel):
    """Individual fact value for a project.

    Represents a single fact value recorded for a project with scoring,
    weighting, and audit information.
    """

    fact_type_id: int
    fact_name: str | None = None
    recorded_at: str | None = None
    recorded_by: str | None = None
    value: bool | int | float | str | None = None
    score: int | None = None
    weight: int | None = None


class ImbiProjectFactType(base.BaseModel):
    """Definition of a project fact type with validation rules.

    Defines metadata schema for project facts including data type
    (boolean, integer, number, string), fact type (enum, free-form,
    range), and UI options.
    """

    id: int
    created_by: str | None = None
    last_modified_by: str | None = None
    name: str
    description: str | None = None
    project_type_ids: list[int] = pydantic.Field(default_factory=list)
    fact_type: typing.Literal['enum', 'range', 'free-form']
    data_type: typing.Literal[
        'boolean', 'date', 'decimal', 'integer', 'string', 'timestamp'
    ]
    ui_options: list[str] = pydantic.Field(default_factory=list)
    weight: float = 0.0


class ImbiProjectFactTypeEnum(base.BaseModel):
    """Enumerated value option for enum-type project facts.

    Defines a single allowed value for enum fact types with optional icon
    and scoring information.
    """

    id: int
    fact_type_id: int
    created_by: str | None = None
    last_modified_by: str | None = None
    value: str
    icon_class: str | None = None
    score: int


class ImbiProjectFactTypeRange(base.BaseModel):
    """Range min/max values for range-type project facts."""

    id: int
    fact_type_id: int
    created_by: str | None = None
    last_modified_by: str | None = None
    max_value: int | float
    min_value: int | float
    score: int


class ImbiProjectType(base.BaseModel):
    """Project type definition in Imbi.

    Categorizes projects with metadata for icon display and environment URL
    support.
    """

    id: int
    created_by: str | None = None
    last_modified_by: str | None = None
    name: str
    plural_name: str
    description: str | None = None
    slug: str
    icon_class: str
    environment_urls: bool = False
    gitlab_project_prefix: str | None = None

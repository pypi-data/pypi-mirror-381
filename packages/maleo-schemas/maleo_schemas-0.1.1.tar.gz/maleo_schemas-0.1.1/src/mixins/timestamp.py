from datetime import datetime
from pydantic import BaseModel, Field
from typing import Generic, TypeVar
from maleo.types.datetime import OptionalDatetime
from maleo.types.float import OptionalFloat


TimestampT = TypeVar("TimestampT", bound=OptionalDatetime)


class FromTimestamp(BaseModel, Generic[TimestampT]):
    from_date: TimestampT = Field(..., description="From date")


class ToTimestamp(BaseModel, Generic[TimestampT]):
    to_date: TimestampT = Field(..., description="To date")


class ExecutionTimestamp(BaseModel, Generic[TimestampT]):
    executed_at: TimestampT = Field(..., description="executed_at timestamp")


class CompletionTimestamp(BaseModel, Generic[TimestampT]):
    completed_at: TimestampT = Field(..., description="completed_at timestamp")


class CreationTimestamp(BaseModel):
    created_at: datetime = Field(..., description="created_at timestamp")


class UpdateTimestamp(BaseModel):
    updated_at: datetime = Field(..., description="updated_at timestamp")


class LifecycleTimestamp(
    UpdateTimestamp,
    CreationTimestamp,
):
    pass


DeletionTimestampT = TypeVar("DeletionTimestampT", bound=OptionalDatetime)


class DeletionTimestamp(BaseModel, Generic[DeletionTimestampT]):
    deleted_at: DeletionTimestampT = Field(..., description="deleted_at timestamp")


RestorationTimestampT = TypeVar("RestorationTimestampT", bound=OptionalDatetime)


class RestorationTimestamp(BaseModel, Generic[RestorationTimestampT]):
    restored_at: RestorationTimestampT = Field(..., description="restored_at timestamp")


DeactivationTimestampT = TypeVar("DeactivationTimestampT", bound=OptionalDatetime)


class DeactivationTimestamp(BaseModel, Generic[DeactivationTimestampT]):
    deactivated_at: DeactivationTimestampT = Field(
        ..., description="deactivated_at timestamp"
    )


ActivationTimestampT = TypeVar("ActivationTimestampT", bound=OptionalDatetime)


class ActivationTimestamp(BaseModel, Generic[ActivationTimestampT]):
    activated_at: ActivationTimestampT = Field(
        ..., description="activated_at timestamp"
    )


class StatusTimestamp(
    ActivationTimestamp[ActivationTimestampT],
    DeactivationTimestamp[DeactivationTimestampT],
    RestorationTimestamp[RestorationTimestampT],
    DeletionTimestamp[DeletionTimestampT],
    Generic[
        DeletionTimestampT,
        RestorationTimestampT,
        DeactivationTimestampT,
        ActivationTimestampT,
    ],
):
    pass


class DataStatusTimestamp(
    StatusTimestamp[
        OptionalDatetime,
        OptionalDatetime,
        OptionalDatetime,
        datetime,
    ],
):
    pass


class DataTimestamp(
    DataStatusTimestamp,
    LifecycleTimestamp,
):
    pass


DurationT = TypeVar("DurationT", bound=OptionalFloat)


class Duration(BaseModel, Generic[DurationT]):
    duration: DurationT = Field(..., description="Duration")


class InferenceDuration(BaseModel, Generic[DurationT]):
    inference_duration: DurationT = Field(..., description="Inference duration")

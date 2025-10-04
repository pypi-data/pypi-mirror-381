# fastkafka2\message.py
from typing import Generic, TypeVar
from pydantic import Field, BaseModel


TData = TypeVar("TData")
THeaders = TypeVar("THeaders")


class KafkaMessage(BaseModel, Generic[TData, THeaders]):
    topic: str
    data: TData
    headers: THeaders = Field(default_factory=dict)
    key: str | None = None

    model_config = {"extra": "forbid", "frozen": True, "slots": True}

from __future__ import annotations

from typing import ClassVar

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    model_config: ClassVar[ConfigDict] = ConfigDict(from_attributes=True)

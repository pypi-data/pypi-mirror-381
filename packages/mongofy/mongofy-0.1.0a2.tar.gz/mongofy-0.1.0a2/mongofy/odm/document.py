# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import Optional, TypeVar

from bson import ObjectId
from msgspec import Struct, field


DocType = TypeVar("DocType", bound="Document")


class Document(Struct):
    """Base document class."""

    _id: Optional[ObjectId] = field(default=None)

    def save(self) -> DocType:
        return self
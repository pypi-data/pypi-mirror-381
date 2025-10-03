from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class ObjectId(BaseModel):
    scope: str
    code: str
    version: Optional[str] = None

    def label(self) -> str:
        return f"{self.scope}/{self.code}:{self.version or 'latest'}"


class ObjectMetadata(BaseModel):
    code: str
    scope: str
    version: str
    description: Optional[str] = None
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None

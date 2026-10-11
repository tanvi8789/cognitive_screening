from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional
class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    hashed_password: str
    is_admin: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Assessment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    audio_path: str
    profile_json: str  # store the full JSON profile as a string
    created_at: datetime = Field(default_factory=datetime.utcnow)
    report_text: str = Field(default="")


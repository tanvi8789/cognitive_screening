import os
from sqlmodel import SQLModel, create_engine, Session

# Database URL – default to a local SQLite file in the project root
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///cognitive_assessment.db")

engine = create_engine(DATABASE_URL, echo=False)

def get_session() -> Session:
    """Create a new SQLModel session.
    Caller is responsible for closing the session (e.g., using a context manager).
    """
    return Session(engine)

def create_db_and_tables():
    """Create all tables defined in the SQLModel models.
    This should be called once at application startup.
    """
    SQLModel.metadata.create_all(engine)


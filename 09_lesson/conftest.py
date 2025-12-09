import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DB_CONNECTION_STRING = "postgresql://postgres:postgres@localhost:5432/QA"


@pytest.fixture(scope="session")
def db_engine():
    engine = create_engine(DB_CONNECTION_STRING, echo=False)

    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        assert result.scalar() == 1

    yield engine
    engine.dispose()


@pytest.fixture
def db_session(db_engine):
    Session = sessionmaker(bind=db_engine)
    session = Session()

    try:
        yield session
    finally:
        session.close()

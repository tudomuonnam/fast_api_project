from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy_utils import create_database, drop_database

import pytest
import os,sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app
from database import Base, get_db


SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread":False})

def override_get_db():
    """" Override """
    try:
        db = Session(autocommit=False, autoflush=False, bind=engine)
        yield db
    finally:
        db.close()


@pytest.fixture(scope="session", autouse=True)
def create_db():
    """ creating db model in database """

    create_database(SQLALCHEMY_DATABASE_URL)
    print("\n" + "\x1b[6;30;42m" + "Creating test database." + "\x1b[0m")

    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = override_get_db

    yield 1

    drop_database(SQLALCHEMY_DATABASE_URL)
    print("\n" + "\x1b[6;30;42m" + "Delete test database." + "\x1b[0m")


@pytest.fixture()
def get_db_session():
    """ Getting session for db transaction """
    session = Session(autocommit=False, autoflush=False, bind=engine)
    yield session

    session.close()


@pytest.fixture()
def client():
    """ Getting testclient of app """
    with TestClient(app) as client:
        yield client




















# TestingSessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

# Base.metadata.create_all(bind=engine)



# @pytest.fixture(scope=)
# def client():
#     def override_get_db():
#         try:
#             db = TestingSessionLocal()
#             yield db
#         finally:
#             db.close()
#     app.dependency_overrides[get_db] = override_get_db()
#     client = TestClient(app)
#     yield client
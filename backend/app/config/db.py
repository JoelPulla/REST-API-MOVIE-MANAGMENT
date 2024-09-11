from sqlmodel import SQLModel, create_engine, Session


DATABASE_NAME = "database.db"

DATABASE_URL = f"sqlite:///{DATABASE_NAME}"

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, echo=True, connect_args=connect_args)


def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
from fastapi import FastAPI
from controllers import post
import sqlalchemy as sa
import databases
from contextlib import asynccontextmanager

DATABASE_URL = "sqlite:///./blog.db"

metadata = sa.MetaData()
database = databases.Database(DATABASE_URL)
engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


@asynccontextmanager
async def lifespan(app: FastAPI):
    from models.post import posts  # noqa

    metadata.create_all(engine)
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(post.router)

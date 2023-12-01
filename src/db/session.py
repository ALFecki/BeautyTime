from typing import AsyncIterator
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession



db_engine = create_async_engine(
    f"postgresql+asyncpg://root:root@localhost/beautytime",
    echo=False,
    max_overflow=4444,
)

class DataBaseManger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DataBaseManger, cls).__new__(cls)

            cls._instance.__session = async_sessionmaker(
                db_engine,
                autoflush=False,
                class_=AsyncSession,
                expire_on_commit=False,
            )
        return cls._instance

    @property
    def session(self):
        return self.__session

async def get_session() -> AsyncIterator[async_sessionmaker]:
    try:
        yield DataBaseManger().session
    except Exception as e:
        raise e


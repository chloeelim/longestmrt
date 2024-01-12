from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy import select, and_, create_engine

engine = create_engine("sqlite+pysqlite:///mrt.db", echo=True)


class Base(DeclarativeBase):
    pass


class Path(Base):
    __tablename__ = "path"

    start: Mapped[str] = mapped_column(primary_key=True)
    end: Mapped[str] = mapped_column(primary_key=True)
    index_: Mapped[int] = mapped_column(primary_key=True)
    part: Mapped[str]

    @classmethod
    def fetch_longest_path(cls, start: str, end: str):
        with Session(engine) as session:
            result = session.scalars(select(Path.part).where(
                and_(Path.start == start, Path.end == end)).order_by(Path.index_)).all()
            return result

from models.init_db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]

    movies: Mapped[list["Movie"]] = relationship("Movie", back_populates="created_by")

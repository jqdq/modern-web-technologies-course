from models.init_db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from models.movie import Movie

class MovieTag(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    tag_name: Mapped[str]
    movie_id: Mapped[int] = mapped_column(ForeignKey('movie.id'))
    movie: Mapped[Movie] = relationship('Movie')
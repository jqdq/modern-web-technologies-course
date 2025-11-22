"""
This model shows how to create a One-to-Many relationship using SQLAlchemy ORM.
Repationships allow you to connect models together, so you can easily retrieve related data.

This is a Many-to-One relationship, so we're adding a foreign key to the "many" side (MovieTag).
One-to-one relationships contain a foreign key on both sides, while Many-to-Many relationships require an association table.
We'll cover those later in the course.

You can use models like this to store:
- Tags of products in an e-commerce app
- Comments on blog posts
- Authors of articles
"""

from models.init_db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from models.movie import Movie


class MovieTag(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    tag_name: Mapped[str]
    # Key to the Movie table - establishes a One-to-Many relationship
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"))
    # The 'movie' attribute will be retrieved on access, based on the movie_id
    movie: Mapped[Movie] = relationship("Movie")

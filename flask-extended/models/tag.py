"""
This model shows how to create a Many-to-Many relationship using SQLAlchemy ORM.
Repationships allow you to connect models together, so you can easily retrieve related data.

This is a Many-to-Many relationship, so we're adding
an association table (movie_tag), and add relationships on both sides.

You can also use Many to Many relationships to store data like:
- Tags/filters associated with objects (e.g. products, articles, movies)
- User roles/permissions ("User X can view file Y")
- Orders and products ("In the X order product Y was purchased Z times")
- Any ambigious relationships, as it's the most flexible option.
"""

from models.init_db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Column

from models.movie import Movie

# Here we define the association table for the Many-to-Many relationship
# We wouldn't be using a full Model class for this, as it only contains foreign keys.
# Hence, we use db.Table to define it.
movie_tag = db.Table(
    # Name of the association table, usually a commonsense name (ex: follows)
    # or combination of the two related tables (movie and tag -> movie_tag)
    "movie_tag",
    # Defining the columns of the association table
    # Note have to use snake_case for ForeignKey references,
    # as these are table (not Model) and column names!
    Column("movie_id", db.Integer, ForeignKey("movie.id"), primary_key=True),
    Column("tag_id", db.Integer, ForeignKey("tag.id"), primary_key=True),
    # You can add additional columns here if needed, but I suggest making a
    # separate model if you need to store more data about the relationship.
)


class Tag(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    tag_name: Mapped[str]

    # Many-to-many relationship
    # Just like in Movie, we define the relationship:
    # - secondary points to the association table
    # - back_populates points to 'tags' in Movie
    movies: Mapped[list[Movie]] = relationship(
        secondary=movie_tag, back_populates="tags"
    )

"""
Models are classes that represent objects of a certain types stored in the DB.
In them we specify the attributes (columns) of these objects and their types.
Mapped[...] is a notation that tells SQLAlchemy what type the attribute is.

You should use models like this to represent all the data stored in the app.

You can use One to One relationships to store data like:
- User profiles (e.g. each user has one profile)
- Extended details (e.g. product has one detailed specification sheet)
Not very common. I'm not showing any examples here, but you just need to create
a foreign key on one side and a relationship on both sides. More info:
https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#one-to-one

Others are described in their respective files.
"""

from models.init_db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Movie(db.Model):
    # Primary key 'id' will be auto-incremented by default,
    # so we do not specify it when creating new Movie objects.
    # It's only available after committing to the database!
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    cat_death: Mapped[bool]
    violence: Mapped[bool]
    loud_noises: Mapped[bool]
    jump_scares: Mapped[bool]

    # Many-to-one relationship
    # relationship to Award model
    # Note the back_populates points to 'movie' in Award to complete the relationship.
    awards: Mapped[list["Award"]] = relationship("Award", back_populates="movie")

    # Many-to-many relationship
    # - secondary points to the association table
    # - back_populates points to 'movies' in Tag
    # - Note the quotes around "Tag" to avoid circular import issues
    tags: Mapped[list["Tag"]] = relationship(
        secondary="movie_tag", back_populates="movies"
    )

    # Many-to-one relationship to User (creator of the movie entry)
    created_by_id: Mapped[int] = mapped_column(db.ForeignKey("user.id"), nullable=True)
    created_by: Mapped["User"] = relationship("User", back_populates="movies")

"""
This model shows how to create a One-to-Many relationship using SQLAlchemy ORM.
Repationships allow you to connect models together, so you can easily retrieve related data.

This is a Many-to-One relationship, so we're adding
a foreign key to the "many" side (MovieTag).

You can use Many to One relationships to store data like:
- Object categories (as long as each object has only one category)
- Ownership data (e.g. object is owned by another object, like user owns posts)
- Hierarchical relationships (e.g. comments on posts, events in locations)
- Status/state data (e.g. orders have one status like 'pending', 'shipped')
"""

from models.init_db import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from models.movie import Movie


class Award(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    award_name: Mapped[str]

    # For the One-to-many-relationship
    # Key to the Movie table - establishes a One-to-Many relationship
    movie_id: Mapped[int] = mapped_column(ForeignKey("movie.id"))
    # The 'movie' attribute will be retrieved on access, based on the movie_id
    # Note the back_populates points to 'awards' in Movie to complete the relationship.
    movie: Mapped[Movie] = relationship("Movie", back_populates="awards")

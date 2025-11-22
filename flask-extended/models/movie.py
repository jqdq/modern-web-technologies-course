"""
Models are classes that represent objects of a certain types stored in the DB.
In them we specify the attributes (columns) of these objects and their types.
Mapped[...] is a notation that tells SQLAlchemy what type the attribute is.

You should use models like this to represent all the data stored in the app.
"""

from models.init_db import db
from sqlalchemy.orm import Mapped, mapped_column


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

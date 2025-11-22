"""
This file is some boilerplate that allows the models to function properly.
You can copy it into your own projects as needed.
"""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

from models.init_db import db
from sqlalchemy.orm import Mapped, mapped_column

class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    cat_death: Mapped[bool]
    violence: Mapped[bool]
    loud_noises: Mapped[bool]
    jump_scares: Mapped[bool]
from typing import TYPE_CHECKING, Optional

from sqlalchemy.orm import Mapped, relationship, mapped_column

from .core import BaseModel

if TYPE_CHECKING:
    from .product import ProductModel


class CategotyModel(BaseModel):
    __tablename__ = "category"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    product: Mapped[Optional[list["ProductModel"]]] = relationship(back_populates="category") 
    
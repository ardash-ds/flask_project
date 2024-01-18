from typing import TYPE_CHECKING, Optional

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .core import BaseModel

if TYPE_CHECKING:
    from .manufacturer import ManufacturerModel
    from .category import CategotyModel


class ProductModel(BaseModel):
    __tablename__ = "product"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    category: Mapped[Optional["CategotyModel"]] = relationship(back_populates="product")
    category_id = mapped_column(Integer, ForeignKey("category.id"))
    manufacturer: Mapped[Optional["ManufacturerModel"]] = relationship(back_populates="product")
    manufacturer_id = mapped_column(Integer, ForeignKey("manufacturer.id"))
    
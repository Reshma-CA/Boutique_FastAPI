from db.base_class import Base
from sqlalchemy import Boolean,Column,String,Integer
from sqlalchemy.orm import relationship

from .boutique import Boutique


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String,nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    confirm_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    boutiques = relationship("Boutique", back_populates="author")  # Rename to `boutiques`


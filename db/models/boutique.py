from datetime import datetime
from sqlalchemy import Column,Integer,String,Text,Boolean,DateTime,ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class Boutique(Base):
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    slug = Column(String, nullable=False)
    content = Column(Text, nullable=True)
    dress_picture = Column(String, nullable=True)  # Field for the dress picture path
    author_id = Column(Integer, ForeignKey("user.id"))
    author = relationship("User", back_populates="boutiques")  # Match the `back_populates` name
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean, default=False)



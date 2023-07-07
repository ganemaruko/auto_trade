from sqlalchemy import Column, Integer, Float

from lib.db.settings import Base


class Market(Base):
    __tablename__ = 'market'

    id = Column(Integer, primary_key=True)
    open = Column(Float, nullable=True)
    high = Column(Float, nullable=True)
    low = Column(Float, nullable=True)
    close = Column(Float, nullable=True)

    def __repr__(self):
        return "<User('name={}', fullname={}, nickname={})>".format(
            self.name,
            self.fullname,
            self.nickname
        )

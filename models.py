from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, Column, BigInteger, Integer, String
import config

Base = declarative_base()
# (?) Is it better to use this variant?
# from sqlalchemy.orm import DeclarativeBase
# class Base(DeclarativeBase):
#     pass
# *** (from documentation)  Changed in version 2.0: Note that the declarative_base() function is superseded by the new DeclarativeBase class, which generates a new “base” class using subclassing, rather than return value of a function. This allows an approach that is compatible with PEP 484 typing tools.

engine = create_engine(config.DATABASE_STRING, echo=True, future=True)

class TelegramChat(Base):
    __tablename__ = "telegram_chat"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    type = Column(String(64))
    telegram_id = Column(BigInteger, unique=True)

    def __repr__(self):
        return f"Chat(id={self.chat_id!r}, name={self.name!r})"  # (?) "Chat" & "chat_id" here == ?

#     messages = relationship( ?? )  # Proceed from here!




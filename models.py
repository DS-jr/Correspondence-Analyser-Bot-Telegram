from sqlalchemy.orm import declarative_base, relationship, DeclarativeBase
from sqlalchemy import create_engine, Column, BigInteger, Integer, String
import config

class Base(DeclarativeBase):
    pass

engine = create_engine(config.DATABASE_STRING, echo=True, future=True)  # Engine is a factory that can create new database connections


class TelegramChat(Base):
    __tablename__ = "telegram_chat"
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    type = Column(String(64))
    telegram_id = Column(BigInteger, unique=True)

    # messages = relationship( ?? )  # Proceed from here!

    def __repr__(self):
        return f"Chat(id={self.telegram_id!r}, name={self.name!r})"  # (?) Why "type" is NOT used here, but only "id" & "name"?


class TelegramMessage(Base):
    __tablename__ = "telegram_message"
    id = Column(BigInteger, primary_key=True)
    telegram_id = Column(BigInteger, unique=True)
    date = Column(DateTime)
    unix_timestamp = Column(BigInteger)
    from_name = Column(String(128))
    from_id = Column(String(128))

    # chat_id = Column(BigInteger, ForeignKey(..??>>))  # Proceed from here!





# (alternative)  # *** (from documentation)  Changed in version 2.0: Note that the declarative_base() function is superseded by the new DeclarativeBase class, which generates a new “base” class using subclassing, rather than return value of a function. This allows an approach that is compatible with PEP 484 typing tools.
# Base = declarative_base()


from sqlalchemy.orm import declarative_base, relationship
# from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import create_engine, Column, BigInteger, Integer, String, DateTime, ForeignKey
import config


# class Base(DeclarativeBase):
#     pass
Base = declarative_base()

engine = create_engine(config.DATABASE_STRING, echo=True, future=True)  # Engine is a factory that can create new database connections


class TelegramChat(Base):
    __tablename__ = "telegram_chat"
    id = Column(Integer, primary_key=True)  # (?!) Convert to string?
    telegram_id = Column(BigInteger, unique=True)
    name = Column(String(128))
    type = Column(String(64))

    messages = relationship("TelegramMessage", back_populates="chat", cascade="all, delete")  # (?) What should be used here: ?"message" or "chat" ?

    def __repr__(self):
        return f"Chat(id={self.telegram_id!r}, name={self.name!r})"  # (??) What for is this line? Why "type" is NOT used here, but only "id" & "name"?


class TelegramMessage(Base):
    __tablename__ = "telegram_message"
    id = Column(Integer, primary_key=True)  # (?!) Convert to string?
    telegram_id = Column(BigInteger, unique=True)
    date = Column(DateTime)
    unix_timestamp = Column(BigInteger)
    from_name = Column(String(128))
    from_id = Column(String(128))
    # text
    # text_entities   # In JSON it contains a list of dictionaries

    chat_id = Column(BigInteger, ForeignKey("telegram_chat.telegram_id"), nullable=False)

    chat = relationship("TelegramChat", back_populates="messages")

    def __repr__(self):
        return f"Message(id={self.id!r}, from_name={self.from_name!r})"

Base.metadata.create_all(engine)

# (alternative)  # *** (from documentation)  Changed in version 2.0: Note that the declarative_base() function is superseded by the new DeclarativeBase class, which generates a new “base” class using subclassing, rather than return value of a function. This allows an approach that is compatible with PEP 484 typing tools.
# Base = declarative_base()


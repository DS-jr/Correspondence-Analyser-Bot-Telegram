from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer, BigInteger
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import config

Base = declarative_base()

engine = create_engine(config.DATABASE_STRING, echo=True, future=True)


class TelegramChat(Base):
    __tablename__ = "telegram_chat"

    id = Column(BigInteger, primary_key=True)
    telegram_id = Column(BigInteger, unique=True)
    name = Column(String(100))
    type = Column(String(50))

    messages = relationship(
        "TelegramMessage", back_populates="message", cascade="all, delete"
    )

    def __repr__(self):
        return f"Chat(id={self.chat_id!r}, name={self.name!r})"


class TelegramMessage(Base):
    __tablename__ = "telegram_message"

    id = Column(BigInteger, primary_key=True)
    telegram_id = Column(BigInteger, unique=True)
    date = Column(DateTime)
    unix_timestamp = Column(BigInteger)
    from_name = Column(String(100))
    from_id = Column(String(100))

    chat_id = Column(BigInteger, ForeignKey("telegram_chat.telegram_id"), nullable=False)

    chat = relationship("TelegramChat", back_populates="messages")

    def __repr__(self):
        return f"Message(id={self.id!r}, from_name={self.from_name!r})"


Base.metadata.create_all(engine)

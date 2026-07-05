"""
ORM Models.
Defines the chat_messages table using SQLAlchemy.
Uses String instead of Enum for SQLite compatibility.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime
from app.database.connection import Base


class ChatMessage(Base):
    """
    Stores every chat turn in a single row.
    session_id groups messages belonging to the same conversation.
    """
    __tablename__ = "chat_messages"

    id         = Column(Integer, primary_key=True, index=True, autoincrement=True)
    session_id = Column(String(100), index=True, nullable=False)
    role       = Column(String(20), nullable=False)   # 'user' or 'assistant'
    content    = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return (
            f"<ChatMessage id={self.id} session={self.session_id} "
            f"role={self.role} created_at={self.created_at}>"
        )

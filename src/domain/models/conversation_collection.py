from datetime import datetime, timezone

from sqlalchemy import Column, BigInteger, String, Boolean, DateTime

from src.domain.models.base import Base


class ConversationCollection(Base):
    __tablename__ = "conversation_collection"

    id = Column(BigInteger, primary_key=True)
    # user_id = Column(BigInteger, nullable=False, index=True)
    name = Column(String(150), nullable=False)
    is_active = Column(Boolean, default=True)
    is_archived = Column(Boolean, default=False)
    created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    updated_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
    deleted_at = Column(DateTime(timezone=True), nullable=True)

"""
SQLAlchemy models for Memori v2.0
Provides cross-database compatibility using SQLAlchemy ORM
"""

from datetime import datetime
from typing import Any

from sqlalchemy import (
    JSON,
    Boolean,
    Column,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base: Any = declarative_base()


class ChatHistory(Base):
    """Chat history table - stores all conversations"""

    __tablename__ = "chat_history"

    chat_id = Column(String(255), primary_key=True)
    user_input = Column(Text, nullable=False)
    ai_output = Column(Text, nullable=False)
    model = Column(String(255), nullable=False)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    session_id = Column(String(255), nullable=False)
    namespace = Column(String(255), nullable=False, default="default")
    tokens_used = Column(Integer, default=0)
    metadata_json = Column(JSON)

    # Relationships
    short_term_memories = relationship(
        "ShortTermMemory", back_populates="chat", cascade="all, delete-orphan"
    )

    # Indexes
    __table_args__ = (
        Index("idx_chat_namespace_session", "namespace", "session_id"),
        Index("idx_chat_timestamp", "timestamp"),
        Index("idx_chat_model", "model"),
    )


class ShortTermMemory(Base):
    """Short-term memory table with expiration"""

    __tablename__ = "short_term_memory"

    memory_id = Column(String(255), primary_key=True)
    chat_id = Column(
        String(255), ForeignKey("chat_history.chat_id", ondelete="SET NULL")
    )
    processed_data = Column(JSON, nullable=False)
    importance_score = Column(Float, nullable=False, default=0.5)
    category_primary = Column(String(255), nullable=False)
    retention_type = Column(String(50), nullable=False, default="short_term")
    namespace = Column(String(255), nullable=False, default="default")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    expires_at = Column(DateTime)
    access_count = Column(Integer, default=0)
    last_accessed = Column(DateTime)
    searchable_content = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)
    is_permanent_context = Column(Boolean, default=False)

    # Relationships
    chat = relationship("ChatHistory", back_populates="short_term_memories")

    # Indexes
    __table_args__ = (
        Index("idx_short_term_namespace", "namespace"),
        Index("idx_short_term_category", "category_primary"),
        Index("idx_short_term_importance", "importance_score"),
        Index("idx_short_term_expires", "expires_at"),
        Index("idx_short_term_created", "created_at"),
        Index("idx_short_term_access", "access_count", "last_accessed"),
        Index("idx_short_term_permanent", "is_permanent_context"),
        Index(
            "idx_short_term_namespace_category",
            "namespace",
            "category_primary",
            "importance_score",
        ),
    )


class LongTermMemory(Base):
    """Long-term memory table with enhanced classification"""

    __tablename__ = "long_term_memory"

    memory_id = Column(String(255), primary_key=True)
    original_chat_id = Column(String(255))
    processed_data = Column(JSON, nullable=False)
    importance_score = Column(Float, nullable=False, default=0.5)
    category_primary = Column(String(255), nullable=False)
    retention_type = Column(String(50), nullable=False, default="long_term")
    namespace = Column(String(255), nullable=False, default="default")
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    access_count = Column(Integer, default=0)
    last_accessed = Column(DateTime)
    searchable_content = Column(Text, nullable=False)
    summary = Column(Text, nullable=False)
    novelty_score = Column(Float, default=0.5)
    relevance_score = Column(Float, default=0.5)
    actionability_score = Column(Float, default=0.5)

    # Enhanced Classification Fields
    classification = Column(String(50), nullable=False, default="conversational")
    memory_importance = Column(String(20), nullable=False, default="medium")
    topic = Column(String(255))
    entities_json = Column(JSON)
    keywords_json = Column(JSON)

    # Conscious Context Flags
    is_user_context = Column(Boolean, default=False)
    is_preference = Column(Boolean, default=False)
    is_skill_knowledge = Column(Boolean, default=False)
    is_current_project = Column(Boolean, default=False)
    promotion_eligible = Column(Boolean, default=False)

    # Memory Management
    duplicate_of = Column(String(255))
    supersedes_json = Column(JSON)
    related_memories_json = Column(JSON)

    # Technical Metadata
    confidence_score = Column(Float, default=0.8)
    extraction_timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    classification_reason = Column(Text)

    # Processing Status
    processed_for_duplicates = Column(Boolean, default=False)
    conscious_processed = Column(Boolean, default=False)

    # Indexes
    __table_args__ = (
        Index("idx_long_term_namespace", "namespace"),
        Index("idx_long_term_category", "category_primary"),
        Index("idx_long_term_importance", "importance_score"),
        Index("idx_long_term_created", "created_at"),
        Index("idx_long_term_access", "access_count", "last_accessed"),
        Index(
            "idx_long_term_scores",
            "novelty_score",
            "relevance_score",
            "actionability_score",
        ),
        Index("idx_long_term_classification", "classification"),
        Index("idx_long_term_memory_importance", "memory_importance"),
        Index("idx_long_term_topic", "topic"),
        Index(
            "idx_long_term_conscious_flags",
            "is_user_context",
            "is_preference",
            "is_skill_knowledge",
            "promotion_eligible",
        ),
        Index("idx_long_term_conscious_processed", "conscious_processed"),
        Index("idx_long_term_duplicates", "processed_for_duplicates"),
        Index("idx_long_term_confidence", "confidence_score"),
        Index(
            "idx_long_term_namespace_category",
            "namespace",
            "category_primary",
            "importance_score",
        ),
    )


# Database-specific configurations
def configure_mysql_fulltext(engine):
    """Configure MySQL FULLTEXT indexes"""
    if engine.dialect.name == "mysql":
        with engine.connect() as conn:
            try:
                # Create FULLTEXT indexes for MySQL
                conn.execute(
                    "ALTER TABLE short_term_memory ADD FULLTEXT INDEX ft_short_term_search (searchable_content, summary)"
                )
                conn.execute(
                    "ALTER TABLE long_term_memory ADD FULLTEXT INDEX ft_long_term_search (searchable_content, summary)"
                )
                conn.execute(
                    "ALTER TABLE long_term_memory ADD FULLTEXT INDEX ft_long_term_topic (topic)"
                )
                conn.commit()
            except Exception:
                # Indexes might already exist
                pass


def configure_postgresql_fts(engine):
    """Configure PostgreSQL full-text search"""
    if engine.dialect.name == "postgresql":
        with engine.connect() as conn:
            try:
                # Add tsvector columns for PostgreSQL
                conn.execute(
                    "ALTER TABLE short_term_memory ADD COLUMN IF NOT EXISTS search_vector tsvector"
                )
                conn.execute(
                    "ALTER TABLE long_term_memory ADD COLUMN IF NOT EXISTS search_vector tsvector"
                )

                # Create GIN indexes
                conn.execute(
                    "CREATE INDEX IF NOT EXISTS idx_short_term_search_vector ON short_term_memory USING GIN(search_vector)"
                )
                conn.execute(
                    "CREATE INDEX IF NOT EXISTS idx_long_term_search_vector ON long_term_memory USING GIN(search_vector)"
                )

                # Create triggers to maintain tsvector
                conn.execute(
                    """
                    CREATE OR REPLACE FUNCTION update_short_term_search_vector() RETURNS trigger AS $$
                    BEGIN
                        NEW.search_vector := to_tsvector('english', COALESCE(NEW.searchable_content, '') || ' ' || COALESCE(NEW.summary, ''));
                        RETURN NEW;
                    END
                    $$ LANGUAGE plpgsql;
                """
                )

                conn.execute(
                    """
                    CREATE TRIGGER update_short_term_search_vector_trigger
                    BEFORE INSERT OR UPDATE ON short_term_memory
                    FOR EACH ROW EXECUTE FUNCTION update_short_term_search_vector();
                """
                )

                conn.execute(
                    """
                    CREATE OR REPLACE FUNCTION update_long_term_search_vector() RETURNS trigger AS $$
                    BEGIN
                        NEW.search_vector := to_tsvector('english', COALESCE(NEW.searchable_content, '') || ' ' || COALESCE(NEW.summary, '') || ' ' || COALESCE(NEW.topic, ''));
                        RETURN NEW;
                    END
                    $$ LANGUAGE plpgsql;
                """
                )

                conn.execute(
                    """
                    CREATE TRIGGER update_long_term_search_vector_trigger
                    BEFORE INSERT OR UPDATE ON long_term_memory
                    FOR EACH ROW EXECUTE FUNCTION update_long_term_search_vector();
                """
                )

                conn.commit()
            except Exception:
                # Extensions or functions might already exist
                pass


def configure_sqlite_fts(engine):
    """Configure SQLite FTS5"""
    if engine.dialect.name == "sqlite":
        with engine.connect() as conn:
            try:
                # Create FTS5 virtual table for SQLite
                conn.execute(
                    """
                    CREATE VIRTUAL TABLE IF NOT EXISTS memory_search_fts USING fts5(
                        memory_id,
                        memory_type,
                        namespace,
                        searchable_content,
                        summary,
                        category_primary,
                        content='',
                        contentless_delete=1
                    )
                """
                )

                # Create triggers to maintain FTS5 index
                conn.execute(
                    """
                    CREATE TRIGGER IF NOT EXISTS short_term_memory_fts_insert AFTER INSERT ON short_term_memory
                    BEGIN
                        INSERT INTO memory_search_fts(memory_id, memory_type, namespace, searchable_content, summary, category_primary)
                        VALUES (NEW.memory_id, 'short_term', NEW.namespace, NEW.searchable_content, NEW.summary, NEW.category_primary);
                    END
                """
                )

                conn.execute(
                    """
                    CREATE TRIGGER IF NOT EXISTS long_term_memory_fts_insert AFTER INSERT ON long_term_memory
                    BEGIN
                        INSERT INTO memory_search_fts(memory_id, memory_type, namespace, searchable_content, summary, category_primary)
                        VALUES (NEW.memory_id, 'long_term', NEW.namespace, NEW.searchable_content, NEW.summary, NEW.category_primary);
                    END
                """
                )

                conn.execute(
                    """
                    CREATE TRIGGER IF NOT EXISTS short_term_memory_fts_delete AFTER DELETE ON short_term_memory
                    BEGIN
                        DELETE FROM memory_search_fts WHERE memory_id = OLD.memory_id AND memory_type = 'short_term';
                    END
                """
                )

                conn.execute(
                    """
                    CREATE TRIGGER IF NOT EXISTS long_term_memory_fts_delete AFTER DELETE ON long_term_memory
                    BEGIN
                        DELETE FROM memory_search_fts WHERE memory_id = OLD.memory_id AND memory_type = 'long_term';
                    END
                """
                )

                conn.commit()
            except Exception:
                # FTS5 might not be available
                pass


class DatabaseManager:
    """SQLAlchemy-based database manager for cross-database compatibility"""

    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine = create_engine(
            database_url,
            json_serializer=self._json_serializer,
            json_deserializer=self._json_deserializer,
            echo=False,  # Set to True for SQL debugging
        )

        # Configure database-specific features
        self._setup_database_features()

        # Create session factory
        self.SessionLocal = sessionmaker(bind=self.engine)

    def _json_serializer(self, obj):
        """Custom JSON serializer"""
        import json

        return json.dumps(obj, default=str, ensure_ascii=False)

    def _json_deserializer(self, value):
        """Custom JSON deserializer"""
        import json

        return json.loads(value)

    def _setup_database_features(self):
        """Setup database-specific features like full-text search"""
        dialect_name = self.engine.dialect.name

        if dialect_name == "mysql":
            configure_mysql_fulltext(self.engine)
        elif dialect_name == "postgresql":
            configure_postgresql_fts(self.engine)
        elif dialect_name == "sqlite":
            configure_sqlite_fts(self.engine)

    def create_tables(self):
        """Create all tables"""
        Base.metadata.create_all(bind=self.engine)

        # Setup database-specific search features after table creation
        self._setup_database_features()

    def get_session(self):
        """Get database session"""
        return self.SessionLocal()

    def get_database_info(self) -> dict[str, Any]:
        """Get database information"""
        return {
            "database_type": self.engine.dialect.name,
            "database_url": (
                self.database_url.split("@")[-1]
                if "@" in self.database_url
                else self.database_url
            ),
            "driver": self.engine.dialect.driver,
            "server_version": getattr(self.engine.dialect, "server_version_info", None),
        }

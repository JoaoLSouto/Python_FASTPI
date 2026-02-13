import sqlalchemy as sa
from main import metadata

posts = sa.table(
    "posts",
    metadata,
    sa.Column("id", sa.integer, primary_key=True),
    sa.Column("title", sa.String(150), nullable=False, unique=True),
    sa.Column("content", sa.String, nullable=False),
    sa.Column("published_at", sa.DateTime, nullable=True),
    sa.Column("published", sa.DateTime, sa.Boolean, default=False),
)

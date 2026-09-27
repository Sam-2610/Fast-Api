from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '2c84de402fc0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False),
        sa.Column('content', sa.String(), nullable=False),
        sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE'),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
    )


def downgrade() -> None:
    op.drop_table('posts')
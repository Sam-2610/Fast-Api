"""users_table

Revision ID: 7cb28ed574ad
Revises: 2c84de402fc0
Create Date: 2026-09-26 11:42:09.263109

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7cb28ed574ad'
down_revision: Union[str, Sequence[str], None] = '2c84de402fc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
            'users',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('email', sa.String(), nullable=False),
            sa.Column('password', sa.String(), nullable=False),
            sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('now()')),
            sa.PrimaryKeyConstraint('id'),
            sa.UniqueConstraint('email')
        )
   
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass

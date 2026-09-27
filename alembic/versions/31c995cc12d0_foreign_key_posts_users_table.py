"""foreign_key_posts_users_table

Revision ID: 31c995cc12d0
Revises: 7cb28ed574ad
Create Date: 2026-09-26 12:17:44.770187

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '31c995cc12d0'
down_revision: Union[str, Sequence[str], None] = '7cb28ed574ad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )

    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass

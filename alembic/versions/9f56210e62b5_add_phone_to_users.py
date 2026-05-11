"""add_phone_to_users

Revision ID: 9f56210e62b5
Revises: d691dc733ffd
Create Date: 2026-05-08 15:22:10.727782

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9f56210e62b5'
down_revision: Union[str, Sequence[str], None] = 'd691dc733ffd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'users',
        sa.Column('telefon_raqami', sa.String(20), nullable=True)
    )
    # Index ham qo'shamiz:
    op.create_index(
        'ix_users_telefon_raqami',
        'users',
        ['telefon_raqami'],
        unique=False
    )


def downgrade() -> None:
    op.drop_index('ix_users_telefon_raqami', table_name='users')
    op.drop_column('users', 'telefon_raqami')

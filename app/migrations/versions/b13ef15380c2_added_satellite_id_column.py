"""Added satellite id column

Revision ID: b13ef15380c2
Revises: ae166a7fbd92
Create Date: 2022-06-24 04:24:46.296337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b13ef15380c2'
down_revision = 'ae166a7fbd92'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('space_track', sa.Column('satellite_id', sa.String(length=64), nullable=False))


def downgrade() -> None:
    op.drop_column('space_track', 'satellite_id')


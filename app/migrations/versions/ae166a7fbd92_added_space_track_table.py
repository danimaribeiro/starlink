"""Added space track table

Revision ID: ae166a7fbd92
Revises: 
Create Date: 2022-06-24 03:23:36.649662

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae166a7fbd92'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('space_track',
        sa.Column('eid', sa.String(length=64), nullable=False),
        sa.Column('name', sa.String(length=64), nullable=False),
        sa.Column('created_date', sa.DateTime(), nullable=False),
        sa.Column('epoch', sa.DateTime(), nullable=False),
        sa.Column('longitude', sa.Float(), nullable=True),
        sa.Column('latitude', sa.Float(), nullable=True),
        sa.Column('velocity_kms', sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint('eid')
    )


def downgrade() -> None:
    op.drop_table('space_track')

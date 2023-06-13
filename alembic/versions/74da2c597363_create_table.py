"""Create table

Revision ID: 74da2c597363
Revises: 
Create Date: 2023-06-12 22:30:22.075500

"""
from datetime import datetime

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74da2c597363'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'currency',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('tiker', sa.String(), nullable=False),
        sa.Column('index_price', sa.Float(), nullable=False),
        sa.Column('date', sa.DateTime(), nullable=False)
    )


def downgrade() -> None:
    op.drop_table('currency')

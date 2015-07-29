"""create appointments table

Revision ID: 3e7ebdde2eb
Revises:
Create Date: 2015-07-20 17:47:37.704508

"""

# revision identifiers, used by Alembic.
revision = '3e7ebdde2eb'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'appointments',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('phone_number', sa.String(20), nullable=False),
        sa.Column('delta', sa.Integer, nullable=False),
        sa.Column('time', sa.DateTime, nullable=False),
        sa.Column('timezone', sa.String(), nullable=False)
    )


def downgrade():
    op.drop_table('appointments')

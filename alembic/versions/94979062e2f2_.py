"""empty message

Revision ID: 94979062e2f2
Revises: b8a7a9a4c675
Create Date: 2024-07-03 21:16:46.744551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94979062e2f2'
down_revision = 'b8a7a9a4c675'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('description', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'description')
    # ### end Alembic commands ###

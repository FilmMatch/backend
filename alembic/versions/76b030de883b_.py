"""empty message

Revision ID: 76b030de883b
Revises: b16c157b1d74
Create Date: 2024-05-09 01:46:10.390533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76b030de883b'
down_revision = 'b16c157b1d74'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subusers', sa.Column('type', sa.Enum('Admin', 'User', 'Producer', 'Manager', 'Actor', name='usertype'), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('subusers', 'type')
    # ### end Alembic commands ###

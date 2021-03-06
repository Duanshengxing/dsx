"""empty message

Revision ID: 4c08c2cea32b
Revises: defa14e37bb1
Create Date: 2018-10-17 11:06:42.192328

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c08c2cea32b'
down_revision = 'defa14e37bb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cinemas',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('district', sa.String(length=100), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('phone', sa.String(length=100), nullable=True),
    sa.Column('score', sa.Float(), nullable=True),
    sa.Column('hallnum', sa.Integer(), nullable=True),
    sa.Column('servicecharge', sa.Float(), nullable=True),
    sa.Column('astrict', sa.Integer(), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cinemas')
    # ### end Alembic commands ###

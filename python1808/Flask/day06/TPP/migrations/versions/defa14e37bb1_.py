"""empty message

Revision ID: defa14e37bb1
Revises: deab68da9a3a
Create Date: 2018-10-17 09:20:30.316172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'defa14e37bb1'
down_revision = 'deab68da9a3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('movies',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('showname', sa.String(length=50), nullable=True),
    sa.Column('shownameen', sa.String(length=200), nullable=True),
    sa.Column('director', sa.String(length=200), nullable=True),
    sa.Column('leadingRole', sa.String(length=200), nullable=True),
    sa.Column('type', sa.String(length=200), nullable=True),
    sa.Column('country', sa.String(length=200), nullable=True),
    sa.Column('language', sa.String(length=200), nullable=True),
    sa.Column('duration', sa.Integer(), nullable=True),
    sa.Column('screeningmodel', sa.String(length=200), nullable=True),
    sa.Column('openday', sa.DateTime(), nullable=True),
    sa.Column('backgroundpicture', sa.String(length=200), nullable=True),
    sa.Column('flag', sa.Integer(), nullable=True),
    sa.Column('isdelete', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('movies')
    # ### end Alembic commands ###

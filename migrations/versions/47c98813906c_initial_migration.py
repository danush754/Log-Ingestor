"""Initial migration

Revision ID: 47c98813906c
Revises: 
Create Date: 2023-11-20 11:21:15.776656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47c98813906c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('level', sa.String(length=50), nullable=True),
    sa.Column('message', sa.Text(), nullable=True),
    sa.Column('resoureID', sa.String(length=50), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('traceID', sa.String(length=50), nullable=True),
    sa.Column('spanID', sa.String(length=50), nullable=True),
    sa.Column('commit', sa.String(length=50), nullable=True),
    sa.Column('parentResourceId', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('log')
    # ### end Alembic commands ###

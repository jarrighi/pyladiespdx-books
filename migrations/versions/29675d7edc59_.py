"""empty message

Revision ID: 29675d7edc59
Revises: 57d7a4d2dc24
Create Date: 2015-07-06 23:28:32.969796

"""

# revision identifiers, used by Alembic.
revision = '29675d7edc59'
down_revision = '57d7a4d2dc24'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('possessor', sa.String(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'possessor')
    ### end Alembic commands ###

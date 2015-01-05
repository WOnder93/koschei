"""Add table for admin notices

Revision ID: 525ad809cccb
Revises: 260dfbee9be1
Create Date: 2015-01-05 16:28:37.829171

"""

# revision identifiers, used by Alembic.
revision = '525ad809cccb'
down_revision = '260dfbee9be1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_notice',
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('key')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin_notice')
    ### end Alembic commands ###

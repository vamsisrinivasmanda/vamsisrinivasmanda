"""dbthirdmig

Revision ID: 52152c3da058
Revises: b3f6ff11e75e
Create Date: 2020-04-27 12:05:20.509973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52152c3da058'
down_revision = 'b3f6ff11e75e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_image', sa.String(length=70), nullable=False))
    op.drop_column('users', 'profileimage')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profileimage', sa.VARCHAR(length=70), nullable=False))
    op.drop_column('users', 'profile_image')
    # ### end Alembic commands ###

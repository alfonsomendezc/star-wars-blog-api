"""empty message

Revision ID: 3e65977cbeb4
Revises: 057c57ed9de2
Create Date: 2022-05-31 21:37:00.244688

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e65977cbeb4'
down_revision = '057c57ed9de2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('people', sa.Column('skin_color', sa.String(length=120), nullable=False))
    op.create_unique_constraint(None, 'people', ['skin_color'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'people', type_='unique')
    op.drop_column('people', 'skin_color')
    # ### end Alembic commands ###

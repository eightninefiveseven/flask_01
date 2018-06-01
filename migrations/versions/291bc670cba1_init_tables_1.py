"""init_tables_1

Revision ID: 291bc670cba1
Revises: 0b01656fb735
Create Date: 2018-05-30 16:59:44.505406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '291bc670cba1'
down_revision = '0b01656fb735'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('author', sa.Column('name2', sa.String(length=64), nullable=True))
    op.create_unique_constraint(None, 'author', ['name2'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'author', type_='unique')
    op.drop_column('author', 'name2')
    # ### end Alembic commands ###
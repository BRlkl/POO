"""empty message

Revision ID: 90b4c48a3e0f
Revises: 8e61e2a00d5e
Create Date: 2023-02-20 21:14:20.212383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90b4c48a3e0f'
down_revision = '8e61e2a00d5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.add_column(sa.Column('nome', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('categoria', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.drop_column('categoria')
        batch_op.drop_column('nome')

    # ### end Alembic commands ###

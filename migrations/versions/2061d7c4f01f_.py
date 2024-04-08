"""empty message

Revision ID: 2061d7c4f01f
Revises: 469c23c90924
Create Date: 2024-03-26 16:45:03.840380

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2061d7c4f01f'
down_revision = '469c23c90924'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('temperature', schema=None) as batch_op:
        batch_op.alter_column('temperature',
               existing_type=sa.NUMERIC(precision=2),
               type_=sa.Double(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('temperature', schema=None) as batch_op:
        batch_op.alter_column('temperature',
               existing_type=sa.Double(),
               type_=sa.NUMERIC(precision=2),
               existing_nullable=False)

    # ### end Alembic commands ###

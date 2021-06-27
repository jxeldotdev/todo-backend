"""Initial Tables

Revision ID: e027c0dc791b
Revises:
Create Date: 2021-06-26 00:01:16.808757

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e027c0dc791b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('todo',
                    sa.Column(
                        'id', postgresql.UUID(
                            as_uuid=True), nullable=False),
                    sa.Column('title', sa.String(length=128), nullable=False),
                    sa.Column('notes', sa.String(length=256), nullable=False),
                    sa.Column('completed', sa.Boolean(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todo')
    # ### end Alembic commands ###

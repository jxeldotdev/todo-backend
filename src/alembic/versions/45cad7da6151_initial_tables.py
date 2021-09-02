"""initial Tables

Revision ID: 45cad7da6151
Revises: 4ee595c9eacd
Create Date: 2021-08-29 14:32:26.630921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "45cad7da6151"
down_revision = "4ee595c9eacd"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "todo",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=128), nullable=False),
        sa.Column("notes", sa.String(length=256), nullable=False),
        sa.Column("completed", sa.Boolean(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False, server_default=sa.sql.func.now()),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("todo")
    # ### end Alembic commands ###

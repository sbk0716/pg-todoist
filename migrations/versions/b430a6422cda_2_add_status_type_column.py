"""2_add_status_type_column

Revision ID: b430a6422cda
Revises: e5cc805f99e4
Create Date: 2022-01-16 08:09:12.304373

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "b430a6422cda"
down_revision = "e5cc805f99e4"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("tasks", sa.Column("status_type", sa.Integer(), nullable=False))
    op.create_index(op.f("ix_tasks_status_type"), "tasks", ["status_type"], unique=False)
    op.create_index(op.f("ix_tasks_title"), "tasks", ["title"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_tasks_title"), table_name="tasks")
    op.drop_index(op.f("ix_tasks_status_type"), table_name="tasks")
    op.drop_column("tasks", "status_type")
    # ### end Alembic commands ###

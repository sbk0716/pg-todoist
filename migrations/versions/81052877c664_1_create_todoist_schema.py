"""1_create_todoist_schema

Revision ID: 81052877c664
Revises: 
Create Date: 2022-01-18 21:57:59.036277

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "81052877c664"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ============================================================
    # [MANUAL]CREATE SCHEMA IF NOT EXISTS "todoist";
    # ============================================================
    op.execute('CREATE SCHEMA IF NOT EXISTS "todoist";')


def downgrade():
    # ============================================================
    # [MANUAL]DROP SCHEMA IF EXISTS "todoist";
    # ============================================================
    op.execute('DROP SCHEMA IF EXISTS "todoist";')

"""Rename room id field

Revision ID: 26b9be4716f8
Revises: e8fba2b19c6b
Create Date: 2022-03-17 20:14:21.285406

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26b9be4716f8'
down_revision = 'e8fba2b19c6b'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column(
        table_name="room",
        column_name="id",
        new_column_name="room_id"
    )


def downgrade():
    op.alter_column(
        table_name="room",
        column_name="room_id",
        new_column_name="id"
    )

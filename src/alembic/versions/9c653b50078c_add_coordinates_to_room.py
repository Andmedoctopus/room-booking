"""Add coordinates to room

Revision ID: 9c653b50078c
Revises: 26b9be4716f8
Create Date: 2022-03-18 17:38:09.382045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c653b50078c'
down_revision = '26b9be4716f8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        table_name="room",
        column=sa.Column("longitude", sa.String, nullable=True),
    )

    op.add_column(
        table_name="room",
        column=sa.Column("latitude", sa.String, nullable=True),
    )


def downgrade():
    pass

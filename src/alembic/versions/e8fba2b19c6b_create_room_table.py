"""create room table

Revision ID: e8fba2b19c6b
Revises: 
Create Date: 2021-07-22 22:13:53.591899

"""
from alembic import op
from sqlalchemy import Column,Integer, String, text
from sqlalchemy.schema import CreateSequence
from room_booking.infrastructure.models.room import room_id_seq

# revision identifiers, used by Alembic.
revision = 'e8fba2b19c6b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute(CreateSequence(room_id_seq))
    op.create_table(
        "room",
        Column("id", Integer, room_id_seq, primary_key=True, server_default=text(f"nextval('{room_id_seq.name}'::regclass)")),
        Column("name", String),
        Column("floor", Integer, nullable=False),
        Column("number", Integer, nullable=False),
    )


def downgrade():
    pass

"""followers

Revision ID: ae346256b650
Revises: 37f06a334dbf
Create Date: 2017-09-17 15:41:30.211082

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "ae346256b650"
down_revision = "37f06a334dbf"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "followers",
        sa.Column("follower_id", sa.Integer(), nullable=True),
        sa.Column("followed_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["followed_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["follower_id"],
            ["user.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("followers")
    # ### end Alembic commands ###

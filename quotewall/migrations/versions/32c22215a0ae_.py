"""empty message

Revision ID: 32c22215a0ae
Revises: 
Create Date: 2017-02-27 01:22:31.920175

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32c22215a0ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('registration_link',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', sa.String(length=32), nullable=True),
    sa.Column('uses', sa.Integer(), nullable=True),
    sa.Column('expires', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('users', sa.Column('is_admin', sa.Boolean(), server_default=sa.false(), nullable=False))
    op.add_column('users', sa.Column('registration_link_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'registration_link', ['registration_link_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'registration_link_id')
    op.drop_column('users', 'is_admin')
    op.drop_table('registration_link')
    # ### end Alembic commands ###

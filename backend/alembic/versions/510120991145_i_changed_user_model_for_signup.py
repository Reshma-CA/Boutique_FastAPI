"""I changed user model for signup

Revision ID: 510120991145
Revises: c0872d2dfc9a
Create Date: 2024-11-27 20:35:33.770541

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '510120991145'
down_revision: Union[str, None] = 'c0872d2dfc9a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    # Add 'confirm_password' column
    op.add_column('user', sa.Column('confirm_password', sa.String(), nullable=False, server_default=''))

    # Add 'username' column with nullable=True initially to avoid issues with existing records
    op.add_column('user', sa.Column('username', sa.String(), nullable=True))

    # Update all records to ensure 'username' has a value
    op.execute("UPDATE \"user\" SET username = 'default_username' WHERE username IS NULL")

    # Alter 'username' column to be NOT NULL after it is populated for all records
    op.alter_column('user', 'username', nullable=False)
    
    # Alter 'confirm_password' to be NOT NULL
    op.alter_column('user', 'confirm_password', nullable=False)

def downgrade() -> None:
    # Remove the 'confirm_password' and 'username' columns
    op.drop_column('user', 'confirm_password')
    op.drop_column('user', 'username')



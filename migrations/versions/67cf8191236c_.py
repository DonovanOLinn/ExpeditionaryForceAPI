"""empty message

Revision ID: 67cf8191236c
Revises: 
Create Date: 2022-06-23 18:21:24.151492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67cf8191236c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(length=80), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.drop_constraint('characters_first_appearence_fkey', 'characters', type_='foreignkey')
    op.drop_constraint('characters_species_name_fkey', 'characters', type_='foreignkey')
    op.alter_column('planets', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('ships', 'shipname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_constraint('ships_species_name_fkey', 'ships', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('ships_species_name_fkey', 'ships', 'species', ['species_name'], ['species_name'])
    op.alter_column('ships', 'shipname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('planets', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_foreign_key('characters_species_name_fkey', 'characters', 'species', ['species_name'], ['species_name'])
    op.create_foreign_key('characters_first_appearence_fkey', 'characters', 'books', ['first_appearence'], ['bookname'])
    op.drop_table('user')
    # ### end Alembic commands ###

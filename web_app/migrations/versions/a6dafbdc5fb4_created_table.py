"""created table

Revision ID: a6dafbdc5fb4
Revises: 
Create Date: 2022-11-25 16:30:47.733847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6dafbdc5fb4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('company',
    sa.Column('ein_id', sa.Integer(), nullable=False),
    sa.Column('adsh', sa.Text(), nullable=True),
    sa.Column('cik_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('sic', sa.Integer(), nullable=True),
    sa.Column('countryba', sa.Text(), nullable=True),
    sa.Column('stprba', sa.Text(), nullable=True),
    sa.Column('cityba', sa.Text(), nullable=True),
    sa.Column('zipba', sa.Text(), nullable=True),
    sa.Column('bas1', sa.Text(), nullable=True),
    sa.Column('bas2', sa.Text(), nullable=True),
    sa.Column('baph', sa.Text(), nullable=True),
    sa.Column('countryma', sa.Text(), nullable=True),
    sa.Column('stprma', sa.Text(), nullable=True),
    sa.Column('cityma', sa.Text(), nullable=True),
    sa.Column('zipma', sa.Text(), nullable=True),
    sa.Column('mas1', sa.Text(), nullable=True),
    sa.Column('mas2', sa.Text(), nullable=True),
    sa.Column('countryinc', sa.Text(), nullable=True),
    sa.Column('stprinc', sa.Text(), nullable=True),
    sa.Column('former', sa.Text(), nullable=True),
    sa.Column('changed', sa.Integer(), nullable=True),
    sa.Column('afs', sa.Text(), nullable=True),
    sa.Column('wksi', sa.Integer(), nullable=True),
    sa.Column('fye', sa.Integer(), nullable=True),
    sa.Column('form', sa.Text(), nullable=True),
    sa.Column('period', sa.Integer(), nullable=True),
    sa.Column('fy', sa.Integer(), nullable=True),
    sa.Column('fp', sa.Text(), nullable=True),
    sa.Column('filed', sa.Integer(), nullable=True),
    sa.Column('accepted', sa.Text(), nullable=True),
    sa.Column('prevrpt', sa.Integer(), nullable=True),
    sa.Column('detail', sa.Integer(), nullable=True),
    sa.Column('instance', sa.Text(), nullable=True),
    sa.Column('nciks', sa.Integer(), nullable=True),
    sa.Column('aciks', sa.Text(), nullable=True),
    sa.Column('edgar_year', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('ein_id')
    )
    op.create_table('financial',
    sa.Column('record_id', sa.Integer(), nullable=False),
    sa.Column('tag_sec', sa.Text(), nullable=True),
    sa.Column('label_sec', sa.Text(), nullable=True),
    sa.Column('report', sa.Text(), nullable=True),
    sa.Column('line', sa.Text(), nullable=True),
    sa.Column('stmt', sa.Text(), nullable=True),
    sa.Column('data_date', sa.Text(), nullable=True),
    sa.Column('fy', sa.Text(), nullable=True),
    sa.Column('fq', sa.Text(), nullable=True),
    sa.Column('qtrs', sa.Text(), nullable=True),
    sa.Column('uom', sa.Text(), nullable=True),
    sa.Column('tag_renamed', sa.Text(), nullable=True),
    sa.Column('value', sa.Text(), nullable=True),
    sa.Column('line_item', sa.Text(), nullable=True),
    sa.Column('url', sa.Text(), nullable=True),
    sa.Column('ein_id', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['ein_id'], ['company.ein_id'], ),
    sa.PrimaryKeyConstraint('record_id')
    )
    op.create_index(op.f('ix_financial_ein_id'), 'financial', ['ein_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_financial_ein_id'), table_name='financial')
    op.drop_table('financial')
    op.drop_table('company')
    # ### end Alembic commands ###
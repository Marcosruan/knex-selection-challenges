"""migracao inicial

Revision ID: c0ffca9300a3
Revises: 
Create Date: 2025-06-24 23:51:20.475776

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c0ffca9300a3'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Deputados',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('uf', sa.String(), nullable=False),
    sa.Column('cpf', sa.String(), nullable=True),
    sa.Column('partido', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Deputados_id'), 'Deputados', ['id'], unique=False)
    op.create_table('Despesas',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('dataEmissao', sa.String(), nullable=True),
    sa.Column('fornecedor', sa.String(), nullable=True),
    sa.Column('valorLiquido', sa.Float(), nullable=True),
    sa.Column('deputado_id', sa.Integer(), nullable=True),
    sa.Column('urlDocumento', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['deputado_id'], ['Deputados.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Despesas')
    op.drop_index(op.f('ix_Deputados_id'), table_name='Deputados')
    op.drop_table('Deputados')
    # ### end Alembic commands ###

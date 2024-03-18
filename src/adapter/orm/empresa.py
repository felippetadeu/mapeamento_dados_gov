from decimal import Decimal
from typing import Optional
from src.adapter.orm.base import Base
from sqlmodel import Field

class Empresa(Base):
    __tablename__ = 'empresas'
    id: Optional[int] = Field(default=None, primary_key=True)
    cnpj_basico: Optional[str] = Field(default=None)
    razao_social: Optional[str] = Field(default=None)
    natureza_juridica: Optional[str] = Field(default=None)
    qualificacao_responsavel: Optional[int] = Field(default=None)
    capital_social: Optional[Decimal] = Field(default=None, decimal_places=2, max_digits=10)
    porte_empresa: Optional[int] = Field(default=None)
    ente_federativo_responsavel: Optional[str] = Field(default=None)

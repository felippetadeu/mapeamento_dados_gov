from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field

class Base(SQLModel):
    u_inclusao: Optional[int] = Field(default=None, description='Código usuário da inclusão')
    inclusao: Optional[datetime] = Field(default=None, description='Data e Hora da inclusão')
    u_alteracao: Optional[int] = Field(default=None, description='Código usuário da alteração')
    alteracao: Optional[datetime] = Field(default=None, description='Data e Hora da alteração')
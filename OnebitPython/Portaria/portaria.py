from datetime import datetime
from typing import Optional

class Convidado:
    def __init__(self, nome: str, status: str = "pendente", entrada_em: str = "", codigo: Optional[str] = None):
        self._nome = nome
        self._status = status
        self._entrada_em = entrada_em

        if codigo:
            self._codigo = codigo
        else:
            self._codigo = self._gerar_codigo(nome)

    def _gerar_codigo(self, nome: str) -> str:
        return (nome[:3] + nome[-2:]).upper()

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def codigo(self) -> str:
        return self._codigo

    @property
    def status(self) -> str:
        return self._status

    @property
    def entrada_em(self) -> str:
        return self._entrada_em

class GerenciadorPortaria:
    pass
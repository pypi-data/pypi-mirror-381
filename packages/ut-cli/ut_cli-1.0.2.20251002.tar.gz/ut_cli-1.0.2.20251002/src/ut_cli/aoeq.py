# coding=utf-8
from typing import Any

TyArr = list[Any]
TyDoEq = dict[Any, Any]
TyStr = str


class AoEq:
    """ Dictionary of Equates
    """
    @classmethod
    def sh_d_eq(cls, a_eq: TyArr) -> TyDoEq:
        _d_eq: TyDoEq = {}
        for eq in a_eq:
            _a_eq = eq.split('=')
            _d_eq[_a_eq[0]] = _a_eq[1]
        return _d_eq

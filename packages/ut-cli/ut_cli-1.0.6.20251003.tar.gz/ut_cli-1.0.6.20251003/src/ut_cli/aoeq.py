# coding=utf-8
from typing import Any

TyArr = list[Any]
TyDic = dict[Any, Any]
TyStr = str


class AoEq:
    """ Dictionary of Equates
    """
    @classmethod
    def sh_d_eq(cls, a_eq: TyArr) -> TyDic:
        _d_eq: TyDic = {}
        for eq in a_eq:
            _a_kv: TyArr = eq.split('=')
            _k = _a_kv[0]
            _v = _a_kv[1]
            if _k == 'cmd':
                _d_eq[_k] = _v.split()
            else:
                _d_eq[_k] = _v
        return _d_eq

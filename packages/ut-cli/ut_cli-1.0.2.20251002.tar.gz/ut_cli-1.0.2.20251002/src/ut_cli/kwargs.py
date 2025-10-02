from ut_dic.dic import Dic
from ut_cli.aoeq import AoEq
from ut_cli.doeq import DoEq

from typing import Any
TyAny = Any
TyArr = list[Any]
TyDic = dict[Any, Any]
TyDoEq = dict[Any, Any]

TnDic = None | TyDic
TnDoEq = None | TyDoEq


class KwArgs:
    """
    Command Line Interface
    """
    @staticmethod
    def sh_d_parms(d_eq: TyDoEq, d_parms: TnDic) -> TnDoEq:
        if d_parms is None:
            return None
        if 'cmd' in d_eq:
            _a_cmd: TyArr = d_eq['cmd']
            _d_parms: TnDoEq = Dic.locate(d_parms, _a_cmd)
            return _d_parms
        else:
            return d_parms

    @classmethod
    def sh(cls, cls_com, cls_app, sys_argv: TyArr) -> TyDic:
        """
        show keyword arguments
        """
        _args = sys_argv[1:]
        _d_eq: TyDic = AoEq.sh_d_eq(_args)
        _cls_parms, _cls_task = cls_app.sh_cls_parms_task(_d_eq)
        _d_eq_new: TyDic = DoEq.verify(_d_eq, _cls_parms.d_parms)

        _sh_prof = _d_eq_new.get('sh_prof')
        if callable(_sh_prof):
            _d_eq_new['sh_prof'] = _sh_prof()
        _d_eq_new['cls_parms'] = _cls_parms
        _d_eq_new['cls_task'] = _cls_task
        _d_eq_new['cls_app'] = cls_app
        _d_eq_new['com'] = cls_com

        return _d_eq_new

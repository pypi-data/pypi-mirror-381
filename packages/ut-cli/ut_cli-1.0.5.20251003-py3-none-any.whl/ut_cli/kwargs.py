from ut_dic.dic import Dic
from ut_cli.aoeq import AoEq
from ut_cli.doeq import DoEq

from typing import Any
TyAny = Any
TyArr = list[Any]
TyDic = dict[Any, Any]
TyTup = tuple[Any, Any]

TnDic = None | TyDic
TnTup = tuple[None | Any, None | Any]


class KwArgs:
    """
    Keyword arguments processor
    """
    @staticmethod
    def sh_cls_parms_task(cls_app, d_eq: TyDic) -> TnTup:
        if 'cmd' in d_eq:
            _t_parms_task: TyTup = Dic.locate(cls_app.d_parms_task, d_eq['cmd'][0])
            return _t_parms_task
        return None, None

    @classmethod
    def sh(cls, cls_com, cls_app, sys_argv: TyArr) -> TyDic:
        """
        show keyword arguments
        """
        _args = sys_argv[1:]
        _d_eq: TyDic = AoEq.sh_d_eq(_args)
        _cls_parms, _cls_task = cls.sh_cls_parms_task(cls_app, _d_eq)
        if _cls_parms is not None:
            _d_parms = _cls_parms.d_parms
        else:
            _d_parms = None
        _d_eq_new: TyDic = DoEq.verify(_d_eq, _d_parms)

        _sh_prof = _d_eq_new.get('sh_prof')
        if callable(_sh_prof):
            _d_eq_new['sh_prof'] = _sh_prof()
        _d_eq_new['cls_parms'] = _cls_parms
        _d_eq_new['cls_task'] = _cls_task
        _d_eq_new['cls_app'] = cls_app
        _d_eq_new['com'] = cls_com

        return _d_eq_new

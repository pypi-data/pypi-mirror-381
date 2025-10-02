# coding=utf-8

from ut_dic.dic import Dic
from ut_obj.str import Str
from ut_obj.strdate import StrDate

from typing import Any
from collections.abc import Callable

TyArr = list[Any]
TyDic = dict[Any, Any]
TyCallable = Any | Callable[..., Any]
TyDoEq = dict[str, Any]
TyStr = str

TnArr = None | TyArr
TnDic = None | TyDic
TnDoEq = None | TyDoEq
TnStr = None | TyStr


class DoEq:
    """ Manage Commandline Arguments
    """
    sh_value_msg1 = "Wrong parameter: {}; valid parameters are: {}"
    sh_value_msg2 = "Parameter={} value={} is invalid; valid values are={}"

    @classmethod
    def verify(cls, d_eq: TyDoEq, d_parms: TnDic) -> TyDoEq:
        if not d_parms:
            return d_eq

        _d_eq_new = {}
        _cmd = d_eq.pop('cmd', None)
        if _cmd is not None:
            _a_cmd = _cmd.split()
            _d_eq_new['cmd'] = _cmd.split()
            _d_parms = Dic.locate(d_parms, _a_cmd)
        else:
            _d_parms = d_parms

        for _key, _value in d_eq.items():
            _type: TnStr = _d_parms.get(_key)
            if _type is None:
                raise Exception(cls.sh_value_msg1.format(_key, _d_parms))
            match _type:
                case 'str':
                    pass
                case 'int':
                    _value = int(_value)
                case 'bool':
                    _value = Str.sh_boolean(_value)
                case 'dict':
                    _value = Str.sh_dic(_value)
                case 'list':
                    _value = Str.sh_arr(_value)
                case '%Y-%m-%d':
                    _value = StrDate.sh(_value, _type)
                case '_':
                    match _type[0]:
                        case '{':
                            _obj = Str.sh_dic(_type)
                            if _value not in _obj:
                                raise Exception(cls.sh_value_msg2.format(_value, _obj))
                        case '[':
                            _obj = Str.sh_dic(_type)
                            if _value not in _obj:
                                raise Exception(cls.sh_value_msg2.format(_value, _obj))
            _d_eq_new[_key] = _value
        return _d_eq_new

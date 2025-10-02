# SPDX-FileCopyrightText: 2025 Genome Research Ltd.
#
# SPDX-License-Identifier: MIT

from typing import Any

from flask import request


class NoArg:
    """
    Flags an parameter which was not specified in the request, distinguishing
    it from `None`, which is a valid argument when searching for SQL `null`
    values.
    """


class RequestArgs:
    """
    Takes the Flask request.args values and (case-insensitively) transforms
    the string values:

        'null'  -> None
        'true'  -> True
        'flase' -> False

    Long strings are truncated to 256 characters to guard against excessively
    long param values being passed to the SQL layer.
    """

    def __init__(self) -> None:
        self.__req_args = self.parse_args(request.args)

    @classmethod
    def parse_args(cls, arg_dict: dict[str, str]) -> dict[str, Any]:
        parsed = {}
        for arg, val in arg_dict.items():
            val = val[:256]
            match val.lower():
                case 'null':
                    val = None
                case 'true':
                    val = True
                case 'false':
                    val = False
            parsed[arg] = val
        return parsed

    def pop_default(self, arg: str, default: Any) -> Any:
        """
        Removes the arg if present in the instance and returns it, or the
        default value (which must be specified).
        """
        return self.__req_args.pop(arg, default)

    def pop_arg(self, arg: str) -> NoArg | Any:
        """
        Removes the arg if present in the instance and returns it, or `NoArg`
        if it is not present.
        """
        return self.__req_args.pop(arg) if arg in self.__req_args else NoArg

    def pop_args_dict(self, *args: str) -> dict[str, Any]:
        """
        Removes any of the args which are present in the instance, returning
        them in a dict keyed under their names.
        """
        ret = {}
        for n in args:
            if n in self.__req_args:
                ret[n] = self.__req_args.pop(n)
        return ret

    def pop_all(self) -> dict[str, Any]:
        """
        Empty instance of arguments, returning them as a dict.
        """
        ret = self.__req_args
        self.__req_args = None
        return ret

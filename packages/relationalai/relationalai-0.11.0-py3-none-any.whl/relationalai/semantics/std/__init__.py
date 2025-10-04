from __future__ import annotations
from typing import Any

from relationalai.semantics.internal import internal as i
from .std import _Date, _DateTime, _Number, _String, _Integer, _make_expr
from . import dates, math, strings, decimals, integers, floats, pragmas, constraints

def range(*args: _Integer) -> i.Expression:
    # supports range(stop), range(start, stop), range(start, stop, step)
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise ValueError(f"range expects 1, 2, or 3 arguments, got {len(args)}")
    step = step if isinstance(step, i.ConceptMember) and step._op == i.Int64 else cast(i.Int64, step)
    start = start if isinstance(start, i.ConceptMember) and start._op == i.Int64 else cast(i.Int64, start)
    # unlike Python, Rel's range is 1..stop inclusive, so we need to subtract 1 from stop
    return _make_expr("range", start, cast(i.Int64, stop-1), step, i.Int64.ref("res"))

def hash(*args: Any, type=i.Hash) -> i.Expression:
    if len(args) == 0:
        raise ValueError("hash expects at least one argument")
    return _make_expr("hash", i.TupleArg(args), type.ref("res"))

def uuid_to_string(arg:_Integer) -> i.Expression:
    return _make_expr("uuid_to_string", arg, i.String.ref("res"))

def cast(type: i.Concept, arg: _Date|_DateTime|_Number|_String) -> i.Expression:
    return _make_expr("cast", i.TypeRef(type), arg, type.ref("res"))

__all__ = [
    "range",
    "hash",
    "cast",
    "dates",
    "math",
    "strings",
    "decimals",
    "integers",
    "floats",
    "pragmas",
    "constraints",
    "uuid_to_string"
]

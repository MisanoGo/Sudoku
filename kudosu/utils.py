from typing import Any, Iterable
from time import sleep, time

def NoneFilter(itrable:Iterable):
    return list(filter(lambda i:i is not None,itrable))

def checkEquality(itrable: Iterable) -> bool:
    return True if len(set(itrable)) == 1 else False

def checkCountEqualty(*itrables: Iterable) -> bool:
    return checkEquality([len(itrable) for itrable in itrables])

def checkDepublicate(itrable:Iterable):
    itrable = NoneFilter(itrable)
    return checkCountEqualty(set(itrable),itrable)

def checkListDepublicate(*itrables:Iterable):
    return all([checkDepublicate(itrable) for itrable in itrables])

def noneable(a: Any, b: Any):
    return a if a is not None else b

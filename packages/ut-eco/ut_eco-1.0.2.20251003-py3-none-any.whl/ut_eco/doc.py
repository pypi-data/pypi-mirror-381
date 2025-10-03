"""
This module provides utility classes for the management of OmniTracker
EcoVadis NHRR (Nachhaltigkeits Risiko Rating) processing for Department UMH
"""
from ut_eco.rst.taskioc import TaskIoc as EcoRstTaskIoc
from ut_eco.xls.taskioc import TaskIoc as EcoXlsTaskIoc

from typing import Any, Callable
TyCallable = Callable[..., Any]
TyDoC = dict[str, TyCallable]
TyDoDoC = dict[str, TyDoC]


DoDoC: TyDoDoC = {
    'srr': {
        'xls': {
            'evupadm': EcoXlsTaskIoc.evupadm,
            'evupdel': EcoXlsTaskIoc.evupdel,
            'evupreg': EcoXlsTaskIoc.evupreg,
            'evdomap': EcoXlsTaskIoc.evdomap,
        },
        'rst': {
            'evupadm': EcoRstTaskIoc.evupadm,
            'evupdel': EcoRstTaskIoc.evupdel,
            'evupreg': EcoRstTaskIoc.evupreg,
            'evdoexp': EcoRstTaskIoc.evdoexp,
            'evdomap': EcoRstTaskIoc.evdomap,
        },
    },
}

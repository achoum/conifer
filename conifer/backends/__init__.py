import sys
import importlib.util

from conifer.backends import xilinxhls

SPEC_XILINXHLS = importlib.util.find_spec('.xilinxhls', __name__)

vivadohls = importlib.util.module_from_spec(SPEC_XILINXHLS)
vivadohls._tool = 'vivadohls'
SPEC_XILINXHLS.loader.exec_module(vivadohls)

vitishls = importlib.util.module_from_spec(SPEC_XILINXHLS)
vitishls._tool = 'vitishls'
SPEC_XILINXHLS.loader.exec_module(vitishls)

del SPEC_XILINXHLS

from conifer.backends import vhdl
from conifer.backends import cpp
from conifer.backends import fpu
from conifer.backends import boards

class python_backend:
  '''
  Simple backend to make a ModelBase object
  '''
  def make_model(ensembleDict, config):
    from conifer.model import ModelBase
    return ModelBase(ensembleDict, config)

_backend_map = {'xilinxhls' : xilinxhls,
                'vivadohls' : vivadohls,
                'vitishls'  : vitishls,
                'vhdl'      : vhdl,
                'cpp'       : cpp,
                'fpu'       : fpu,
                'python'    : python_backend,
                'py'        : python_backend,
                }

def get_backend(backend):
  '''Get backend object from string'''
  backend_obj = _backend_map.get(backend)
  if backend_obj is None:
    raise RuntimeError(f'No backend "{backend}" found. Options are {[k for k in _backend_map.keys()]}')
  return backend_obj

def get_available_backends():
  return [k for k in _backend_map.keys()]

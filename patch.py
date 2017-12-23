import os
import sys

import vim

sys.path.insert(0, vim.eval('expand(s:script_path)'))

python_executable = vim.vars.get('jedi_rpc#python')
jedi_pythonx_path = os.path.dirname(jedi_vim.__file__)

try:
    import jedi_remote

    if not isinstance(jedi_vim.jedi, jedi_remote.JediRemote):
        jedi_vim.jedi = jedi_remote.JediRemote(
            python_executable,
            jedi_pythonx_path=jedi_pythonx_path
        )

finally:
    sys.path.pop(0)

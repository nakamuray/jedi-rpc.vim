import os
import sys

import vim

sys.path.insert(0, vim.eval('expand(s:script_path)'))

python_executable = vim.vars.get('jedi_rpc#python')
jedi_path = os.path.join(os.path.dirname(jedi_vim.__file__), 'jedi')

try:
    import jedi_remote

    if not isinstance(jedi_vim.jedi, jedi_remote.JediRemote):
        jedi_vim.jedi = jedi_remote.JediRemote(python_executable,
                                               jedi_path=jedi_path)

finally:
    sys.path.pop(0)

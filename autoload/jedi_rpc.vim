let s:script_path = fnameescape(expand('<sfile>:p:h:h'))

function! jedi_rpc#init()
  if !jedi#init_python()
    finish
  endif

  if has('python')
    execute 'pyfile ' . s:script_path . '/patch.py'
  endif

  if has('python3')
    execute 'py3file ' . s:script_path . '/patch.py'
  endif
endfunction

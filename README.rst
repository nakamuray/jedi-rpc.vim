**Because recent version of jedi has similar separate python process method to support venv,
you don't need to use this workaround plugin anymore**

jedi-rpc.vim
============

Complemental plugin for jedi-vim to run python as a separate process.

It patch jedi-vim and allow you to get completion result using any version of
python you want, not restricted by the version vim linked.


Installation
============

Install both jedi-vim and jedi-rpc.


Settings
========

``g:jedi_rpc#python``
  Python executable name jedi-rpc use.

  default: ``python``

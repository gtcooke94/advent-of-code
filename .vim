set nocompatible              " be iMproved, required
filetype off                  " required 
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
"call vundle#begin('~/some/path/here')
Plugin 'VundleVim/Vundle.vim' 
Plugin 'Shougo/deoplete.nvim'
Plugin 'deoplete-plugins/deoplete-jedi'
call vundle#end()            " required
filetype plugin indent on    " required
let g:deoplete#enable_at_startup = 1
let g:python3_host_prog = '/Users/gcooke/.virtualenvs/neovim/bin/python3'
let g:python_host_prog = '/Users/gcooke/.virtualenvs/neovim2/bin/python2'
call deoplete#custom#source('jedi', 'is_debug_enabled', 1)
call deoplete#enable_logging('DEBUG', '/tmp/deoplete.log')

set number
syntax on
set expandtab
set tabstop=4 softtabstop=4
set shiftwidth=4
set smartindent
set noswapfile
set incsearch
set laststatus=2
set noshowmode

call plug#begin('~/.vim/plugged')

Plug 'scrooloose/nerdtree'
Plug 'yggdroot/indentline'
Plug 'scrooloose/nerdcommenter'
Plug 'itchyny/lightline.vim'
Plug 'terryma/vim-multiple-cursors'
Plug 'ap/vim-css-color'
Plug 'vimwiki/vimwiki'
"Plug 'ycm-core/YouCompleteMe'
"Plug 'neoclide/coc.nvim', {'branch': 'release'}

call plug#end()

let $PYTHONPATH="/usr/lib/python3.8/site-packages"
let g:indentLine_color_term = 243
let g:indentLine_char = '┊'
let g:lightline = {'colorscheme': 'wombat',}
let mapleader = " "

let g:termdebug_wide=1
packadd termdebug

"nmap <C-n> :NERDTreeToggle<CR>
colo rexocyan

hi Comment ctermfg = 7
"hi Identifier ctermfg = 5
"hi Statement ctermfg = 12
"hi PreProc ctermfg = 7 cterm = italic
"hi Type ctermfg = 3
"hi Special ctermfg = 5
"hi Function ctermfg = 1 cterm = bold
"hi String ctermfg = 2

"highlight LineNr           ctermfg=8    ctermbg=none    cterm=none
"highlight CursorLineNr     ctermfg=7    ctermbg=8       cterm=none
"highlight VertSplit        ctermfg=0    ctermbg=8       cterm=none
"highlight Statement        ctermfg=2    ctermbg=none    cterm=none
"highlight Directory        ctermfg=4    ctermbg=none    cterm=none
"highlight StatusLine       ctermfg=7    ctermbg=8       cterm=none
"highlight StatusLineNC     ctermfg=7    ctermbg=8       cterm=none
"highlight NERDTreeClosable ctermfg=2
"highlight NERDTreeOpenable ctermfg=8
"highlight Comment          ctermfg=4    ctermbg=none    cterm=none
"highlight Constant         ctermfg=12   ctermbg=none    cterm=none
"highlight Special          ctermfg=4    ctermbg=none    cterm=none
"highlight Identifier       ctermfg=6    ctermbg=none    cterm=none
"highlight PreProc          ctermfg=5    ctermbg=none    cterm=none
"highlight String           ctermfg=12   ctermbg=none    cterm=none
"highlight Number           ctermfg=1    ctermbg=none    cterm=none
"highlight Function         ctermfg=1    ctermbg=none    cterm=none

let g:vimwiki_list = [{'path': '~/My/vimwiki/', 'syntax': 'markdown', 'ext': '.wiki'}]

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

" for vimwiki
set nocompatible
filetype plugin on

call plug#begin('~/.vim/plugged')

Plug 'scrooloose/nerdtree'
Plug 'yggdroot/indentline'
Plug 'scrooloose/nerdcommenter'
Plug 'itchyny/lightline.vim'
Plug 'terryma/vim-multiple-cursors'
Plug 'ap/vim-css-color'
Plug 'vimwiki/vimwiki'
Plug 'davisdude/vim-love-docs'
Plug 'ycm-core/YouCompleteMe'
Plug 'joshdick/onedark.vim'
Plug 'drewtempelmeyer/palenight.vim'
Plug 'cocopon/iceberg.vim'
"Plug 'neoclide/coc.nvim', {'branch': 'release'}
call plug#end()

colo iceberg

let $PYTHONPATH="/usr/lib/python3.8/site-packages"
let g:indentLine_color_term = 243
let g:indentLine_char = '┊'
let g:lightline = {'colorscheme': 'wombat',}
let mapleader = " "

let g:termdebug_wide=1
packadd termdebug

nmap <leader>n :NERDTreeToggle<CR>
nmap <leader>l :!love .<CR>

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

let g:vimwiki_list = [{'path': '~/My/vimwiki/', 'ext': '.wiki'}]

"Use 24-bit (true-color) mode in Vim/Neovim when outside tmux.
"If you're using tmux version 2.2 or later, you can remove the outermost $TMUX check and use tmux's 24-bit color support
"(see < http://sunaku.github.io/tmux-24bit-color.html#usage > for more information.)
if (empty($TMUX))
  if (has("nvim"))
    "For Neovim 0.1.3 and 0.1.4 < https://github.com/neovim/neovim/pull/2198 >
    let $NVIM_TUI_ENABLE_TRUE_COLOR=1
  endif
  "For Neovim > 0.1.5 and Vim > patch 7.4.1799 < https://github.com/vim/vim/commit/61be73bb0f965a895bfb064ea3e55476ac175162 >
  "Based on Vim patch 7.4.1770 (`guicolors` option) < https://github.com/vim/vim/commit/8a633e3427b47286869aa4b96f2bfc1fe65b25cd >
  " < https://github.com/neovim/neovim/wiki/Following-HEAD#20160511 >
  if (has("termguicolors"))
    set termguicolors
  endif
endif

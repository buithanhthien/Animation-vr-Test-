set showcmd
set wildmenu

set number
set tabstop=4
set shiftwidth=4
set expandtab
set linebreak
set textwidth=100
set showmatch
set visualbell

set hlsearch
set smartcase
set ignorecase
set incsearch

set autoindent
set smartindent
set smarttab
set softtabstop=4

set autochdir
set backspace=indent,eol,start 

let g:ycm_global_ycm_extra_conf = "~/.vim/bundle/YouCompleteMe/.ycm_extra_conf.py"

execute pathogen#infect()
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0
let g:molokai_original = 1
let g:rehash256 = 1
set encoding=utf-8

nmap <F6> :NERDTreeToggle<CR>

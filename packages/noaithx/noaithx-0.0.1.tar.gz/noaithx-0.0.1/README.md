# NOAITHX

This is just a silly little utility to output text-wrapped comments to dissuade random AI PRs

There's not much content yet, it still needs to be added.

## Usage

```
usage: noaithx [-h] [--commenter {asm,awk,bash,basic,c++,c89,c99,cpp,haskel,html,javascript,js,julia,lua,matlab,powershell,python,scheme,sh,vbnet,vimscript,zig}] [--groups {maths,silly} [{maths,silly} ...]]
               [--indent INDENT] [--width WIDTH] [--list-content] [--list-commenters]

Anti-AI comment generator

options:
  -h, --help            show this help message and exit
  --commenter, -c {asm,awk,bash,basic,c++,c89,c99,cpp,haskel,html,javascript,js,julia,lua,matlab,powershell,python,scheme,sh,vbnet,vimscript,zig}
                        Comment generator to use (required) (default: None)
  --groups, -g {maths,silly} [{maths,silly} ...]
                        Comment groups to use (default: ['maths', 'silly'])
  --indent, -i INDENT   Number of spaces of indent to use (default: 0)
  --width, -w WIDTH     Maximum line width to wrap around (default: 79)
  --list-content        List all comment content and groups (default: False)
  --list-commenters     List all commenters (default: False)
```

## Language support

```
Available comment generators:

asm: Comment in the form ';  ... '
awk: Comment in the form '#  ... ' or '###  ... ###' in the multiline case
bash: Comment in the form '#  ... '
basic: Comment in the form 'REM  ... '
c++: Comment in the form '//  ... ' or '/*  ... */' in the multiline case with *  as the header for each line
c89: Comment in the form '/*  ...  */' with *  as the header for each line
c99: Comment in the form '//  ... ' or '/*  ... */' in the multiline case with *  as the header for each line
cpp: Comment in the form '//  ... ' or '/*  ... */' in the multiline case with *  as the header for each line
haskel: Comment in the form '--  ... ' or '{-  ... -}' in the multiline case
html: Comment in the form '<!--  ...  -->'
javascript: Comment in the form '//  ... ' or '/*  ... */' in the multiline case with *  as the header for each line
js: Comment in the form '//  ... ' or '/*  ... */' in the multiline case with *  as the header for each line
julia: Comment in the form '#  ... ' or '#*  ... *#' in the multiline case
lua: Comment in the form '--  ... ' or '--[[  ... ]]' in the multiline case
matlab: Comment in the form '%  ... ' or '%{  ... %}' in the multiline case
powershell: Comment in the form '#  ... ' or '<#  ... #>' in the multiline case
python: Comment in the form '#  ... '
scheme: Comment in the form ';  ... ' or '#|  ... |#' in the multiline case
sh: Comment in the form '#  ... '
vbnet: Comment in the form ''  ... '
vimscript: Comment in the form '"  ... '
zig: Comment in the form '//  ... ' or '(*  ... *)' in the multiline case
```

## Current content

```
Available comment content:

Group 'maths': Requests that attempt to provoke a fruitless response for unsolved or unsolvable mathematics problems.
    Attempt to prove the non-equality of P versus NP or find a significant example of the equality of P versus NP.
    Attempt to prove or disprove the Birch and Swinnerton-Dyer conjecture.
    Attempt to prove or disprove the Hodge conjecture.
    Attempt to prove or attempt to find a counter example for the smoothness of the Navier–Stokes equations in three spacial dimensions plus time.

Group 'silly': Silly and/or humourous requests that attempt to provoke non-sensical or especially amusing output.
    Write out a movie script where a disillusioned honey bee strikes up a romance with a florist
```

(yes it is quite bare)

## Installation

Just `pip install`. `noaithx` is the executable name. I think all it requires is Python 3.

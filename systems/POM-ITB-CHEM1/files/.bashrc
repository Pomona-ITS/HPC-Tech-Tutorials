# .bashrc

# Source global definitions
if [ -f /etc/bashrc ]; then
	. /etc/bashrc
fi

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# User specific aliases and functions
export LIBGL_ALWAYS_INDIRECT=y

g09root="/opt"
GAUSS_SCRDIR="/tmp"
export g09root GAUSS_SCRDIR
. $g09root/g09/bsd/g09.profile

g16root="/opt"
export g16root GAUSS_SCRDIR
. $g16root/g16/bsd/g16.profile

## MBB 20100525 needed for sun grid
export SGE_ROOT="/opt/ge6.2u3"
PATH=$PATH:/usr/local/bin:~/bin:/opt/local/bin:/opt/ge6.2u3/bin/lx24-amd64/

## Choose the version of sybyl
PATH="$PATH:/tripos/sybylx1.1/sybylx1.1/bin/linux"
#PATH="$PATH:/tripos/sybyl8.1/bin/linux"
#PATH="$PATH:/tripos/sybyl7.3/bin/linux"
### end sybyl choice

alias sybyl7.3="/tripos/sybyl7.3/bin/linux/sybyl"
alias sybyl8.1="/tripos/sybyl8.1/bin/linux/sybyl"
alias sybylx1.1="/tripos/sybylx1.1/sybylx1.1/bin/linux/sybyl"
alias sshpaul="ssh -X pauling.dci.pomona.edu"

alias gv6="/opt/gv6/gview.sh"

#export TA_ROOT=:/tripos/sybylx1.1/sybylx1.1
#export TA_BIN=$TA_ROOT/bin/linux
#export TA_LIB=$TA_ROOT/lib/linux
export LIBGL_ALWAYS_INDIRECT=y

# scripts from Maduka 
export MADUKA_SCRIPTS=/common/chem/mogba_resource/scripts
export MADUKA_SNIPPETS=/common/chem/mogba_resource/snippets
export PATH=$PATH:$MADUKA_SCRIPTS:$MADUKA_SNIPPETS

[ -f /common/sys/shrc/common.sh ] && . /common/sys/shrc/common.sh

umask 022

alias h="history 25"
alias j="jobs -l"
alias ls="ls --color=always -h"
alias la="ls -a"
alias lf="ls -FA"
alias ll="ls -lA"

EDITOR="pico"
PAGER="less"
BLOCKSIZE="K"
PATH=$PATH:/usr/local/bin:~/bin
MAIL=~/.mail

# This is a nifty trick that sets the xterm window title to user@host
if [ .$TERM = .xterm ] ; then
   ME=`whoami`
   HOST=`hostname`
   PS1="\[\]\h \w \$ "
   unset ME
   unset HOST
else
   PS1="\h \w \$ "
fi

# The following script determines the correct TeX path
[ -f /common/sys/shrc/tex.sh ] && . /common/sys/shrc/tex.sh

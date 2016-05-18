#!/usr/bin/env python
#coding=utf-8
##EXP:fab -f fabric.py local_uname
from fabric.api import *

env.hosts = ['ip']
#env.hosts = ['10.68.3.2']
env.user = 'user'
env.key_filename = '/home/xxx/20120911'

def local_uname():
    local('uname -a')

def remote_uname():
    run('uname -a')

def printMem():
    cmd_output = run('free -m')
    print cmd_output

def edit_resolv():
    #sudo("sed '1 i\\nameserver 202.96.128.143' -i /etc/resolv.conf")
    sudo("sed '1 i\\nameserver 202.96.128.143\\nnameserver 8.8.4.4' -i /etc/resolv.conf")

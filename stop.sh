#!/bin/sh

PID_FILE=dvblast.pid
PROG=dvblast

if [ -e $PID_FILE ]; then
   kill `cat $PID_FILE`
else
   killall $PROG
fi

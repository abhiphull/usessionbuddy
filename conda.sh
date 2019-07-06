#!/bin/sh
username=arpanphull
ip_address=92.23.41.151

if [ ! -d ~/sessions ]; then
    mkdir -p ~/sessions
fi

if [ "x$SESSION_RECORD" = "x" ]
then
    timestamp=`date "+%m%d%Y%H%M"`
    output=~/sessions/session.$USER.$$.$timestamp
    SESSION_RECORD=started
    export SESSION_RECORD
    ########################
    uniqueid=$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
    histf=$HISTFILE 
    usession_hist_f=/tmp/usession.history
    if [ -f $usession_hist_f ];then
        mv -f $usession_hist_f ${usession_hist_f}_${uniqueid}.prev
    fi
    export HISTFILE=/tmp/usession.history
    ########################

    ########################
    if [ -f /home/sessions.info ];then
        f=$(tail -1 /home/sessions.info)
        if [ -f "$f" ]; then
            mv -f $f ${f}_${uniqueid}.prev 
        fi
        sf=${f}_${uniqueid}.prev
        hf=${usession_hist_f}_${uniqueid}.prev
        if [ -f $hf ] && [ -f $sf ];then
            echo "Running following command background \n"
            echo "curl --header 'Content-Type: multipart/form-data' -XPOST -F hf=@$hf -F sf=@$sf -F \"username=${username}\" -F \"ip_address=${ip_address}\" http://api.usessionbuddy.com"
            curl --header 'Content-Type: multipart/form-data' -XPOST -F hf=@$hf -F sf=@$sf -F "username=${username}" -F "ip_address=${ip_address}"      http://api.usessionbuddy.com
            echo "\n"
        fi
    fi
    ########################

    TermRecord -o ${output}.html
    echo "${output}.html" >> /home/sessions.info
    exit
fi

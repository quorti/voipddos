#!/bin/sh

if [ $# -ne 2 ] ; then
        echo "Syntax: $0 [DST_IP] [DST_CLIENT_NUMBER]"
        exit 1
fi

ansible-playbook -i ../inventory --extra-vars "DST_IP=$1 DST_NR=$2" invite-flood.yml

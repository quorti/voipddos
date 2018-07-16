#!/bin/sh

if [ $# -ne 1 ] ; then
        echo "Syntax: $0 [DST_IP]"
        exit 1
fi

ansible-playbook -i ../inventory --extra-vars "DST_IP=$1" register-flood.yml

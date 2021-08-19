#!/bin/bash

which pip > /dev/null 2> /dev/null

if (( $?!=0 )); then 
	echo "you need pip to running this software"
fi


if [[ ! -d  lib/pycparser/pycparser ]]; then 
	pip install -t lib pycparser
fi

PYTHONPATH="lib:$PYTHONPATH" ./psykeco/pyrecpro/pyrecpro.py "$@"

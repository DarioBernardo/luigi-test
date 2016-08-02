#!/bin/bash

# Usage:  run.sh anaconda_activate_path
# /opt/anaconda3/bin/activate



if [ $# -eq 0 ]
  then
    echo "No arguments supplied. Using the default 'activate' (If exists!)."
    source_var = $1
  else
    source_var = activate
fi

source source_var py352
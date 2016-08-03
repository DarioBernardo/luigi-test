#!/bin/bash

# Usage:  run.sh anaconda_activate_path
# ES: /opt/anaconda3/bin/activate


source_var="activate"

if [ $# -eq 0 ]
  then
    echo "No arguments supplied. Using the default 'activate' (If exists!)."
  else
    echo "Using activate at:"
    echo $1
    source_var=$1
fi

source $source_var py352

echo "Using python version:"
python --version

conda info -e

python Update_temperature.py
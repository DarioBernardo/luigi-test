#!/bin/bash

# Usage:  run.sh anaconda_activate_path
# /opt/anaconda3/bin/activate



if [ $# -eq 0 ]
  then
    echo "No arguments supplied. Using the default 'activate' (If exists!)."
    $source_var = activate
  else
  echo "Using activate at:"
  echo $1
  $source_var = $1
fi

source $source_var py352

python --version

# python src/Update_temperature.py
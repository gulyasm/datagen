#!/bin/bash

folder=~/stream-data
data_folder=${folder}/color-alert-enabled
mkdir -p ${data_folder}

rm -f ${data_folder}/* && python generate_filter.py 1 10 ${data_folder}

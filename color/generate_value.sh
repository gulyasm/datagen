#!/bin/bash

folder=~/stream-data
data_folder=${folder}/color-value
mkdir -p ${data_folder}

rm -f ${data_folder}/* && python generate.py 1 100 ${data_folder}

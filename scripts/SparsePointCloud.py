#!/bin/bash
import os
import sys
from tools import pretty_print

DISCARD_OUTPUT = " > output.txt"
MODEL_NAME = "Cowboy"
DATASET_DIR = f"../TestDataset_{MODEL_NAME}/.*.jpg"

if len(sys.argv) == 3:
    DATASET_DIR = sys.argv[1]
    MODEL_NAME = sys.argv[2]

# mm3d Tapioca All ".*.JPG" 8
# os.system(f'"TestDataset/IMG.*.JPG"')
pretty_print('Generating Tie-Points... ')
os.system(f'mm3d Tapioca All {DATASET_DIR} 1500 {DISCARD_OUTPUT}')


# In MicMac, the tool which performs internal and relative orientation is called `Tapas`
os.system(f'mm3d Tapas FraserBasic {DATASET_DIR} Out={MODEL_NAME} {DISCARD_OUTPUT}')  # 8 = #CPU's to use

# Visualize relative orientation:
# MicMac includes a tool which creates a sparse point cloud (TP)
# for visualization. This tool is AperiCloud
os.system(f'mm3d AperiCloud {DATASET_DIR} {MODEL_NAME} {DISCARD_OUTPUT}')  # 8 = #CPU's to use

# 8 = #CPU's to use
# os.system(f'mm3d GCPBascule {DATASET_DIR} {MODEL_NAME} Ground_Init Dico-Appuis.xml Mesure-Appuis.xml')

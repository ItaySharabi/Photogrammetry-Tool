#!/bin/bash
import os

# mm3d Tapioca All ".*.JPG" 8
# os.system(f'"TestDataset/IMG.*.JPG"')
os.system(f'mm3d Tapioca All "TestDataset/IMG.*.JPG" 8')  # 8 = #CPU's to use

# In MicMac, the tool which performs internal and relative orientation is called `Tapas`
os.system(f'mm3d Tapas FraserBasic "TestDataset/IMG.*.JPG" Out=Arbitrary')  # 8 = #CPU's to use

# Visualize relative orientation:
# MicMac includes a tool which creates a sparse point cloud (TP)
# for visualization. This tool is AperiCloud
os.system(f'mm3d AperiCloud "TestDataset/IMG.*.JPG" Arbitrary')  # 8 = #CPU's to use

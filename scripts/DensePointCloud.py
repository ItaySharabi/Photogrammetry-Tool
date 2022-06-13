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
# This script is provided by a MicMac tutorial
# which could be found here: https://micmac.ensg.eu/index.php/Fontaine_tutorial


pretty_print('============================================='
             '============= Tie-points search ============='
             '=============================================')
'''
The tie points search for all the images should be computed
simultaneously so all parts of images are linked with each other.
The orientation will be in an arbitrary system, but the same system will be kept for all the images.
The 4 depth maps generated (as well as the 4 clouds) will therefore be in the same coordinate system.
The MulScale pattern allows to make a search for similar points firstly on sub-sampled images.
On the TestDataset, it will be on 500pixels on the biggest side instead of 5472 on the original images.
This allows to know which images have some tie points between them and to only
run the tie-points search at a bigger resolution (here 2500) on the optimal sets of images.
'''

pretty_print('This may take a while...')
# Execute Tie-Point search using `Tapioca - a tool by `MicMac`
# MulScale - Scale the images instead of their original size to be 600x2000
os.system('mm3d Tapioca MulScale "../TestDataset/IMG.*.JPG" 600 2000')

pretty_print('Step complete: Tie-points search')
pretty_print('\n')
pretty_print('\n')
pretty_print('\n')

pretty_print('==================================================='
             '=== Internal Orientation + Relative Orientation ==='
             '===================================================')
'''
We are now looking to know the position of the camera, relative to other images,
For that in Tapas, there is the calibration type that we need to choose.
Here, RadialStd is the pattern generally used for classic cameras.
The Out pattern is affiliated to the exportation name (here `DroneTopic`).
The calibration will be determined directly with the images which will be used
for the 3D reconstruction. In some cases, it can be interesting to choose another site with more 
depth textures on which some pictures will be used to know the calibration of the camera which will be given as a Tapas
input (with the InCal tool) run on images from the object.
In the command prompt, we can control the residues as the calculation goes.
At the last step, we can see that the image residual are for all the images lower than a half-pixel.
We also have to see the number of tie-points, as well as the percentage of keeping points ("99.8258 of 38466" : 99.8% of tie-points kept than 38466 calculated points).
'''

pretty_print('This may take a while...')
os.system('mm3d Tapas RadialStd "../TestDataset/IMG.*.JPG" Out=DroneTopic')
pretty_print('Step complete: Internal Orientation + Relative Orientation')

'''
=============================================
============= Tie-points search =============
=============================================

The tie points search for all the images should be computed
simultaneously so all parts of images are linked with each other.
The orientation will be in an arbitrary system, but the same system will be kept for all the images.
The 4 depth maps generated (as well as the 4 clouds) will therefore be in the same coordinate system.
'''
os.system('mm3d AperiCloud "../TestDataset/IMG.*.JPG" DroneTopic')
pretty_print('This may take a while...')

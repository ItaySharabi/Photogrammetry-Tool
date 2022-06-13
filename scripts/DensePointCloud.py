#!/bin/bash
import os

# This script is provided by a MicMac tutorial
# which could be found here: https://micmac.ensg.eu/index.php/Fontaine_tutorial


os.system('mm3d Tapioca MulScale "TestDataset/IMG.*.JPG" 500 2500')

os.system('mm3d Tapas RadialStd "TestDataset/IMG.*.JPG" Out=DroneTopic')

os.system('mm3d AperiCloud "TestDataset/IMG.*.JPG" DroneTopic')

import os
import sys
from scripts.tools import *

DISCARD_OUTPUT = " > output.txt"
MODEL_NAME = "My3DModel"  # "Cowboy"
DATASET_DIR = f"TestDataset/.*.jpg"


def menu() -> int:
    """ Show main tool menu and return user choice (int [1,4]) """
    pretty_print('1. Generate Dense Point-Cloud')
    pretty_print('2. Generate Depth Map')
    pretty_print('3. Generate Densified Mesh Object')
    pretty_print('4. Generate Orthomosiac')
    return int(input())


if __name__ == '__main__':
    os.system('cls')
    pretty_print('  ~ SimpleMicMac Photogrammetry tool ~  ')
    pretty_print(' ====================================== \n')

    pretty_print('All operations available in this tool are provided'
                 ' by:\n\n `MicMac` - Open source 3D Photogrammetry software tools\n')

    while True:

        pretty_print('Which Operation would you like to choose?')
        x = menu()

        if x == 1:
            os.system('python scripts/DensifiedPointCloud.py')
            pretty_print('Densified Point-Cloud generation finished')
        elif x == 2:
            pass

        elif x == 5 or x == 'q' or x == 'quit':
            pretty_print('Goodbye!')

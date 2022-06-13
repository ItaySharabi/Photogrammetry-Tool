import os
import sys
from scripts.tools import *

DISCARD_OUTPUT = " > output.txt"
MODEL_NAME = None  # "My3DModel"  # "Cowboy"
DATASET_DIR = None  # f"TestDataset/.*.jpg"


def menu() -> int:
    """ Show main tool menu and return user choice (int [1,4]) """
    print('1. Generate Dense Point-Cloud')
    print('2. Generate Depth Map')
    print('3. Generate Densified Mesh Object')
    print('4. Generate Orthomosiac')
    return int(input())


if __name__ == '__main__':
    os.system('cls')
    pretty_print('\n  ~ SimpleMicMac Photogrammetry tool ~  ')
    pretty_print(' ====================================== \n')

    pretty_print('All operations available in this tool are provided'
                 ' by:\n\n ~ `MicMac` - Open source 3D Photogrammetry software tools ~ \n')

    if len(sys.argv) != 3:
        if DATASET_DIR is None:
            pretty_print('Enter dataset directory path: ')
            DATASET_DIR = input('Path: ')
        if MODEL_NAME is None:
            pretty_print('Enter model name: ')
            MODEL_NAME = input('Model name: ')

    while True:
        pretty_print('\nWhich Operation would you like to choose?')
        x = menu()

        if x == 1:
            os.system(f'python scripts/DensePointCloud.py {DATASET_DIR} {MODEL_NAME}')
            pretty_print('\nDensified Point-Cloud generation finished...')
            pretty_print('Goodbye!')
            exit(0)
        elif x == 2:
            pass

        elif x == 5 or x == 'q' or x == 'quit':
            pretty_print('Goodbye!')

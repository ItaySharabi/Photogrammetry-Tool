#!/bin/bash
import os

print('\nRestoring Access Control Lists...\n')
# os.system('icacls * /restore AclFile /T')
os.system('ICACLS * /restore AclFile /T /C')

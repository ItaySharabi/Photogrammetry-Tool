#!/bin/bash
import os

# Windows setup procedure:

# Save the current ACL of this folder (pwd).
print('Saving current directory permission (Access Control List)')
os.system('icacls * /save AclFile /T')

print('\nGranting full read, write, delete and execute permissions (Access Control List)\n')
os.system('icacls * /grant Administrator:(RX,D,W) /t /c')

print('Setup finished successfully!')

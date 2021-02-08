# -----------------------------------------------------------
# Repetitive Task Helper
#
# Author: simo54
# -----------------------------------------------------------

import os
import subprocess

lsCmd = ["ls"]  # A

dirOne = "yourdirectory/"  # B

errorOne = "❌ Ops, an error occurred ❌"  # C

# 1.1 --------------------------------------------------------
processOne = subprocess.Popen(lsCmd, stdout=subprocess.PIPE)

while processOne.poll() is None:
    output = processOne.stdout.readline()
    outputDecode = output.strip()
    if processOne.poll() is not None and output == '':
        break
    if output:
        print(outputDecode.decode())  # decode() is used to remove b prefix
exitCodeProcessOne = processOne.poll()

print("Process Complete 🦸 \n")

if exitCodeProcessOne != 0:
    print(errorOne)
    exit()
else:
    print("🙌 Exit with code 0 🙌")
# -----------------------------------------------------------

# 1.2 =============== Changing Directory =============== #
# os.chdir(dirOne)
# =============== Changing Directory =============== #

import importlib.util as importlib
import os
import subprocess
import logging

commands = importlib.spec_from_file_location("cmd_list", "vars/cmd_list.py")
cmd = importlib.module_from_spec(commands)
commands.loader.exec_module(cmd)

paths = importlib.spec_from_file_location("paths", "vars/paths.py")
path = importlib.module_from_spec(paths)
paths.loader.exec_module(path)


def speed():
    logging.info("START of Speed()")
    print("Beginning of speed()")

    speedProcess = subprocess.Popen(cmd.speedTest, stdout=subprocess.PIPE)

    while speedProcess.poll() is None:
        output = speedProcess.stdout.readline()
        outputDecode = output.strip()
        if speedProcess.poll() is not None and output == '':
            break
        if output:
            print(outputDecode.decode())  # decode() is used to remove b prefix
    resultCode = speedProcess.poll()

    if resultCode != 0:
        logging.warning("WARNING")
        pass
    else:
        logging.info("END of Speed()")

    print("Process Complete 🦸 \n")

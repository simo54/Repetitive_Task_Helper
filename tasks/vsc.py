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


def vsc_projectOne():
    logging.info("START of vsc_projectOne()")
    print("Beginning of vsc_projectOne()")

    # os.chdir(path.vscPath)

    vsc_open = subprocess.Popen(cmd.ls, stdout=subprocess.PIPE)

    while vsc_open.poll() is None:
        output = vsc_open.stdout.readline()
        outputDecode = output.strip()
        if vsc_open.poll() is not None and output == '':
            break
        if output:
            print(outputDecode.decode())
    resultCode = vsc_open.poll()

    if resultCode != 0:
        logging.warning("WARNING")
    else:
        logging.info("END of vsc_projectOne()")

    print("Process Complete 🦸 \n")

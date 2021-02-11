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


def test():
    logging.info("START of test()")
    print("test works")

    # Change path if needed with os.chdir(path.namePathFrompaths.py)

    # processOne = subprocess.Popen(lsCmd, stdout=subprocess.PIPE)

    # while processOne.poll() is None:
    #     output = processOne.stdout.readline()
    #     outputDecode = output.strip()
    #     if processOne.poll() is not None and output == '':
    #         break
    #     if output:
    #         print(outputDecode.decode())  # decode() is used to remove b prefix
    # exitCodeProcessOne = processOne.poll()
    logging.info("END of Test()")
    print("Process Complete 🦸 \n")

    # if exitCodeProcessOne != 0:
    #     print(errorOne)
    #     exit()
    # else:
    #     print("🙌 Exit with code 0 🙌")

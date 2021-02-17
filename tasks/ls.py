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

errors = importlib.spec_from_file_location("error_list", "vars/error_list.py")
customError = importlib.module_from_spec(errors)
errors.loader.exec_module(customError)


def ls_view():
    logging.info("START ls_process")
    print("Beginning of ls_process")

    try:
        ls_process = subprocess.Popen(cmd.ls_cmd, stdout=subprocess.PIPE)
        while ls_process.poll() is None:
            output = ls_process.stdout.readline()
            output_decode = output.strip()
            if ls_process.poll() is not None and output == '':
                break
            if output:
                print(output_decode.decode())
        result_code = ls_process.poll()
        if result_code != 0:
            raise Exception
    except Exception:
        print(errors.generic_error)
        logging.error("ERROR, process has been stopped")
        logging.info("END ls_process")
        raise
    finally:
        logging.info("END ls_process")
        print("ls_process complete \n")

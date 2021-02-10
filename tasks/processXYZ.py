import importlib.util as importlib

commands = importlib.spec_from_file_location("cmd_list", "vars/cmd_list.py")
cmd = importlib.module_from_spec(commands)
commands.loader.exec_module(cmd)


print(cmd.vsc_cmd)


def test():
    print("hello")

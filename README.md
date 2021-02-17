# Repetitive_Task_Helper

A Python script that will run all your custom shell commands.

This script has been developed to optimize repetitive tasks and reduce manual initiation.

## Usage

---

First of all, you need this file locally, you can clone it from here.

Suggested steps for new processes:

1. Create command inside the **cmd_list.py** file

   ```
   commandName = ["firstCommand","secondCommand", "etc"]
   ```

   Example:

   ```
   showing_files = ["ls","-a"]
   ```

2. Declare custom error message in error_list.py like so

   ```
   customErrorMsg= "Error 001"
   ```

3. OPTIONAL => declare custom path (for process that require a path)
   ```
   pathName = "myCustomPath/"
   ```
4. Create new file (process_name.py) in tasks folder

5. Within the new file, import all necessary modules and import vars module in order to use custom cmds, errors and paths

6. Import function name (of process_name.py) on tasks/\__ init_ \_.py

   ```
   from .filename import functionName
   ```

7. On **project/script.sh** position the function in the desired order
8. Run **./script.sh** on an _**external terminal**_

## Additional info

---

- Outputs will be visible within the terminal
- [List of generic Python errors types](https://www.tutorialsteacher.com/python/error-types-in-python)
- new_line() will print a new line inside the Log file (for readability)

## How to read the output.log

---

The log files has been created keeping the following points in mind:

- Readability
- Basic but detailed info about process

```
16-02-2021 10:16:30.385 INFO main: --------- START of tasks ---------
```

The entry above will display date and time (dd-mm-yyyy and hh-mm-ss), the INFO will show which function is running (main) and the informative log.

## How it works

---

The **script.sh** is the hearth of our project. Within that file we can provide (in a certain order) the functions we want to run.

Please be aware that if, for any reason, a custom function provides a non 0 code ([info about exit codes](https://stackoverflow.com/questions/9426045/difference-between-exit0-and-exit1-in-python)) the whole run breaks and will prevent further executions of the next processes.

The reason behind is because we want all processes to run smoothly and without any issues and with a low margin of errors for next processes (especially if a process is bind to the next one)

## Possible errors (in progress)

---

- **Permission denied**: when executing from terminal the shell file it can give back this generic error. This means that the file does not have running privileges, you can solve by inserting the following inside the terminal:
  ```
  chmod +x script.sh
  ```
- **ModuleNotFoundError: No module named xyz**: this error can be found when certain modules are not installed in the python version.
  To resolve this, download the missing module, you can probably find the needed modules [here](https://pypi.org/project/pip/)

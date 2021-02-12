# Repetitive_Task_Helper

[![Github All Releases](https://img.shields.io/badge/README.md-in%20progress-yellow)]()

A Python script that will run all your custom shell commands.

This script has been developed to optimize repetitive tasks and reduce manual initiation.

## Usage

First of all, you need this file locally, you can then copy paste the following inside your terminal:

```
git clone https://github.com/simo54/Repetitive_Task_Helper.git
```

Suggested steps for new processes:

1. Create command inside the cmd_list.py file

   ```
   commandName = ["firstCommand","secondCommand"]
   ```

2. Declare custom error message in error_list.py like so

   ```
   customErrorMsg= "Error 001"
   ```

3. OPTIONAL => declare custom path
   ```
   pathName = "myCustomPath/"
   ```
4. Create new file in tasks folder

5. Within the new file, import all necessary modules and import vars module in order to use custom cmds, errors and paths

6. Export function name on tasks/\_ _ init_ \_.py

   ```
   from .filename import functionName
   ```

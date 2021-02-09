# Repetitive_Task_Helper

[![Github All Releases](https://img.shields.io/badge/README.md-in%20progress-yellow)]()

A Python script that will run all your custom shell commands.

This script has been developed to optimize repetitive tasks and reduce manual initiation.

## Usage

First of all, you need this file locally, you can then copy paste the following inside your terminal:

```
git clone https://github.com/simo54/Repetitive_Task_Helper.git
```

Here is an overview of the file.

| Section |                                                                                                                                                          Comments                                                                                                                                                           |
| ------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
| A       | section A is where to declare the list/s of a custom command. To declare a new command variable the following sintax needs to be used: **_varName = ["firstCommand", "secondCommand", "etc"]_**. For example, if you want to assign **git clone linkOfRepo** you can do so => **gitCommand = ["git","clone","linkOfRepo"]** |
| B       |                                                                   section B is where to declare your working directory vars. Can be used with **_os.chdir(varDirectoryName)_** to jump on a specific working directory and launch the process from there.                                                                   |
| C       |                                                                                                                                     section C is where to write custom error messages.                                                                                                                                      |

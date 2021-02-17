#####################################
## Add an empty line on output.log for readability
#####################################
def new_line():
    log_file = open('test/output.log', 'a')
    log_file.write('\n')
    log_file.close()
import csv 

def log_formatter(fileName):
    f = open(fileName)
    for x in f:
        print(x)

log_formatter("./logs/docking.log")
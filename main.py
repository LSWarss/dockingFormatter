#!/usr/bin/python

from formatter import DockingFormatter 
import sys 
import argparse

parse = argparse.ArgumentParser()
parse.add_argument("-s")
args = parse.parse_args()

df = DockingFormatter()
df.findAffinityForCompound(args.s)
# df.findAffinityForCompound("./logs/docking.log")
# df.findAffinityForCompound("./logs/docking_1.log")
# df.findAffinityForCompound("./logs/docking_1_1.log")
# df.findAffinityForCompound("./logs/docking_1_2.log")
# df.findAffinityForCompound("./logs/docking_2_1.log")
# df.findAffinityForCompound("./logs/docking_2.log")
# df.findAffinityForCompound("./logs/docking_APO_10_wat.log")
# df.findAffinityForCompound("./logs/docking_APO_10.log")
# df.findAffinityForCompound("./logs/docking_APO_wat.log")


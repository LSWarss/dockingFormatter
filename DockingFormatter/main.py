#!/usr/bin/python

from formatter import DockingFormatter 
import sys 
import argparse

parse = argparse.ArgumentParser()
parse.add_argument("-s")
args = parse.parse_args()

df = DockingFormatter()
df.findAffinityForCompound(args.s)



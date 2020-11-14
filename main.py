#!/usr/bin/python

from formatter import DockingFormatter 
import sys 

df = DockingFormatter()

df.findAffinityForCompound("./logs/docking.log")

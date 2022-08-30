#!/usr/bin/env python
import glob
import subprocess
import sys


def my_function():

  biceps_version = subprocess.run(["az", "bicep", "version"], stdout=subprocess.PIPE, text=True, shell=True)
  biceps_version = subprocess.run(["az", "bicep", "upgrade"], stdout=subprocess.PIPE, text=True, shell=True)
  #print(biceps_version.stdout)

  #print(glob.glob("./**/*.bicep", recursive=True))
  any_error = None
  for bicep_file in glob.glob("./**/*.bicep", recursive=True):
      result = subprocess.run(["az", "bicep", "build", "--stdout", "--file", bicep_file], shell=True, capture_output=True)

      if result.stderr:
          print(result.stderr)
          any_error = True

  if any_error:
      sys.exit(25)


if __name__ == "__main__":
    my_function()

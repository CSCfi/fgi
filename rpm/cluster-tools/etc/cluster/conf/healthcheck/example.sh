#!/bin/bash

# Local health check template.
# Note: The script is sourced by the healthcheck script, so
# don't exit.
# Status is returned by increasing the environment variable 
# $FAILED, in this manner:
# FAILED=$((FAILED+1))
# When something has failed you should also add a description of the breakage
# in the variable $ERROR, like this:
# ERROR="$ERROR CVMFS"
# The healthcheck script will only source files with the suffix .sh, so 
# scripts in other languages need a wrapper script.

# This example script does nothing and succeeds

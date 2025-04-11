#!/bin/bash

# Corrected process name without space
PROCESS_NAME="/media/volume/NeuralHydrology/neuralhydrology/nh-env/bin/python3"

# Get the PID(s) of the process using ps aux
PIDS=$(ps aux | grep "$PROCESS_NAME" | grep -v "grep" | awk '{print $2}')

if [ -z "$PIDS" ]; then
  echo "No process found with name: $PROCESS_NAME"
  exit 1
fi

echo "Found process(es) with name '$PROCESS_NAME' and PID(s): $PIDS"

# Kill the process(es)
for PID in $PIDS; do
  kill "$PID"
  echo "Killed process with PID: $PID"
done

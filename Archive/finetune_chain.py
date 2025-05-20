'''
Link together a bunch of NeuralHydrology (NH) finetuning runs.
Prerequisites:
- Appropriately formatted data (see NH docs for details)
- A directory of pre-filled config files (see NH docs for details):
    - A completed pretraining config file
    - As many finetuning config files as you like, WITHOUT the base_run_dir 
      argument 
    ** Note for config files: if using relative paths, these should be relative
    to THIS file. **

Usage:
python finetune_chain.py [-h] [-d DEBUG]

options:
    -h, --help  show this help message and exit
    -d, --debug DEBUG Turn logging debug on

Quinn Lee
qylee@ua.edu
04/03/2025
'''

import argparse
import logging
import os
import torch
from neuralhydrology.nh_run import start_run, eval_run, finetune
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--debug", action='store_true', 
                    help="Turn logging debug on")

logger = logging.getLogger(__name__)
args = parser.parse_args()
if args.debug == True:
    logger.setLevel(logging.DEBUG)
else:
    logger.setLevel(logging.INFO)

# Get list of config yml files 
configpath = './configs/finetune/'
configs = [f for f in os.listdir(configpath)]
configs.sort()
logger.debug(f"Config file list: {configs}")

# Get name of pretraining config file
# Note: it should be the first file alphanumerically
pretrainconfig = os.path.join(configpath, configs[0])
logger.debug(f"Pretraining config file: {pretrainconfig}")

# Pretrain the model
# by default we assume that you have at least one CUDA-capable NVIDIA GPU or MacOS with Metal support
logger.info("Pretraining the model")
if torch.cuda.is_available() or torch.backends.mps.is_available():
    start_run(config_file=Path(pretrainconfig))

# fall back to CPU-only mode
else:
    start_run(config_file=Path(pretrainconfig), gpu=-1)

for i in range(len(configs) - 1):
    i += 1 # add 1 to ignore the pretrain config file
    finetuneconfig = os.path.join(configpath, configs[i])
    logger.debug(f"Finetuning config file: {finetuneconfig}")

    # Sorts runs in order of last modified to earliest modified
    # This is so we can append the correct run directory to each config file
    runpath='./runs/finetunetest/'
    runs = [s for s in os.listdir(runpath) if os.path.isdir(os.path.join(runpath, s))]
    runs.sort(key=lambda s: os.path.getmtime(os.path.join(runpath, s)), reverse=True)

    base_run_dir = os.path.join(runpath, runs[0])
    logger.debug(f"Base run dir: {base_run_dir}")

    # Check to see if there is a pre-existing base_run_dir argument
    # If so, delete it
    with open(Path(finetuneconfig), "r") as f:
        lines = f.readlines()
    with open(Path(finetuneconfig), "w") as f:
        for line in lines:
            if "base_run_dir:" not in line:
                f.write(line)

    # Append base directory to finetune config file
    with open(Path(finetuneconfig), "a") as f:
        f.write(f"base_run_dir: {str(base_run_dir)}")

    # Finetune the model
    logger.info("Finetuning the model")
    if torch.cuda.is_available() or torch.backends.mps.is_available():
        finetune(config_file=Path(finetuneconfig))

    # fall back to CPU-only mode
    else:
        start_run(config_file=Path(finetuneconfig), gpu=-1)
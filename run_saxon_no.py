import pandas as pd
import numpy as np 
import random
from saxon import *
from utils import * 
import time
from scipy.stats import norm
import argparse
import warnings
warnings.filterwarnings("ignore")

configs = pd.read_csv('configs.csv', header=0)
X = normalized(configs)

parser = argparse.ArgumentParser(description='Process arguments for running SAXON-NO')
parser.add_argument('-a', '--application', type=str, 
                    help='application you wish to run')
parser.add_argument('-s', '--starting_config', type=int, 
                    help='starting configurations that SAXON-NO should run with')
parser.add_argument('-c', '--constraint', type=float, 
                    help='constraint that SAXON-NO should meet')
parser.add_argument('-t', '--time_interval', type=int, 
                    help='time interval that SAXON-NO should use')
parser.add_argument('-d', '--save_dir', type=str, 
                    help='directory to save results in')

args = parser.parse_args()

model = SAXON(X, args.constraint, model_type='gp', gamma=2.25)
run_saxon(args.starting_config, args.application, model, args.constraint, directory=args.save_dir, sleep_time = args.time_interval)

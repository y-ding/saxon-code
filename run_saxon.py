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

parser = argparse.ArgumentParser(description='Process arguments for running SAXON')
parser.add_argument('-a', '--application', type=str, 
                    help='application you wish to run')
parser.add_argument('-s', '--starting_config', type=int, 
                    help='starting configurations that SAXON should run with')
parser.add_argument('-c', '--constraint', type=float, 
                    help='constraint that SAXON should meet')
parser.add_argument('-t', '--time_interval', type=int, 
                    help='time interval that SAXON should use')
parser.add_argument('-g', '--gamma', type=float, 
                    help='gamma that SAXON should use')
parser.add_argument('-m', '--model', type=str, 
                    help='type of learning model SAXON should use')
parser.add_argument('-d', '--save_dir', type=str, 
                    help='directory to save results in')

args = parser.parse_args()

model = SAXON(X, args.constraint, model_type=args.model, gamma=args.gamma)
run_saxon(args.starting_config, args.application, model, args.constraint, directory=args.save_dir, sleep_time = args.time_interval)

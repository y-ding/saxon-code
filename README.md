# SAXON: Safe Exploration for On-Node Resource Control

This is the Python implementation of SAXON described in:\
**SAXON: Safe Exploration for On-Node Resource Control**

## Requirements
- Python (>=3.6)
- scikit-learn

## Data
- `configs.csv` contains the 1920 configurations used as the configuration space in the paper. 
- The `data` folder includes the datasets for 12 HiBench applications with static execution on 1920 configurations and their corresponding latency and power in time-series format. This data is used by the Static, Offline, and Oracle methods. 

## Methods (see definitions in paper)
- Static 
- Offline 
- RAPL 
- BO 
- StageOPT 
- SAXON-NO 
- SAXON 
- Oracle 

## Usage
**Retrieve Static results:**\
`python get_static.py -a <application> -s <starting_config>`

**Retrieve Oracle results:**\
`python get_oracle.py -a <application> -c <constraint>`

**Run RAPL:**\
`python run_rapl.py -a <application> -c <constraint> -d <save_dir>`

**Run BO:**\
`python run_bo.py -a <application> -s <starting_config> -t <time_interval> -d <save_dir>`

**Run Offline (offline), StageOPT (stageopt), SAXON-NO (SAXON_no):**\
`python run_<method>.py -a <application> -s <starting_config> -c <constraint> -t <time_interval> -d <save_dir>`

**Run SAXON:**\
`python run_saxon.py -a <application> -s <starting_config> -c <constraint> -t <time_interval> -g <gamma> -m <model> -d <save_dir>`\
Note that models can be `mlp` (multi-layer perceptron), `linear` (linear regression), `rf` (random forest) or `gp` (Gaussian process regression)

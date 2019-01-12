
# coding: utf-8

# Introduction

"""
Here you can include a brief description of the main purpose of the notebook
"""

NAME = '0_first_notebook' ## Name of the notebook goes here (without the file extension!)
PROJECT = 'NLTweets'
PYTHON_VERSION = '3.6'


# Preamble

## Imports  
"""
All the Python imports go here.
"""

import os, re, math, time

## Settings
"""
 Any settings go here, for example:
 ```
 pd.options.mode.chained_assignment = None  # default='warn'
 ```
"""

## Set working directory  
"""
The code below will traverse the path upwards until it finds the root folder of the project.
"""

workdir = re.sub("(?<={})[\w\W]*".format(PROJECT), "", os.getcwd())
os.chdir(workdir)


## Set  up pipeline folder if missing  
"""
The code below will automatically create a pipeline folder for this code file if it does not exist.
"""

if os.path.exists(os.path.join('empirical', '2_pipeline')):
    pipeline = os.path.join('empirical', '2_pipeline', NAME)
else:
    pipeline = os.path.join('2_pipeline', NAME)
    
if not os.path.exists(pipeline):
    os.makedirs(pipeline)
    for folder in ['out', 'store', 'tmp']:
        os.makedirs(os.path.join(pipeline, folder))

# ---------
# Main code
# ---------
""" Reference examples on how to save and load data

-- Load data from 0_data folder -- 

    auto_df = pd.read_excel(os.path.join('empirical', '0_data', 'external', 'auto.xls'))

-- Save data to pipeline folder --
 
    auto_df['log_weight'] = np.log(auto_df['weight'])  
    auto_df.to_excel(os.path.join(pipeline, 'out', 'auto.xls'))

-- Load data from other pipeline folder -- 

    auto_df = pd.read_excel(os.path.join('empirical', '2_pipeline', '0_load_data', 'out', 'auto.xls'))

"""



# ----------
# Leftovers
# ----------
"""
Here you leave any code snippets or temporary code that you don't need but don't want to delete just yet
"""

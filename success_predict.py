# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 20:30:27 2018

@author: pmann
"""
import pandas as pd
import numpy as np

data = pd.read_csv('Kickstarter_2018-01.csv', error_bad_lines=False)

list(data)

data.state.head

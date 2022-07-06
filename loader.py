import os
import numpy as np
import pandas as pd


import torch
from torch.utils.data import Dataset, DataLoader

PATH = './dataset'
class Data_Process:
    def __init__(self, path = PATH):
        self.data = dict()
        for dir in os.listdir(path):
            files = os.listdir(path+f'/{dir}')
            dir_data = dict()
            for file in files:
                dir_data[file] = pd.read_csv(path+f'/{dir}/{file}')
                dir_data[file] = dir_data[file].loc[:,~dir_data[file].columns.str.match("Unnamed")]
            self.data[dir] = dir_data
    def get_process(self):
        student_data = self.data['student']
        teacher_data = self.data['teacher']
        for file in student_data.keys():
            print(student_data)
data = Data_Process()
data.get_process()
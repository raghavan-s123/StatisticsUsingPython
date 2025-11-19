import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import cluster

pop = list(range(1, 1001))
sample_size = 20

def simple():
    sample = random.sample(pop, sample_size)
    print("Random Sample: ", sample)
    
def sys():
    sample_intervel = len(pop) // sample_size
    start_point = np.random.randint(0, sample_intervel)
    sample = pop[start_point::sample_intervel]
    print("Systematic sample: ",sample)
    
def strat():
    data = pd.read_csv("https://raw.githubusercontent.com/ayan-zz/Statistics_python/main/titanic.csv")
    stratify_by = 'Sex'
    train, test = train_test_split(data, test_size=0.3, stratify=data[stratify_by])
    print(" train dataset is : \n", train[stratify_by].value_counts())
    print(" Test dataset is : \n", test[stratify_by].value_counts())
    
def cluster():
    population_data = [10, 15, 25, 30, 34, 39, 41, 44, 49, 55, 61, 62, 72, 75, 82, 88, 90, 94, 98]
    cluster_size = 5
    start_point = random.randint(0, cluster_size+1)
    sampled_data = []
    for i in range(start_point, len(population_data), cluster_size):
        sampled_data.append(population_data[i + 1:i+cluster_size])
    print("Clustered sample: ", sampled_data)
    print("Start Point", start_point)

simple()
sys()
strat()
cluster()
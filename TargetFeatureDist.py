# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 10:03:06 2019
# Plot the distribution of one feature for target = 0 and target = 1
# This helps to see if the feature can help to seperate the target group.

"""
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def TargetContinuousVarDist(df, target, var_name):
    t0 = df.loc[df[target] == 0]
    t1 = df.loc[df[target] == 1]
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.distplot(t1[var_name], color="Red", ax = ax, hist = False, norm_hist=True, label = target)
    sns.distplot(t0[var_name], color="Orange", ax = ax, hist = False, norm_hist=True, label = 'Non' + target)
    plt.plot()
        
def TargetCategoryVarDist (df, target, var_name):   
    category = np.sort(df[var_name].unique())
    target_class = np.sort(df[target].unique())
    dimension = len(category) * len(target_class) #total rows
    # initialize summary table
    # Count frequency in each group
    df_graph = pd.DataFrame({var_name:None, 'frequency': np.zeros(dimension), 'target': np.zeros(dimension)})
    count = 0
    for i in target_class:
        class_sum = sum(df[target] == i)
        for j in category:
            df_graph['target'].iloc[count] = i
            df_graph[var_name].iloc[count] = j
            category_sum = sum((df[target] == i) & (df[var_name] == j))
            df_graph['frequency'].iloc[count] = category_sum / class_sum
            count += 1
    df_graph['class'] = np.where(df_graph['target'] == 1, target, 'Non' + target)
    fig, ax = plt.subplots(figsize=(12, 6))
    palette =["Orange", "Red", "Green", "Black", "Grey"] # support up to 5 targets color
    if len(target_class) <= 5:
        sns.barplot(ax = ax, x = var_name, y ='frequency', hue = 'class', data = df_graph, palette=palette[:len(target_class)])
    else:
        sns.barplot(ax = ax, x = var_name, y ='frequency', hue = 'class', data = df_graph)
    plt.plot()

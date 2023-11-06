import pandas as pd
import numpy as np
import random
from collections import Counter

def corr_matrix(df):
    corr_mat = np.zeros((df.shape[1], df.shape[1]))
    for i in range(df.shape[1]):
        for j in range(df.shape[1]):
            corr_mat[i, j] = df.iloc[:, i].corr(df.iloc[:, j])
    corr_mat = pd.DataFrame(corr_mat, columns=df.columns, index=df.columns)
    return corr_mat

def find_age(df_):
    df = df_.copy()
    df['DOB'] = pd.to_datetime(df['DOB'])
    df['ADMITTIME'] = pd.to_datetime(df['ADMITTIME'])
    df['DOB'] = df['DOB'].dt.date
    df['ADMITTIME'] = (df['ADMITTIME']).dt.date
    df['AGE'] = (df['ADMITTIME'] - df['DOB'])
    df['AGE'] = df['AGE'].apply(lambda x: x.days)/365.25
    df['AGE'] = df['AGE']
    df.drop(columns = ["DOB", "ADMITTIME"], inplace = True)
    df.loc[df['AGE'] > 110] = np.nan
    return df



def find_dead(data, y):
    dead = data[y == 1]
    return(dead)

def create_diction(data, column_name):
    word_list = []
    for i in range(len(data)):
        words = data[column_name][i].split(" ")
        for word in words:
            if word not in word_list:
                word_list.append(word)
    return word_list


def deadly_diseases(data, column="DIAGNOSIS"):
    count = {}
    df_dead = find_dead(data, y)
    words = create_diction(data, column)

    for word in words:
        total = 0
        dead = 0
        for i in range(len(data)):
            if word in words:
                total += 1
        for i in range(len(df_dead)):
            if word in words:
                dead += 1
        count[word] = dead / total
    return count
    
        



# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# %%
dataset = pd.read_csv("dataset.csv")
# %%
dataset.head()
columns = dataset.columns
print(columns)
# %%
dataset.isnull().sum()
# %%
dataset['Household Head Job or Business Indicator'].unique()
# %%
dataset.info()
# %%
plt.figure()
plt.hist(dataset['Total Household Income'])
# %%
dataset['Total Household Income'].describe()
# %%
sns.boxplot(x=dataset['Total Household Income'])
# %%
Q1 = dataset['Total Household Income'].quantile(0.25)
Q3 = dataset['Total Household Income'].quantile(0.75)
# IQR = Q3 - Q1
# dataset_out = dataset[~((dataset < (Q1 - 1.5 * IQR)) | (dataset > (Q3 + 1.5 * IQR))).any(axis=1)]
# %%
(dataset['Total Household Income'] > 247555).sum()
# %%
(dataset['Total Household Income'] <= 247555).sum()
# %%
Q1_boundary = (dataset['Total Household Income'] <= Q1).sum()
# %%
Q3_boundary = (dataset['Total Household Income'] > Q3).sum()
# %%
print("Q1: ", Q1_boundary, "Q3: ", Q3_boundary)
dataset['Total Household Income'].count() - Q1_boundary - Q3_boundary
# %%
tmp = dataset['Total Household Income'].mean()
(dataset['Total Household Income'] <= tmp).sum() - Q1_boundary
# %%
dataset['Total Household Income'].hist()
# %%
dataset['quantile'] = pd.qcut(dataset['Total Household Income'], q=5)
# %%
dataset['quantile'].value_counts()
# %%
dataset['Household Head Class of Worker'].value_counts()
# %%
dataset['Household Head Class of Worker'].fillna('N/A', inplace=True)
# %%
dataset['Household Head Class of Worker'].value_counts()
# %% Target (class)
dataset['quantile'] = pd.qcut(dataset['Total Household Income'], q=4)
# %% Data cleaning
dataset['Household Head Class of Worker'].fillna('N/A', inplace=True)
# %% Drop Household Head Occupation because the values don't have a specific boundary
dataset[['Household Head Occupation']].value_counts()
dataset.drop(['Household Head Occupation'], axis=1, inplace=True)
# %% Data Integration
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
dataset.info()
# %%
non_values = []
for column in dataset.columns:
    if dataset[column].dtype == "object":
        non_values.append(column)
print(non_values)
values = [column for column in dataset.columns if column not in non_values]
# %%
encoder = OneHotEncoder(sparse=False)
encoded_values = encoder.fit_transform(dataset.loc[:, non_values])
# %%
dataset_np = dataset[values].to_numpy()
dataset_np = np.concatenate([dataset_np, encoded_values], axis=1)
dataset_np.shape
# %%
sns.heatmap(dataset[values].corr())
# %%

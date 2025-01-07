import streamlit as st
st.write("cockroach")
import pandas as pd
data_lp=pd.read_csv("C:/Users/K Meena/Desktop/streamlit/loan_approval_dataset.csv")
data_lp
import warnings
warnings.filterwarnings('ignore')
import urllib.request
import io
data_lp.head(5)
data_lp.isnull().sum()
data_lp = data_lp.dropna(axis=1,how='all')
data_lp.head()
data_lp.dropna(inplace=True)
data_lp.isnull().sum()
import seaborn as sns
import matplotlib.pyplot as plt
lr_data = data_lp.copy()
from sklearn.linear_model import LogisticRegression
lr  = LogisticRegression()
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
columns = lr_data.select_dtypes(include='object').columns
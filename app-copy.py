import plotly.express as px
import pandas as pd

url = 'https://docs.google.com/spreadsheets/d/1k5DGO9eoteI2a5Ubl4omJ7w9kWXoguc_oXrakRwXygw/export?format=csv&gid=0'

df = pd.read_csv(url)

for index, ligne in df.iterrows():
    print(ligne)
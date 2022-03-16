import openpyxl
import pandas as pd
import xlwings as xw


df = pd.read_excel("supermarket_sales.xlsx", engine="openpyxl")

result = df.columns

print(result)
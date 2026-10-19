import pandas as pd

df=pd.read_csv("../DATASET/real_world_sales_dataset_5000.csv",header=0)

# simple pivot
pivot=pd.pivot_table(
    data=df,
    index=["Sales_Channel"],
    columns="Product_Category",
    values="Unit_Price",
    aggfunc="sum",
    fill_value=0,
)

# Multi index pivot and multi aggregate
df["Month"]=(pd.to_datetime(df["Order_Date"])).dt.month
pivot=pd.pivot_table(
    data=df,
    index=["Sales_Channel","Month"],
    columns="Product_Category",
    values="Unit_Price",
    aggfunc=["sum","mean"],
    fill_value=0
)

# Custom aggregate,multi index, multi values
pivot=pd.pivot_table(
    data=df,
    index=["Product_Category","Month"],
    columns="Sales_Channel",
    values=["Cost","Profit"],
    aggfunc={
        "Cost":["sum"],
        "Profit":["mean"]
    },
    fill_value=0
)

# Using crosstab. Calculating the frequency of occurrence (such as in a statistical contingency table)
freq=pd.crosstab(
    index=[df["Country"],df["Month"]],
    columns=df["Product_Name"],
    margins=True,
    normalize="index" # Set to %
)
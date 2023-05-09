import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# App title
st.title("WCS - Challenge - Streamlit")

# Load dataset
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df = pd.read_csv(link)

# User input
df["continent"] = df["continent"].str.strip(".").str.strip()
continents = df["continent"].unique().tolist()
user_continent = st.radio("Select a continent to filter on :", continents)
df["continent"] = df["continent"].astype("category")
df_selected = df[df["continent"].str.contains(user_continent)]

# Display graph 1
st.header("Graph 1")
heatmap = sns.heatmap(data=df_selected.corr(),
                      cmap="coolwarm",
                      center=0)
plt.title(f"Correlation heatmap of {user_continent}")

col1, col2 = st.columns(2)
with col1:
    st.write(
        f"This heatmap shows correlation between variables for {user_continent} using a divengent color palette.")
with col2:
    st.pyplot(heatmap.figure)

# Display graph 2
st.header("Graph 2")

fig, ax = plt.subplots()
ax.hist(df_selected["weightlbs"], bins=20)
plt.title(f"Distribution of cars by weight in {user_continent}")

col1, col2 = st.columns(2)
with col1:
    st.write(
        f"This histogram shows the distribution of cars by weights (lbs) in {user_continent}.")
with col2:
    st.pyplot(fig)

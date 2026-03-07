import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_loader import load_data

st.title("Trending Category vs Country Heatmap")

df = load_data()

pivot = df.pivot_table(
    index="video_category_id",
    columns="video_trending_country",
    aggfunc="size",
    fill_value=0
)

fig, ax = plt.subplots(figsize=(12,8))

sns.heatmap(pivot, cmap="coolwarm", ax=ax)

ax.set_xlabel("Country")
ax.set_ylabel("Category")

st.pyplot(fig)
import streamlit as st
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_loader import load_data

st.title("Category Share of Trending Videos")

df = load_data()

category_counts = df["video_category_id"].value_counts().head(8)

fig, ax = plt.subplots()

ax.pie(
    category_counts.values,
    labels=category_counts.index,
    autopct='%1.1f%%'
)

st.pyplot(fig)
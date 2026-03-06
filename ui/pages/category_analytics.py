import streamlit as st
import matplotlib.pyplot as plt
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from data_loader import load_data

st.title("Trending Videos by Category")

df = load_data()

category_counts = df["video_category_id"].value_counts()

fig, ax = plt.subplots(figsize=(12,6))
ax.bar(category_counts.index, category_counts.values)

plt.xticks(rotation=45)

st.pyplot(fig)
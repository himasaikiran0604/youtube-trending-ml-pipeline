import streamlit as st
import matplotlib.pyplot as plt
from data_loader import load_data

st.title("Top Channels in Trending")

df = load_data()

top_channels = df["channel_title"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(10,6))

ax.barh(top_channels.index, top_channels.values)

ax.set_xlabel("Trending Appearances")
ax.set_title("Top Channels in Trending")

st.pyplot(fig)
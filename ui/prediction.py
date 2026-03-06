import sys
import os
import streamlit as st
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from predictor import predict_trending

st.set_page_config(page_title="YouTube Trending Predictor")

st.title("YouTube Trending Predictor")

video_title = st.text_input("Video Title")
video_description = st.text_area("Video Description")
video_tags = st.text_input("Video Tags")
channel_title = st.text_input("Channel Title")

video_category_id = st.text_input("Video Category ID")
country = st.text_input("Country Code (US, IN, GB...)")

video_duration_sec = st.number_input("Video Duration (seconds)", min_value=0)
channel_subscriber_count = st.number_input("Subscribers", min_value=0)
channel_video_count = st.number_input("Total Videos", min_value=0)
channel_view_count = st.number_input("Total Views", min_value=0)

if st.button("Predict"):

    user_input = {
        "video_title": video_title,
        "video_description": video_description,
        "video_tags": video_tags,
        "channel_title": channel_title,
        "video_category_id": video_category_id,
        "country": country,
        "video_duration_sec": video_duration_sec,
        "channel_subscriber_count": channel_subscriber_count,
        "channel_video_count": channel_video_count,
        "channel_view_count": channel_view_count
    }

    result = predict_trending(user_input)

    st.metric("Trending Probability", f"{result['final_probability']*100:.2f}%")
    st.write("Text Score:", result["text_score"])
    st.write("Numeric Score:", result["numeric_score"])
    st.write("Psych Score:", result["psychology_score"])
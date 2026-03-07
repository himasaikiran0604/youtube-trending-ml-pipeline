import streamlit as st
import plotly.express as px
import pandas as pd
from data_loader import load_data

st.set_page_config(page_title="YouTube Trending Dashboard", layout="wide")

# ---------- HELPER FUNCTION ----------
def format_number(n):
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    elif n >= 1_000:
        return f"{n/1_000:.0f}K"
    else:
        return str(int(n))

# ---------- NAVIGATION ----------
page = st.sidebar.radio("Navigation", ["Dashboard", "Predict"])

# =====================================================
# ===================== DASHBOARD =====================
# =====================================================
if page == "Dashboard":

    df = load_data()

    st.title("YouTube Trending Analytics Dashboard")

    # ---------- FILTERS ----------
    st.sidebar.header("Filters")

    country = st.sidebar.selectbox(
        "Trending Country",
        ["All"] + sorted(df["video_trending_country"].dropna().unique())
    )

    category = st.sidebar.selectbox(
        "Video Category",
        ["All"] + sorted(df["video_category_id"].dropna().unique())
    )

    filtered_df = df.copy()

    if country != "All":
        filtered_df = filtered_df[
            filtered_df["video_trending_country"] == country
        ]

    if category != "All":
        filtered_df = filtered_df[
            filtered_df["video_category_id"] == category
        ]

    # ---------- UNIQUE VIDEO DATA ----------
    unique_videos = filtered_df.drop_duplicates("video_id")

    avg_views = unique_videos["video_view_count"].mean()
    avg_likes = unique_videos["video_like_count"].mean()

    # ---------- KPI CARDS ----------
    k1, k2, k3, k4 = st.columns(4)

    k1.metric("Trending Videos", format_number(len(unique_videos)))
    k2.metric("Avg Views", format_number(avg_views))
    k3.metric("Avg Likes", format_number(avg_likes))
    k4.metric("Unique Channels", format_number(unique_videos["channel_title"].nunique()))

    # =====================================================
    # CATEGORY ANALYSIS
    # =====================================================
    col1, col2 = st.columns(2)

    with col1:

        category_counts = (
            unique_videos["video_category_id"]
            .value_counts()
            .reset_index()
        )

        category_counts.columns = ["Category", "Videos"]

        fig1 = px.bar(
            category_counts,
            x="Category",
            y="Videos",
            title="Trending Videos by Category",
            labels={"Videos": "Number of Videos"}
        )

        st.plotly_chart(fig1, use_container_width=True)

    with col2:

        if len(category_counts) > 1:

            fig2 = px.pie(
                category_counts,
                names="Category",
                values="Videos",
                hole=0.5,
                title="Category Share"
            )

            st.plotly_chart(fig2, use_container_width=True)

        else:
            st.info("Only one category selected.")

    # =====================================================
    # CHANNEL & COUNTRY ANALYSIS
    # =====================================================
    col3, col4 = st.columns(2)

    with col3:

        top_channels = (
            unique_videos["channel_title"]
            .value_counts()
            .head(10)
            .reset_index()
        )

        top_channels.columns = ["Channel", "Videos"]

        fig3 = px.bar(
            top_channels,
            x="Videos",
            y="Channel",
            orientation="h",
            title="Top Trending Channels"
        )

        st.plotly_chart(fig3, use_container_width=True)

    with col4:

        country_counts = (
            unique_videos["video_trending_country"]
            .value_counts()
            .reset_index()
        )

        country_counts.columns = ["Country", "Videos"]

        fig4 = px.bar(
            country_counts,
            x="Country",
            y="Videos",
            title="Trending Videos by Country"
        )

        st.plotly_chart(fig4, use_container_width=True)

    # =====================================================
    # ENGAGEMENT ANALYSIS
    # =====================================================
    col5, col6 = st.columns(2)

    with col5:

        fig5 = px.scatter(
            unique_videos,
            x="video_view_count",
            y="video_like_count",
            color="video_trending_country",
            title="Views vs Likes",
            labels={
                "video_view_count": "Views",
                "video_like_count": "Likes"
            }
        )

        st.plotly_chart(fig5, use_container_width=True)

    with col6:

        fig6 = px.histogram(
            unique_videos,
            x="video_view_count",
            nbins=40,
            title="Views Distribution",
            labels={"video_view_count": "Views"}
        )

        st.plotly_chart(fig6, use_container_width=True)

    # =====================================================
    # TRENDING TIMELINE
    # =====================================================
    if "video_trending_date" in filtered_df.columns:

        filtered_df["video_trending_date"] = pd.to_datetime(
            filtered_df["video_trending_date"]
        )

        timeline = filtered_df.groupby(
            filtered_df["video_trending_date"].dt.date
        ).size()

        fig7 = px.line(
            x=timeline.index,
            y=timeline.values,
            title="Trending Videos Over Time",
            labels={"x": "Date", "y": "Trending Videos"}
        )

        st.plotly_chart(fig7, use_container_width=True)

# =====================================================
# ===================== PREDICT PAGE ==================
# =====================================================
elif page == "Predict":

    import prediction
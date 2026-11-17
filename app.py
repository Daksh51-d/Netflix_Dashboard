
import os
import pandas as pd
import plotly.express as px
import streamlit as st

# --------------------------------------------------
# NETFLIX ANALYTICS DASHBOARD
# --------------------------------------------------

st.set_page_config(
    page_title="Netflix Analytics Dashboard",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Netflix-inspired styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #111111;
        color: #F5F5F5;
    }

    [data-testid="stSidebar"] {
        background-color: #1B1B1B;
    }

    h1, h2, h3 {
        color: #E50914 !important;
    }

    div[data-testid="stMetric"] {
        background: #202020;
        border: 1px solid #3A3A3A;
        padding: 15px;
        border-radius: 10px;
    }

    div[data-testid="stMetric"] label {
        color: #DDDDDD !important;
    }

    div[data-testid="stMetricValue"] {
        color: #FFFFFF !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎬 NETFLIX ANALYTICS")
st.caption(
    "Explore Netflix movies and TV shows "
    "through interactive data visualizations."
)

# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

DATA_PATH = os.path.join("data", "Netflix.csv")


@st.cache_data
def load_data(path):
    data = pd.read_csv(path)
    data.columns = [str(c).strip() for c in data.columns]
    return data


if not os.path.exists(DATA_PATH):
    st.error(f"Dataset not found: {DATA_PATH}")
    st.info(
        "Please put your Netflix.csv file "
        "inside the data folder."
    )
    st.stop()

try:
    df = load_data(DATA_PATH)

except Exception as error:
    st.error(f"Could not read CSV file: {error}")
    st.stop()

if df.empty:
    st.warning("Your dataset is empty.")
    st.stop()

# Convert numeric columns
numeric_columns = [
    "release_year",
    "imdb_votes",
    "Rating Votes",
    "imdb_score",
    "runtime"
]

for column in numeric_columns:
    if column in df.columns:
        df[column] = pd.to_numeric(
            df[column], errors="coerce"
        )

# Check required column
if "type" not in df.columns:
    st.error("The type column is missing.")
    st.write("Available columns:", list(df.columns))
    st.stop()

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.title("🎬 Dashboard Filters")

types = sorted(
    df["type"].dropna().astype(str).unique()
)

selected_types = st.sidebar.multiselect(
    "Content Type",
    options=types,
    default=types
)

filtered = df[
    df["type"].astype(str).isin(selected_types)
].copy()

if "release_year" in filtered.columns:

    years = sorted(
        filtered["release_year"].dropna().astype(int).unique()
    )

    if years:

        year_range = st.sidebar.slider(
            "Release Year",
            min_value=int(min(years)),
            max_value=int(max(years)),
            value=(int(min(years)), int(max(years)))
        )

        filtered = filtered[
            filtered["release_year"].between(
                year_range[0], year_range[1]
            )
        ]

if "age_certification" in filtered.columns:

    ratings = sorted(
        filtered["age_certification"]
        .dropna()
        .astype(str)
        .unique()
    )

    selected_ratings = st.sidebar.multiselect(
        "Age Certification",
        options=ratings,
        default=ratings
    )

    if selected_ratings:
        filtered = filtered[
            filtered["age_certification"]
            .astype(str)
            .isin(selected_ratings)
        ]
    elif ratings:
        filtered = filtered.iloc[0:0]

st.sidebar.caption(
    "Change filters to update the dashboard."
)

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

total_titles = len(filtered)

movie_count = (
    filtered["type"].astype(str).str.lower() == "movie"
).sum()

tv_count = (
    filtered["type"].astype(str).str.lower()
    .isin(["show", "tv show", "tv_show"])
).sum()

k1, k2, k3, k4 = st.columns(4)

k1.metric("Total Titles", f"{total_titles:,}")
k2.metric("Movies", f"{movie_count:,}")
k3.metric("TV Shows", f"{tv_count:,}")

if (
    "imdb_score" in filtered.columns
    and filtered["imdb_score"].notna().any()
):
    average_score = filtered["imdb_score"].mean()
    k4.metric("Average IMDb Score", f"{average_score:.2f}/10")
else:
    k4.metric("Average IMDb Score", "N/A")

st.divider()

# --------------------------------------------------
# DASHBOARD TABS
# --------------------------------------------------

tab1, tab2, tab3, tab4 = st.tabs([
    "Overview",
    "Release Trends",
    "IMDb Analysis",
    "Runtime & Ratings"
])

chart_template = "plotly_dark"

# --------------------------------------------------
# TAB 1: OVERVIEW
# --------------------------------------------------

with tab1:

    st.subheader("Netflix Content Overview")

    left, right = st.columns(2)

    with left:

        type_counts = (
            filtered["type"]
            .astype(str)
            .value_counts()
            .rename_axis("Content Type")
            .reset_index(name="Titles")
        )

        if not type_counts.empty:

            fig = px.pie(
                type_counts,
                names="Content Type",
                values="Titles",
                title="Movies vs TV Shows",
                hole=0.48,
                color_discrete_sequence=[
                    "#E50914", "#777777", "#B20710"
                ]
            )

            fig.update_layout(template=chart_template)

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:
            st.info("No content available.")

    with right:

        if "release_year" in filtered.columns:

            yearly = (
                filtered.dropna(subset=["release_year"])
                .groupby("release_year")
                .size()
                .reset_index(name="Titles")
            )

            if not yearly.empty:

                fig = px.bar(
                    yearly,
                    x="release_year",
                    y="Titles",
                    title="Titles by Release Year",
                    color_discrete_sequence=["#E50914"]
                )

                fig.update_layout(
                    template=chart_template,
                    xaxis_title="Release Year",
                    yaxis_title="Number of Titles"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:
                st.info("No release-year data available.")

    st.subheader("Most Voted Netflix Titles")

    vote_column = (
        "imdb_votes"
        if "imdb_votes" in filtered.columns
        else (
            "Rating Votes"
            if "Rating Votes" in filtered.columns
            else None
        )
    )

    if vote_column and "title" in filtered.columns:

        top_voted = (
            filtered.dropna(subset=[vote_column])
            .nlargest(10, vote_column)
        )

        if not top_voted.empty:

            fig = px.bar(
                top_voted.sort_values(vote_column),
                x=vote_column,
                y="title",
                orientation="h",
                title="Top 10 Titles by Votes",
                color_discrete_sequence=["#E50914"]
            )

            fig.update_layout(
                template=chart_template,
                yaxis_title="",
                xaxis_title="Votes"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:
            st.info("No vote data available.")

    else:
        st.info(
            "This chart needs title and IMDb votes columns."
        )

# --------------------------------------------------
# TAB 2: RELEASE TRENDS
# --------------------------------------------------

with tab2:

    st.subheader("Netflix Content Release Trends")

    if "release_year" in filtered.columns:

        trend_data = filtered.dropna(
            subset=["release_year"]
        ).copy()

        trend_data["release_year"] = (
            trend_data["release_year"].astype(int)
        )

        trend_data = (
            trend_data.groupby(["release_year", "type"])
            .size()
            .reset_index(name="Titles")
        )

        if not trend_data.empty:

            fig = px.line(
                trend_data,
                x="release_year",
                y="Titles",
                color="type",
                markers=True,
                title="Content Released by Year",
                color_discrete_sequence=[
                    "#E50914", "#AAAAAA"
                ]
            )

            fig.update_layout(
                template=chart_template,
                xaxis_title="Release Year",
                yaxis_title="Number of Titles"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        else:
            st.info("No release-year data available.")

    else:
        st.info("Release year column is missing.")

# --------------------------------------------------
# TAB 3: IMDb ANALYSIS
# --------------------------------------------------

with tab3:

    st.subheader("IMDb Votes & Ratings Analysis")

    left, right = st.columns(2)

    if "imdb_score" in filtered.columns:

        score_data = filtered.dropna(
            subset=["imdb_score"]
        )

        with left:

            if not score_data.empty:

                fig = px.histogram(
                    score_data,
                    x="imdb_score",
                    nbins=20,
                    title="IMDb Score Distribution",
                    color_discrete_sequence=["#E50914"]
                )

                fig.update_layout(
                    template=chart_template,
                    xaxis_title="IMDb Score",
                    yaxis_title="Number of Titles"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:
                st.info("No IMDb score data available.")

    else:
        with left:
            st.info("IMDb score column is missing.")

    vote_column = (
        "imdb_votes"
        if "imdb_votes" in filtered.columns
        else (
            "Rating Votes"
            if "Rating Votes" in filtered.columns
            else None
        )
    )

    with right:

        if vote_column and "imdb_score" in filtered.columns:

            scatter_data = filtered.dropna(
                subset=[vote_column, "imdb_score"]
            )

            if not scatter_data.empty:

                fig = px.scatter(
                    scatter_data,
                    x=vote_column,
                    y="imdb_score",
                    color="type",
                    hover_name=(
                        "title"
                        if "title" in scatter_data.columns
                        else None
                    ),
                    title="IMDb Score vs Votes",
                    color_discrete_sequence=[
                        "#E50914", "#AAAAAA"
                    ]
                )

                fig.update_layout(
                    template=chart_template,
                    xaxis_title="IMDb Votes",
                    yaxis_title="IMDb Score"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:
                st.info("No matching IMDb data available.")

        else:
            st.info(
                "IMDb score and vote columns are required."
            )

# --------------------------------------------------
# TAB 4: RUNTIME & RATINGS
# --------------------------------------------------

with tab4:

    st.subheader("Content Runtime & Age Certification")

    left, right = st.columns(2)

    with left:

        if "runtime" in filtered.columns:

            runtime_data = filtered.dropna(
                subset=["runtime"]
            )

            if not runtime_data.empty:

                fig = px.histogram(
                    runtime_data,
                    x="runtime",
                    color="type",
                    nbins=25,
                    title="Runtime Distribution",
                    color_discrete_sequence=[
                        "#E50914", "#AAAAAA"
                    ]
                )

                fig.update_layout(
                    template=chart_template,
                    xaxis_title="Runtime (Minutes)",
                    yaxis_title="Number of Titles"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:
                st.info("No runtime data available.")

        else:
            st.info("Runtime column is missing.")

    with right:

        if "age_certification" in filtered.columns:

            cert_data = (
                filtered["age_certification"]
                .fillna("Not Rated")
                .astype(str)
                .value_counts()
                .reset_index()
            )

            cert_data.columns = [
                "Age Certification",
                "Titles"
            ]

            if not cert_data.empty:

                fig = px.bar(
                    cert_data,
                    x="Age Certification",
                    y="Titles",
                    title="Titles by Age Certification",
                    color_discrete_sequence=["#E50914"]
                )

                fig.update_layout(
                    template=chart_template,
                    xaxis_title="Age Certification",
                    yaxis_title="Number of Titles"
                )

                st.plotly_chart(
                    fig,
                    use_container_width=True
                )

            else:
                st.info("No certification data available.")

        else:
            st.info("Age certification column is missing.")

# --------------------------------------------------
# FILTERED DATA TABLE
# --------------------------------------------------

st.divider()

st.subheader("Netflix Dataset")

st.dataframe(
    filtered,
    use_container_width=True,
    hide_index=True
)
st.caption(
    "Netflix Analytics Dashboard | "
    "Built with Python, Streamlit, Pandas and Plotly"
)

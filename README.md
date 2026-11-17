# 🎬 Netflix Data Analysis Dashboard

An interactive data analytics project built using Python and Streamlit to explore Netflix movies and TV shows through data visualization and exploratory data analysis.

🔗 **Live Dashboard:** https://netflix-analysis-dashboard.streamlit.app/

🔗 **GitHub Repository:** https://github.com/Daksh51-d/Netflix-Dashboard

---

## 📌 Project Overview

This project focuses on analyzing Netflix movies and TV shows using an interactive dashboard developed with Python, Streamlit, Pandas, and Plotly.

The dashboard provides an interactive way to explore Netflix content, understand release trends, examine IMDb ratings, and analyze runtime and content certifications.

The project aims to transform the Netflix dataset into meaningful visual insights through interactive charts, filters, and analytical summaries.

**Important:** This repository documents the dashboard implementation and its intended analysis areas. It does not claim that every insight, metric, or calculation has been independently validated. Review the source data, column definitions, data types, and calculations before using the results for business decisions.

---

## 🎯 Project Objectives

- Explore the distribution of Netflix movies and TV shows.
- Analyze content releases across different years.
- Examine IMDb ratings and voting patterns.
- Understand the runtime distribution of movies and TV shows.
- Explore content distribution by age certification.
- Build an interactive dashboard for data exploration.
- Present data through clear and meaningful visualizations.

---

## 📊 Dashboard Features

The project includes four major analytical sections.

### Dashboard 1 — Netflix Content Overview

**Key metrics and analysis**

- Total Netflix titles.
- Movie and TV show distribution.
- Content breakdown by type.
- Interactive content filters.

**Visualizations**

- Movies vs TV Shows distribution.
- Content distribution by selected categories.
- Overview of Netflix titles.

### Dashboard 2 — Release Trends Analysis

**Analysis requirements**

- Explore Netflix content by release year.
- Identify changes in content releases over time.
- Compare movie and TV show release patterns.

**Visualizations**

- Content releases by year.
- Year-wise content distribution.
- Release trend comparisons.

### Dashboard 3 — IMDb Ratings Analysis

**Analysis requirements**

- Examine IMDb scores.
- Explore IMDb voting patterns.
- Understand the relationship between content ratings and audience engagement.

**Visualizations**

- IMDb score distribution.
- IMDb voting analysis.
- Rating comparisons.

### Dashboard 4 — Runtime & Ratings Analysis

**Analysis requirements**

- Explore movie and TV show runtime.
- Analyze content age certifications.
- Understand the distribution of content across certification categories.

**Visualizations**

- Runtime distribution.
- Age certification analysis.
- Content rating comparisons.

**Note:** The sections above describe the intended analytical areas of the dashboard. Actual chart availability and metric definitions should be checked against the deployed application and source code.

---

## 🔍 Interactive Dashboard Filters

The dashboard provides filters to explore selected portions of the dataset.

- **Content Type:** Filter between Movies and TV Shows.
- **Release Year:** Select the release year or year range.
- **Age Certification:** Explore content by certification category.

These filters help users investigate different segments of Netflix content.

---

## 🗂️ Repository Structure

```text
Netflix-Dashboard/
│
├── README.md
├── app.py
├── requirements.txt
│
├── data/
│   ├── Netflix.csv
│   └── Netflix.xlsx
│
└── assets/
    ├── background.jpg
    └── netflix_logo.png
```

The assets folder is optional if the application does not use external background or logo images.

---

## 🧾 Included Files

| File | Purpose |
|---|---|
| app.py | Main Streamlit dashboard application |
| requirements.txt | Python project dependencies |
| data/Netflix.csv | CSV dataset used by the application |
| data/Netflix.xlsx | Excel version of the dataset |
| assets/ | Dashboard background and logo images, if used |
| README.md | Project documentation |

---

## 📚 Source Data Overview

**Dataset:** Netflix Movies and TV Shows

The application uses the Netflix CSV dataset for analysis.

The following columns are used or expected by the dashboard code:

| Column | Purpose |
|---|---|
| title | Movie or TV show title |
| type | Movie or TV Show classification |
| release_year | Year of release |
| age_certification | Content age certification |
| imdb_score | IMDb rating score |
| imdb_votes | IMDb voting information |
| runtime | Content runtime |
| Rating Votes | Additional voting-related field, if present |

**Data validation warning:** Confirm the actual CSV column names before running the application. Check for missing values, duplicate records, inconsistent data types, and differences between IMDb voting fields. Do not assume that `imdb_votes` and `Rating Votes` represent the same metric.

---

## 🚀 How to Run the Project Locally

Follow these steps to run the dashboard on your computer.

**1. Clone the repository**

```bash
git clone https://github.com/Daksh51-d/Netflix-Dashboard.git
```

**2. Navigate to the project directory**

```bash
cd Netflix-Dashboard
```

**3. Install the required dependencies**

```bash
pip install -r requirements.txt
```

**4. Check the dataset location**

Make sure the CSV file is available at:

```text
data/Netflix.csv
```

**5. Run the Streamlit application**

```bash
python -m streamlit run app.py
```

**6. Open the dashboard**

```text
http://localhost:8501
```

---

## 🌐 Live Dashboard

The application is deployed using Streamlit Community Cloud.

🔗 **Explore the live dashboard:**

https://netflix-analysis-dashboard.streamlit.app/

---

## 🧪 Data & Dashboard Validation Checklist

Before presenting the project as a completed analytical report, check the following:

- The Netflix CSV file loads without errors.
- Dataset column names match the Python application.
- Missing values are reviewed and handled appropriately.
- Duplicate records are identified and reviewed.
- Release years are stored using suitable data types.
- IMDb scores are numeric and handled consistently.
- IMDb voting fields are correctly identified.
- Runtime values are numeric and valid.
- Age certification categories are reviewed.
- Movie and TV show classifications are consistent.
- Dashboard filters update the displayed visualizations correctly.
- Charts reflect the filtered dataset.
- The application runs successfully after deployment.
- All required assets are available at their expected paths.

---

## 🛠️ Tools & Technologies

| Technology | Purpose |
|---|---|
| Python | Programming and data analysis |
| Pandas | Data cleaning and manipulation |
| Streamlit | Interactive web application |
| Plotly | Interactive data visualization |
| Microsoft Excel | Dataset inspection |
| CSV | Data storage |
| Git & GitHub | Version control and project hosting |
| Streamlit Community Cloud | Dashboard deployment |

---

## 💡 Skills Demonstrated

- Exploratory Data Analysis (EDA)
- Data Cleaning and Preparation
- Data Visualization
- Interactive Dashboard Development
- Python Programming
- Data Filtering and Analysis
- Data Storytelling

---

## ⚠️ Data, Licensing & Usage

- Verify the source and licensing conditions of the Netflix dataset before redistribution.
- Do not represent this project as an official Netflix product or an officially endorsed Netflix analysis.
- Netflix names and branding belong to their respective owners.
- The dashboard is an independent portfolio project developed for educational and analytical purposes.
- Validate the dataset and calculations before using any analytical results in formal reports.

---

## 👨‍💻 Author

**Daksh Dewangan**

Aspiring Data Analyst | Python | SQL | Excel | Tableau

- GitHub: https://github.com/Daksh51-d
- Project Repository: https://github.com/Daksh51-d/Netflix-Dashboard
- Live Dashboard: https://netflix-analysis-dashboard.streamlit.app/

---

⭐ If you find this project useful or interesting, consider giving the repository a star!


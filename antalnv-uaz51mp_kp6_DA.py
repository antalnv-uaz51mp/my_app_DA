import streamlit as st
import pandas as pd
import plotly.express as px

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

st.set_page_config(
    page_title="Business Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    return pd.read_csv("dataset.csv")

df = load_data()

st.sidebar.title("Business Performance Dashboard")

selected_year = st.sidebar.selectbox(
    "Year",
    sorted(df["Year"].unique())
)

selected_regions = st.sidebar.multiselect(
    "Region",
    sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

selected_scenario = st.sidebar.radio(
    "Scenario",
    sorted(df["Scenario"].unique())
)

only_profitable = st.sidebar.checkbox(
    "Only profitable companies",
    value=False
)

filtered_df = df[
    (df["Year"] == selected_year)
    & (df["Region"].isin(selected_regions))
    & (df["Scenario"] == selected_scenario)
]

if only_profitable:
    filtered_df = filtered_df[filtered_df["Profit"] > 0]

st.title("Business Performance Dashboard")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Companies",
    len(filtered_df)
)

col2.metric(
    "Average Revenue",
    f"{filtered_df['Revenue'].mean():,.0f}"
)

col3.metric(
    "Average Profit",
    f"{filtered_df['Profit'].mean():,.0f}"
)

col4.metric(
    "Average ROI",
    f"{filtered_df['ROI'].mean():.2f}"
)

selected_columns = st.multiselect(
    "Columns",
    df.columns.tolist(),
    default=[
        "Company",
        "Region",
        "Industry",
        "Revenue",
        "Profit",
        "ROI"
    ]
)

st.dataframe(
    filtered_df[selected_columns],
    use_container_width=True
)

region_profit = (
    filtered_df.groupby("Region")["Profit"]
    .mean()
    .reset_index()
)

fig_bar = px.bar(
    region_profit,
    x="Region",
    y="Profit",
    title="Average Profit by Region"
)

st.plotly_chart(fig_bar, use_container_width=True)

industry_count = (
    filtered_df["Industry"]
    .value_counts()
    .reset_index()
)

industry_count.columns = ["Industry", "Count"]

fig_pie = px.pie(
    industry_count,
    names="Industry",
    values="Count",
    title="Industry Distribution"
)

st.plotly_chart(fig_pie, use_container_width=True)

fig_scatter = px.scatter(
    filtered_df,
    x="Investment",
    y="Profit",
    color="Industry",
    size="Revenue",
    hover_name="Company",
    title="Investment vs Profit"
)

st.plotly_chart(fig_scatter, use_container_width=True)

features = [
    "Revenue",
    "Expenses",
    "Investment",
    "Customers",
    "ConversionRate",
    "MarketGrowth",
    "AdBudget"
]

X = df[features]
y = df["Profit"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

r2 = r2_score(y_test, predictions)
mae = mean_absolute_error(y_test, predictions)

c1, c2 = st.columns(2)

c1.metric("R² Score", f"{r2:.3f}")
c2.metric("MAE", f"{mae:,.0f}")

comparison = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})

fig_ml = px.scatter(
    comparison,
    x="Actual",
    y="Predicted",
    title="Actual vs Predicted Profit"
)

st.plotly_chart(fig_ml, use_container_width=True)
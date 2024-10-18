import streamlit as st
import pandas as pd
import plotly.express as px
import json

# Load the data from the JSON file
with open('fertility_gdp_2014_2024.json') as f:
    data = json.load(f)

# Convert the JSON data into a DataFrame
df = pd.DataFrame(data)

# Convert Year to an integer and handle missing/numeric data
df['Year'] = df['Year'].astype(int)
df['GDP'] = pd.to_numeric(df['GDP'], errors='coerce')
df['Fertility Rate'] = pd.to_numeric(df['Fertility Rate'], errors='coerce')
df['GDP Percentage'] = pd.to_numeric(df['GDP Percentage'], errors='coerce')

# Streamlit App Layout
st.title("Global Population Growth and Fertility Trends in Relation to Economic Development (2014-2023)")

# Dropdown for selecting the metric (GDP, Fertility Rate, GDP Percentage)
metric = st.selectbox("Select Metric to Display", ['GDP per Capita', 'Fertility Rate', 'GDP Percentage'])

# Choropleth Map
st.subheader(f"Choropleth Map - {metric}")
if metric == 'GDP per Capita':
    fig = px.choropleth(df, locations='Country Code', color='GDP', hover_name='Country Name',
                        color_continuous_scale=px.colors.sequential.Plasma, title='Global GDP per Capita (2014-2023)',
                        animation_frame='Year', range_color=[df['GDP'].min(), df['GDP'].max()])
elif metric == 'Fertility Rate':
    fig = px.choropleth(df, locations='Country Code', color='Fertility Rate', hover_name='Country Name',
                        color_continuous_scale=px.colors.sequential.Plasma, title='Global Fertility Rates (2014-2023)',
                        animation_frame='Year', range_color=[df['Fertility Rate'].min(), df['Fertility Rate'].max()])
else:
    fig = px.choropleth(df, locations='Country Code', color='GDP Percentage', hover_name='Country Name',
                        color_continuous_scale=px.colors.sequential.Plasma, title='Global GDP Percentage Growth (2014-2023)',
                        animation_frame='Year', range_color=[df['GDP Percentage'].min(), df['GDP Percentage'].max()])

st.plotly_chart(fig)

# Scatter Plot - Fertility vs GDP
st.subheader("Scatter Plot - Fertility vs GDP")

# Ensure GDP Percentage is non-negative for bubble size (using absolute values)
df['GDP Percentage Size'] = df['GDP Percentage'].abs()

# Create the scatter plot
fig = px.scatter(df, x='GDP', y='Fertility Rate', color='Country Name', hover_name='Country Name',
                 title="Fertility Rate vs GDP Per Capita (2014-2023)", animation_frame='Year', 
                 size='GDP Percentage Size', size_max=15)  # Use the new non-negative size column

st.plotly_chart(fig)

# Line Chart - Trends over Time
st.subheader("Trends over Time")
# Select countries for comparison
countries = df['Country Name'].unique()
selected_countries = st.multiselect('Select Countries to Compare', countries, default=['Afghanistan', 'Albania', 'Algeria'])

# Filter data for selected countries and years between 2014 and 2022
df_filtered = df[(df['Country Name'].isin(selected_countries)) & (df['Year'] >= 2014) & (df['Year'] <= 2022)]

# Ensure there are no NaN or 0 values in Fertility Rate or GDP
df_filtered = df_filtered[(df_filtered['Fertility Rate'] > 0) & (df_filtered['GDP'] > 0)]

# Create the line plot for Fertility Rate
fig = px.line(df_filtered, x='Year', y='Fertility Rate', color='Country Name', 
              title="Fertility Rate Trends Over Time (2014-2022)")

# Add markers for selected countries
for country in selected_countries:
    fig.add_scatter(x=df_filtered[df_filtered['Country Name'] == country]['Year'], 
                    y=df_filtered[df_filtered['Country Name'] == country]['Fertility Rate'], 
                    mode='markers', name=country)



st.plotly_chart(fig)


# Bar Chart - Top 10 and Bottom 10 Countries
st.subheader("Top 10 and Bottom 10 Countries")

# Filter for the most recent year (2023) and exclude rows with null or zero GDP
df_gdp_2023 = df[(df['Year'] == 2023) & (df['GDP'] > 0)]

# Get top 10 and bottom 10 countries by GDP
top_10_gdp = df_gdp_2023.nlargest(10, 'GDP')
bottom_10_gdp = df_gdp_2023.nsmallest(10, 'GDP')

# Bar chart for top 10 countries by GDP in 2023
top_10_gdp_fig = px.bar(top_10_gdp, x='Country Name', y='GDP', labels={'GDP': 'GDP per Capita'}, 
                        title="Top 10 Countries by GDP in 2023")

# Bar chart for bottom 10 countries by GDP in 2023
bottom_10_gdp_fig = px.bar(bottom_10_gdp, x='Country Name', y='GDP', labels={'GDP': 'GDP per Capita'}, 
                           title="Bottom 10 Countries by GDP in 2023")

st.plotly_chart(top_10_gdp_fig)
st.plotly_chart(bottom_10_gdp_fig)

# Filter for the most recent year (2022) and exclude rows with null or zero fertility rate
df_fertility_2022 = df[(df['Year'] == 2022) & (df['Fertility Rate'] > 0)]

# Get top 10 and bottom 10 countries by Fertility Rate
top_10_fertility = df_fertility_2022.nlargest(10, 'Fertility Rate')
bottom_10_fertility = df_fertility_2022.nsmallest(10, 'Fertility Rate')

# Bar chart for top 10 countries by Fertility Rate in 2022
top_10_fertility_fig = px.bar(top_10_fertility, x='Country Name', y='Fertility Rate', 
                              title="Top 10 Countries by Fertility Rate in 2022",
                              labels={'Fertility Rate': 'Fertility Rate (births per woman)'})

# Bar chart for bottom 10 countries by Fertility Rate in 2022
bottom_10_fertility_fig = px.bar(bottom_10_fertility, x='Country Name', y='Fertility Rate', 
                                 title="Bottom 10 Countries by Fertility Rate in 2022",
                                 labels={'Fertility Rate': 'Fertility Rate (births per woman)'})

# Display the bar charts
st.plotly_chart(top_10_fertility_fig)
st.plotly_chart(bottom_10_fertility_fig)


# Interactivity: Country Search
st.subheader("Search for a Country")
country_search = st.text_input("Enter a country name:")
if country_search:
    country_data = df[df['Country Name'].str.contains(country_search, case=False)]
    if not country_data.empty:
        st.write(country_data)
    else:
        st.write("No data found for the selected country.")

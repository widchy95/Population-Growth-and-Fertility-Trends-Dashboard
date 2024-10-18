# Global Fertility and GDP Visualization Dashboard

This project provides an interactive data visualization dashboard for exploring global trends in **Fertility Rates**, **GDP per Capita**, and **GDP Growth** across countries for the years 2014 to 2023. The dashboard is built using **Streamlit** and **Plotly** for interactive visualizations.

## Features

The dashboard offers the following visualizations:

### 1. Choropleth Map (Global View)
- **Metrics**: Fertility Rate, GDP per Capita, or Population Growth.
- **Interaction**: Dropdown to toggle between metrics.
- **Tooltips**: Detailed statistics (e.g., fertility rate, GDP) displayed when hovering over countries.
- **Geographical Focus**: Zoom and pan for better exploration.

### 2. Scatter Plot (Fertility Rate vs. GDP)
- **X-axis**: GDP per capita.
- **Y-axis**: Fertility rate.
- **Filters**: Select countries by region (continents) or income levels (World Bank classifications).
- **Bubble Size**: Optionally size bubbles by population growth.

### 3. Line Chart (Trends over Time)
- **Metrics**: Fertility Rate over time (2014-2022).
- **Filters**: Select specific countries or regions.
- **Interaction**: Compare multiple countries on the same chart.

### 4. Bar Chart (Top/Bottom Countries)
- **Metrics**: Rank countries by Fertility Rate or GDP per Capita.
- **Top 10 and Bottom 10**: Toggle to display the top or bottom countries.
- **Data Cleaning**: Excludes countries with null or zero values.

## Data Sources

The data used in this project comes from:
- **Fertility Rate**: [World Bank Data](https://data.worldbank.org/indicator/SP.DYN.TFRT.IN)
- **GDP per Capita**: [World Bank Data](https://data.worldbank.org/indicator/NY.GDP.PCAP.CD)
- **GDP Growth**: [World Bank Data](https://data.worldbank.org/indicator/NY.GDP.PCAP.KD.ZG)

The dataset includes **Country Name**, **Country Code**, and the following indicators for the years 2014-2023:
- **Fertility Rate** (births per woman)
- **GDP per Capita** (current US$)
- **GDP Growth** (annual %)

## Project Structure
. ├── Resources │ ├── Population and Fertility Data by Country.csv │ ├── GDP by Country_Data.csv │ └── fertility_gdp_2014_2024.json ├── Python_Analysis │ ├── data_cleaning.py │ └── visualization.py ├── README.md └── requirements.txt


- **`Resources/`**: Contains the source data files (CSV and JSON).
- **`Python_Analysis/`**: Contains Python scripts for data cleaning and visualization.
- **`README.md`**: This file, providing an overview of the project.
- **`requirements.txt`**: List of required Python packages.

## Getting Started

### Prerequisites

Make sure you have Python 3.7+ installed. You also need to install the required Python packages, which are listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```
## Run the Dashboard

### Clone the repository:
```bash
git clone https://github.com/widchy95/global-fertility-gdp-dashboard.git
```

## Navigate to the project directory:
```bash
cd global-fertility-gdp-dashboard
```

## Run the Streamlit app:
```bash
streamlit run global-fertility-gdp-dashboard/visualization.py
```
## Open your browser and go to:
```arduino
http://localhost:8501
```
to view the dashboard.

## Usage

The dashboard provides several interactive visualizations that allow users to explore global trends in fertility and GDP data. You can filter by country, year, and different metrics to analyze patterns and compare countries.

### Example Use Cases:

- Compare fertility rates and GDP per capita across countries for a given year.
- Explore trends in fertility rate over time for selected countries.
- Identify the top 10 and bottom 10 countries based on GDP per capita or fertility rate.

## Technologies Used

- **Python**: Programming language used for data processing and visualization.
- **Streamlit**: Web framework for building interactive dashboards.
- **Plotly**: Library for creating interactive plots and charts.
- **Pandas**: Data manipulation and analysis.
- **GeoPandas**: Geospatial data processing (for choropleth maps).

## Future Enhancements

- Add **population growth** data to provide a more comprehensive view of country-level demographics.
- Include additional **filters** such as income levels and continent-based views.
- Optimize for **mobile devices** to ensure responsiveness across different platforms.
- Improve performance by **caching data** and using more efficient data processing techniques.

---

**Author**: Widchy Joachim - Data Analyst



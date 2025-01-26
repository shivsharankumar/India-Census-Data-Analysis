# India Census Dashboard

## Overview
The India Census Dashboard is a Streamlit-based web application that allows users to explore and analyze detailed census data for India. The application provides insights into demographics, literacy rates, workforce distribution, household amenities, and more, with interactive visualizations and filters.

## Features
- **Dynamic Filters**: Select states and districts to refine the dataset.
- **Overview Metrics**: Displays total population, sex ratio, and literacy rate.
- **Interactive Visualizations**:
  - Age group distribution (Pie chart).
  - Male vs. Female literacy comparison (Bar chart).
  - Household amenities distribution (Bar chart).
  - Workforce distribution (Pie chart).
  - Religious composition (Bar chart).
  - Population distribution map (Geographical scatter plot).
- **Custom Comparisons**: Compare any metric across states.
- **Downloadable Reports**: Export filtered data as a CSV file.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/india-census-dashboard.git
   cd india-census-dashboard
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   streamlit run app.py
   ```

## Dataset
The application uses a census dataset with the following columns:
- State
- District
- Latitude, Longitude
- Population, Male, Female
- Literacy, Male_Literate, Female_Literate
- Various demographic, education, and household parameters (e.g., LPG households, internet access, education levels, etc.)

Ensure the dataset is available as `india_census_data.csv` in the root directory of the project or update the file path in the code.

## Usage
1. **Filters**: Select states and districts from the sidebar to filter the dataset.
2. **View Metrics**: The "Overview" section provides key statistics based on the filtered data.
3. **Analyze Visualizations**: Explore various visualizations for detailed insights.
4. **Export Data**: Download filtered data for offline analysis.

## Example Visualizations
- **Age Group Distribution**: Understand the population distribution across different age groups.
- **Workforce Distribution**: Analyze the workforce composition (Main Workers, Marginal Workers, Non-Workers).
- **Religious Composition**: Explore the distribution of major religions.
- **Geographical Insights**: View population distribution on an interactive map.

## Folder Structure
```
india-census-dashboard/
|-- app.py                # Main application file
|-- requirements.txt      # Python dependencies
|-- india_census_data.csv # Census dataset (replace with your dataset)
```

## Dependencies
- Python 3.8+
- Streamlit
- Pandas
- NumPy
- Plotly

Install dependencies using the `requirements.txt` file:
```bash
pip install -r requirements.txt
```

## Contributing
Contributions are welcome! If you have suggestions for new features or improvements, feel free to create an issue or submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
This project is inspired by the need to make census data easily accessible and understandable through interactive visualizations.


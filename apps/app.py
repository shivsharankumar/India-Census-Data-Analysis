import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
def main():
    # st.set_page_config(layout='wide')
    # st.title("India Census Data Analysis")
    
    # #add data
    # df=pd.read_csv('../datasets/india-census.csv')
    # df['State']=df['State'].str.title()
    # st.subheader("Dataset Preview")
    # st.dataframe(df.head())

    # st.subheader("Dataset Summary")
    # st.write(df.describe())
    # list_of_states=list(df['State'].unique())
    # list_of_states.insert(0,'All States')
    # st.sidebar.title('Indiviz')
    # selected_state=st.sidebar.selectbox('Select a state',list_of_states)
    # primary=st.sidebar.selectbox('Select primary parameters',sorted(df.columns[5:]))
    # secondary=st.sidebar.selectbox('Select secondary parameters',sorted(df.columns[5:]))
    # plot=st.sidebar.button('Plot Graph')

    # if plot:
    #     st.text('Size Represents Primary Parameter')
    #     st.text('Color Represents Secondary Parameter')
    #     if selected_state=='All States':
    #         st.subheader("India Data Analysis")
    #         #plotting for india
    #         fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary,
    #                             color=secondary,zoom=4,size_max=35,mapbox_style='carto-positron'
    #                             ,width=1200,height=700,hover_name='District')
    #         st.plotly_chart(fig,use_container_width=True)
    #     else:
    #         st.subheader("State-wise Data Analysis")
    #         state_df=df[df['State']==selected_state]
    #         fig=px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude',
    #                             size=primary,color=secondary,zoom=4,size_max=35,
    #                             mapbox_style='carto-positron',width=1200,height=700
    #                             ,hover_name='District')
    #         st.plotly_chart(fig,use_container_width=True)

    # Load Data
    @st.cache_data
    def load_data():
        data = pd.read_csv('../../datasets/india-census.csv')  # Replace with actual file path
        return data

    
    data = load_data()

    # Sidebar Filters
    st.sidebar.title("Filters")
    states = st.sidebar.multiselect("Select State(s):", options=data['State'].unique())

    districts = []
    if states:
        filtered_districts = data[data['State'].isin(states)]['District'].unique()
        districts = st.sidebar.multiselect("Select District(s):", options=filtered_districts)

    filtered_data = data
    if states:
        filtered_data = filtered_data[filtered_data['State'].isin(states)]
    if districts:
        filtered_data = filtered_data[filtered_data['District'].isin(districts)]

    # Dashboard Layout
    st.title("India Census Dashboard")

    # Overview Section
    st.header("Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Population", f"{filtered_data['Population'].sum():,}")
    col2.metric("Sex Ratio", f"{(filtered_data['Female'].sum() / filtered_data['Male'].sum() * 1000):.0f} females per 1000 males")
    col3.metric("Literacy Rate", f"{(filtered_data['Literate'].sum() / filtered_data['Population'].sum() * 100):.2f}%")

    # Demographics Section
    st.header("Demographics Analysis")
    age_groups = ["Age_Group_0_29", "Age_Group_30_49", "Age_Group_50"]
    age_data = filtered_data[age_groups].sum().reset_index()
    age_data.columns = ["Age Group", "Population"]
    fig_age = px.pie(age_data, names="Age Group", values="Population", title="Age Group Distribution")
    st.plotly_chart(fig_age)

    # Literacy Analysis
    st.header("Literacy Analysis")
    literacy_data = filtered_data[['Male_Literate', 'Female_Literate']].sum().reset_index()
    literacy_data.columns = ["Gender", "Literate"]
    fig_literacy = px.bar(literacy_data, x="Gender", y="Literate", title="Male vs Female Literacy")
    st.plotly_chart(fig_literacy)

    # Household Amenities
    st.header("Household and Amenities")
    amenities = ["LPG_or_PNG_Households", "Housholds_with_Electric_Lighting", "Households_with_Internet"]
    amenities_data = filtered_data[amenities].sum().reset_index()
    amenities_data.columns = ["Amenity", "Count"]
    fig_amenities = px.bar(amenities_data, x="Amenity", y="Count", title="Household Amenities")
    st.plotly_chart(fig_amenities)

    # Workforce Analysis
    # st.header("Workforce Distribution")
    # workforce = ["Main_Workers", "Marginal_Workers", "Non_Workers"]
    # print("----->",filtered_data.columns)
    # workforce_data = filtered_data[workforce].sum().reset_index()
    # workforce_data.columns = ["Workforce Type", "Count"]
    # fig_workforce = px.pie(workforce_data, names="Workforce Type", values="Count", title="Workforce Distribution")
    # st.plotly_chart(fig_workforce)

    # Religion Insights
    st.header("Religion Composition")
    religions = ["Hindus", "Muslims", "Christians", "Sikhs", "Buddhists", "Jains", "Others_Religions"]
    religion_data = filtered_data[religions].sum().reset_index()
    religion_data.columns = ["Religion", "Population"]
    fig_religion = px.bar(religion_data, x="Religion", y="Population", title="Religious Composition")
    st.plotly_chart(fig_religion)

    # Maps
    st.header("Geographical Distribution")
    fig_map = px.scatter_mapbox(filtered_data, lat="Latitude", lon="Longitude", zoom=4,size_max=35,
                             mapbox_style="carto-positron",width=1200,height=500,
                            size="Population", color="State", hover_name="District",
                            title="Population Distribution Map")
    st.plotly_chart(fig_map,use_container_width=True)
    #fig=px.scatter_mapbox(df,lat='Latitude',lon='Longitude',size=primary,
    #                             color=secondary,zoom=4,size_max=35,mapbox_style='carto-positron'
    #                             ,width=1200,height=700,hover_name='District')
    #         st.plotly_chart(fig,use_container_width=True)
    # Comparison Section
    st.header("Custom Comparisons")
    comparison_col = st.selectbox("Select a Metric to Compare:", options=data.columns)
    comparison_fig = px.bar(filtered_data, x="State", y=comparison_col, color="State",
                            title=f"State-wise Comparison of {comparison_col}")
    st.plotly_chart(comparison_fig)

    # Downloadable Reports
    st.header("Download Data")
    st.download_button("Download Filtered Data as CSV", 
                    data=filtered_data.to_csv(index=False).encode('utf-8'), 
                    file_name="filtered_census_data.csv", mime="text/csv")




if __name__ == "__main__":
    main()

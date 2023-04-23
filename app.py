import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide')

df = pd.read_csv('india.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall India')

st.sidebar.title('SOCIAL INDICATORS OF INDIA')

select_state = st.sidebar.selectbox('Select state',list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(list(df.columns[5:])))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(list(df.columns[5:])))

plot = st.sidebar.button('Plot Graph')

if plot:
    st.text('Size :  Primary parameter')
    st.text('Color : Secondary parameter')
    if select_state == 'Overall India':
        fig = px.scatter_mapbox(df, lat='Latitude',lon='Longitude',size=primary,color=secondary, size_max=30, zoom=5, height = 1000, width=2500,
                                mapbox_style='carto-positron',hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        state_df = df[df['State'] == select_state]

        fig = px.scatter_mapbox(state_df, lat='Latitude', lon='Longitude', size=primary, color=secondary, size_max=30, zoom=5, height=1000, width=2500,
                                mapbox_style='carto-positron',hover_name='District')
        st.plotly_chart(fig, use_container_width=True)


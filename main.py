import streamlit as st
import pandas as pd
import plotly.express as px


def get_data(x, y):
    country_data = pd.read_csv('happy.csv')
    fig = px.scatter(country_data, x=x.lower(), y=y.lower())
    return fig


if __name__ == '__main__':
    st.title('In Search of Happiness')

    axis_options = ('GDP', 'Happiness', 'Generosity')
    x_axis = st.selectbox('Select the data for the X-axis', options=axis_options, index=0, key='x-axis')
    y_axis = st.selectbox('Select the data for the Y-axis', options=axis_options, index=0, key='y-axis')

    chart_data = get_data(x_axis, y_axis)

    st.subheader(f'{x_axis} and {y_axis}')
    st.plotly_chart(chart_data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

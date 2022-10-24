import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

# set title 
st.title('California Housing Data (1990) by Xiyin Deng')
df = pd.read_csv('housing.csv')

# add a slider (have to give float)
median_house_price_filter = st.slider('Median house price', 0.0, 500001.0, 200000.0)

# create a multi select
location_filter = st.sidebar.multiselect(
     'choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique())  # defaults

# filter by house value
df = df[df.median_house_value <= median_house_price_filter]

# filter by location
df = df[df.ocean_proximity.isin(location_filter)]

# create button widget
button=st.sidebar.radio(label='Choose income level',options=('Low','Medium','High'))
if button=='Low':
    df=df[df.median_income<=2.5]
elif button=='Medium':
    df=df[(df['median_income']>=2.5)&(df['median_income']<=4.5)]
else:
    df=df[df.median_income>4.5]

# show on map (need columns named 'atittude' and 'longitude')
st.markdown('### See more filters in the sidebar:')
st.map(df)

# show histogram
st.markdown('### Histogram of the Median House Value')
fig,ax=plt.subplots()
ax.hist(df.median_house_value,bins=30)
st.pyplot(fig)
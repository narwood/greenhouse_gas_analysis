import streamlit as st
import pandas as pd

@st.cache()
def load_data(path: str):
    data = pd.read_csv(path, index_col=[0])
    return data

@st.cache()
def df_to_csv(df: pd.DataFrame):
    return df.to_csv().encode('utf-8')

st.title("Greenhouse Gas Emissions")
st.markdown(
"""
Hi! This is our project for CDC 2022 :)
""")
data = load_data("/Users/mateo/Documents/PROJECTS/CDC - 2022/Annual_Greenhouse_Gas_(GHG)_Air_Emissions_Accounts.csv")

regions = ['All']
for country in data.Country.unique():
  regions.append(country)
industries = ['All']
for industry in data.Industry.unique():
  industries.append(industry)
gas_types = ['All']
for gastype in data.Gas_Type.unique():
  gas_types.append(gastype)



display_region = st.selectbox(label='Region', options=regions, help="Choose a region to view.")
display_industry = st.selectbox(label='Industry', options=industries, help="Choose an industry to view.")
display_gas_types = st.selectbox(label='Gas Type', options=gas_types, help="Choose a gas type to view.")


if display_region != 'All' and display_industry == 'All' and display_gas_types == 'All':
  data = data[data['Country'] == display_region]
elif display_region == 'All' and display_industry != 'All' and display_gas_types == 'All':
  data = data[data['Industry']== display_industry]
elif display_region == 'All' and display_industry == 'All' and display_gas_types != 'All':
  data = data[data['Gas_Type']==display_gas_types]
elif display_region != 'All' and display_industry != 'All' and display_gas_types == 'All':
  data = data[data['Country'] == display_region][data['Industry']== display_industry]
elif display_region != 'All' and display_industry == 'All' and display_gas_types != 'All':
  data = data[data['Country'] == display_region][data['Gas_Type']==display_gas_types]
elif display_region == 'All' and display_industry != 'All' and display_gas_types != 'All':
  data = data[data['Industry']== display_industry][data['Gas_Type']==display_gas_types]
elif display_region != 'All' and display_industry != 'All' and display_gas_types != 'All':
  data = data[data['Country'] == display_region][data['Industry']== display_industry][data['Gas_Type']==display_gas_types]

st.dataframe(data)
region_text = display_region.lower().replace(" ", "")
industry_text = display_industry.lower().replace(" ", "")
gas_type_text = display_gas_types.lower().replace(" ", "")
st.download_button(
    label="Download data!",
    data=df_to_csv(data),
    file_name=f"{region_text}_{industry_text}_{gas_type_text}.csv",
    mime="text/csv"
)
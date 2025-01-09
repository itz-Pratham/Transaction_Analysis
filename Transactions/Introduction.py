import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Welcome",
    page_icon="👋",
)

#image = Image.open('Final_Periodic_App/Stax_Banner.png')

#st.image(image)

st.write("# Welcome to Transaction Analyzer!")

st.markdown(
    """
    **Effortlessly gain insights into your financial data with our interactive platform. Upload your transaction history to:**

    - Visualize spending patterns through dynamic graphs and charts.
    - Categorize expenses to understand where your money goes.
    - Monitor income and expenditures over time for better budgeting.
    - Breakdowns the transaction data into various fields to ensure systematic analysis.
    - Start by uploading your transaction CSV file, and let our tool transform your data into meaningful visualizations!

    
     **👈 Select an app from the sidebar** to get started

"""
)
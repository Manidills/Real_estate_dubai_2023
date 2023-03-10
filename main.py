from os import pread
from grant import grant
from mortgage import mortgage
from pre_register import pre
from sell import sell
import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt
from streamlit_option_menu import option_menu


# Layout
st.set_page_config(page_title="DUBAI",
    page_icon="chart_with_upwards_trend",layout="wide")

padding_top = 0

st.markdown(f"""
    <style>
        .reportview-container .main .block-container{{
            padding-top: {padding_top}rem;
        }}
    </style>""",
    unsafe_allow_html=True,
)

IMAGE = "https://i.gifer.com/Nad3.gif"

a, b= st.columns([1,2])
a.image(IMAGE, width=200)
b.title(" Habibi Come to Dubai\n Insights about 2023 real estate transactions in DUBAI, we have four categories (Pre-Register,Sell,Grant,Mortgage Register), and our dashboard provides detailed information about these four procedure names.")
st.markdown("##")
st.markdown("##")




option =  option_menu("DUBAI", ["About", "Pre-Register", "Sell", "Grant", "Mortgage Register"],
                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,orientation="horizontal",
                         styles={
        "container": {"padding": "5!important", "background-color": "black"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "black"},
    }
    )

if option == 'About':
    st.write("""   
    #### :red[Pre-Register] :  It is a real estate procedure that refers to the process of registering a property for sale before it is officially launched on the market.  ####  """)
    st.markdown("##")
    st.write("""   
    #### :red[Sell] : When a property is sold in Dubai, the ownership of the property is transferred from the seller to the buyer in exchange for an agreed upon price. This is a straightforward transaction where the seller is transferring ownership of the property to the buyer and receiving payment in return. ####  """)
    st.markdown("##")
    st.write("""   
    #### :red[Grant] : In Dubai, a property can also be granted to someone. This means that the owner of the property is giving ownership of the property to someone else without receiving any payment in return. This can be done as a gift or as part of an inheritance. ####  """)
    st.markdown("##")
    st.write("""   
    #### :red[Mortgage Register]: It is the process of registering a mortgage on a property with the Dubai Land Department (DLD). A mortgage is a loan that is taken out to purchase a property, and the registration of the mortgage provides security to the lender by giving them a legal claim on the property in case the borrower defaults on the loan. ####  """)

    st.markdown("##")
    st.success(f"Source data from {'https://www.dubaipulse.gov.ae/data/dld-transactions/dld_transactions-open'}")
    st.info (f"{'https://github.com/Manidills/Real_estate_dubai_2023'}")
elif option == 'Pre-Register':
    pre()
elif option == 'Sell':
    sell()
elif option == 'Grant':
    grant()
elif option == 'Mortgage Register':
    mortgage()

import streamlit as st
import plotly.express as px
import pandas as pd
import datetime
import altair as alt
import math


def millify(n):
    n = float(n)
    millnames = ['',' K',' M',' B',' T']
    millidx = max(0,min(len(millnames)-1,
                        int(math.floor(0 if n == 0 else math.log10(abs(n))/3))))

    return '£' + str(n / 10**(3 * millidx)) + str(millnames[millidx])


def sell():
    df = pd.read_csv("2023_dubai.csv")
    df = df[df['procedure_name_en'] == 'Sell']
    df = df[['instance_date','property_type_en','actual_worth','property_usage_en','rooms_en','nearest_landmark_en','nearest_metro_en','area_name_en','procedure_area','meter_sale_price','building_name_en']]
    st.markdown("#")
    st.markdown("#")
    col1, col2, col3 = st.columns(3)
    col1.metric("Properties Total Worth In AED", millify(int(df['actual_worth'].sum())))
    col2.metric("Properties Counts", len(df))
    col3.metric("Peoples Favourite Area", df['area_name_en'].max())
    property_type_grp = df.groupby(['instance_date', 'property_type_en']).sum().reset_index()
    st.markdown("#")
    st.markdown("#")
    a, b = st.columns([6,2])
    with a:
        st.write("""   
        #### Property Types Total Worth ####  """)
        st.markdown("#")
        dom = ['Land', 'Unit', 'Villa', 'Building']
        rng = ['red', 'green', 'yellow', 'white']
        st.altair_chart(
            alt.Chart(property_type_grp).mark_circle(color='red').encode(
            x='instance_date:T',
            y="actual_worth:Q",
            color=alt.Color('property_type_en', scale=alt.
                            Scale(domain=dom, range=rng))
            
        )
       ,
        use_container_width=True
    )
    with b:
        st.markdown("##")
        st.markdown("##")
        st.write(
            '''
            Units, Villa, bulidings and Land flooded all over but still Units having upper hands in :red[Price]. But its a good insights to check Lands also selling frequently and giving tough fights to villas and units. 
            
            '''
        )
    landmark_grp = df.groupby(['nearest_landmark_en']).sum().reset_index()
    st.markdown("##")
    st.write("""
    ###  Properties Total Worth Near Landmarks  ###
    """)
    st.altair_chart(
        alt.Chart(landmark_grp).mark_bar(color='#6da832').encode(
            x='nearest_landmark_en:N',
            y="actual_worth:Q",
            
        ).properties(
            width=800,
            height=300
        ),  use_container_width=True
    
                    )
    st.write("Properties around Buj AL Arab, Downtown and Buj Khalifa seems very costlier compare with others landmarks. Properties around the :red[Sports city] are rapidliy increasing, studios , clubs and inititutes are increaing near to that. ")

    
    landmark_grp = df.groupby(['instance_date']).mean().reset_index()
    st.markdown("##")
    st.write("""
    ###  Properties AVG Sale Per Day  ###
    """)
    st.altair_chart(
        alt.Chart(landmark_grp).mark_circle(color='yellow').encode(
            x='instance_date:T',
            y="actual_worth:Q",
            
        ).properties(
            width=800,
            height=300
        ),  use_container_width=True
    
                    )



    a,b = st.columns([1,2])

    with a:
        room_grouped = df.groupby(['rooms_en']).sum().reset_index()
        st.markdown("##")
        st.write("""
        ###  Rooms Total Worth  ###
        """)
        st.markdown("##")
        st.altair_chart(
             alt.Chart(room_grouped).mark_bar(color='blue').encode(
            x='rooms_en:N',
            y="actual_worth:Q",
            
        ).properties(
            width=800,
            height=300
        )
            ,  use_container_width=True
       , )
        st.write("3 B/R, 2 B/R, 1 B/R are high selling rooms thats expected but studios and offices are slowly getting in to the picture ")

    with b:
        area_grouped = df.groupby(['area_name_en']).sum().reset_index()
        st.markdown("##")
        st.write("""
        ### Area Size in SQ-M  ###
        """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(area_grouped).mark_bar(color='white').encode(
            x='area_name_en:N',
            y="procedure_area:Q",
            
        ).properties(
            width=800,
            height=300
        )
            ,  use_container_width=True
    , )
        st.write("The area called :blue[AL Jadaf] that contain property with high produce area.This area is well known for properties tradings.")

    st.markdown("##")
    st.write("""
        ### Top 5 high worth properties  ###
        """)
    st.markdown("##")
    st.dataframe(df.sort_values('actual_worth',ascending=False).head())

   
    
    st.markdown("##")
    st.write("""
        ### Rooms Total Worth Based on Area's  ###
        """)
    st.markdown("##")
    room_area_grp = df.groupby(['area_name_en','rooms_en']).sum().reset_index()
    st.altair_chart(
            alt.Chart(room_area_grp).mark_bar().encode(
            x='area_name_en:N',
            y="actual_worth:Q",
            color='rooms_en:N',
            
        ).properties(
            width=800,
            height=300
        ),  use_container_width=True
                )

    a, b = st.columns([2,6])
    with b:
        metro = df.groupby(['nearest_metro_en']).sum().reset_index()
        st.markdown("##")
        st.write("""
        ### Properties Total Worth Near Metro's  ###
        """)
        st.markdown("##")
        st.altair_chart(
             alt.Chart(metro).mark_bar(color='#329da8').encode(
            x='actual_worth:Q',
            y="nearest_metro_en:N",
            
        ).properties(
            width=800,
            height=300
        )
        )
    with a:
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.write("""
         Buj Khalifa mall metro leads the way with big margin and most of the people already aware of it.
        """)
    
    st.markdown("##")
    st.write("""
        ### Total Meter sale Price Based on Area's  ###
        """)
    st.markdown("##")
    st.altair_chart(
         alt.Chart(area_grouped).mark_circle(color='red').encode(
            x='area_name_en:N',
            y="meter_sale_price:Q",
    
            )
                )



    st.markdown("##")
    st.write("""
        ### Daily Total Worth  ###
        """)
    st.markdown("##")
    property_heat = df.groupby(['instance_date']).sum().reset_index()
    st.altair_chart(
        alt.Chart(property_heat).mark_rect().encode(
    x=alt.X("date(instance_date):O", title="Day", axis=alt.Axis(format="%e", labelAngle=0)),
    y=alt.Y("month(instance_date):O", title="Month"),
    color=alt.Color("actual_worth", legend=alt.Legend(title=None)),
    tooltip=[
        alt.Tooltip("monthdate(instance_date)", title="Date"),
        alt.Tooltip("max(actual_worth)", title="Total Worth"),
    ],
),use_container_width=True
    )
    st.write(" We can see Jan. Feb, March are updated with daily numbers but others months initial days only have numbers, thats due to mutual aggrements between seller and buyer and transactions date not yet confirmed.")


    st.markdown("##")
    st.write("""
        ### Total Worth On Property Usage  ###
        """)
    st.markdown("##")
    property_usage = df.groupby(['instance_date', 'property_usage_en']).sum().reset_index()
    st.altair_chart(
         alt.Chart(property_usage).mark_circle(color='red').encode(
    x='instance_date:T',
    y="actual_worth:Q",
    color='property_usage_en:N',
    ).properties(
        width=800,
        height=300
    ), use_container_width=True
    )
    st.markdown('##')
    st.write(" Residential is leads the way comparing with hospital and commercial that was interesting to know.")

    a,b = st.columns([2,2])
    with a:
        building_name = df.groupby(['area_name_en', 'building_name_en']).sum().reset_index()
        st.markdown("##")
        st.write("""
            ### Properties (Building name) Total Worth Based on Area's ###
            """)
        st.markdown("##")
        st.altair_chart(
            alt.Chart(building_name).mark_bar().encode(
                y='area_name_en:N',
                x="actual_worth:Q",
                color='building_name_en:N',
                
                
                
            )
        )
    with b:
        st.markdown("##")
        st.markdown("##")
        st.markdown("##")
        st.write("""
         Marsa Dubai is very high demanding area in dubai and Bussiness bay areas bulidings are that quoted for huge money.
        """)

        st.markdown("##")

        st.write(" Over these insights we can understand DUBAI is :blue[costly], even through many are more interested to buy some properties and the demand was at sky high.We can understand peoples are very interested to buy something near to happening areas or big residential areas. Most of the registeration happens for :red[residential units with 2 or 3 B/R]. In upcoming years DUBAI will beacame :green[top costlier city to live in a world], we can clearly see how much money was flowing between these properties.")



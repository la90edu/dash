import streamlit as st
import pandas as pd
import draw_table
import connect_to_google_sheet
import plotly.graph_objects as go
import consts
from class_school_info import SchoolInfo
import plotly
import init
import menu

# restart_im="🔄"
# st.session_state.is_school_chosen=False

def draw(df,school):
    
    # st.write(school)
    
# if not st.session_state.is_school_chosen:
    
    # df=init.init()

    # unique_schools = df["school"].unique().tolist()
    # school = st.selectbox('בחר בית ספר', unique_schools)
    school_df=df[df['school']==school]
    school_info = SchoolInfo(df[df['school']==school])
    fig_ici=school_info.get_fig_ici("ici")
    fig_risc=school_info.get_fig_risc("risc")
    fig_spider=school_info.get_fig_spider()
    
    # First row: Three graphs side by side
    col1, col2 = st.columns([3,2])

    with col1:
        col_1, col_2=st.columns(2)
        with col_1:
            st.plotly_chart(fig_ici, key="unique_key_ici", use_container_width=True)
        with col_2:
            st.plotly_chart(fig_risc, key="unique_key_risc", use_container_width=True)
        st.plotly_chart(fig_spider, key="unique_key_spider", use_container_width=True)


    with col2:
        menu.start_menu(school_df)
    
   



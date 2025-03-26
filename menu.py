import streamlit as st
from answers import Answers,medida
from class_school_info import SchoolInfo



def start_menu(df):
    
    st.session_state.stage=0
    school_info=SchoolInfo(df)
    school_dic_anigmas_avg=school_info.return_anigmas_result_as_dict()
    
    
    ici_class=Answers("ici",school_dic_anigmas_avg)
    risc_class=Answers("risc",school_dic_anigmas_avg)
    future_class=Answers("future",school_dic_anigmas_avg)
    current_class=ici_class
    st.write("מה תרצה לשאול?")

    col1, col2, col3,col4 = st.columns(4)
    
    answer=""

    with col1:
        if st.button("תפיסת מיקוד זמן"):
            current_class=ici_class
            st.session_state.stage=1              
            answer=current_class.get_what_is()

    with col2:
        if st.button("חוסן"):
            current_class=risc_class
            st.session_state.stage=1
            answer=current_class.get_what_is()

    with col3:
        if st.button("תפיסת זמן"):
            current_class=future_class
            st.session_state.stage=1
            answer=current_class.get_what_is()
            
    with col4:
        if st.button("מדידת הנתונים"):
            st.session_state.stage=0
            answer=medida
            
    st.write(answer)
            
    if (st.session_state.stage==1):
        col5, col6, col7 = st.columns(3)

        with col5:
            if st.button("מה אפשר להבין מהגרף?"):
                st.write(current_class.get_graph_insights())

        with col6:
            if st.button("חוזקות וחולשות"):
                st.write("risc_class.get_strengths_weaknesses()")

        with col7:
            if st.button("מה כדאי לשפר"):
                st.write("future_class.get_improvements()")
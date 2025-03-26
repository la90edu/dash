import streamlit as st
import init
from graph_with_chatbot import draw


# st.set_page_config(page_title="ניתוח על פי בית ספר")
if "is_schhol_selected" not in st.session_state:
    st.session_state.is_schhol_selected = False

# st.set_page_config(page_title="ניתוח על פי בית ספר", layout="wide")
df=init.init()
school=""
def on_school_change():
    st.session_state.is_schhol_selected = st.session_state.selected_school_main != "בחר בית ספר"
    st.write(school)
    draw(df, school)
    
if (st.session_state.is_schhol_selected==False):
    unique_schools = df["school"].unique()
    school = st.selectbox(
        "בחר בית ספר",
        # ["בחר בית ספר"] + 
        list(unique_schools),
        index=0,
        key="selected_school_main",
        on_change=on_school_change

    )
    


# school = st.selectbox(
#     "בחר בית ספר",
#     ["בחר בית ספר"] + list(unique_schools),
#     index=0,
#     key="selected_school_main",
#     on_change=on_school_change
# )
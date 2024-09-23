# Set up and run this Streamlit App
import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("Streamlit App")

form = st.form(key="form")
form.subheader("Hello Nisa Khan")

user_prompt = form.text_area("Tell me your worse nightmare", height=200)

if form.form_submit_button("Submit"):
    st.toast("User Input Submitted - {user_prompt}")
    print(f"User Input is {user_prompt}")
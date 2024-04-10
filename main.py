import streamlit as st
import openai


#type streamlit run main.py (to execute the program)
#or type python -m streamlit run main.py

#add username and password to app
#Step 1 - create a folder named ".streamlit"
#Step 2 - inside folder create "secrets.toml" 
#Step 3 - write username and password and open ai key in secrets.toml
'''
    [passwords]
    #Follow the rule: username = "password"
    pranav = "pranav123"

    [OPEN_AI]
    apikey = ""
'''
#Step 4 - write inside .gitignore type secrets.toml
#Step 5 - Paste the sign in page code given in Option 2 step 3 for streamlit https://docs.streamlit.io/knowledge-base/deploy/authentication-without-sso


import hmac

#from folder_name.file_name import function_name
from services.call_open_ai import process_subject
 


def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()


st.title('Generative AI app')

st.write('Welcome to Open AI app')

#Step 6: Give the user a text box in which user will type name of a character
subjects = st.text_input("Enter your subject for the peom")

#Step 7: Give the user a submit button
if st.button('Submit'):
    #on click call the function process_subject(subjects)
    process_subject(subjects)

#Step 8: Create a folder "services" and inside a file "call_open_ai.py"
#Step 9: Create our function process_subject(subjects) inside the file
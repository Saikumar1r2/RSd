import streamlit as st

# Function to show the steps
def show_wizard_step(step):
    if step == 1:
        st.title("Step 1: Personal Information")
        name = st.text_input("What is your name?")
        age = st.number_input("How old are you?", min_value=1)
        if st.button("Next"):
            # Store data in session state and go to next step
            st.session_state.name = name
            st.session_state.age = age
            st.session_state.step = 2

    elif step == 2:
        st.title("Step 2: Contact Information")
        email = st.text_input("What is your email?")
        phone = st.text_input("What is your phone number?")
        if st.button("Next"):
            # Store data and move to next step
            st.session_state.email = email
            st.session_state.phone = phone
            st.session_state.step = 3

    elif step == 3:
        st.title("Step 3: Review & Submit")
        st.write(f"Name: {st.session_state.name}")
        st.write(f"Age: {st.session_state.age}")
        st.write(f"Email: {st.session_state.email}")
        st.write(f"Phone: {st.session_state.phone}")
        if st.button("Submit"):
            st.success("Form Submitted Successfully!")
            st.session_state.step = 1  # Reset wizard after submission

# Initialize session state variables if they don't exist
if "step" not in st.session_state:
    st.session_state.step = 1

# Show the current step based on session state
show_wizard_step(st.session_state.step)

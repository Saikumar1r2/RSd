import streamlit as st

# Initialize session state to keep track of the current step and user inputs
if 'step' not in st.session_state:
    st.session_state.step = 1

# Function to go to the next step
def next_step():
    if st.session_state.step < 3:  # Assuming 3 steps in the wizard
        st.session_state.step += 1

# Function to go to the previous step
def previous_step():
    if st.session_state.step > 1:
        st.session_state.step -= 1

# Function to reset the wizard (optional)
def reset_wizard():
    st.session_state.step = 1
    st.session_state.name = ''
    st.session_state.age = ''
    st.session_state.city = ''

# Wizard Steps
if st.session_state.step == 1:
    st.title("Step 1: Enter Your Name")
    st.session_state.name = st.text_input("What is your name?", value=st.session_state.name)

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Next"):
            if st.session_state.name != "":
                next_step()
            else:
                st.warning("Please enter your name!")
    with col2:
        if st.button("Reset"):
            reset_wizard()

elif st.session_state.step == 2:
    st.title("Step 2: Enter Your Age")
    st.session_state.age = st.number_input("How old are you?", min_value=0, max_value=120, value=st.session_state.age)

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Next"):
            if st.session_state.age > 0:
                next_step()
            else:
                st.warning("Please enter a valid age!")
    with col2:
        if st.button("Previous"):
            previous_step()

elif st.session_state.step == 3:
    st.title("Step 3: Enter Your City")
    st.session_state.city = st.text_input("Which city do you live in?", value=st.session_state.city)

    # Navigation buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Finish"):
            if st.session_state.city != "":
                st.success("Wizard Completed!")
                st.write(f"Name: {st.session_state.name}")
                st.write(f"Age: {st.session_state.age}")
                st.write(f"City: {st.session_state.city}")
            else:
                st.warning("Please enter a valid city!")
    with col2:
        if st.button("Previous"):
            previous_step()

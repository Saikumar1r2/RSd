import streamlit as st

# Initialize session state to keep track of the current step and user inputs
if 'step' not in st.session_state:
    st.session_state.step = 1

# Initialize the fields for wizard
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'age' not in st.session_state:
    st.session_state.age = None
if 'city' not in st.session_state:
    st.session_state.city = ""

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
    st.session_state.name = ""
    st.session_state.age = None
    st.session_state.city = ""

# CSS to style the result box
st.markdown("""
    <style>
    .result-box {
        border: 2px solid #4CAF50;
        border-radius: 10px;
        padding: 20px;
        background-color: #f9f9f9;
        width: 300px;
        margin: auto;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

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
            if st.session_state.age is not None and st.session_state.age > 0:
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
                # Displaying the final result in the rectangular box
                st.markdown(f"""
                    <div class="result-box">
                        <h3>Summary</h3>
                        <p><strong>Name:</strong> {st.session_state.name}</p>
                        <p><strong>Age:</strong> {st.session_state.age}</p>
                        <p><strong>City:</strong> {st.session_state.city}</p>
                    </div>
                """, unsafe_allow_html=True)
            else:
                st.warning("Please enter a valid city!")
    with col2:
        if st.button("Previous"):
            previous_step()

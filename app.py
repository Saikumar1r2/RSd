import streamlit as st

# Define the wizard steps
steps = ["Personal Information", "Preferences", "Confirmation"]
if "step" not in st.session_state:
    st.session_state.step = 0

# Function to navigate steps
def next_step():
    if st.session_state.step < len(steps) - 1:
        st.session_state.step += 1

def prev_step():
    if st.session_state.step > 0:
        st.session_state.step -= 1

st.title("Streamlit Wizard")

# Display the current step
st.subheader(f"Step {st.session_state.step + 1}: {steps[st.session_state.step]}")

if st.session_state.step == 0:
    st.text_input("Enter your name:")
    st.text_input("Enter your email:")
    
elif st.session_state.step == 1:
    st.selectbox("Choose your favorite programming language", ["Python", "JavaScript", "C++", "Java"])
    st.checkbox("Do you like AI?")
    
elif st.session_state.step == 2:
    st.write("Please confirm your selections and proceed.")
    st.button("Finish")

# Navigation buttons
col1, col2 = st.columns(2)
with col1:
    st.button("Previous", on_click=prev_step, disabled=st.session_state.step == 0)
with col2:
    st.button("Next", on_click=next_step, disabled=st.session_state.step == len(steps) - 1)

import streamlit as st

# Define wizard steps
steps = ["Personal Information", "Preferences", "Confirmation"]
if "step" not in st.session_state:
    st.session_state.step = 0

# Functions to navigate steps
def next_step():
    if st.session_state.step < len(steps) - 1:
        st.session_state.step += 1

def prev_step():
    if st.session_state.step > 0:
        st.session_state.step -= 1

# Styling for a strict rectangular box layout
st.markdown("""
    <style>
        .wizard-container {
            max-width: 500px;
            margin: auto;
            border: 2px solid #4CAF50;
            padding: 20px;
            border-radius: 10px;
            background-color: #f9f9f9;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
        }
        .button-container {
            display: flex;
            justify-content: space-between;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Streamlit Wizard")

# Create a rectangular box using container
with st.container():
    st.markdown('<div class="wizard-container">', unsafe_allow_html=True)
    
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
    st.markdown('<div class="button-container">', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.button("Previous", on_click=prev_step, disabled=st.session_state.step == 0)
    with col2:
        st.button("Next", on_click=next_step, disabled=st.session_state.step == len(steps) - 1)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

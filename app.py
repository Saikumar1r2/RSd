import streamlit as st

# Function to display the wizard step inside a box
def wizard_step(step, title, content):
    st.markdown(
        f"""
        <div style="border:2px solid #4A90E2; padding:20px; border-radius:10px; background-color:#F5F7FA; text-align:center;">
            <h2 style="margin-bottom:20px;">{title}</h2>
            <p style="margin-bottom:20px;">{content}</p>
            <div style="display:flex; justify-content:space-between;">
                {"<button style='padding:10px; font-size:16px;' onclick='history.back();'>Previous</button>" if step > 1 else ""}
                {"<button style='padding:10px; font-size:16px;' onclick='window.location.reload();'>Next</button>" if step < len(wizard_steps) else ""}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Define the wizard steps
wizard_steps = [
    {"title": "Step 1: Introduction", "content": "Welcome to the wizard sequence! Let's get started."},
    {"title": "Step 2: User Details", "content": "Please provide your personal details."},
    {"title": "Step 3: Preferences", "content": "Set your preferences for the wizard process."},
    {"title": "Step 4: Review", "content": "Review the information before proceeding."},
    {"title": "Step 5: Completion", "content": "Congratulations! You have completed the wizard."}
]

# Streamlit app
st.title("Wizard Sequence")

# Session state to track current step
if 'step' not in st.session_state:
    st.session_state.step = 0

# Display the current step inside the box
wizard_step(st.session_state.step + 1, wizard_steps[st.session_state.step]["title"], wizard_steps[st.session_state.step]["content"])

# Navigation within the box
col1, col2 = st.columns([1, 1])
with col1:
    if st.session_state.step > 0:
        if st.button("Previous"):
            st.session_state.step -= 1
with col2:
    if st.session_state.step < len(wizard_steps) - 1:
        if st.button("Next"):
            st.session_state.step += 1

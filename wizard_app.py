import streamlit as st

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1
if "form_data" not in st.session_state:
    st.session_state.form_data = {}

# Navigation functions
def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

# Title
st.title("Label Registration Wizard")
st.markdown(f"### Step {st.session_state.step} of 6")

# Wizard Steps
if st.session_state.step == 1:
    st.header("1. Select Label Template")
    label_template = st.selectbox(
        "Choose a label template:",
        ["Glassware Label", "Nilotinib Capsule 150mg"]
    )
    st.session_state.form_data["Label Template"] = label_template

elif st.session_state.step == 2:
    st.header("2. Enter Dilution Details")
    media_detail = st.text_input("Enter Media Details", placeholder="e.g., 0.01 N HCL")
    st.session_state.form_data["Dilution Details"] = media_detail

elif st.session_state.step == 3:
    st.header("3. Enter Time Points")
    time_points = st.number_input("Number of Time Points", min_value=0, step=1)
    st.session_state.form_data["Time Points"] = time_points

elif st.session_state.step == 4:
    st.header("4. Enter AR Number")
    ar_no = st.text_input("Enter AR Number", placeholder="e.g., CAI25000854")
    st.session_state.form_data["AR Number"] = ar_no

elif st.session_state.step == 5:
    st.header("5. Electronic Signature")
    user_id = st.text_input("User ID")
    e_sign = st.text_input("E-Signature", type="password")
    st.session_state.form_data["User ID"] = user_id
    st.session_state.form_data["E-Signature"] = e_sign

elif st.session_state.step == 6:
    st.success("Labels generated successfully!")
    st.balloons()
    st.subheader("Summary:")
    for key, value in st.session_state.form_data.items():
        st.write(f"**{key}:** {value}")

# Navigation Buttons
col1, col2 = st.columns([1, 1])

with col1:
    if st.session_state.step > 1:
        st.button("Previous", on_click=prev_step)

with col2:
    if st.session_state.step < 6:
        st.button("Next", on_click=next_step)

import streamlit as st

# Initialize session state
if "step" not in st.session_state:
    st.session_state.step = 1

# Navigation buttons
def next_step():
    st.session_state.step += 1

def prev_step():
    st.session_state.step -= 1

st.title("Label Registration Wizard")

# Wizard Steps
if st.session_state.step == 1:
    st.header("1. Select Label Template")
    label_template = st.selectbox("Choose Label Template:", 
                                  ["Glassware Label", "Nilotinib Capsule 150mg"])
elif st.session_state.step == 2:
    st.header("2. Enter Dilution Details")
    media_detail = st.text_input("Enter Media Details", placeholder="e.g., 0.01 N HCL")
elif st.session_state.step == 3:
    st.header("3. Enter Time Points")
    time_points = st.number_input("Number of Time Points", min_value=0, step=1)
elif st.session_state.step == 4:
    st.header("4. Enter AR.No")
    ar_no = st.text_input("Enter AR Number", placeholder="e.g., CAI25000854")
elif st.session_state.step == 5:
    st.header("5. Electronic Signature")
    user_id = st.text_input("User ID")
    e_sign = st.text_input("E-Signature", type="password")
elif st.session_state.step == 6:
    st.success("Labels generated successfully!")
    st.balloons()

# Navigation Buttons
col1, col2 = st.columns(2)
with col1:
    if st.session_state.step > 1 and st.session_state.step < 6:
        st.button("Previous", on_click=prev_step)
with col2:
    if st.session_state.step < 6:
        st.button("Next", on_click=next_step)


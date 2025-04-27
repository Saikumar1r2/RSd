import streamlit as st

st.title("Simple Calculator")

# State variables to store the current input and operation
if 'display' not in st.session_state:
    st.session_state['display'] = '0'
if 'operation' not in st.session_state:
    st.session_state['operation'] = None
if 'first_number' not in st.session_state:
    st.session_state['first_number'] = None
if 'second_number_entered' not in st.session_state:
    st.session_state['second_number_entered'] = False

def update_display(number):
    if st.session_state['display'] == '0' or st.session_state['second_number_entered']:
        st.session_state['display'] = str(number)
        st.session_state['second_number_entered'] = False
    else:
        st.session_state['display'] += str(number)

def perform_operation(operator):
    if st.session_state['first_number'] is None:
        st.session_state['first_number'] = float(st.session_state['display'])
        st.session_state['operation'] = operator
        st.session_state['second_number_entered'] = True
    elif st.session_state['operation'] is not None:
        calculate()
        st.session_state['first_number'] = float(st.session_state['display'])
        st.session_state['operation'] = operator
        st.session_state['second_number_entered'] = True

def calculate():
    if st.session_state['operation'] and st.session_state['first_number'] is not None:
        num1 = st.session_state['first_number']
        num2 = float(st.session_state['display'])
        if st.session_state['operation'] == '+':
            st.session_state['display'] = str(num1 + num2)
        elif st.session_state['operation'] == '-':
            st.session_state['display'] = str(num1 - num2)
        elif st.session_state['operation'] == '*':
            st.session_state['display'] = str(num1 * num2)
        elif st.session_state['operation'] == '/':
            if num2 == 0:
                st.session_state['display'] = "Error"
            else:
                st.session_state['display'] = str

import streamlit as st
from streamlit import caching
from streamlit import session_state

# Initialize session state
if 'current_step' not in session_state:
    session_state.current_step = 0
if 'model_name' not in session_state:
    session_state.model_name = ''
if 'model_type' not in session_state:
    session_state.model_type = ''
if 'hyperparameters' not in session_state:
    session_state.hyperparameters = {}

# Define the steps in the wizard
steps = [
    {
        'title': 'Step 1: Model Name',
        'description': 'Enter a name for your model',
        'form': [
            st.text_input('Model Name', key='model_name_input')
        ]
    },
    {
        'title': 'Step 2: Model Type',
        'description': 'Select a type for your model',
        'form': [
            st.selectbox('Model Type', ['Linear Regression', 'Decision Tree', 'Random Forest'], key='model_type_select')
        ]
    },
    {
        'title': 'Step 3: Hyperparameters',
        'description': 'Configure hyperparameters for your model',
        'form': [
            st.number_input('Learning Rate', min_value=0.0, max_value=1.0, value=0.1, key='learning_rate'),
            st.number_input('Number of Estimators', min_value=1, value=100, key='n_estimators')
        ]
    },
    {
        'title': 'Step 4: Review',
        'description': 'Review your model configuration',
        'form': []
    }
]

# Function to render the current step
def render_current_step():
    current_step = session_state.current_step
    step = steps[current_step]

    st.header(step['title'])
    st.write(step['description'])

    for form_element in step['form']:
        form_element()

    if current_step < len(steps) - 1:
        if st.button('Next'):
            session_state.current_step += 1
            session_state.model_name = st.session_state.model_name_input
            session_state.model_type = st.session_state.model_type_select
            session_state.hyperparameters['learning_rate'] = st.session_state.learning_rate
            session_state.hyperparameters['n_estimators'] = st.session_state.n_estimators
    else:
        if st.button('Finish'):
            st.success('Model configuration complete!')
            st.write('Model Name:', session_state.model_name)
            st.write('Model Type:', session_state.model_type)
            st.write('Hyperparameters:', session_state.hyperparameters)

# Render the current step
render_current_step()
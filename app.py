import streamlit as st

st.title('Interactive Dashboard Example')

# Input widgets
number = st.number_input('Enter a number')
text = st.text_input('Enter some text')
option = st.selectbox('Select an option', ['Option 1', 'Option 2', 'Option 3'])

# Function to process inputs
def process_inputs(number, text, option):
    result = f'You entered number {number}, text "{text}", and selected {option}.'
    return result

# Display output
if st.button('Submit'):
    output = process_inputs(number, text, option)
    st.write(output)

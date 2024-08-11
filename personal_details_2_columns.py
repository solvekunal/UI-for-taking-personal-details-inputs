import streamlit as st

st.title("KUNAL's FIRST APP")
st.header('PERSONAL DETAILS')

# Create two columns
col1, col2 = st.columns(2)

# Name input in the first column
with col1:
    user_input1 = st.text_input('ENTER YOUR NAME:')

# Age input in the second column
with col2:
    user_input2 = st.text_input('ENTER YOUR AGE:')

# Additional inputs and components
user_input3 = st.text_input('ENTER YOUR MOTHER\'S NAME')

uploaded_file = st.file_uploader('Choose a file')

if uploaded_file is not None:
    st.write(f'Uploaded file: {uploaded_file.name}')

slider_value = st.slider('Select a value', 0, 100)

st.write(f'Slider value: {slider_value}')

if st.button('Click me'):
    st.write('Button clicked!')

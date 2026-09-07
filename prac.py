text = input("Enter Company Name: ")

def print_text(text):
    print(text)

print_text(f"{text}             Growing Your Business                Get a proposal ->" )





import streamlit as st

# 1. Input fields
text = st.text_input("Enter Company Name:")

# 2. Display the business text
if text:
    st.write(f"{text} Growing Your Business")
    
    # 3. Create a clickable link button
    st.link_button("Get a proposal ->", "kebabriver.netlify.app")
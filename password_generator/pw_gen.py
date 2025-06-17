import streamlit as st
import random
import string

def generate_password(length, use_digits, use_special):
    characvters = string.ascii_letters

    if use_digits:
        characvters += string.digits

    if use_special:
        characvters += string.punctuation

    return ''.join(random.choice(characvters) for _ in range(length))

st.title("🔐✨ Password Generator  🔐✨")

length = st.slider("Select password length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("include Digits")

use_special = st.checkbox("Include Special characters")

if st.button("🔐✨GENERATE PASSWORD"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generate Password:  `{password}`")


st.write("=======================")    
st.write("Build By (HINA NADIR)")

st.markdown("🌟 *Made with love by HINA NADIR* 🌟")

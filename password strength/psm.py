import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Meter By Zara Asim", page_icon="⏳", layout="centered")
#custom css
st.markdown("""
<style>
     .main {text-align: center;}
    .stTextInpur {width: 60% !important; margin: auto;}
    .stButton button {width: 50%; background-color #4CF50; color: white; font-size: 10px;}
    .stButton button:hover {background-color: #45a049;} 
</style>
""", unsafe_allow_html=True)

#page title and description
st.title("🔐 Password Strength Generator")
st.write("Enter your password below to check its security level.🔍")

#function to check password strength
def check_password_strenth(password):
    score =0
    feedback = []

    if len(password)>= 8:
        score +=1 #increased score by 1
    else:
        feedback.append("❌Password should be atleast 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should include **both uppercase (A-Z and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌Password should include **at least one number(0-9) **.")

#special characters
if re.search(r"[!@#$%*]", password):
         score += 1
else:
     feedback.append("❌ Include ** at least one special character (!@#$%^&*)**.")

#display password strength results
if score ==4:
     st.success("✔ **Strong Password** Your password is secure.")
elif score ==3:
     st.info("⚠ Moderate Password** - Consider improving security by adding more feature")
else: 
     st.error("❌ **Weak Password** - Follow the suggestion below to strength it. ")

#feedback
if feedback:
     with st.expander("🔍**Improve Your Password** "):
          for item in feedback:
               st.write(item)
password = st.text_input("Enter yout=r password:", type="Password", help="Ensure your password is strong 🔐")

#Button working
if st.button("Check Strength"):
     if password:
          check_password_strength(password)
    else:
     st.warning("⚠ Please enter a password first!") # show warning if password empty
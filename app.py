import streamlit as st
st.title("Division App")

num1 = st.number_input(label="Enter Numerator")
 
# input 2
num2 = st.number_input(label="Enter Denominator")
 
st.write("Division")
ans = 0
 
def calculate():
    if num2!=0:
        ans = num1 / num2
    else:
        st.warning("Division by 0 error. Please enter a non-zero number.")
        ans = "Not defined"
 
    st.success(f"Answer = {ans}")
 
if st.button("Calculate result"):
    calculate()

import forallpeople
forallpeople.environment('structural', top_level=True)
import math
from math import sqrt
import streamlit as st
from handcalcs.decorator import handcalc



# First, create a python file
# add/import  necessary library
# Now, we have to add path to anaconda to run this file using streamlit 
# Copy the path -> double right click on the anaconda prompt -> modify the property and change starts in location
# next use the command "streamlit run app_name"
# Now, set up the web page 
# Everytime we save this .py file. The app will be updated automatically

st.set_page_config(layout = 'wide')

st.title(f':blue[Flexural Reinforcement Calculator]')

# Add sidebar for input parameters

st.sidebar.write('Input parameters')

project_name = st.sidebar.text_input('Project Name: ')
project_no = st.sidebar.text_input('Project No: ')
Designer = st.sidebar.text_input('Designer: ')


# Lets start taking the input parameters for calculation

# Inputs
M_f = st.sidebar.number_input('Factored Moment, Mf (kN-m/m)',value = 70)   # I am using a defualt value 70 kN-m/m 
h_c = st.sidebar.number_input('Concrete section height, h_c (mm)',value = 250)
b = st.sidebar.number_input('Concrete section width, b (mm)',value = 1200)
cover = st.sidebar.number_input('Concrete cover (mm)',value = 38)
db = st.sidebar.number_input('Bar diameter, db (mm)',value = 0.65)
phi_c = st.sidebar.number_input('phi_c',value = 0.65)
f_c = st.sidebar.number_input('Concrete compressive strength, f_c (MPa)', value = 30)
f_y = st.sidebar.number_input('Steel yield strength, f_y (MPa)',value = 400)

M_f = M_f*10**6   # N-mm/m
d = min(0.9*h_c,h_c-cover-db/2)

# Now we can write the input value to the app layout 

st.write("### **Input paramerts:**")
st.write(f'	:black_medium_small_square:  Factored moment = **{M_f}** N-mm/m')  # I am using the st.write function to write the text and {} to use the parameters 
st.write(f':black_medium_small_square: Concrete section height, h_c = **{h_c}** mm')
st.write(f':black_medium_small_square: Concrete section width,b= **{b}** mm')
st.write(f':black_medium_small_square: Clear cover = **{cover}** mm')
st.write(f':black_medium_small_square: Bar diameter,db = **{db}** mm')
st.write(f':black_medium_small_square: phi_c = **{phi_c}**')
st.write(f':black_medium_small_square: Concrete compressive strength, f_c = **{f_c}** MPa')
st.write(f':black_medium_small_square: Steel yield strength, f_y = **{f_y}** MPa')
st.write(f':black_medium_small_square: Effective depth, d = **{d}** mm')


# Now, we can calculate the required reinforcement equation
# But to render the equations, we can use handcalc decorator. Handcalc can render equation if it is used as a wrapper to a function

st.write(f'## :blue[Required Area Calculation]')
@handcalc()
def as_calc(f_c,b,d,M_f):
    As_req = 0.0015*f_c*b*(d-sqrt(d**2-(3.85*M_f)/(f_c*b)))
    return As_req

# Now, if have to get the latex output from the function to render it 

As_latex, As_req = as_calc(f_c,b,d,M_f)

# to render latex code use st. latex()

st.latex(As_latex)

st.write (f'Required reinforcement area, As = {round(As_req,2)} mm2/m')

# Congrates! thats the easiest way to deploy the app
#  YTou can stop the process by simply clicking Cltr+C on anaconda prompt



















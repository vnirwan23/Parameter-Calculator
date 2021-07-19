# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 00:53:08 2021
@author: Pranav
"""

import streamlit as st

def main():
    st.title('Cutting Parameter Calculations')
    st.header('Made with :heart: by Pranav Garg and Vikash Nirwan')
    
    st.subheader('Turning Process')
    st.markdown('1. _Cutting speed_')
    st.image(r'pic1.png')
    D = st.number_input('Diamter of workpiece(in mm)',0.0,2000.0,step =1.)
    n = st.number_input('Spindle speed(in (min)^-1)',step = 1.)
    vc = round(3.14*D*n/10,2)
    st.markdown(f'**Cutting speed is {vc}mm/min**')
    st.write('\n\n')
    
    st.markdown('2. _Net Power Requirement_')
    vc2 = st.number_input('Cutting speed(in m/min)',0.,1000000.0,step =1.)
    f = st.number_input('Feed rate(in mm/rev)',0.,1000000.,step = 1.)
    ap = st.number_input('Depth of cut(in mm)',0.,1000000.,step=1.)
    eta = st.number_input('Machine efficiency',0.1,1.,step =0.1)
    kc = st.number_input('Specific cutting force(in MPa)',0.,1000000.,step = 1.)
    pc = round((vc2*f*ap*kc)/(60*eta),2)
    st.markdown(f'**Net power requirement is {pc}W.**')
    st.write('\n\n')
    

    st.markdown('3. _Machined Surface Roughness_')
    st.image(r'pic3.png')
    f = st.number_input('Feed rate(mm/rev)',0.,1000000.,step =1.)
    re = st.number_input('Nose Radius(mm)',0.1,10000.,step=1.)
    h = round(f*f*1000/(8*re),2)
    st.markdown(f'**Machined surface roughness is {h} micrometer.**')
    st.write('\n\n')
    
    st.markdown('4. _Grooving Time_')
    st.image(r'pic4.png')
    D1 = st.number_input('Max. diameter(mm)',0.,100000.,step=1.)
    D2 = st.number_input('Min. diameter(mm)',0.,100000.,step=1.)
    f = st.number_input('Feed rate(mm/rev)',0.1,100000.,step=1.)
    n = st.number_input('Spindle speed(1/min)',0.1,10000.,step=1.)
    T = round(30*(D1-D2)/(f*n),2)
    st.markdown(f'**Net grooving time is {T}seconds.**')
    st.write('\n\n')
    
    st.subheader('Milling Process')
    st.markdown('1. _Rotational Speed_')
    st.image(r'pic6.png')
    vc = st.number_input('Cutting speed(m/min)',0.,100000.,step =1.)
    dc = st.number_input('Cuuter diameter(mm)',0.1,1000000.,step =1.)
    n = 1000*vc/(3.14*dc)
    n = round(n,2)
    st.markdown(f'Rotational speed is {n}1/min.')
    st.write('\n\n')
    
    st.markdown('2. _Feed speed per minute_')
    fz = st.number_input('feed rate per tooth(mm/t)',0.,100000.,step =1.)
    z = st.number_input('znumber of pieces',0.,100000.,step =1.)
    n = st.number_input('Rotation speed(1/min)',0.,1000000.,step =1.)
    vf = fz*z*n/1000
    vf = round(vf,2)
    st.markdown(f'**Feed speed is {vf}m/min.**')
    st.write('\n\n')
    
    st.markdown('3. _Chip Removal Amount_')
    ae = st.number_input('Cutting width(mm)',0.,100000.,step=1.)
    ap = st.number_input('Depth of cut(mm)',0.,10000.,step=1.)
    vf = st.number_input('Feed rate per minute(m/min)',0.,100000.,step=1.)
    Q = ae*ap*vf/1000
    Q = round(Q,2)
    st.markdown(f'**Chip removal amount is {Q}cubic cm per minute.**')
    st.write('\n\n')
    
    st.markdown('4. _Power Requirement_')
    st.image(r'pic7.png')
    kc = st.number_input('Specific Cutting force(MPa)',0.,1000000.,step=1.)
    eta = st.number_input('Efficiency',0.1,1.,step =1.)
    Q = st.number_input('Chip removal amount(cm^3/min)',0.,10000.,step =1.)
    pc = (Q*kc)/(60*1000*eta)
    pc = round(pc,2)
    st.markdown(f'**Power requirement is {pc}KW.**')
    

    
if __name__ =="__main__":
    main()
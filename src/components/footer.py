import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/WNs9K6mK/final-logo.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center;">
        <p style="font-weight:bold; color:white;margin:0;"> Developed with ❤️ by  </p>  
        <img src='{logo_url}' style='max-height:40px'  style='max-height:40px; transform:translateY(-8px);'/>
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://i.ibb.co/WNs9K6mK/final-logo.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center;">
        <p style="font-weight:bold; color:black;margin:0;"> Developed with ❤️ by  </p>  
        <img src='{logo_url}' style='max-height:40px'  style='max-height:40px; transform:translateY(-8px);' />
        </div>
                
                """, unsafe_allow_html=True)
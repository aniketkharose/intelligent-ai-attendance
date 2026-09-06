import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/k2mTCGgM/99a873bb-39b6-40bd-9e6f-5e769472e6db.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Developed with ❤️ by  </p>  
        <img src='{logo_url}' style='max-height:45px' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://i.ibb.co/k2mTCGgM/99a873bb-39b6-40bd-9e6f-5e769472e6db.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Developed with ❤️ by  </p>  
        <img src='{logo_url}' style='max-height:45px' />
        </div>
                
                """, unsafe_allow_html=True)
import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/xSfk7NWg/Codex-Image-Sep-6-2026-04-03-27-PM.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:white;"> Developed with ❤️ by  </p>  
        <img src='{logo_url}' style='max-height:45px' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://i.ibb.co/xSfk7NWg/Codex-Image-Sep-6-2026-04-03-27-PM.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; align-items:center">
        <p style="font-weight:bold; color:black;"> Developed with ❤️ by  </p>  
        <img src='{logo_url}' style='max-height:45px' />
        </div>
                
                """, unsafe_allow_html=True)
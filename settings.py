import streamlit as st

def show_settings(data):
    """Display the Settings page"""
    
    # Page header
    st.title("⚙️ Settings")
    st.markdown("### *App Configuration - Coming Soon*")
    
    # Placeholder content with visual appeal
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 50px; background-color: #f0f2f6; border-radius: 10px; margin: 20px 0;">
            <h2 style="color: #ff6347;">🔧 Configuration Panel</h2>
            <p style="font-size: 18px; margin: 20px 0;">Customize your Local Explorer experience!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Feature preview
    st.subheader("🎯 Coming Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 👤 User Preferences:
        - Profile management
        - Language settings
        - Notification preferences
        - Privacy controls
        - Theme customization
        - Location settings
        """)
    
    with col2:
        st.markdown("""
        #### 🛠️ App Configuration:
        - Search preferences
        - Filter defaults
        - Display options
        - Data management
        - Cache settings
        - Backup & restore
        """)
    
    # Current app info
    st.markdown("---")
    st.subheader("📋 Current App Info")
    
    app_info = data.get('settings', {}) if data else {}
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            "App Name", 
            app_info.get('app_name', 'Local Explorer')
        )
    
    with col2:
        st.metric(
            "Version", 
            app_info.get('version', '1.0.0')
        )
    
    with col3:
        st.metric(
            "Status", 
            "MVP"
        )
    
    # Temporary settings preview
    st.markdown("---")
    st.subheader("🎮 Demo Settings (Non-functional)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.selectbox("🌍 Language", ["English", "Spanish", "French"], disabled=True)
        st.selectbox("🎨 Theme", ["Light", "Dark", "Auto"], disabled=True)
        st.checkbox("📧 Email Notifications", value=True, disabled=True)
    
    with col2:
        st.selectbox("📍 Default Location", ["Current Location", "Custom"], disabled=True)
        st.slider("🔍 Search Radius (km)", 1, 50, 10, disabled=True)
        st.checkbox("🔔 Push Notifications", value=False, disabled=True)
    
    st.info("💡 These settings are placeholders and will be functional in future versions.")
    
    # Navigation
    st.markdown("---")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.session_state.current_page = "Home"
        st.rerun()
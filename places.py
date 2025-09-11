import streamlit as st

def show_places(data):
    """Display the Places page"""
    
    # Page header
    st.title("📍 Places")
    st.markdown("### *Tourism Guide - Coming Soon*")
    
    # Placeholder content with visual appeal
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 50px; background-color: #f0f2f6; border-radius: 10px; margin: 20px 0;">
            <h2 style="color: #2e8b57;">🗺️ Exploring Soon</h2>
            <p style="font-size: 18px; margin: 20px 0;">Get ready to discover amazing local places and hidden gems!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Feature preview
    st.subheader("🎯 Coming Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🗺️ Tourism Features:
        - Interactive maps
        - Location details & photos
        - Visitor reviews & ratings
        - Opening hours & contact info
        - Directions & transportation
        - Nearby recommendations
        """)
    
    with col2:
        st.markdown("""
        #### 📍 Place Categories:
        - Historical sites
        - Natural attractions
        - Museums & galleries
        - Parks & recreation
        - Restaurants & cafes
        - Shopping districts
        """)
    
    # Temporary data display
    if data and data.get('places'):
        st.markdown("---")
        st.subheader("📊 Current Data Preview")
        st.info(f"Found {len(data['places'])} place(s) in database")
        
        with st.expander("View Raw Places Data"):
            st.json(data['places'])
    
    # Quick navigation
    st.markdown("---")
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🏠 Back to Home", use_container_width=True):
            st.session_state.current_page = "Home"
            st.rerun()
    
    with col2:
        if st.button("🛍️ Check Products", use_container_width=True):
            st.session_state.current_page = "Products"
            st.rerun()
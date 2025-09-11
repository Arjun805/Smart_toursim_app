import streamlit as st

def show_products(data):
    """Display the Products page"""
    
    # Page header
    st.title("🛍️ Products")
    st.markdown("### *Local Marketplace - Coming Soon*")
    
    # Placeholder content with visual appeal
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("""
        <div style="text-align: center; padding: 50px; background-color: #f0f2f6; border-radius: 10px; margin: 20px 0;">
            <h2 style="color: #1f77b4;">🚧 Under Construction</h2>
            <p style="font-size: 18px; margin: 20px 0;">We're working hard to bring you an amazing local marketplace experience!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Feature preview
    st.subheader("🎯 Coming Features")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🛒 Marketplace Features:
        - Local product listings
        - Search and filter options
        - Vendor profiles
        - Price comparison
        - Customer reviews
        - Wishlist functionality
        """)
    
    with col2:
        st.markdown("""
        #### 📦 Product Categories:
        - Handmade crafts
        - Local food & beverages  
        - Art & souvenirs
        - Clothing & accessories
        - Home & garden
        - Services & experiences
        """)
    
    # Temporary data display
    if data and data.get('products'):
        st.markdown("---")
        st.subheader("📊 Current Data Preview")
        st.info(f"Found {len(data['products'])} product(s) in database")
        
        with st.expander("View Raw Product Data"):
            st.json(data['products'])
    
    # Back to home
    st.markdown("---")
    if st.button("🏠 Back to Home", use_container_width=True):
        st.session_state.current_page = "Home"
        st.rerun()
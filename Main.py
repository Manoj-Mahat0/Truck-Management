import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import os
import numpy as np
import pickle




st.set_page_config(layout="wide")

# Your Streamlit app code goes here
def apply_custom_css():
    custom_css = """
    <style>
        body {
            background-color: #f0f2f6;
        }
        .stApp {
            padding: 2rem;
        }
        .stTextInput input {
            border-radius: 5px;
            border: 1px solid #ced4da;
            padding: 0.5rem;
        }
        .stButton>button {
            border-radius: 5px;
            width: 100%; /* Full width */
            background-color: #ffd803;
            color: white;
            padding: 0.5rem 1rem;
            font-size: 1rem;
            border: none;
        }
        .stButton>button:hover {
            background-color: #272343;
            text-color: #ffd803;
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
    
def Main():
    # Static driver details
    static_driver_info = [
        {
            "num_deliveries": 10,
            "aadhar_number": "1234 5678 9012",
            "driver_name": "John Doe",
            "phone_number": "9876543210",
            "driver_id": "DRV001"
        },
        
    # Add more driver details as needed
        ]

# Display driver information
    def display_driver_info(driver_info):
        st.title("Driver Information")

        col1, col2 = st.columns([2,1])
        with col1:
            if not driver_info:
                st.warning("No driver information available.")
                return

            for driver in driver_info:
                st.write()
                st.write()
                st.write(f"Number of Deliveries: {driver.get('num_deliveries', 'N/A')}")
                st.write(f"Aadhar Number: {driver.get('aadhar_number', 'N/A')}")
                st.write(f"Driver Name: {driver.get('driver_name', 'N/A')}")
                st.write(f"Phone Number: {driver.get('phone_number', 'N/A')}")
                st.write(f"Driver ID: {driver.get('driver_id', 'N/A')}")

        with col2:
            image = Image.open('SiteStats-amico.png')
            st.image(image)
        st.write("-" * 50)  # Separator between truck details
    

# Static truck details
    static_truck_info = [
    {
        "truck_number": "TRK001",
        "capacity": "10 tons",
        "driver_name": "John Doe",
        "current_location": "Warehouse A",
        "status": "Available"
    },
    {
        "truck_number": "TRK002",
        "capacity": "15 tons",
        "driver_name": "Jane Smith",
        "current_location": "Warehouse B",
        "status": "In Transit"
    },
    {
        "truck_number": "TRK003",
        "capacity": "8 tons",
        "driver_name": "Bob Johnson",
        "current_location": "Warehouse C",
        "status": "Available"
    },
    {
        "truck_number": "TRK004",
        "capacity": "12 tons",
        "driver_name": "Alice Brown",
        "current_location": "Warehouse D",
        "status": "In Transit"
    },
    {
        "truck_number": "TRK005",
        "capacity": "20 tons",
        "driver_name": "Charlie Wilson",
        "current_location": "Warehouse E",
        "status": "Available"
    }
]

# Display individual truck details using expander
    def display_individual_truck(truck):
        col1, col2 = st.columns([3,1])
        with col1:
            st.subheader(f"Truck {truck['truck_number']}")
            st.info(f"Capacity: {truck['capacity']}")
            st.info(f"Driver: {truck['driver_name']}")
            st.info(f"Current Location: {truck['current_location']}")
            st.info(f"Status: {truck['status']}")
            
        with col2:
            image = Image.open('Logistics-rafiki.png')
            st.image(image)
        st.write("-" * 50)  # Separator between truck details

# Display truck information in expandable cards
    def display_truck_cards(truck_info):
        st.title("Truck Details")

        if not truck_info:
            st.warning("No truck information available.")
            return

        for truck in truck_info:
            expander = st.expander(f"Truck {truck['truck_number']} Details")
            with expander:
                display_individual_truck(truck)


    
    # Display static driver information
    display_driver_info(static_driver_info)
    # Display truck information in expandable cards
    display_truck_cards(static_truck_info)

    


def contact_form():
    st.header(":mailbox: Get In Touch With Me!")
    contact_form = """
    <form action="https://formsubmit.co/jeetverma0721@gmail.com" method="POST">
         <input type="hidden" name="_template" value="table">
         <input type="text" name="name" placeholder="Your name" required>
         <input type="email" name="email" placeholder="Your email" required>
         <textarea name="message" placeholder="Your message here"></textarea>
         <button type="submit">Send</button>
    </form>
    """

    st.markdown(contact_form, unsafe_allow_html=True)

    # Use Local CSS File
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}<Style/style>", unsafe_allow_html=True)


    local_css("Style/style.css")
    
def home_scr():
    col1, col2 = st.columns([3,1])

    with col1:
        st.header('Welcome To Automatic Heavy Vehicle Navigation System')
        st.write('Our Automatic Heavy Vehicle Navigation System revolutionizes navigation for heavy vehicles. With our user-friendly AHN software, drivers can effortlessly input their location and destination. The Al then analyzes real-time data on road conditions, traffic, and weather to optimize the driving mode, making navigation and monitoring for heavy vehicles easy, efficient, and safe.')
        st.markdown(
            """
            <style>
            .footer {
                text-align: center;
                font-size: 24px;
                </style>
            """,
            unsafe_allow_html=True
        )
        st.markdown('<p class="footer">Subscribe for ❤️ Latest Updates</p>', unsafe_allow_html=True)
        News_Latter = """
        <form action="https://formsubmit.co/jeetverma0721@gmail.com" method="POST">
             <input type="hidden" name="_template" value="table">
             <input type="email" name="email" placeholder="Your email" required>
             <button type="submit">Subscribe</button>
        </form>
        """

        st.markdown(News_Latter, unsafe_allow_html=True)

        # Use Local CSS File
        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        local_css("Style/News_style.css")

        
    with col2:
        image = Image.open('shipping-amico.png')
        st.image(image)
        
    st.markdown("""---""")
    
    
    
    st.markdown(
        """
        <style>
        .foot {
            text-align: center;
            font-size: 24px;
            </style>
        """,
        unsafe_allow_html=True
    )
    
    

       
    
selected = option_menu(None, ["Home", "Dashboard",  "About", 'Contact'], 
                icons=['house', 'cloud-upload', "list-task", 'gear'], 
                menu_icon="cast", default_index=0, orientation='horizontal',
                styles={
                    "container": {"padding": "0!important", "background-color": "#272343"},
                    "icon": {"color": "orange", "font-size": "20px"}, 
                    "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#272343"},
                    "nav-link-selected": {"background-color": "#ffd803"},
                })
    
if selected == "About":
    
    st.markdown("""
    ## Our Mission

    Our mission is to leverage the power of machine learning to help individuals and healthcare providers predict medical expenses more accurately. By doing so, we aim to improve financial planning and resource allocation in the healthcare industry.

    ## Our Team

    We are a team of dedicated data scientists, software engineers, and healthcare professionals who are passionate about using technology to improve healthcare outcomes.

    ## Our Values

    - **Innovation:** We are committed to exploring new ideas and technologies to stay at the forefront of machine learning and healthcare.
    - **Collaboration:** We believe in the power of teamwork and open communication to achieve our goals.
    - **Accuracy:** We strive for the highest level of precision in our predictions to ensure reliable results for our users.
    - **User Focus:** We prioritize the needs of our users and work tirelessly to create intuitive and user-friendly tools.
    - **Ethics:** We are dedicated to maintaining the privacy and security of our users' data and adhering to the highest ethical standards in our work.

    

    If you have any questions or would like to learn more about our medical expenses prediction project, please feel free to reach out to us at [contact@jeetverma.com](mailto:jeetverma0721@gmail.com).
    """)
    
if selected == "Contact":
    contact_form()
    
if selected == "Dashboard":
    Main()
    
if selected == "Home":
    # Display the image in the hero section
   home_scr()
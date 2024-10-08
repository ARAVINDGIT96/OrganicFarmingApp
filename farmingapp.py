import csv
import os
import streamlit as st



st.set_page_config(page_title="AgriGrove", page_icon="🌾")



def home():
    st.title("🌱 AgriGrove Solutions")
    st.write("""
    Welcome to the Organic Fertilizer Recommendation platform! Here, you can find
    personalized fertilizer suggestions tailored to your crop type, soil conditions, 
    and farming practices. Start by exploring our recommendations or learning more 
    about organic farming!
    """)


def about_us():
    st.title("About Us")
    st.write("""
    We are a team of passionate agricultural experts focused on bringing sustainable 
    solutions to farmers around the world. Our mission is to promote organic farming 
    and ensure the health of both crops and the environment.
    """)
    st.header("""Team Name: Arganic""")
    st.subheader("""Team Members:""")
    st.write("""Sarnala Aravind
    (Team leader)""")
    st.write("""Dabide Shivani(Manager)""")
    st.write("""Prem lohit H.M(Developer)""")
    st.write("""Kinnera siddhi(Tester)""")
    st.write("""Dyaga Nishmitha(Designer)""")
    st.write("""Mergu Varshini(Designer)""")

#  Create a fertilizer recommendation page
def fertilizer_recommendations():
    st.title("Fertilizer Recommendations")
    st.write("Get personalized organic fertilizer recommendations based on your inputs.")
    
    
    crop_type = st.selectbox('Select Crop Type:', ['Choose one', 'Wheat', 'Rice', 'Maize', 'Soybean'])
    
    symptoms = []
    if crop_type == "Wheat":
        symptoms = ['Choose one', 'Orange, yellow, or brown pustules on leaves and stems', 
                    'White, powdery fungal growth on leaves and stems', 
                    'Bleached spikelets, shriveled grains, pink or white mold on heads']
    elif crop_type == "Rice":
        symptoms = ['Choose one', 'Grayish-green lesions on leaves, stems, and panicles', 
                    'Yellowing of leaf tips, wilting, and brown streaks', 
                    'Elliptical lesions on the leaf sheath, causing lodging']
    elif crop_type == "Maize":
        symptoms = ['Choose one', 'Yellow streaks on leaves, stunted growth', 
                    'Large grayish-green or brown lesions on leaves', 
                    'Small necrotic lesions that expand and coalesce']
    elif crop_type == "Soybean":
        symptoms = ['Choose one', 'Small brown to black pustules on the undersides of leaves', 
                    'Circular gray or brown lesions with reddish borders on leaves', 
                    'White moldy growth on stems, wilting of plants']
    
    selected_symptom = st.selectbox('Select Symptoms', symptoms)
    
    soil_type = st.selectbox('Select Soil Type:', ['Choose one', 'Clay', 'Loam', 'Sandy', 'Peaty'])
    season_type = st.selectbox('Select Seasonal Type:', ['Choose one', 'Kharif (June to October)', 
                                                          'Rabi (October to April)', 'Zaid (March to June)'])
    climate = st.selectbox('Select Climate Type:', ['Choose one', 'Tropical', 'Temperate', 'Arid', 'Continental'])
    
    st.subheader("Camera and Image")
    if st.checkbox("Show camera"):
        picture = st.camera_input("Take a picture")
        if picture:
            st.image(picture)
    
    #
    if st.button('Get Recommendation'):
        if crop_type == "Wheat" and selected_symptom == "Orange, yellow, or brown pustules on leaves and stems":
            st.success(f"For {crop_type} symptoms like {selected_symptom}, we recommend using 'Neem oil spray to deter the spores.'")
        elif crop_type == "Wheat" and selected_symptom == "White, powdery fungal growth on leaves and stems":
            st.success(f"For {crop_type} symptoms like {selected_symptom}, we recommend using 'Spray of baking soda solution (1 tbsp baking soda + 1 liter of water).'")
        elif crop_type == "Wheat" and selected_symptom == "Bleached spikelets, shriveled grains, pink or white mold on heads":
            st.success(f"For {crop_type} symptoms like {selected_symptom}, we recommend using 'Biological control using Trichoderma spp.'")
        elif crop_type == "Rice" and selected_symptom == "Grayish-green lesions on leaves, stems, and panicles":
            st.success(f"For {crop_type} symptoms like {selected_symptom}, we recommend using 'Neem oil as a foliar spray.'")
        elif crop_type == "Rice" and selected_symptom == "Yellowing of leaf tips, wilting, and brown streaks":
            st.success(f"For {crop_type} symptoms like {selected_symptom}, we recommend using 'Compost tea as a foliar spray.'")
        elif crop_type == "Rice" and selected_symptom == "Elliptical lesions on the leaf sheath, causing lodging":
            st.success(f"For {crop_type} symptoms like {selected_symptom}, we recommend using 'Bacillus subtilis and ensuring proper spacing and crop residue management.'")
        elif crop_type == "Maize" and selected_symptom == "Yellow streaks on leaves, stunted growth":
            st.success(f"For {crop_type} symptoms like {selected_symptom}, we recommend using 'Neem or garlic-based sprays to manage insect vectors or intercropping with legumes to deter vector insects.'")
        elif crop_type == "Maize" and selected_symptom == "Large grayish-green or brown lesions on leaves":
            st.success(f"For {crop_type} symptoms like {selected_symptom}, we recommend using 'Spray compost tea or Bacillus subtilis.'")
        elif crop_type == "Maize" and selected_symptom == "Small necrotic lesions that expand and coalesce":
            st.success(f"For {crop_type} symptoms like {selected_symptom}, we recommend using 'Apply Trichoderma or Bacillus subtilis as a foliar spray.'")
        elif crop_type == "Soybean" and selected_symptom == "Small brown to black pustules on the undersides of leaves":
            st.success(f"For {crop_type} symptoms like {selected_symptom}, we recommend using 'Neem oil spray to inhibit spore germination.'")
        elif crop_type == "Soybean" and selected_symptom == "Circular gray or brown lesions with reddish borders on leaves":
            st.success(f"For {crop_type} symptoms like {selected_symptom}, we recommend using 'Bacillus subtilis or compost tea as a foliar spray.'")
        elif crop_type == "Soybean" and selected_symptom == "White moldy growth on stems, wilting of plants":
            st.success(f"For {crop_type} symptoms like {selected_symptom}, we recommend using 'Trichoderma as a soil amendment and ensuring proper spacing to improve air circulation.'")



def blog():
    st.title("Organic Farming Blog")
    st.write("""
    Stay updated with the latest articles and tips on organic farming, fertilizer use, 
    and sustainable agricultural practices.
    """)



def contact_us():
    st.title("Contact Us")
    st.write("Feel free to get in touch with us through the form below.")
    
    
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Message")
    
   
    file_path = 'contacts.csv'
    
    
    if not os.path.exists(file_path):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Name", "Email", "Message"])
    
    if st.button("Send Message"):
        
        if name.strip() and email.strip() and message.strip():
            with open(file_path, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow([name, email, message])
                st.success("Thank you for reaching out! We will get back to you shortly.")
        else:
            st.error("Please fill in all fields.")



menu = st.selectbox("Navigation", ["Home", "Fertilizer Recommendations", "About Us", "Blog", "Contact Us"])

if menu == "Home":
    home()
elif menu == "Fertilizer Recommendations":
    fertilizer_recommendations()
elif menu == "About Us":
    about_us()
elif menu == "Blog":
    blog()
elif menu == "Contact Us":
    contact_us()

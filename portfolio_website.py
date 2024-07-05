import base64
from io import BytesIO
import streamlit as st
from PIL import Image
import google.generativeai as genai

api_key = st.secrets["GOOGLE_API_KEY"]
# api_key =""
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')

st.markdown(
    """
    <style>
    .stApp {
        background-color: #e8e8ed66;
        background-size: cover;
        background-position: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Load social media icons
twitter_icon = Image.open("icons/twitter.png")
linkedin_icon = Image.open("icons/linkedin.png")
github_icon = Image.open("icons/github.png")

# Social media URLs
twitter_url = "https://x.com/Sanath122"
linkedin_url = "https://www.linkedin.com/in/yourprofile"
github_url = "https://github.com/yourprofile"


# Function to convert image to base64
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()


# Convert images to base64
twitter_base64 = image_to_base64(twitter_icon)
linkedin_base64 = image_to_base64(linkedin_icon)
github_base64 = image_to_base64(github_icon)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Hi :wave:")
    st.title("I am Sanath S Kamath")

with col2:
    st.image("images/sanath.jpg")
st.title("")

persona = """
        You are Murtaza AI bot. You help people answer questions about your self (i.e Murtaza)
        Answer as if you are responding . dont answer in second or third person.
        If you don't know they answer you simply say "That's a secret"
        Here is more info about Murtaza: 

        Murtaza Hassan is an Educator/Youtuber/Entrepreneur in the field of Computer Vision and Robotics.
        He runs one of the largest YouTube channels in the field of Computer Vision,
        educating over 3 Million developers,
        hobbyists and students. Murtaza obtained his Bachelor’s degree in
        Mechatronics and later specialized in the field of Robotics from
        Bristol University (UK). He is also a serial entrepreneur having launched several
        successful ventures including CVZone, which is a one stop solution for learning 
        and building vision projects. Prior to starting his entrepreneurial career, 
        Murtaza worked as a university lecturer and a design engineer, evaluating 
        and developing rapid prototypes of US patents.

        Murtaza's Youtube Channel: https://www.youtube.com/channel/UCYUjYU5FveRAscQ8V21w81A
        Murtaza's Email: contact@murtazahassan.com 
        Murtaza's Facebook: https://www.facebook.com/murtazasworkshop
        Murtaza's Instagram: https://www.instagram.com/murtazasworkshop/
        Murtaza's Linkdin: https://www.linkedin.com/in/murtaza-hassan-8045b38a/
        Murtaza's Github :https://github.com/murtazahassan
        """

st.title("Sanath's AI Bot")

user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.title(" ")
col1, col2 = st.columns(2)
with col1:
    st.subheader("Youtube channel")
    st.write("- Largest Computer Vision Channel")
    st.write("- 400k+ Subscribers")
    st.write("- Over 150 free tutorials")
    st.write("- 15 Million+ Views")
    st.write("- 1.5 Million Hours+ Watch time")
with col2:
    st.video("https://youtu.be/BFlRmIvqwSA?si=a6qL3")

st.title(" ")
st.title("My Setup")
st.image("images/setup.jpg")

st.title(" ")
st.title("My Skills")
st.slider("Programming", 0, 100, 40)
st.slider("Teaching", 0, 100, 50)
st.slider("Robotics", 0, 100, 20)

st.title("")
st.title("Gallery")

#without loops
# col1, col2, col3 = st.columns(3)
#
# with col1:
#     st.image("images/g1.jpg")
#     st.image("images/g2.jpg")
#     st.image("images/g3.jpg")
# with col2:
#     st.image("images/g4.jpg")
#     st.image("images/g5.jpg")
#     st.image("images/g6.jpg")
# with col3:
#     st.image("images/g7.jpg")
#     st.image("images/g8.jpg")
#     st.image("images/g9.jpg")

# with loops
images = [
    "images/g1.jpg", "images/g2.jpg", "images/g3.jpg",
    "images/g4.jpg", "images/g5.jpg", "images/g6.jpg",
    "images/g7.jpg", "images/g8.jpg", "images/g9.jpg"
]

# Create three columns
cols = st.columns(3)

# Loop through the images and assign them to columns
for i, image in enumerate(images):
    col = cols[i % 3]
    col.image(image)

st.subheader("")
st.write("Contact")
st.title("For any inquiries,please email me at")
st.subheader("contact at sanathkamath11@gmail.com")

# Create columns for social media icons
cols = st.columns(3)

# Display social media icons with clickable links
with cols[0]:
    if st.button('Twitter'):
        st.markdown(
            f'<a href="{twitter_url}" target="_blank"><img src="data:image/png;base64,{twitter_base64}" width="50"></a>',
            unsafe_allow_html=True)

with cols[1]:
    if st.button('LinkedIn'):
        st.markdown(
            f'<a href="{linkedin_url}" target="_blank"><img src="data:image/png;base64,{linkedin_base64}" width="50"></a>',
            unsafe_allow_html=True)

with cols[2]:
    if st.button('GitHub'):
        st.markdown(
            f'<a href="{github_url}" target="_blank"><img src="data:image/png;base64,{github_base64}" width="50"></a>',
            unsafe_allow_html=True)

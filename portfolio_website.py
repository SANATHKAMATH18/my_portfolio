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
        background: linear-gradient(135deg, #ece9e6, #ffffff);
        font-family: 'Arial', sans-serif;
        color: #333;
        padding: 20px;
    }
    .navbar {
        display: flex;
        justify-content: center;
        background-color: #333;
        padding: 10px;
        position: sticky;
        top: 0;
        z-index: 1000;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .navbar a {
        color: white;
        text-decoration: none;
        padding: 14px 20px;
        font-size: 18px;
    }
    .navbar a:hover {
        background-color: #575757;
        border-radius: 4px;
    }
    .title {
        text-align: center;
        margin-top: 20px;
        margin-bottom: 40px;
        font-size: 36px;
        color: #444;
    }
    .section-title {
        font-size: 24px;
        color: #555;
        margin-bottom: 20px;
    }
    .contact {
        text-align: center;
        margin-top: 40px;
    }
    .contact h2 {
        font-size: 28px;
        margin-bottom: 20px;
    }
    .contact a {
        color: #1e90ff;
        text-decoration: none;
        font-size: 20px;
    }
    .contact a:hover {
        text-decoration: underline;
    }
    .skill-slider .stSlider {
        background: linear-gradient(90deg, #1e90ff, #00bfff);
    }
    .gallery img {
        border-radius: 8px;
        margin-bottom: 20px;
        transition: transform 0.2s;
    }
    .gallery img:hover {
        transform: scale(1.05);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="navbar">
        <a href="#">About Me</a>
        <a href="#skills">Skills</a>
        <a href="#gallery">Gallery</a>
        <a href="#contact">Contact</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Load social media icons
twitter_icon = Image.open("icons/twitter.png")
linkedin_icon = Image.open("icons/linkedin.png")
github_icon = Image.open("icons/github.png")

# Social media URLs
twitter_url = "https://x.com/Sanath122"
linkedin_url = "https://www.linkedin.com/in/sanath-s-kamath-391b9b24b/"
github_url = "https://github.com/SANATHKAMATH18"

# Function to convert image to base64
def image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Convert images to base64
twitter_base64 = image_to_base64(twitter_icon)
linkedin_base64 = image_to_base64(linkedin_icon)
github_base64 = image_to_base64(github_icon)

st.markdown('<div class="title">Sanath\'s AI Bot</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.subheader("Hi :wave:")
    st.header("I am Sanath S Kamath, a young developing python developer in the field of computer vision.")

with col2:
    st.image("images/sanath.jpg")

st.markdown('<a name="about"></a>', unsafe_allow_html=True)
persona = """
        You are Sanath AI bot. You help people answer questions about yourself (i.e. Sanath)
        Answer as if you are responding. Don't answer in second or third person.
        If you don't know the answer, simply say "That's a secret."
        Here is more info about Sanath: 

        I am Sanath S Kamath from Bangalore, India, 19 years of age born on May 3, 2004. I am currently a student 
        pursuing my bachelor's in computer science and engineering at Vellore Institute of Technology in Tamil Nadu. 
        I am interested in Python with computer vision,ai  and development using React and Next.js. I also enjoy playing 
        sports, especially badminton, cricket, and football. I am quite good at chess. I completed my primary schooling 
        at Carmel High School in Bangalore and my PU at Base College in Rajajinagar. My mother tongue is Konkani, and I 
        also speak English, Hindi, and Kannada. My family consists of four members: my father Satish R Kamath, my mother 
        Reshma S Kamath, and my brother Raksheeth S Kamath. We live as a joint family with my father's brother Suresh R 
        Kamath, his fiancée Veena S Kamath, and their three children, my cousins Rahul, Megha, and Madhu and along with
        my grandparents Ramananda kamath and Nirupama kamath. I aspire to become a proficient computer vision developer 
        in Python. My blood group is B positive. My biggest inspiration is Virat Kohli; I admire him a lot. 
        my father owns a Hyundai Aura car and two motor vehicles: a TVS scooty and a TVS bike. and my uncle has a Xuv 500
        I love watching anime, with favorites including One Piece, Bleach, Black Clover, and Hunter x Hunter. I also enjoy 
        Bollywood and South Indian movies, with favorite actors like Salman Khan, Shah Rukh Khan, and Tiger Shroff. 
        Ronaldo is my favorite footballer, and Novak Djokovic is my favorite tennis player. My achievements include 
        obtaining 93% in my 10th boards, 95% in my 12th boards, and several sports medals during my school days.

        Sanath's YouTube Channel: https://www.youtube.com/channel/UCJJRaMQLv_XaAA8mzdP21oA
        Sanath's Email: sanathkamath11@gmail.com
        Sanath's Facebook: https://www.facebook.com/sanath.kamath.1/
        Sanath's Instagram: https://www.instagram.com/_sanath_18/
        Sanath's LinkedIn: https://www.linkedin.com/in/sanath-s-kamath-391b9b24b/
        Sanath's GitHub: https://github.com/SANATHKAMATH18
        """

user_question = st.text_input("Ask anything about me")
if st.button("ASK"):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = model.generate_content(prompt)
    st.write(response.text)

st.markdown('<a name="skills"></a>', unsafe_allow_html=True)
st.title("")
st.title("My Skills")
st.slider("Programming in Python", 0, 100, 60, key="skill_slider")
st.slider("Teaching", 0, 100, 50, key="skill_slider2")
st.slider("Web skills", 0, 100, 50, key="skill_slider3")

st.markdown('<a name="gallery"></a>', unsafe_allow_html=True)
st.title("My projects")

images = [
    "images/g1.png", "images/g2.jpg", "images/g3.jpg",
    "images/g4.jpg", "images/g5.jpg", "images/g6.png",
    "images/g7.png", "images/g8.png", "images/g9.png"
]

# Desired size for all images
desired_size = (200, 200)

cols = st.columns(3)
for i, image_path in enumerate(images):
    # Open and resize image
    image = Image.open(image_path)
    image = image.resize(desired_size)

    # Display image in the appropriate column
    col = cols[i % 3]
    col.image(image, use_container_width =True)



st.title("My Setup")
st.image("images/setup.jpg")

st.title("My favorite anime scene")
st.video("https://youtu.be/thMXb5r792s?si=6UYnoseyuHsWdJnS")


st.markdown('<a name="contact"></a>', unsafe_allow_html=True)
st.title("Contact")
st.write("For any inquiries, please email me at:")
st.subheader("sanathkamath11@gmail.com")

cols = st.columns(3)
with cols[0]:
    st.markdown(
        f'<a href="{twitter_url}" target="_blank"><img src="data:image/png;base64,{twitter_base64}" width="50"></a>',
        unsafe_allow_html=True)
with cols[1]:
    st.markdown(
        f'<a href="{linkedin_url}" target="_blank"><img src="data:image/png;base64,{linkedin_base64}" width="50"></a>',
        unsafe_allow_html=True)
with cols[2]:
    st.markdown(
        f'<a href="{github_url}" target="_blank"><img src="data:image/png;base64,{github_base64}" width="50"></a>',
        unsafe_allow_html=True)


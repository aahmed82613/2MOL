import streamlit as st
import random

# --- PAGE CONFIG ---
st.set_page_config(page_title="2 Months of Love", page_icon="💙", layout="centered")

# Initialize slide counter
if 'slide_count' not in st.session_state:
    st.session_state.slide_count = 0

# --- CUSTOM MANGA STYLE CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #fcfcfc; }

    /* Forcing all text to black */
    h1, h2, h3, p, span, div, li { 
        color: #1a1a1a !important; 
        font-family: 'Courier New', Courier, monospace;
    }

    h1, h2 { 
        text-transform: uppercase;
        border-bottom: 2px solid #1a1a1a;
        padding-bottom: 10px;
        font-weight: bold;
    }

    .reason-card {
        background-color: #ffffff;
        padding: 25px;
        border: 2px solid #1a1a1a;
        box-shadow: 8px 8px 0px #dddddd;
        margin-top: 20px;
        margin-bottom: 20px;
        font-size: 1.2rem;
        line-height: 1.6;
    }

    .stButton>button {
        width: 100%;
        border-radius: 0px;
        border: 2px solid #1a1a1a;
        background-color: white;
        color: #1a1a1a !important;
        font-weight: bold;
        height: 3em;
    }
    .stButton>button:hover {
        background-color: #1a1a1a;
        color: white !important;
    }

    /* Falling Rose Animation */
    @keyframes falling-roses {
        0% { transform: translateY(-10vh) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .rose {
        position: fixed;
        top: -10vh;
        font-size: 2rem;
        user-select: none;
        z-index: 9999;
        animation: falling-roses linear infinite;
    }
    </style>
    """, unsafe_allow_html=True)


# Function to generate falling blue roses
def blue_rose_fall():
    rose_html = ""
    for i in range(20):
        left = random.randint(0, 95)
        duration = random.randint(5, 10)
        delay = random.randint(0, 5)
        rose_html += f'<div class="rose" style="left:{left}%; animation-duration:{duration}s; animation-delay:{delay}s;">🌹</div>'
    # Note: Using red rose emoji as the base, but we can style it via CSS if needed.
    # For a true blue rose feel, we use the 💙 or a blue rose image.
    st.markdown(rose_html.replace('🌹', '💙'), unsafe_allow_html=True)


# --- NAVIGATION LOGIC ---
def next_slide():
    st.session_state.slide_count += 1


def reset_slides():
    st.session_state.slide_count = 0


# --- SLIDES ---

# Introduction Page
if st.session_state.slide_count == 0:
    st.title("2 Months of Love")
    st.subheader("5 Reasons Why I Love Maria")
    st.write("By: Abubakar Ahmed")
    st.write("---")
    st.write("Wanted to make a little gift for you for our two months, thank you for being you!")
    st.button("Start the Journey", on_click=next_slide)

# Reason 1: Kind [cite: 3-6]
elif st.session_state.slide_count == 1:
    st.header("Reason 1: You’re Kind")
    st.image("nagikind.png")
    st.markdown(
        '<div class="reason-card">You always apologize for things that you never need to apologize for. I used to find it annoying, but I’ve grown to like this because it shows you care. <br><br>I’m a very apologetic guy as well, so we will always be apologizing to each other but I think it’s cute and I hope we apologize to each other forever.</div>',
        unsafe_allow_html=True)
    st.button("Next Reason →", on_click=next_slide)

# Reason 2: Determined [cite: 7-11]
elif st.session_state.slide_count == 2:
    st.header("Reason 2: You’re Determined")
    st.image("nagidetermined.png")
    st.markdown(
        '<div class="reason-card">I love that you truly want to change who you are. Whether you’re good or bad as a person, you want to be BETTER and that’s amazing. <br><br>Going back to school, coming to me about your very serious problems—you’re amazing and I truly hope you become someone you’re proud to be. Even if you never do, I’m proud of you Maria.</div>',
        unsafe_allow_html=True)
    st.button("Next Reason →", on_click=next_slide)

# Reason 3: Smart [cite: 12-16]
elif st.session_state.slide_count == 3:
    st.header("Reason 3: You’re Smart")
    st.image("nagismart.png")
    st.markdown(
        '<div class="reason-card">You want to learn, dip your toes in different things, and when I talk to you about things you don’t really know about, you engage yourself and try to understand and that makes me happy. <br><br><b>You’re a smart cookie Maria, sweet too! Best kind of cookies!!</b></div>',
        unsafe_allow_html=True)
    st.button("Next Reason →", on_click=next_slide)

# Reason 4: Funny [cite: 17-19]
elif st.session_state.slide_count == 4:
    st.header("Reason 4: You’re Funny")
    st.image("nagifunny.png")
    st.markdown(
        '<div class="reason-card">You make me laugh a lot, always making me feel better. Idk what I’d do without your humor and kindness! You’re awesome and you make me laugh.</div>',
        unsafe_allow_html=True)
    st.button("Next Reason →", on_click=next_slide)

# Reason 5: Stunning
elif st.session_state.slide_count == 5:
    st.header("Reason 5: You’re Stunning")
    st.image("nagistunning.png")
    st.markdown(
        '<div class="reason-card">You never think so, but I do. Since I saw you I always thought you were pretty. You’re gorgeous, and I can’t believe you’d like someone like me. <br><br>I hope I can continue to be with you my gorgeous beautiful queen!!</div>',
        unsafe_allow_html=True)
    st.button("Final Surprise 🎁", on_click=next_slide)

# Final Message
elif st.session_state.slide_count == 6:
    blue_rose_fall()  # This triggers the blue roses!
    st.balloons()
    st.header("I LOVE YOU!!!")
    st.image("nagireo.png")
    st.markdown("""
    <div class="reason-card">
    <b>Happy 2 months to my one and only.</b><br><br>
    I hope we have many more months. I’ll never stop loving you no matter what, so be prepared.<br><br>
    <i>— your "friend", Abubakar Ahmed</i>
    </div>
    """, unsafe_allow_html=True)
    st.button("Restart Journey", on_click=reset_slides)
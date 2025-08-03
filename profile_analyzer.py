import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Career Advisor", page_icon="💼", layout="centered")

# ---- CUSTOM CSS FOR STYLING ----
st.markdown("""
    <style>
        body {
            background-color: #f8f9fa;
        }
        .main {
            # background-color: #ffffff;
            # padding: 2rem;
            # border-radius: 20px;
            # box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }
        .title {
            font-size: 2.5rem;
            font-weight: bold;
            color: #2c3e50;
            text-align: center;
        }
        .subtitle {
            font-size: 1.2rem;
            color: #7f8c8d;
            text-align: center;
            margin-bottom: 30px;
        }
    </style>
""", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<div class="title">🚀 Career Recommendation System</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Personalized advice based on your interests & skills</div>', unsafe_allow_html=True)

    # ✅ Step 1: User Input Section (Streamlit UI)
    Name = st.text_input("🧑 Enter Your Name:")
    Age = st.number_input("🎂 Enter Your Age:", min_value=0, max_value=100, step=1)
    Gender = st.radio("🚻 Select Your Gender:", ["Male", "Female", "Other"])
    User_Intrest = st.selectbox("🎯 Choose Your Interest:", ["Coding", "Art", "Public Speaking", "Business"])
    Skill_Level = st.slider("📈 Rate Your Skill Level (1 to 10):", 1, 10)
    Career_Goal = st.selectbox("🎓 What is Your Career Goal?", ["Financial Freedom", "Impact", "Fame", "Safety", "Others"])

    # ✅ Step 2: Personality Mapping (Interest-Based Logic)
    Intrest_Map = {
        "Coding": "Logical",
        "Art": "Creative",
        "Public Speaking": "Expressive",
        "Business": "Strategic"
    }

    if User_Intrest in Intrest_Map:
        Mapped_Personality = Intrest_Map[User_Intrest]
        st.info(f"🎭 Personality Type: **{Mapped_Personality}**")
    else:
        Mapped_Personality = "Not Recognized"
        st.warning("❌ Interest Not Recognized")

    # ✅ Step 3: Skill Level Evaluation
    if Skill_Level <= 4:
        st.write("🟠 **Beginner**")
    elif Skill_Level <= 7:
        st.write("🟡 **Intermediate**")
    else:
        st.write("🟢 **Expert**")

    # ✅ Step 4: Interest + Skill Based Suggestions

    if Skill_Level <= 4 and User_Intrest == "Business":
        st.success("Start with Freelance Digital Marketing or E-commerce Selling")
    elif 4 < Skill_Level < 8 and User_Intrest == "Business":
        st.success("Start your own business or become a digital entrepreneur.")
    elif Skill_Level >= 8 and User_Intrest == "Business":
        st.success("Build a scalable business model or mentor others in digital entrepreneurship.")

    if Skill_Level <= 4 and User_Intrest == "Coding":
        st.success("Start with HTML, CSS, and Python basics on YouTube or FreeCodeCamp.")
    elif 4 < Skill_Level < 8 and User_Intrest == "Coding":
        st.success("Start making small projects like calculator, portfolio website, or logic-based games.")
    elif Skill_Level >= 8 and User_Intrest == "Coding":
        st.success("Build full web apps using frameworks like Django or Streamlit, and contribute to GitHub.")

    if Skill_Level <= 4 and User_Intrest == "Art":
        st.success("Practice sketching or digital drawing using apps like IbisPaint or Procreate.")
    elif 4 < Skill_Level < 8 and User_Intrest == "Art":
        st.success("Start building your online art portfolio on Instagram or Behance.")
    elif Skill_Level >= 8 and User_Intrest == "Art":
        st.success("Create a personal brand, sell digital prints on Etsy, and teach art online.")

    if Skill_Level <= 4 and User_Intrest == "Public Speaking":
        st.success("Start practicing speeches in front of a mirror or record yourself.")
    elif 4 < Skill_Level < 8 and User_Intrest == "Public Speaking":
        st.success("Join Toastmasters, start a podcast or speak at school/college events.")
    elif Skill_Level >= 8 and User_Intrest == "Public Speaking":
        st.success("Host webinars, become a motivational speaker, and offer workshops.")

    # ✅ Step 5: Career Goal Suggestions
    Career_Goals_Map = {
        "Financial Freedom": "💸 Work towards scalable business or long-term investing.",
        "Impact": "🌍 Try NGOs, social startups or purpose-driven work.",
        "Fame": "🌟 You may explore YouTube, public speaking or creative performance.",
        "Safety": "🔐 Look into stable jobs like Govt, Teaching, or Corporate.",
        "Others": "🌈 Unique career goal! Follow your passion."
    }

    if Career_Goal in Career_Goals_Map:
        st.info(Career_Goals_Map[Career_Goal])
    else:
        st.info("🚀 Explore Unique Careers")

    # ✅ Final Summary
    Final_Summary = {
        "Name": Name,
        "Age": Age,
        "Gender": Gender,
        "Interest": User_Intrest,
        "Skill_Level": Skill_Level,
        "Personality_Type": Mapped_Personality,
        "Career Goal": Career_Goal
    }

    st.markdown("## 🧾 Final Career Report")

for key, value in Final_Summary.items():
    st.markdown(f"**{key}:** {value}")

# ✅ Footer
st.markdown("""
    <hr style="margin-top: 50px; margin-bottom:10px;">
    <div style='text-align: center; font-size: 14px; color: #95a5a6;'>
        Made with ❤️ by Mohammad Ahsan | Career Advisor Streamlit App
    </div>
""", unsafe_allow_html=True)

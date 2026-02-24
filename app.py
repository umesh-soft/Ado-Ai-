import streamlit as st

st.set_page_config(page_title="DesiAds AI", layout="centered")

st.title("🚀 DesiAds AI - Free Ads Generator")

product = st.text_input("Enter Product / Service Name")

language = st.selectbox("Select Language", ["English", "Hindi", "Hinglish"])

platform = st.selectbox("Select Platform", [
    "Facebook Ads",
    "Instagram Ads",
    "Google Ads",
    "YouTube Ads",
    "LinkedIn Ads"
])

tone = st.selectbox("Select Tone", [
    "Professional",
    "Emotional",
    "Aggressive Sales",
    "Friendly"
])

if st.button("Generate Ad"):
    if product:
        if language == "Hindi":
            ad = f"""
Primary Text:
Apne business ko grow kare {product} ke saath!

Headline:
Sabse Behtar {product}

Description:
Limited samay ke liye khaas offer.

CTA:
Abhi Kharide 🚀
"""
        elif language == "Hinglish":
            ad = f"""
Primary Text:
Apna business boost karo {product} ke saath!

Headline:
Best {product} Live Hai!

Description:
Limited time deal boss!

CTA:
Order Now 🔥
"""
        else:
            ad = f"""
Primary Text:
Boost your business with {product}!

Headline:
Best {product} Available Now!

Description:
Limited time offer.

CTA:
Shop Now 🚀
"""

        st.success("Ad Generated Successfully!")
        st.text_area("Your Ad Copy", ad, height=250)
    else:
        st.warning("Please enter product name.")

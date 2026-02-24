import streamlit as st

st.set_page_config(page_title="Ado AI", layout="centered")

# --------- Custom Button Style ----------
st.markdown("""
<style>
.stButton>button {
    background-color: #ff4b4b;
    color: white;
    font-size: 18px;
    border-radius: 8px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("Ado AI - Ads Generator")

# --------- INPUT SECTION ----------
product = st.text_input("Enter Product Name")
offer = st.text_input("Enter Special Offer (Example: 20% Off, Free Delivery)")

platform = st.selectbox("Select Platform",
                        ["Instagram", "Facebook", "Google", "YouTube"])

language = st.selectbox("Select Language",
                        ["English", "Hindi", "Hinglish"])

# --------- GENERATE BUTTON ----------
if st.button("Generate Professional Ads"):

    if product and offer:

        # PLATFORM BASED EXTRA
        if platform == "Instagram":
            extra = "Use trending hashtags and emotional appeal."
            hashtags = f"#{product} #Sale #LimitedOffer #ShopNow"
        elif platform == "Facebook":
            extra = "Focus on engagement and benefits."
            hashtags = f"#{product} #BestDeal #Offer"
        elif platform == "Google":
            extra = "Keep it short and direct."
            hashtags = ""
        else:
            extra = "Make it engaging for video audience."
            hashtags = ""

        # -------- LANGUAGE BASED OUTPUT --------

        if language == "English":

            ad1 = f"""
### 1️⃣ ENGLISH AD

**Headline:** Best {product} Now with {offer}!

**Body:** Looking for premium {product}? Now is your chance! Enjoy quality, durability, and unbeatable value. {extra}

**Call To Action:** Shop Now and Save Big! 🚀
"""

            ad2 = f"""
### 2️⃣ ENGLISH AD

**Headline:** Limited Time {offer} on {product}!

**Body:** Don’t miss this amazing deal. Trusted by customers and built for performance.

**Call To Action:** Buy Now Before Offer Ends! 🛒
"""

        elif language == "Hindi":

            ad1 = f"""
### 1️⃣ हिंदी विज्ञापन

**हेडलाइन:** सबसे बेहतरीन {product} अब {offer} के साथ!

**विवरण:** क्या आप उच्च गुणवत्ता वाले {product} की तलाश में हैं? अभी पाएँ शानदार ऑफर। {extra}

**कॉल टू एक्शन:** अभी खरीदें और बचत करें! 🚀
"""

            ad2 = f"""
### 2️⃣ हिंदी विज्ञापन

**हेडलाइन:** {product} पर {offer} – सीमित समय ऑफर!

**विवरण:** ग्राहकों द्वारा भरोसेमंद और उच्च गुणवत्ता वाला उत्पाद।

**कॉल टू एक्शन:** अभी ऑर्डर करें! 🛒
"""

        else:

            ad1 = f"""
### 1️⃣ HINGLISH AD

**Headline:** Best {product} Ab {offer} ke Saath!

**Body:** Premium quality {product} ab special price par. {extra}

**Call To Action:** Order Now aur Save Karo! 🚀
"""

            ad2 = f"""
### 2️⃣ HINGLISH AD

**Headline:** {product} Par {offer} – Limited Time Deal!

**Body:** Trusted aur stylish product ab amazing price me available hai.

**Call To Action:** Buy Now! 🛒
"""

        # -------- OUTPUT SECTION --------
        st.success("Ads Generated Successfully!")

        st.markdown(ad1)
        st.markdown(ad2)

        full_output = ad1 + "\n\n" + ad2

        st.text_area("📋 Copy Your Ads Below", full_output, height=300)

        if hashtags:
            st.markdown("### 🔥 Suggested Hashtags")
            st.write(hashtags)

    else:
        st.warning("Please enter product name and offer.")

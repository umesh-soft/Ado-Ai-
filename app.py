import streamlit as st

st.set_page_config(page_title="Ado AI Generator", layout="centered")

st.title(" Ado AI - Structured Ads Generator")

product = st.text_input("Enter Product Name")
offer = st.text_input("Enter Special Offer (Example: 15% Off, Free Delivery)")
language = st.selectbox("Select Language", ["English", "Hindi", "Hinglish"])

if st.button("Generate Professional Ads"):
    if product and offer:

        if language == "English":

            ad1 = f"""
### 1. ENGLISH AD

• **Headline:** Get the Best {product} – Now with {offer}!

• **Body:** Looking for premium quality {product}? Now is your chance! Enjoy unbeatable performance, stylish design, and maximum comfort. Perfect for everyday use.

• **Call to Action:** Shop Now and Upgrade Your Experience! 🚀
"""

            ad2 = f"""
### 2. ENGLISH AD

• **Headline:** Limited Time {offer} on {product}!

• **Body:** Don’t miss this exclusive deal. Our {product} is trusted by customers and built for top performance. Grab yours before the offer ends.

• **Call to Action:** Buy Now & Save Big! 🛒
"""

        elif language == "Hindi":

            ad1 = f"""
### 1. हिंदी विज्ञापन

• **हेडलाइन:** सबसे बेहतरीन {product} अब {offer} के साथ!

• **विवरण:** क्या आप उच्च गुणवत्ता वाले {product} की तलाश में हैं? अब पाएँ शानदार प्रदर्शन, स्टाइलिश डिज़ाइन और बेहतरीन आराम — सीमित समय के लिए विशेष ऑफर।

• **कॉल टू एक्शन:** अभी खरीदें और ऑफर का लाभ उठाएँ! 🚀
"""

            ad2 = f"""
### 2. हिंदी विज्ञापन

• **हेडलाइन:** {product} पर {offer} – मौका न गँवाएँ!

• **विवरण:** हमारे {product} को ग्राहकों का भरोसा मिला है। बेहतर गुणवत्ता और शानदार अनुभव के लिए आज ही ऑर्डर करें।

• **कॉल टू एक्शन:** अभी ऑर्डर करें और बचत करें! 🛒
"""

        else:

            ad1 = f"""
### 1. HINGLISH AD

• **Headline:** Best {product} Ab {offer} ke Saath!

• **Body:** Kya aap premium quality {product} dhund rahe ho? Ab milega stylish design aur powerful performance ke saath limited time offer me.

• **Call to Action:** Order Now aur Deal Grab Karo! 🚀
"""

            ad2 = f"""
### 2. HINGLISH AD

• **Headline:** {product} Par {offer} – Limited Time Deal!

• **Body:** Trusted aur high-quality {product} ab special price par available hai. Aaj hi kharido aur fayda uthao.

• **Call to Action:** Buy Now aur Save Karo! 🛒
"""

        st.success("2 Structured Ads Generated Successfully!")

        st.markdown(ad1)
        st.markdown(ad2)

    else:
        st.warning("Please enter product name and offer.")

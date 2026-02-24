import streamlit as st

st.set_page_config(page_title="DesiAds AI", layout="centered")

st.title("🚀 DesiAds AI - Smart Free Ads Generator")

product = st.text_input("Enter Product Name")
offer = st.text_input("Enter Special Offer / Feature (Example: 50% Off, Free Delivery)")

language = st.selectbox("Select Language", ["English", "Hindi", "Hinglish"])

if st.button("Generate Ads"):
    if product and offer:

        if language == "Hindi":

            ad1 = f"""
🔥 क्या आप {product} ढूंढ रहे हैं?

अब पाएँ {product} सिर्फ {offer} के साथ!

✔ उच्च गुणवत्ता
✔ भरोसेमंद सेवा
✔ सीमित समय का ऑफर

👉 अभी खरीदें और लाभ उठाएँ!
"""

            ad2 = f"""
✨ मौका हाथ से न जाने दें!

{product} अब उपलब्ध है {offer} के साथ।

आज ही ऑर्डर करें और शानदार डील पाएं।

🚀 अभी ऑर्डर करें!
"""

        elif language == "Hinglish":

            ad1 = f"""
🔥 Kya aap best {product} dhund rahe ho?

Ab milega {product} sirf {offer} ke saath!

✔ Premium Quality
✔ Trusted by Customers
✔ Limited Time Deal

👉 Order Now!
"""

            ad2 = f"""
✨ Ye deal miss mat karo!

{product} ab available hai {offer} ke saath.

Aaj hi kharido aur fayda uthao!

🚀 Shop Now!
"""

        else:

            ad1 = f"""
🔥 Looking for the best {product}?

Now get {product} with {offer}!

✔ Premium Quality
✔ Trusted Brand
✔ Limited Time Offer

👉 Shop Now!
"""

            ad2 = f"""
✨ Don’t miss this amazing deal!

Grab your {product} today with {offer}.

Limited stock available.

🚀 Buy Now!
"""

        st.success("2 Ads Generated Successfully!")

        st.subheader("Ad Version 1")
        st.text_area("", ad1, height=200)

        st.subheader("Ad Version 2")
        st.text_area(" ", ad2, height=200)

    else:
        st.warning("Please enter both product name and offer.")

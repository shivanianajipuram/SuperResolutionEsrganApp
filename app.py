import streamlit as st
from PIL import Image
from inference import enhance_image

st.title("🚀 Real-ESRGAN Super Resolution App")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)

    st.image(image, caption="Original Image", use_container_width=True)

    if st.button("Enhance Image"):
        with st.spinner("Processing with Real-ESRGAN..."):
            output = enhance_image(image)

        st.image(output, caption="Enhanced Image", use_container_width=True)

        # Save properly (FIXED)
        output.save("output.png")

        with open("output.png", "rb") as file:
            st.download_button(
                "Download Image",
                file,
                file_name="sr_image.png",
                mime="image/png"
            )
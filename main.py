import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Passing the Key for auth
API_KEY = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=API_KEY)

# Load the original model (can be moved outside the app for efficiency)
text_model = genai.GenerativeModel('gemini-pro')
vision_model = genai.GenerativeModel('gemini-pro-vision')


# Function to generate response
def generate_response(prompt, model, images=None):
    with st.spinner("Generating response..."):
        if model == text_model:
            response = model.generate_content(prompt)
        elif model == vision_model and images:
            # Convert the uploaded file to PIL.Image.Image
            images = Image.open(io.BytesIO(images.read()))
            response = model.generate_content([prompt, images], stream=True)
            response.resolve()
        else:
            response = None
    return response.text if response else None, images


# Streamlit app
def main():
    # Set page title and favicon
    st.set_page_config(
        page_title="Gemini-Powered chatGPT-Like App",
        page_icon="✨",
        layout="wide"
    )

    # Set app title
    st.title("Gemini-Powered🚀 ChatGPT-Like App✨ ")

    # Choose from available models
    available_models = ["Text Generation", "Image to Text Generation"]
    model_name = st.sidebar.selectbox("Choose Model", available_models)

    if model_name == "Text Generation":
        model = text_model
        # Input prompt from user
        prompt = st.text_input("Enter your prompt:", placeholder="Ask me anything...")
        images = None
    elif model_name == "Image to Text Generation":
        model = vision_model
        # Input prompt from user
        prompt = st.text_area("Enter your text prompt:", placeholder="Write a short, engaging blog post...")
        # Upload image option
        images = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

    if st.button("Generate Response"):
        if prompt:
            # Display generated response
            response, image = generate_response(prompt, model, images)
            if response:
                st.markdown(f"**Response:**  \n{response}")
                if image:
                    st.image(image, caption="Your Provided Image", width=300, use_column_width=False)
            else:
                st.info("Failed to generate a response. Please check your input and try again.")
        else:
            st.warning("Please check your input and try again.")

    # Sidebar with additional features
    st.sidebar.header("About this app")
    st.sidebar.write(
        "This app leverages the Gemini LLM models to generate human-quality text "
        "responses to your prompts. It includes a vision model that can generate text "
        "from a combination of text and images. Explore the capabilities by selecting "
        "different models and providing prompts or images."
    )

    # Developer information
    st.sidebar.header("Developer✨🚀")
    st.sidebar.write(
        "Developed🚀 by **Rakesh Kumar**\n"
        "\n Feel free to connect and share your feedback(✨)"
        "\n on LinkedIn: [Rakesh Kumar](https://www.linkedin.com/in/m-rakesh-kr/)"
    )

    # Add some styling to the sidebar
    st.sidebar.markdown(
        """
        <style>
            .sidebar .sidebar-content {
                background: linear-gradient(to bottom, #f5f5f5, #e0e0e0);
                padding: 20px;
                border-radius: 10px;
            }
            .sidebar .sidebar-content .block-container {
                margin-bottom: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()

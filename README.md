# GeminiChatGPT🚀 App - Powered by Gemini✨

**GeminiChatGPT** is an interactive AI-powered application that leverages Google's Gemini language and vision models to generate human-like responses for both text-based and image-assisted prompts. The app offers a streamlined interface, allowing users to experiment with Gemini's large language models (LLMs) for tasks like text generation and image-to-text generation.

## Features

### 1. **Text Generation**
- Users can input any prompt, and the **Gemini Text Model** (`gemini-pro`) will generate a human-like response.
- Suitable for tasks such as general Q&A, blog writing, creative storytelling, and more.

### 2. **Image-to-Text Generation**
- Users can upload images (JPG, JPEG, PNG) and combine them with text prompts.
- The **Gemini Vision Model** (`gemini-pro-vision`) generates a contextually aware response based on the text prompt and image.
- Useful for generating image descriptions, captions, or creative responses that mix visual and textual elements.

### 3. **Rain Effect**
- The app adds a playful touch with a falling emoji effect on the main interface, enhancing user experience.

### 4. **Easy Model Selection**
- Users can seamlessly switch between text and image-to-text generation models using the sidebar dropdown.

### 5. **Interactive and User-Friendly**
- The app is built with a clean and responsive interface using Streamlit, making it easy for users to interact and experiment with advanced AI models.

### 6. **Developer Information**
- Users can find developer contact information and feedback options directly in the sidebar.

## Installation and Setup

Follow the steps below to install and run the **GeminiChatGPT** app on your local machine.

### Prerequisites
- Python 3.8 or higher
- A Google Gemini API key

### Step 1: Clone the Repository

```bash
git clone https://github.com/tech-rakesh-ai/GeminiChatGPT.git
cd GeminiChatGPT
```

### Step 2: Create and Activate a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Step 3: Install the Required Dependencies

```bash
pip install -r requirements.txt
```

Make sure your `requirements.txt` contains the following:

```text
streamlit
google-generativeai
streamlit-extras
Pillow
```

### Step 4: Set Up API Key

Create a file called `.streamlit/secrets.toml` in the root directory and add your Google Gemini API key:

```toml
[secrets]
GOOGLE_API_KEY = "your-google-api-key"
```

Replace `your-google-api-key` with the actual API key you obtained from Google Generative AI.

### Step 5: Run the Application

To start the Streamlit app, run:

```bash
streamlit run app.py
```

The application will open in your browser, where you can begin experimenting with text and image-to-text generation.

## How to Use

1. **Model Selection**: Use the sidebar to select either:
   - 📑 Text Generation: For text-only prompts.
   - 🚀 Image to Text Generation: For text prompts with an optional image upload.
   
2. **Input Prompt**: Type your question or request into the text input field:
   - For text generation, enter your prompt in the text box.
   - For image-to-text generation, upload an image and optionally provide a text prompt.

3. **Generate Response**: Click the "Generate Response" button to see the AI's response based on the selected model and your input.

4. **View Results**: The AI-generated response will be displayed, and if an image was uploaded, it will also be shown.

## Application Structure

```bash
gemini-chatgpt-app/
│
├── app.py                     # Main application code
├── requirements.txt            # Dependencies file
└── .streamlit/
    └── secrets.toml            # API key configuration (not included in repo)
```

## Key Components

- **Gemini Models**: Uses Google's `gemini-pro` and `gemini-pro-vision` models for text and image-to-text generation.
- **Streamlit for UI**: Streamlit is used to create an intuitive and interactive user interface for generating and displaying responses.
- **Pillow for Image Handling**: The `Pillow` library is used for handling uploaded images, converting them into a format the AI model can process.

## Future Enhancements

- Support for additional media types (e.g., video, audio) for further multimodal generation.
- Real-time response streaming for a more interactive experience.
- Enhanced styling and layout for better mobile and desktop compatibility.

## Developer

Developed by **Rakesh Kumar**.  
Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/tech-rakesh-ai/) to provide feedback and discuss improvements.

## License

MIT License © 2024 GeminiChatGPT.

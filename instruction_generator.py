import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
import io

# Configure the API key securely
# genai.configure(api_key="Your gemini api key") #OR streamlit secrets OR environment variables
# Configure the API key using streamlit secrets
api_key = st.secrets["GEMINI_API_KEY"]  
if not api_key:
    st.error("API key not found. Please set the GOOGLE_API_KEY environment variable.")
else:
    genai.configure(api_key=api_key)

# Choose a Gemini model.
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

st.title('Instruction Generator')

st.header("Upload Multiple Screenshots")
uploaded_images = st.file_uploader("Choose images", accept_multiple_files=True, type=["png", "jpg", "jpeg"])

st.header('Optional Context')
optional_context = st.text_area("Context",placeholder="Provide any optional context here...")
optional_context='Additional context: '+optional_context

def generate_content_with_status(prompt):
    with st.spinner('Generating test instructions, please wait...'):
        try:

            response = model.generate_content(prompt)
            st.success("Testing instructions generated successfully!")
            return response
        except Exception as e:
            st.error(f"An error occurred: {e}")
            return None


if st.button('Describe testing instructions'):
        # Create the prompt.
        prompt = '''Analyze the provided screenshots and generate a comprehensive, step-by-step guide for testing the functionality of each feature depicted. For each test case, ensure the following details are included:

                Description: Provide a concise summary of the feature and what the test case aims to validate.

                Pre-conditions: Outline any necessary setup or conditions required before performing the test (e.g., logged-in state, data inputs, or prerequisite selections).

                Testing Steps: Detail a series of precise, step-by-step instructions on how to execute the test, ensuring clarity and logical flow. Each step should guide the tester through actions on the interface, ensuring completeness.

                Expected Result: Describe the outcome if the feature functions as intended, specifying what should appear or happen on the screen, including any UI/UX feedback, data changes, or transitions.

                Additional Requirements:

                Ensure that each test case accounts for relevant edge cases and error handling scenarios where applicable.
                If a feature includes multiple states or variations (e.g., success/failure states, different input conditions), include test cases for each state.
                Where applicable, integrate multi-step processes (e.g., navigation through multiple screens) and ensure test cases address the end-to-end workflow.
                Use structured, multi-shot prompting to improve the clarity and depth of the test case descriptions.
                Highlight any assumptions made about functionality not explicitly depicted in the screenshots.
                Focus on covering key functionalities such as selections, filters, interactions, and dynamic responses, ensuring that test cases are thorough and reflective of user expectations.'''
        
        # Make the LLM request.
        inputs=[]
        # Assuming you have a list of uploaded images and a prompt
        for uploaded_image in uploaded_images:
                # Convert uploaded image to a PIL Image object
                image_data = uploaded_image.read()  # Read the image data from the uploaded file
                image = Image.open(io.BytesIO(image_data))  # Convert it to a PIL Image object
                inputs.append(image)
        
        if optional_context:
            prompt += "\nAdditional context: " + optional_context
        inputs.append(prompt)
        
        response = generate_content_with_status(inputs)
    
        # Display the response
        st.subheader("Generated Test Instructions")
        st.markdown(response.text)
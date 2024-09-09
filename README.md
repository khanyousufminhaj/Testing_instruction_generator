
# AI-Powered Testing Instruction Generator
# [Live Website](https://testinginstructiongenerator.streamlit.app/)
![image](https://github.com/user-attachments/assets/30e0abce-804a-4f37-8a81-b7224b301126)

## Overview

This **AI-Powered Testing Instruction Generator** is a web application built using **Streamlit** and **Google's Gemini API** to automatically generate comprehensive testing instructions from uploaded screenshots. The tool creates detailed, step-by-step test cases for software testers, helping them assess key functionalities depicted in the images.

## Features

- **Multiple Screenshot Uploads**: Upload multiple screenshots and generate test cases for each feature shown in the images.
- **AI-Powered Instruction Generation**: Uses Google's Gemini API to generate detailed, multi-step testing instructions.
- **Optional Context Input**: Provide additional context to guide the AI in generating more tailored test instructions.

## Project Structure

```
├── instruction_generator.py    # Main script for running the web application
├── requirements.txt            # Dependencies
└── Test Demo File              #Demo files for using the tool
```

## Requirements

- **Python 3.7+**
- **Streamlit**: For building the web application.
- **Google's Gemini API**: For generating the testing instructions.
- **PIL (Python Imaging Library)**: For handling image uploads.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/ai-testing-instruction-generator.git
   ```

2. Navigate into the project directory:

   ```bash
   cd ai-testing-instruction-generator
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your Google Gemini API key in **Streamlit Secrets** or environment variables.

   - Add your API key to the `secrets.toml` file in the `.streamlit/` folder:
   
     ```toml
     [secrets]
     GEMINI_API_KEY = "your_gemini_api_key"
     ```

   - Alternatively, set it as an environment variable:
   
     ```bash
     export GEMINI_API_KEY="your_gemini_api_key"
     ```

## Running the Application

1. Start the Streamlit web application by running the following command:

   ```bash
   streamlit run instruction_generator.py
   ```

2. Open your browser to the local Streamlit server (typically `http://localhost:8501`).

3. On the webpage:
   - **Upload screenshots** in PNG, JPG, or JPEG format.
   - Provide **optional context** to guide the AI in generating specific test cases.
   - Click on **Describe testing instructions** to generate the instructions.

## Example Usage

1. Run the application:

   ```bash
   streamlit run instruction_generator.py
   ```

2. Upload images of your application's interface or feature, add optional context (if any), and generate AI-driven testing instructions based on the screenshots.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch-name`.
3. Make your changes.
4. Commit your changes: `git commit -m 'Add some feature'`.
5. Push to the branch: `git push origin feature-branch-name`.
6. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.

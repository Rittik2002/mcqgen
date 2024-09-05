## Libraries Used:
# os & dotenv: For managing environment variables, particularly to fetch the Google API key for Google Generative AI.
# json : For handling JSON data (MCQs and quiz structure).
# PyPDF2: To extract text from a PDF file uploaded by the user.
# FPDF: To create and format the PDF containing the MCQs.
# streamlit: To create the user interface.

## Template Strings:
# TEMPLATE: A prompt template used to generate the quiz by interacting with Google Generative AI (Gemini model). It asks for a certain number of # # MCQs based on a provided text, in a specific subject and tone.
# TEMPLATE2: A prompt template for evaluating the complexity and appropriateness of the generated quiz for a particular level (e.g., students)
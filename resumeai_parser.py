import openai
import PyPDF2
import docx
import json
from utils import extract_text_from_file
import fitz
import os

# Set your OpenAI API Key
openai.api_key = "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"  # Replace with your OpenAI API Key

def extract_images_from_pdf(pdf_path):
    """
    Extracts the first image from the PDF and saves it in the static/uploads directory.
    """
    doc = fitz.open(pdf_path)
    image_path = None
    upload_dir = "static/uploads"

    # Ensure the upload directory exists
    os.makedirs(upload_dir, exist_ok=True)

    for page_num in range(len(doc)):
        page = doc[page_num]
        images = page.get_images(full=True)
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            ext = base_image["ext"]
            image_path = os.path.join(upload_dir, f"profile_image_{page_num}_{img_index}.{ext}")
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
            return image_path  # Return the path of the first extracted image
    return None

def parse_resume(file_path):
    """
    Parse the resume to extract details.
    """
    resume_text = extract_text_from_file(file_path)
    profile_image = None

    # Extract profile picture if it's a PDF
    if file_path.endswith(".pdf"):
        profile_image = extract_images_from_pdf(file_path)

    # Define the parsing prompt
    prompt = f"""
    Extract the following details from the provided resume text:
    - Basic Information: full name, email, phone number, address
    - Education: institution name, program name, start date, end date
    - Job Experience: company name, job title, duration, description
    - Skills: list them

    Respond ONLY with a valid JSON object. Do not include any additional commentary or text outside the JSON.

    Resume content:
    {resume_text}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )

    try:
        extracted_data = json.loads(response.choices[0].message['content'])
    except (json.JSONDecodeError, KeyError) as e:
        print("Failed to parse JSON response:", e)
        extracted_data = {
            "Basic Information": {"full name": "", "email": "", "phone number": "", "address": ""},
            "Education": [],
            "Job Experience": [],
            "Skills": [],
        }

    # Include the profile image path in the extracted data
    extracted_data["Profile Picture"] = "uploads/" + os.path.basename(profile_image)

    return extracted_data




    
#openai.api_key = "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"  # Replace with your OpenAI API Key

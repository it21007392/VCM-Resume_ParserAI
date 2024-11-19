# ResumeParser_AI

Recruiters today face the overwhelming task of filtering through thousands, sometimes hundreds of thousands, of resumes from platforms like LinkedIn and Naukri. With the sheer volume of applications, manually reviewing every PDF or DOCX file to identify top candidates becomes not only time-consuming but prone to human error, often resulting in missing out on great talent.

ResumeAI-Parser+ solves this problem by automating the extraction of key resume details, turning resume files into actionable data. With ResumeAI-Parser+, recruiters can quickly analyze candidates based on critical factors like education, years of experience, current company, and skills—presented neatly in an Excel sheet. This allows for efficient sorting and filtering, enabling teams to identify the most qualified candidates in minutes rather than days.

Whether you're hiring for a single role or filling numerous positions across departments, ResumeAI-Parser+ acts as the bridge between endless resumes and the best talent, streamlining the recruitment process, saving time, and ensuring that no great candidate is overlooked. Let AI handle the resume grunt work while you focus on what matters—finding the perfect fit for your team.

## Overview

The **ResumeAI-Parser+** is a Streamlit-based application that allows users to upload multiple resumes in PDF or DOCX format and automatically extracts key details such as the candidate's name, education, work experience, and skills using OpenAI's GPT-3.5-turbo model. The extracted information is presented in a structured table format and can be exported to an Excel file for further analysis.

## Features

- **Supports Multiple File Formats**: Users can upload resumes in PDF and DOCX formats.
- **Automatic Information Extraction**: Uses OpenAI’s GPT-3.5-turbo model to extract information like name, education, work experience, and skills.
- **Structured Output**: Parsed and structured information is displayed in a user-friendly table format.
- **Excel Export**: Extracted resume data can be exported to an Excel file.
- **Downloadable Summary**: The generated Excel summary can be downloaded directly from the app.

## Requirements

- Python 3.7+
- Streamlit
- OpenAI Python package
- PyPDF2
- python-docx
- Pandas
- An OpenAI API key


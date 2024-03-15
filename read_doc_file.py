import docx2txt

academic_paper_file_location="prompts/achievements.docx"
academic_cv_file_location="prompts/academic_cv.docx"
requirements_details_location = "prompts/requirements.docx"

academic_paper = docx2txt.process(academic_paper_file_location)
academic_paper = " ".join(academic_paper.split())

academic_cv = docx2txt.process(academic_cv_file_location)
academic_cv=" ".join(academic_cv.split())

requirements_details = docx2txt.process(requirements_details_location)
requirements_details=" ".join(requirements_details.split())

academic_output = "This is the academic CV: \n" + academic_cv + "\n this is the academic published paper: \n" + academic_paper
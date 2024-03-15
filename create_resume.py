from openai import OpenAI
from helper.read_doc_file import academic_output, requirements_details
from helper.grammar_correction import grammarCorrector
from helper.gemma import gemma_prefix, gemma_suffix, gemma_generator
from input_files.instructions import instructions, review_instructions
from input_files.technical import technical_resume
from input_files.job_requirements import job_requirements
from input_files.motivation_guide import motivation_guide


client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")
gemma = gemma_generator(client=client)

Initial_prompt = gemma_prefix+f"""This is the technical background:\n {str(academic_output)} \n"""+\
    f"""## Instruction: {str(instructions)} and definitely answer in a way that the following questions are covered :\n{motivation_guide} """+"\nWrite a well written Motivation letter based on the following: \n" +  str(job_requirements) + str(requirements_details) +gemma_suffix
#+ """This is the technical background : \n {str(technical_resume)} \n """+


#Initial:
output=gemma.generate_text(Initial_prompt)
corrected_output = grammarCorrector(output)
with open("output_files/Output.txt", "w", encoding="utf-8") as text_file:
    text_file.write(corrected_output)

#Review:
print("Reviewing...")
review_prompt = gemma_prefix + review_instructions + output + gemma_suffix
reviewed_output = gemma.generate_text(review_prompt)
reviewed_output=grammarCorrector(reviewed_output)
with open("output_files/Output_reviewed.txt", "w", encoding="utf-8") as text_file:
    text_file.write(reviewed_output)
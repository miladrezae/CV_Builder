from openai import OpenAI
from read_doc_file import academic_output, requirements_details
from input_files.instructions import instructions
from input_files.technical import technical_resume
from input_files.job_requirements import job_requirements
from input_files.motivation_guide import motivation_guide
from grammar_correction import grammarCorrector

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")


final_prompt = f""" <start_of_turn>user: \nThis is the technical background:\n {str(academic_output)} \n"""+\
    f"""## Instruction: {str(instructions)} and definitely answer in a way that the following questions are covered :\n{motivation_guide} """+"\nWrite a well written Motivation letter based on the following: \n" +  str(job_requirements) + str(requirements_details) +"<end_of_turn>\n<start_of_turn>model\n"
#+ """This is the technical background : \n {str(technical_resume)} \n """+

completion = client.completions.create(
    model="gemma", # this field is currently unused
    prompt=final_prompt,

    temperature=0.3,
    stream=False,
)

output=completion.choices[0].text
corrected_output = grammarCorrector(output)

print(corrected_output)
with open("output_files/Output.txt", "w", encoding="utf-8") as text_file:
    text_file.write(corrected_output)

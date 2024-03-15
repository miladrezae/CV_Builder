from openai import OpenAI
from read_doc_file import academic_output, requirements_details
from input_files.instructions import instructions
from input_files.technical import technical_resume
from input_files.job_requirements import job_requirements


client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

history = [
    {"role": "system", "content": f""" This is the academic background:\n {str(academic_output)} \n
    This is the technical background : \n {str(technical_resume)} \n 
    ### Instruction: {str(instructions)} """},
    {"role": "user", "content": "Write a well written CV based on the following: \n" +  str(job_requirements) +"\n use the academic cv as format"},
]

final_prompt = f""" <start_of_turn>user: \nThis is the academic background:\n {str(academic_output)} \n
    This is the technical background : \n {str(technical_resume)} \n 
    ## Instruction: {str(instructions)} """+"\nWrite a well written CV based on the following: \n" +  str(job_requirements) + str(requirements_details) +"\n use the academic cv as format <end_of_turn>\n<start_of_turn>model\n"

# while True:
completion = client.completions.create(
    model="gemma", # this field is currently unused
    prompt=final_prompt,
    # messages=history,
    temperature=0.3,
    stream=False,
)

    # new_message = {"role": "assistant", "content": ""}
    
    # for chunk in completion:
    #     if chunk.choices[0].delta.content:
    #         print(chunk.choices[0].delta.content, end="", flush=True)
    #         new_message["content"] += chunk.choices[0].delta.content

    # history.append(new_message)
    
    # history.append({"role": "user", "content": input("> ")})
print(completion.choices[0].text)
with open("output_files/Output.txt", "w", encoding="utf-8") as text_file:
    text_file.write(completion.choices[0].text)

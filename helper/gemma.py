from openai import OpenAI


gemma_prefix="<start_of_turn>user: \n"
gemma_suffix="<end_of_turn>\n<start_of_turn>model\n"


class gemma_generator():
    def __init__(self, client: OpenAI) -> None:
        self.client = client

    def generate_text(self,message:str) -> str:
        gemma_message = gemma_prefix + message + gemma_suffix
        completion = self.client.completions.create(
        model="gemma", # this field is currently unused
        prompt=gemma_message,
        temperature=0.3,
        stream=False,
        )
        generated_response = completion.choices[0].text
        return str(generated_response)
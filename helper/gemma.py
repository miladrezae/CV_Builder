from openai import OpenAI
import tiktoken


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
        self.print_generation_info(message,completion)
        generated_response = completion.choices[0].text
        
        return str(generated_response)
    
    @staticmethod
    def print_generation_info(message,completion) -> None:
        number_of_tokens = completion.usage
        print(str(num_tokens_from_string(message, "cl100k_base"))+" Prompt Tokens!")
        print(number_of_tokens)
    

def num_tokens_from_string(string: str, encoding_name: str) -> int:
    encoding = tiktoken.get_encoding(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens

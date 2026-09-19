import os
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

llm = init_chat_model(
    model="deepseek-chat",
    model_provider="deepseek",
    temperature=0.7,
    api_key=os.getenv("DEEPSEEK_API_KEY")

)

def generate_pet_name():
    prompt_template_name = PromptTemplate()
    
    name = llm.invoke("I have a pet dog. Can you suggest five unique and creative name for my dog?")
    
    return name.content

if __name__ == "__main__":
    pet_name = generate_pet_name()
    print(pet_name)
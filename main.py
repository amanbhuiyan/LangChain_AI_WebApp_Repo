# from langchain.llms import OpenAI

# from langchain_community.llms import OpenAI

from langchain_openai import OpenAI
from dotenv import load_dotenv

from langchain.prompts import PromptTemplate
#from langchain_core.prompts import PromptTemplate

from langchain.chains import LLMChain

load_dotenv()

def generate_pet_name(animal_type):
    llm= OpenAI()

    prompt_template_name= PromptTemplate(
        input_variables=['animal_type'],
        template= "I have a dog {animal_type} and I want a cool name for it. Suggest me five cool name for my pet"

    )
    name=llm.invoke("I have a dog pet and I want a cool name for it. Suggest me five cool name for my pet")

    name_chain = LLMChain(llm=llm, prompt= prompt_template_name)

    # name_chain = llm | prompt_template_name
    response =name_chain({'animal_type': animal_type})
    return response

if __name__=="__main__":
    print(generate_pet_name("cat"))
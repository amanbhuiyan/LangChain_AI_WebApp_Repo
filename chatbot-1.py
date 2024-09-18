'''
Source: https://medium.com/@tahreemrasul/how-to-build-your-own-chatbot-with-langchain-and-openai-f092822b6ba6
'''

from langchain_openai import OpenAI
from langchain.chains import LLMChain
import prompts
from prompts import ice_cream_assistant_prompt_template
import streamlit as st

from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct',
             temperature=0)

llm_chain = LLMChain(llm=llm, prompt=ice_cream_assistant_prompt_template)
# chain = llm | ice_cream_assistant_prompt_template


def query_llm(question):
    outputResut = llm_chain.invoke({'question': question})['text']
    print(type(outputResut))
    return outputResut





if __name__ == '__main__':
<<<<<<< HEAD

    question= ""

    
    st.write("")
    st.title("This is your organisation's chatbot")
    print("___________________________________________")
  
    question= st.text_input("What is your question, related to  Ice-cream ?")
    print('\n')
    if question=="":
        st.write("")
    elif question!="":
        st.write(query_llm(question))

   

    
    
=======
    # question = "Who are you?"
    # question = "What is 2+2 ?"
    print("___________________________________________")
    question= input("What you want to know ?\n")
    print('\n')
    # question = "Ok please tell me what i need to make a vanila flavoured ice cream- thanks"
    query_llm(question)
    #print(prompts.testfunc())
>>>>>>> 424a6e7 (prompt to take input from user and some minor changes)

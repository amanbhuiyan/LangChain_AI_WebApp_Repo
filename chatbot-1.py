'''
Source: https://medium.com/@tahreemrasul/how-to-build-your-own-chatbot-with-langchain-and-openai-f092822b6ba6
'''

from langchain_openai import OpenAI
from langchain.chains import LLMChain
import prompts
from prompts import ice_cream_assistant_prompt_template

from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct',
             temperature=0)

llm_chain = LLMChain(llm=llm, prompt=ice_cream_assistant_prompt_template)
# chain = llm | ice_cream_assistant_prompt_template


def query_llm(question):
    print(llm_chain.invoke({'question': question})['text'])
    # print(chain.invoke({'question': question})['text'])


'''
if __name__ == '__main__':
    query_llm("Who are you?")

    '''


if __name__ == '__main__':
    # question = "Who are you?"
    question = "What is 2+2 ?"
    # question = "Ok please tell me what i need to make a vanila flavoured ice cream- thanks"
    query_llm(question)
    #print(prompts.testfunc())
from langchain_community.document_loaders import PyPDFLoader



loader= PyPDFLoader("C:/Everything/Projects/Python Projects/LagnChain_AI_Web_App/Data/magic.pdf",
                    )



docs= loader.load()


for doc in docs:
    print(doc.metadata)
    print(doc.page_content)
    print("------------------------------------------------------------------")










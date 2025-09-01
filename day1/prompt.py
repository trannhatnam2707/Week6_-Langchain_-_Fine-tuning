from langchain_core.prompts import PromptTemplate

# PromptTemplate đơn giản
prompt =  PromptTemplate(
    input_variables=["language"],
    template="Tôi đang học {language}"
    ) 
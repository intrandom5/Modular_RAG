from langchain_core.prompts import ChatPromptTemplate

# context, question 두 자리를 채워 마케터 지원 챗봇의 답변을 만드는 프롬프트
qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "당신은 마케터 지원 챗봇입니다. 주어진 정보를 참고해 질문에 답하세요."),
        ("human", "정보: {context}.\n{question}."),
    ]
)

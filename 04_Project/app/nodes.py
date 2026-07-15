from langchain_core.output_parsers import StrOutputParser

from .prompts import qa_prompt
from .state import GraphState


def make_retrieve_node(retriever):
    """retriever를 주입받아, 질문으로 벡터스토어를 검색해 documents를 채우는 노드를 만듭니다."""

    def retrieve(state: GraphState) -> GraphState:
        question = state["question"]
        documents = retriever.invoke(question)
        print(f"[retrieve] {len(documents)}개 문서 검색됨")
        return {"documents": documents}

    return retrieve


def make_generate_node(llm):
    """llm을 주입받아, 검색된 documents를 근거로 답변을 생성하는 노드를 만듭니다."""

    chain = qa_prompt | llm | StrOutputParser()

    def generate(state: GraphState) -> GraphState:
        question = state["question"]
        context = "\n".join(doc.page_content for doc in state["documents"])
        generation = chain.invoke({"context": context, "question": question})
        print("[generate] 답변 생성 완료")
        return {"generation": generation}

    return generate

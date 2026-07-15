from typing import List, TypedDict

from langchain_core.documents import Document


# 그래프 전체에서 공유되는 상태. 노드는 이 상태를 읽고, 일부 필드를 갱신해 반환합니다.
class GraphState(TypedDict):
    question: str
    documents: List[Document]
    generation: str

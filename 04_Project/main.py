from langchain_openai import ChatOpenAI

from app import config
from app.graph import build_graph
from app.retrieval import build_retriever


def build_llm() -> ChatOpenAI:
    # llm: 답변 생성 (embeddings는 app/retrieval.py에서 별도로 역할 분리)
    return ChatOpenAI(
        model=config.MODEL_NAME,
        base_url=config.BASE_URL,
        api_key=config.OPENAI_API_KEY,
        temperature=0,
    )


def save_graph_diagram(graph, path: str = "graph.png") -> None:
    """그래프 구조를 mermaid png로 저장합니다(주피터 없이도 CLI에서 확인 가능)."""
    png_bytes = graph.get_graph().draw_mermaid_png()
    with open(path, "wb") as f:
        f.write(png_bytes)
    print(f"[graph] 구조를 {path}에 저장했습니다.")


def main() -> None:
    retriever = build_retriever()
    llm = build_llm()
    graph = build_graph(retriever, llm)
    print("[준비 완료] graph가 준비되었습니다.")
    save_graph_diagram(graph)

    question = "키오스크 이용실태 조사에서 가장 주목할 만한 결과는 무엇인가요?"
    result = graph.invoke({"question": question})
    print("\n[답변]\n" + result["generation"])


if __name__ == "__main__":
    main()

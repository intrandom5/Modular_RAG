from langgraph.graph import END, START, StateGraph

from .nodes import make_generate_node, make_retrieve_node
from .state import GraphState


def build_graph(retriever, llm):
    """retriever와 llm을 주입받아 retrieve -> generate 흐름의 그래프를 구성합니다.
    새 단계를 추가하려면 nodes.py에 노드를 만들고 여기서 add_node/add_edge만 늘리면 됩니다.
    """
    workflow = StateGraph(GraphState)
    workflow.add_node("retrieve", make_retrieve_node(retriever))
    workflow.add_node("generate", make_generate_node(llm))

    workflow.add_edge(START, "retrieve")
    workflow.add_edge("retrieve", "generate")
    workflow.add_edge("generate", END)

    return workflow.compile()

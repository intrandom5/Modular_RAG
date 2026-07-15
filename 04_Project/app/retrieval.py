from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from . import config

embeddings = OllamaEmbeddings(model=config.EMBEDDING_MODEL)


def load_vectorstore() -> Chroma:
    """저장소 루트의 공유 vectorstore(../vectorstore)를 불러옵니다.
    비어 있으면(최초 실행) PDF를 청킹해 한 번만 채워 넣습니다.
    """
    vectorstore = Chroma(persist_directory=config.VECTORSTORE_DIR, embedding_function=embeddings)

    if vectorstore._collection.count() == 0:
        docs = PyPDFLoader(config.DATA_PATH).load()
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.CHUNK_SIZE, chunk_overlap=config.CHUNK_OVERLAP
        )
        splited_docs = splitter.split_documents(docs)
        vectorstore.add_documents(splited_docs)
        print(f"[ingest] {len(splited_docs)}개 청크를 새로 임베딩했습니다.")

    return vectorstore


def build_retriever(k: int = config.RETRIEVER_K):
    """벡터스토어를 불러와 상위 k개 문서를 반환하는 retriever를 만듭니다."""
    vectorstore = load_vectorstore()
    return vectorstore.as_retriever(search_kwargs={"k": k})

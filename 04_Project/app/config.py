import os

from dotenv import load_dotenv

load_dotenv()

# 04_Project/ 위치를 기준으로 저장소 루트를 계산해, 실행 위치(cwd)에 상관없이
# 모든 세션이 공유하는 data/, vectorstore/를 정확히 가리킵니다.
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_DIR = os.path.dirname(PROJECT_DIR)

DATA_PATH = os.path.join(ROOT_DIR, "data", "키오스크(무인정보단말기) 이용실태 조사.pdf")
VECTORSTORE_DIR = os.path.join(ROOT_DIR, "vectorstore")

EMBEDDING_MODEL = "qwen3-embedding:0.6b"
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 200
RETRIEVER_K = 4

MODEL_NAME = os.environ["MODEL_NAME"]
BASE_URL = os.environ["BASE_URL"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

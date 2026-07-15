# 준비 방법

1. anaconda 설치

2. visual studio code 설치

    2.1. visual studio code 익스텐션 설치
   
        - continue (AI code assistant)
   
        - jupyter notebook

4. 가상환경 만들고 requirements.txt 설치
```
conda create -n rag python=3.12
conda activate rag
pip install -r requirements.txt
```

4. ollama 설치
    3.1. 터미널에서 ollama serve로 ollama 앱/서버 띄우기.
    3.2. 터미널에서 ollama pull qwen3-embedding:0.6b로 임베딩 모델 pulling
    (선택) 3.3. 로컬 모델 pulling 해서 사용.

5. .env 파일 만들고, .env.sample의 내용 복사한 뒤 api key 채워넣기

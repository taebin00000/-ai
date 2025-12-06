try:
    from fastapi import FastAPI, UploadFile  # pyright: ignore[reportMissingImports]
except ImportError:
    raise ImportError('fastapi 패키지가 설치되어 있지 않습니다. 설치: pip install fastapi')

from modules.stt import speech_to_text
from modules.summarizer import summarize_text
from modules.weakness_analyzer import analyze_weakness
from modules.news_crawler import crawl_news
from modules.chatbot_ai import chatbot_ai_response

app = FastAPI()

# 정적 파일(index.html 등) 서빙 추가
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

# 현재 폴더 전체를 /static으로 공개
app.mount("/static", StaticFiles(directory=".", html=True), name="static")

# 루트 경로로 접속시 index.html 반환
@app.get("/")
def root():
    return FileResponse(os.path.abspath("index.html"))

@app.post("/lecture/summary/")
async def lecture_summary(audio: UploadFile):
    transcript = speech_to_text(audio)
    summary, keywords, topics = summarize_text(transcript)
    return {
        "transcript": transcript,
        "summary": summary,
        "keywords": keywords,
        "topics": topics
    }

@app.post("/user/weakness/")
async def user_weakness(user_id: str, wrong_answers: list):
    weakness_report = analyze_weakness(user_id, wrong_answers)
    return weakness_report

@app.get("/info/summary/")
async def info_summary(keyword: str):
    raw_texts = crawl_news(keyword)
    summary = summarize_text(" ".join(raw_texts))
    return {"summary": summary}

@app.post("/chat/ask/")
async def chat_ask(user_input: str):
    answer, related_links = chatbot_ai_response(user_input)
    return {"answer": answer, "recommendations": related_links}

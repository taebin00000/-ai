import whisper
import tempfile

model = whisper.load_model("base")  # base/small/medium/large 선택 가능

def speech_to_text(audio_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
        tmp.write(audio_file.file.read())
        tmp_path = tmp.name

    result = model.transcribe(tmp_path, language=None)  # 자동 언어 감지
    return result["text"]

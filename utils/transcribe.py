import os
import tempfile
import whisper
from moviepy import VideoFileClip
from pydub import AudioSegment

model = whisper.load_model("base")

def transcribe_file(file_path):
    ext = os.path.splitext(file_path)[-1].lower()
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        if ext in [".mp4", ".mkv", ".avi"]:
            video = VideoFileClip(file_path)
            audio = video.audio
            audio.write_audiofile(tmp.name)
        elif ext in [".mp3", ".ogg", ".wav"]:
            sound = AudioSegment.from_file(file_path)
            sound.export(tmp.name, format="wav")
        else:
            return "Formato não suportado"
        result = model.transcribe(tmp.name)
        return result["text"]

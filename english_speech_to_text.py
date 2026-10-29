import sounddevice as sd
from vosk import Model, KaldiRecognizer
import json
import os

SAMPLE_RATE = 16000        
DURATION = 5               
MODEL_PATH = "model"       

def recognize_english_sentence():
    if not os.path.exists(MODEL_PATH):
        return

    print("📦 Model yükleniyor...")
    model = Model(MODEL_PATH)
    recognizer = KaldiRecognizer(model, SAMPLE_RATE)

    print(f"🎤 Şimdi konuşabilirsin ({DURATION} saniye)...")
    audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    print("🧠 Ses işleniyor...")

    if recognizer.AcceptWaveform(audio.tobytes()):
        result_json = recognizer.Result()
        result = json.loads(result_json)
        text = result.get("text", "").strip()
        if text:
            print(f"📝 Tanınan cümle: {text}")
        else:
            print("🚫 Hiçbir şey algılanamadı.")
    else:
        print("🤔 Yeterli doğrulukta tanıma yapılamadı.")

if __name__ == "__main__":
    recognize_english_sentence()

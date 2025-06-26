import os
from TTS.api import TTS
from langdetect import detect

# ✅ Accept Coqui TOS
os.environ["COQUI_TOS_AGREED"] = "1"

# ✅ Load model
tts = TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False).to("cpu")

# ✅ Reference voices
SPEAKER_WAVS = {
    "British Male": "Voice/en_male.wav",
    "British Female": "Voice/en_female.wav",
    "Indian Male": "Voice/hi_male.wav",
    "Indian Female": "Voice/hi_female.wav"
}

# ✅ Create numbered filename if not provided
def get_output_filename(base=None):
    os.makedirs("output", exist_ok=True)
    if base:
        return f"output/output_{base}.wav"
    else:
        count = 1
        while os.path.exists(f"output/output_{count}.wav"):
            count += 1
        return f"output/output_{count}.wav"

def synthesize_speech(text: str, selected_voice: str, output_path: str):
    try:
        lang_code = detect(text)
        print(f"🌐 Detected Language: {lang_code}")
    except Exception as e:
        raise ValueError(f"Language detection failed: {e}")

    speaker_wav = SPEAKER_WAVS.get(selected_voice)
    if not speaker_wav or not os.path.isfile(speaker_wav):
        raise FileNotFoundError(f"Voice not found: {speaker_wav}")

    try:
        tts.tts_to_file(
            text=text.strip(),
            speaker_wav=speaker_wav,
            language=lang_code,
            file_path=output_path
        )
        print(f"\n✅ Audio saved to: {output_path}")
    except Exception as e:
        raise RuntimeError(f"Voice synthesis failed: {e}")

if __name__ == "__main__":
    print("🗣️ Multilingual Voice Synthesizer")

    input_type = input("\nChoose input type (text/file): ").strip().lower()

    if input_type == "file":
        file_path = input("Enter path to .txt file: ").strip()
        if not os.path.isfile(file_path):
            print("❌ File not found.")
            exit(1)
        with open(file_path, "r", encoding="utf-8") as f:
            text_input = f.read()
        filename_base = os.path.splitext(os.path.basename(file_path))[0]
    elif input_type == "text":
        text_input = input("Enter the text: ").strip()
        filename_base = None
    else:
        print("❌ Invalid input type.")
        exit(1)

    print("\nAvailable voices:")
    for voice in SPEAKER_WAVS:
        print(f"- {voice}")
    selected_voice = input("Select voice (type exactly): ").strip()
    if selected_voice not in SPEAKER_WAVS:
        print("❌ Invalid voice selection.")
        exit(1)

    output_path = get_output_filename(filename_base)
    synthesize_speech(text_input, selected_voice, output_path)

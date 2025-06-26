import os
from TTS.api import TTS

# ✅ Accept Coqui TOS to avoid prompt
os.environ["COQUI_TOS_AGREED"] = "1"

# ✅ Initialize the XTTS model from local path if already downloaded
model_path = "tts_models/multilingual/multi-dataset/xtts_v2"
tts = TTS(model_path)

# ✅ Input: Map language and gender to speaker reference WAVs
speaker_wavs = {
    "en_female": "Voice/en_female.wav",
    "en_male": "Voice/en_male.wav",
    "hi_female": "Voice/hi_female.wav",
    "hi_male": "Voice/hi_male.wav"
}

# ✅ User-defined text and settings
text = "Welcome to the multilingual speech synthesis demo."  # 👈 You can change this
lang = "en"       # "en" for English, "hi" for Hindi
gender = "female" # "female" or "male"

# ✅ Create speaker key and locate reference file
speaker_key = f"{lang}_{gender}"
speaker_wav = speaker_wavs.get(speaker_key)

# ✅ Sanity check: ensure reference file exists
if not os.path.isfile(speaker_wav):
    raise FileNotFoundError(f"Reference WAV file not found: {speaker_wav}")

# ✅ Create output folder
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# ✅ Output file name
output_path = os.path.join(output_dir, f"{speaker_key}_output.wav")

# ✅ Run XTTS inference and generate audio
tts.tts_to_file(
    text=text,
    speaker_wav=speaker_wav,
    language=lang,
    file_path=output_path
)

print(f"✅ Synthesized audio saved to: {output_path}")

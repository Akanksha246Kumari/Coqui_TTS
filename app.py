import os
import streamlit as st
from TTS.api import TTS
from langdetect import detect

# ✅ Coqui license agreement
os.environ["COQUI_TOS_AGREED"] = "1"

# ✅ Load model once
@st.cache_resource
def load_tts_model():
    return TTS(model_name="tts_models/multilingual/multi-dataset/xtts_v2", progress_bar=False).to("cpu")

tts = load_tts_model()

# ✅ Speaker reference voices (Make sure these .wav files exist)
SPEAKER_WAVS = {
    "British Male": "Voice/en_male.wav",
    "British Female": "Voice/en_female.wav",
    "Indian Male": "Voice/hi_male.wav",
    "Indian Female": "Voice/hi_female.wav"
}

# ✅ UI Header
st.title("🗣️ Multilingual Voice Synthesizer")
st.markdown("Upload text or type below. We'll detect the language and speak it in the accent you choose.")

# ✅ Input options
input_type = st.radio("Input Type", ["Text", "Text File"])
user_text = ""
filename_base = None

if input_type == "Text":
    user_text = st.text_area("Enter your text here", height=150)
else:
    uploaded_file = st.file_uploader("Upload .txt file", type=["txt"])
    if uploaded_file:
        user_text = uploaded_file.read().decode("utf-8")
        filename_base = os.path.splitext(uploaded_file.name)[0]

# ✅ Detect language
language_detected = ""
if user_text.strip():
    try:
        lang_code = detect(user_text)
        language_detected = lang_code
        st.info(f"🌐 Auto Detected Language: **{lang_code}**")
    except:
        st.warning("⚠️ Unable to detect language. Please try again.")

# ✅ Voice Accent
selected_voice = st.selectbox("🎙️ Choose Voice Accent + Gender", list(SPEAKER_WAVS.keys()))
speaker_wav = SPEAKER_WAVS[selected_voice]

# ✅ Generate Output Filename
def get_output_filename(base=None):
    os.makedirs("output", exist_ok=True)
    if base:
        return f"output/output_{base}.wav"
    else:
        count = 1
        while os.path.exists(f"output/output_{count}.wav"):
            count += 1
        return f"output/output_{count}.wav"

# ✅ Generate Button
if st.button("Generate Voice 🎧"):
    if not user_text.strip():
        st.warning("❗Please enter some text or upload a file.")
    else:
        output_path = get_output_filename(filename_base)

        try:
            tts.tts_to_file(
                text=user_text.strip(),
                speaker_wav=speaker_wav,
                language=language_detected,
                file_path=output_path
            )
            st.success("✅ Audio generated successfully!")

            audio_bytes = open(output_path, "rb").read()
            st.audio(audio_bytes, format="audio/wav")

            st.download_button(
                label="⬇️ Download Audio",
                data=audio_bytes,
                file_name=os.path.basename(output_path),
                mime="audio/wav"
            )
        except Exception as e:
            st.error(f"❌ Error: {e}")

# Multilingual Voice Synthesizer using XTTS

This project allows you to generate **realistic multilingual speech** from text input using the `xtts_v2` model by Coqui AI. You can input either direct text or upload a text file and generate speech in **different accents and genders**, such as British or Indian (Male/Female). It supports **language auto-detection**, and the final output is saved as a `.wav` file.

---

## Features

* ✔️ Supports direct text or `.txt` file input
* ✔️ Auto-detects language from input text
* ✔️ Choose from multiple voice accents and genders
* ✔️ Outputs high-quality audio (`.wav`)
* ✔️ Supports Streamlit UI and CLI (command-line) mode
* ✔️ Automatically names output files to avoid overwrite

---

## Project Structure

```
.
├── Voice/                 # Reference speaker audio files (manually added)
│   ├── en_male.wav
│   ├── en_female.wav
│   ├── hi_male.wav
│   └── hi_female.wav
├── output/                # Auto-generated speech audio files
├── model/                 # Downloaded XTTS model (auto-downloaded by script)
├── api.py                 # CLI interface to run TTS from terminal
├── app.py                 # Streamlit UI for interactive use
├── synthesizer.py         # Wrapper for generating audio from text + speaker
├── requirements.txt       # Python package dependencies
├── .gitignore             # Git ignore rules
└── README.md              # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/tts-multilingual.git
cd tts-multilingual
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # For macOS/Linux
# OR
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📂 Manual Setup

### 4. Add Voice Samples (REQUIRED)

Create a folder named `Voice/` in the root directory and add the following `.wav` files:

| Voice Label    | File Name       |
| -------------- | --------------- |
| British Male   | `en_male.wav`   |
| British Female | `en_female.wav` |
| Indian Male    | `hi_male.wav`   |
| Indian Female  | `hi_female.wav` |

Place all these files inside the `Voice/` folder.

> These are reference voices used for accent and gender mimicry by XTTS.

---

## Usage

### Option 1: Run with Streamlit UI

```bash
streamlit run app.py
```

* Choose input type: Text or File
* Select voice (e.g., Indian Male)
* It auto-detects the language and generates speech
* Download or play the `.wav` output

### Option 2: Run via CLI (Terminal)

```bash
python api.py
```

You’ll be prompted:

```
Choose input type (text/file): text
Enter the text: Hello world!
Available voices:
- British Male
- British Female
- Indian Male
- Indian Female
Select voice (type exactly): Indian Male
```

### Output File Naming

* For text file input: If file is `bonjour.txt`, output is `output_bonjour.wav`
* For direct text input: Outputs as `output_1.wav`, `output_2.wav`, etc., without overwriting

---

## Powered By

* [Coqui TTS (XTTS v2)](https://github.com/coqui-ai/TTS)
* [langdetect](https://pypi.org/project/langdetect/)
* [Streamlit](https://streamlit.io/)

---

## Notes

* The model is **auto-downloaded** the first time you run it.
* The `Voice/` and `output/` folders are **excluded from GitHub** via `.gitignore`.
* Do **not commit** large `.wav` files or models to GitHub.
* Works best on **Python 3.10**, **macOS ARM** or **Linux systems**.
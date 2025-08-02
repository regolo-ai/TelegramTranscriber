# TelegramTranscriber
[![License](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](http://www.gnu.org/licenses/gpl-3.0)   

A Telegram bot that transcribes voice messages using FasterWhipser model.

<img width="422" height="480" alt="Image" src="https://github.com/user-attachments/assets/a6520069-cfda-474e-9c9a-3f91da42be05" />

## Features

- ✅ Transcribes Telegram voice messages (OGG/OPUS format)
- 🎧 Uses Regolo.ai `faster-whisper-large-v3` model (but can change model and AI inference provider)
- 🔐 Securely loads API keys via `.env`
- 🗑️ Automatically deletes audio files after processing

---

## Requirements

- Python 3.8+
- [Telegram Bot Token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token)
- Regolo.AI API key (or your inference provider)

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/regolo-ai/TelegramTranscriber.git
cd TelegramTranscriber
```
### 2. Create and activate a virtual environment

```
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set up environment variables

Copy the `.env-example` file to `.env` with your keys.

### 5. Run

```
python bot.py
```

---

## Docker Setup (Alternative)

### 1. Build the Docker image

```bash
docker build -t telegram-transcriber .
```

### 2. Run with Docker

```bash
docker run -d --name telegram-transcriber telegram-transcriber
```

**Note:** Make sure your `.env` file is properly configured before building the image.

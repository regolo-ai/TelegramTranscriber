#!/usr/bin/env python
import logging
import json
import openai
import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)
from dotenv import load_dotenv
load_dotenv()
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN", '')
openai.api_key = os.getenv("HOST_API", '')
openai.base_url = os.getenv("API_KEY", "")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi, share the vocal to transcribe it!")


async def transcribe(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.voice:
        await update.message.reply_text("Please, share a vocal message.")
        return

    voice = update.message.voice
    file = await context.bot.get_file(voice.file_id)
    file_path = "/tmp/audio.ogg"
    await file.download_to_drive(file_path)

    try:
        with open(file_path, "rb") as audio_file:
            transcription = openai.audio.transcriptions.create(
                model="faster-whisper-large-v3",
                file=audio_file,
                response_format="text"
            )
        await update.message.reply_text(transcription)

    except Exception as e:
        logging.exception("Transcription error")
        await update.message.reply_text(f"Transcription error: {e}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.VOICE, transcribe))

    logger.info("Bot started...")
    app.run_polling()

if __name__ == '__main__':
    main()

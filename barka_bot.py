import discord
from discord.ext import commands
from discord import app_commands
import datetime
import asyncio
import os
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)

load_dotenv()
GUILD_ID = int(os.getenv('GUILD_ID'))
VOICE_CHANNEL_ID = int(os.getenv('VOICE_CHANNEL_ID'))
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

logging.info(f'GUILD_ID {GUILD_ID}')
logging.info(f'VOICE_CHANNEL_ID {VOICE_CHANNEL_ID}')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sound_file = os.path.join(BASE_DIR, "barka.mp3")
audio_source = discord.FFmpegPCMAudio(sound_file)


intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    logging.info(f'Logged as {bot.user.name}')
    guild = bot.get_guild(GUILD_ID)
    if not guild:
        logging.warning("No server found.")
        return
    channel = bot.get_channel(VOICE_CHANNEL_ID)


    if channel and isinstance(channel, discord.VoiceChannel):
        voice_client  = await channel.connect()
        logging.info(f"Bot joined channel: {channel.name}")
        if voice_client.is_connected():
            audio_source = discord.FFmpegPCMAudio(sound_file, executable='ffmpeg')
            
            def after_playing(error):
                if error:
                    logging.error(f"Error while playing music: {error}")
                coro = voice_client.disconnect()
                fut = asyncio.run_coroutine_threadsafe(coro, bot.loop)

                coro_close = bot.close()
                fut_close = asyncio.run_coroutine_threadsafe(coro_close, bot.loop)

                try:
                    fut.result()
                    logging.info("Bot disconected.")
                    fut_close.result()
                    logging.info("Bot closed.")
                except Exception as e:
                    logging.error(f"Error while disconecting: {e}")
            
            voice_client.play(audio_source, after=after_playing)
        
    else:
        logging.info("Voice channel not found.")


bot.run(DISCORD_BOT_TOKEN)
logging.info("program end")

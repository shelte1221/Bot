s = 0
for i in range(10):
    s += i
s += s

from asyncio.windows_events import NULL
from typing import ClassVar
import discord
from discord import message
from discord import user
from discord import player
from discord.channel import VoiceChannel
from discord.client import Client
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import sleep_until
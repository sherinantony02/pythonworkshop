import asyncio
from config import*
from telethon import TelegramClient,events
async def main():
	bot= await TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
	async with bot:
		print("signed in")
		
		@bot.on(events.NewMessage())
		async def handle_message(message):
			await message.reply("hello")
		await bot.run_until_disconnected()
asyncio.run(main())

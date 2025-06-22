# Barka-Discord-bot
A Discord bot that plays the song 'Barka' every day at 21:37.


### Instruction

Step 1: Create a Bot Account 
As first step You need to create `Bot Account`, to do so please follow this instruction:
 https://discordpy.readthedocs.io/en/stable/discord.html

 After creating the bot, obtain the bot token and generate an invite URL using the OAuth2 tab.


Step 2: Create a `.env` file

You need to add `.env` file to project directory, then add following rows:

```
GUILD_ID=xxx              # Replace with your Server ID
VOICE_CHANNEL_ID=xxx      # Replace with the target Voice Channel ID
DISCORD_BOT_TOKEN=xxx     # Replace with your Bot Token
```


### Running

To run discord bot execute following commands:

1. Build Docker iamge:
```bash
docker build -t discord-bot .
```

2. Run Docker container:
```bash
docker run -d --restart always --name discord-bot discord-bot
```
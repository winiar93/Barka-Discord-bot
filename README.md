# Barka-Discord-bot
A Discord bot that plays the song 'Barka' every day at 21:37.


### Instruction

You need to add `.env` file to project directory, then add following rows:

```
GUILD_ID = xxx
VOICE_CHANNEL_ID = xxx
DISCORD_BOT_TOKEN = xxx
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
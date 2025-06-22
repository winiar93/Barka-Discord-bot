FROM python:3.11-slim

# Install ffmpeg and all packets
RUN apt-get update && apt-get install -y ffmpeg cron && rm -rf /var/lib/apt/lists/*


# Set working directory
WORKDIR /usr/src/app

# Copy file with python requirements
COPY requirements.txt ./

# Install python lib from requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy all other files
COPY . .

# Copy crontab file and add scheduler
COPY crontab /etc/cron.d/discord-bot-cron
RUN chmod 0644 /etc/cron.d/discord-bot-cron
RUN crontab /etc/cron.d/discord-bot-cron

CMD ["cron", "-f"]

FROM python:3.11-slim

# Zainstaluj ffmpeg i inne potrzebne pakiety
RUN apt-get update && apt-get install -y ffmpeg cron && rm -rf /var/lib/apt/lists/*


# Ustaw katalog roboczy
WORKDIR /usr/src/app

# Skopiuj plik z zależnościami
COPY requirements.txt ./

# Zainstaluj pakiety Pythona
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztę plików aplikacji
COPY . .

COPY crontab /etc/cron.d/discord-bot-cron

RUN chmod 0644 /etc/cron.d/discord-bot-cron

RUN crontab /etc/cron.d/discord-bot-cron

CMD ["cron", "-f"]

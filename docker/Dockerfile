# Użyj obrazu bazowego Python 3.8
FROM python:3.11

# Ustaw katalog roboczy na /app
WORKDIR /app

# Skopiuj zawartość bieżącego katalogu do /app w kontenerze
COPY . /app

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Wyeksponuj port 5000
EXPOSE 5000

# Uruchom aplikację po uruchomieniu kontenera
CMD ["python", "main.py"]

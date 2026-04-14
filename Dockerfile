# Imagen base: Python 3.11 mínima (slim = sin paquetes innecesarios)
FROM python:3.11-slim
# Directorio de trabajo dentro del contenedor
WORKDIR /app
# Copiar e instalar dependencias primero (aprovecha la caché de Docker)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Copiar el resto del código
COPY . .
# Puerto que expone el contenedor
EXPOSE 5000
# Comando que se ejecuta al iniciar el contenedor
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "app:app"]
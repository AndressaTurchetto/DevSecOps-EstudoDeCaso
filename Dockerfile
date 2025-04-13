FROM python:3.10

# Define o diretório de trabalho
WORKDIR /app

# Copia e instala dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos do projeto
COPY . .

# Expõe a porta usada pelo Flask
EXPOSE 8080

# Executa o app diretamente com Python
CMD ["python", "run.py"]

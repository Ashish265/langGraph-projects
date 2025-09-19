FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["streamlit","run" ,"src/app.py","--server.port=8000","--server.address=0.0.0.0"]

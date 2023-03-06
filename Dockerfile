FROM python:3.7
RUN mkdir /app
WORKDIR /app/
COPY src/app.py .
COPY src/resources/requirements.txt .

RUN pip install -r requirements.txt
CMD ["python", "app.py"]
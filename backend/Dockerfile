FROM python:3.9.19-slim
RUN mkdir /App
WORKDIR /App
COPY . .
RUN pip install -r requirements.txt
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]


FROM python:3.14 
WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app 
EXPOSE 8000
ENV BACKGROUND_COLOR=red 

ENTRYPOINT ["python","manage.py","runserver"]
CMD ["0.0.0.0:8000"]
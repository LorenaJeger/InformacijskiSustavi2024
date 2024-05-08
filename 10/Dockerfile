FROM python:3.9.16-slim-buster
WORKDIR app/
COPY requirements.txt req.txt
RUN pip3 install -r req.txt 
COPY . . 
EXPOSE 8080
CMD ["python3", "app.py"]
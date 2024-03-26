FROM python

RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app/
COPY main.py /app/

RUN pip3 install -r requirements.txt
CMD ["python3", "main.py"]

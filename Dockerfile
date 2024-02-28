FROM python:3.7
WORKDIR /app
ENV TZ=Europe/Moscow
COPY python_example_api/* /app/

RUN pip3 install --no-cache-dir -r requirements.txt

CMD [ "python3", "./app.py" ]
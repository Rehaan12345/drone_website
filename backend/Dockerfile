FROM python:3.9

WORKDIR /code

ENV HOST 0.0.0.0

COPY requirements.txt /code/requirements.txt

RUN pip3 install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip3 install fastapi uvicorn

COPY . /code/app

# Set environment variable for the port
ENV PORT=8080

# Expose the port
EXPOSE $PORT

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
FROM python:latest
RUN apt update
RUN apt install python3-pip -y
WORKDIR /gun_gen_2
COPY . .
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python3","app.py"]
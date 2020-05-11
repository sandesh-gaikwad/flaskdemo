FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install -y python3 python3-dev python3-pip 
RUN apt-get install -y vim
RUN pip3 install -y curl
COPY ./ ./app
WORKDIR ./app
RUN pip3 install -r requirements.txt
EXPOSE 5000
#ENTRYPOINT [ "python3" ]
CMD [ "python3" "app.py" ]

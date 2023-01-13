FROM ubuntu:18.04
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y python-pip && \
    apt-get install -y python && \
    apt-get -y dist-upgrade
RUN export FLAG='ShaastraCTF{Dev_t001s_are_dan9ger0u5_t0_u5e}'    
RUN readonly FLAG
WORKDIR /app
RUN pip install flask
RUN pip install flask_sqlalchemy
RUN pip install requests
RUN pip install virtualenv
RUN pip install python-dotenv
RUN pip install virtualenvwrapper-win
COPY . .


CMD ["flask","run"] 


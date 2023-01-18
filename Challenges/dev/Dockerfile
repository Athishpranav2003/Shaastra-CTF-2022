FROM python:3.9-slim-buster
RUN mkdir /secret
COPY ./secret.txt /secret
RUN chmod +r /secret



RUN useradd -ms /bin/bash ctf
RUN chown ctf /home
USER ctf
WORKDIR /home/ctf
COPY ./app /home/ctf





RUN cd /home/ctf/
RUN pip install -r requirements.txt
RUN pip install virtualenvwrapper-win
RUN pip install virtualenvwrapper
RUN export FLAG=search_for_secret
RUN export FLASK_APP=app.py
RUN export FLASK_ENV=development
USER root
RUN chown -R ctf:ctf /home
USER ctf


CMD ["python3","-m","flask","run","--host", "0.0.0.0"] 
EXPOSE 5000

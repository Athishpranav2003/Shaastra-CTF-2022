FROM python:3.9-slim-buster
WORKDIR /app

RUN export FLAG='ShaastraCTF{Dev_t001s_are_dan9ger0u5_t0_u5e}'    
RUN readonly FLAG
COPY . /app
RUN pip install -r requirements.txt
RUN pip install virtualenvwrapper-win
RUN pip install virtualenvwrapper

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD ["flask","run","--host", "0.0.0.0"] 
EXPOSE 5000

FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY . /usr/src/app


RUN pip install --no-cache-dir -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate --noinput
RUN python manage.py initadmin


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
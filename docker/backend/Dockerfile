FROM python:3.8.10-slim

WORKDIR /usr/src/app
COPY ./backend/moviesapi .
COPY ./backend/requirements.txt .

RUN pip install --upgrade pip && \
    pip install gunicorn && \
    pip install -r requirements.txt && \
    apt update --allow-unauthenticated --allow-insecure-repositories && \
    apt install -y curl wget

# Remove trailing slashes from dj_rest_auth package
RUN sed -i "s|path('login/'|path('login'|" /usr/local/lib/python3.8/site-packages/dj_rest_auth/urls.py
RUN sed -i "s|path('logout/'|path('logout'|" /usr/local/lib/python3.8/site-packages/dj_rest_auth/urls.py
RUN sed -i "s|path('user/'|path('user'|" /usr/local/lib/python3.8/site-packages/dj_rest_auth/urls.py

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

ENTRYPOINT ["/bin/sh"]
# CMD ["-c", "gunicorn moviesapi.wsgi --bind=0.0.0.0:8000 --reload --workers=2 --threads=2 --timeout=120 --log-level=Debug"]

# For Cloud Run, as we use less resources.
CMD ["-c", "gunicorn moviesapi.wsgi --bind=0.0.0.0:8000 --reload --workers=1 --threads=1 --timeout=120 --log-level=Debug"]
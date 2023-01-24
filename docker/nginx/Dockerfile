# Build React static files
FROM node:13.12.0-alpine as BUILD

WORKDIR /app
COPY ./frontend/ /app
RUN npm ci --silent
RUN npm run build


# Copy React static files and start nginx
FROM nginx:1.23-alpine

COPY --from=BUILD /app/build /usr/share/nginx/html
COPY ./backend/moviesapi/django_static /usr/src/static
COPY ./docker/nginx/templates /etc/nginx/templates

CMD ["nginx", "-g", "daemon off;"]
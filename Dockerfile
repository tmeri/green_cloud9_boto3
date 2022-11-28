#Week 16 Docker Procjet


FROM nginx
COPY index.html /usr/share/nginx/html
EXPOSE 8080

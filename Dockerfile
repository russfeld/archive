FROM nginx:alpine
COPY nginx/default.conf /etc/nginx/conf.d/default.conf
COPY . /usr/share/nginx/html
RUN rm -rf /usr/share/nginx/html/nginx /usr/share/nginx/html/tools /usr/share/nginx/html/Dockerfile \
           /usr/share/nginx/html/README.md /usr/share/nginx/html/.github

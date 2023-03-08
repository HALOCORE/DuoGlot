FROM nginx:1.21.6
RUN apt-get update && apt-get install -y net-tools iputils-ping htop
FROM node:lts-alpine
LABEL authors="Michael"

# install simple http server for serving static content
RUN npm install -g http-server

RUN npm i -g vue@latest

RUN apk --no-cache add curl

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'package-lock.json' (if available)
COPY package*.json ./

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN npm run build

CMD [ "http-server", "dist" ]
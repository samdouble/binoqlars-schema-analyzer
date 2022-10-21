FROM node:18.11.0-alpine

WORKDIR /analyzer
COPY . /analyzer
RUN npm install && npm run build

RUN ["node", "build/index.js"]
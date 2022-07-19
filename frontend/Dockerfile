FROM node:14-alpine
WORKDIR /app
ADD . /app/
RUN npm install
CMD ["npm", "run", "serve", "--", "--host", "--port", "80"]

FROM node:14-alpine
WORKDIR /app
ADD . /app/
RUN npm ci
CMD ["npm", "run", "serve", "--", "--host", "--port", "80"]

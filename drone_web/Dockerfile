# This dockerfile must be built with the monorepo root directory as cwd
FROM node:lts-alpine

WORKDIR /drone_web

#all files needed for the build
COPY package.json .
COPY package-lock.json .
COPY svelte.config.js .
COPY vite.config.js .

#all folders needed for the build
COPY . .

RUN npm i
RUN npm install -g sirv-cli

EXPOSE 3000

ENV NODE_ENV=production

CMD ["npm", "run", "build"]
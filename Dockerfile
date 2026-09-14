FROM plone/frontend-builder:18 AS builder
COPY . /app
WORKDIR /app
RUN yarn install --frozen-lockfile --ignore-engines --network-timeout 600000 --network-concurrency 1
RUN yarn build

FROM node:18-alpine
COPY --from=builder /app /app
WORKDIR /app
ENTRYPOINT ["yarn", "start:prod"]
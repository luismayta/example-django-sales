FROM dgnest/node:6.10.0
MAINTAINER Luis Mayta <@slovacus>

COPY Gemfile /app/Gemfile
COPY package.json /app/package.json

WORKDIR /app

RUN cd /app/ \
    && npm install \
    && bundle install \
    && npm install --global gulp \
    && npm install --global gulp-cli

COPY . /app

CMD ["gulp"]

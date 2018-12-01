FROM ruby:2.3.0-alpine

RUN apk update && \
    apk add build-base openssl

RUN mkdir /ruboty
ADD Gemfile /ruboty
ADD Gemfile.lock /ruboty
ADD .env /ruboty
WORKDIR /ruboty

RUN bundle install --path vendor/bundle

CMD ["bundle", "exec", "ruboty", "--dotenv"]

FROM python:3.8-slim-buster

ENV HOST='hb_model'
ENV PORT='1240'
ENV TOKEN="TOKEN"

#EXPOSE 1240

RUN pip3 install pyTelegramBotAPI

COPY tlg_bot.py .

CMD python tlg_bot.py
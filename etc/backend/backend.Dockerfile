FROM python:3.9-slim

ARG APP_USER=room_booking
ARG APP_GROUP=room_booking

RUN groupadd $APP_GROUP && useradd -m -s /bin/bash -g $APP_GROUP $APP_USER

ENV APP_HOME=/home/$APP_USER/app
WORKDIR $APP_HOME

RUN apt-get update 

COPY  src/requirements/dev.txt ./requirements/dev.txt
RUN pip install --no-cache -r requirements/dev.txt

COPY src .

COPY ./etc/backend/wait-for-it.sh ./etc/backend/entrypoint.sh ./

RUN chown -R $APP_USER:$APP_GROUP $APP_HOME

USER $APP_USER

ENTRYPOINT ["./entrypoint.sh"]

CMD ["uvicorn", "room_booking.main:app", "--reload", "0.0.0.0:8014"]

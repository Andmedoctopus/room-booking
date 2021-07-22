FROM python:3.9-buster

ARG APP_USER=room_booking
ARG APP_GROUP=room_booking

RUN apt-get update && \
    apt-get install -y netcat # for wait-for-it script

RUN groupadd $APP_GROUP && useradd -m -s /bin/bash -g $APP_GROUP $APP_USER

ENV APP_HOME=/home/$APP_USER
WORKDIR $APP_HOME

RUN chown -R $APP_USER:$APP_GROUP $APP_HOME
USER $APP_USER
ENV PATH="$PATH:$APP_HOME/.local/bin"

COPY  src/requirements ./requirements
RUN pip install --user --no-cache pip==21.1.3 -r requirements/dev.txt

COPY src ./etc/backend/wait-for-it.sh ./etc/backend/entrypoint.sh ./


ENTRYPOINT ["./entrypoint.sh"]
CMD ["uvicorn", "room_booking.webapp:app", "--reload"]

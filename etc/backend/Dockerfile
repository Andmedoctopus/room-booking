FROM python:3.9-buster

ARG APP_USER=room_booking\
    APP_GROUP=room_booking

ENV APP_HOME=/home/$APP_USER \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.13

RUN apt-get update && \
    apt-get install -y \
    netcat \
    libpq-dev python-dev

RUN groupadd $APP_GROUP && useradd -m -s /bin/bash -g $APP_GROUP $APP_USER

WORKDIR $APP_HOME

RUN chown -R $APP_USER:$APP_GROUP $APP_HOME
USER $APP_USER
ENV PATH="$PATH:$APP_HOME/.local/bin:$APP_HOME"

RUN pip install -U pip && pip install "poetry==$POETRY_VERSION"

COPY --chown=$APP_USER ./poetry.lock ./pyproject.toml ./
RUN poetry config virtualenvs.create false && poetry install

COPY src ./etc/backend/wait-for-it.sh ./etc/backend/entrypoint.sh tox.ini ./

ENTRYPOINT ["./entrypoint.sh"]

CMD ["uvicorn", "--factory", "room_booking.webapp:create_app", "--reload", "--host", "0.0.0.0", "--port", "5050"]

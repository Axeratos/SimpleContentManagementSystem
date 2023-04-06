FROM python:3.10

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/workdir
ARG USER=user

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER} requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chown=${USER} ./app app

USER ${USER}

EXPOSE 5000

CMD ["python3", "app/main.py"]

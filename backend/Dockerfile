FROM python:3.9-slim
LABEL authors="Michael"

RUN apt-get -q -y update

ENV USERNAME=backend
ENV WORKING_DIR=/home/backend

WORKDIR ${WORKING_DIR}

COPY requirements.txt .
COPY *.py .

RUN groupadd ${USERNAME} && \
    useradd -g ${USERNAME} ${USERNAME}

RUN chown -R ${USERNAME}:${USERNAME} ${WORKING_DIR}
RUN chmod -R u=rwx,g=rwx ${WORKING_DIR}

USER ${USERNAME}
ENV PATH "$PATH:/home/${USERNAME}/.local/bin"

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
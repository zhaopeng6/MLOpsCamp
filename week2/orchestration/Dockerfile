FROM python:3.10
COPY ./requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         vim \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"


COPY decision_trees /opt/program

WORKDIR /opt/program

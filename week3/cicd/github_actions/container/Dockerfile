FROM python:3.10
COPY ./requirements.txt ./requirements.txt
COPY decision_trees /opt/program
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN apt-get -y update && apt-get install -y --no-install-recommends \
         wget \
         nginx \
         ca-certificates \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE
ENV PATH="/opt/program:${PATH}"

WORKDIR /opt/program

CMD ["serve"]

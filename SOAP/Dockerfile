FROM python:3.10
ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirements.txt /code/requirements.txt
COPY soap /code

RUN pip install -r requirements.txt

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/usr/bin/env", "bash", "/docker-entrypoint.sh"]
CMD ["soap"]

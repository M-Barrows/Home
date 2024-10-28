FROM python:3.10-slim

COPY ./src/requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./src /app
WORKDIR /app

ENV OTEL_RESOURCE_ATTRIBUTES=service.name=codecoffee-home 
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://192.168.1.102:4317" 
ENV OTEL_EXPORTER_OTLP_PROTOCOL=grpc 
ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
ENV OTEL_LOGS_EXPORTER=otlp
EXPOSE 8000

CMD ["opentelemetry-instrument", "gunicorn", "--config", "gunicorn.config.py", "app:app"]

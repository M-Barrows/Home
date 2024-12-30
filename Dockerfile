FROM python:3.10-slim

# Install curl 
RUN apt-get update && \ 
    apt-get install -y curl unzip && \ 
    rm -rf /var/lib/apt/lists/*

COPY ./src/requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY ./src /app
WORKDIR /app

# Create a temporary directory for downloading the zip file 
RUN mkdir -p /tmp/highlightjs 

# Download the zip file with curl 
RUN curl -X POST https://highlightjs.org/api/download \
    -H "Content-Type: application/json" \ 
    -o '/tmp/highlightjs/highlightjs.zip' \
    -d '{"api":2,"languages":["makefile","bash","csharp","css","diff","go","graphql","ini","java","javascript","json","less","lua","makefile","markdown","php-template","php","plaintext","python-repl","python","r","scss","shell","sql","typescript","wasm","xml","yaml","dns","dockerfile","ini","nginx","yaml","css","less","scss","pgsql","sql","excel","java","lua","gcode","latex","markdown","json","r","bash","javascript","lua","powershell","typescript","go","css","graphql","javascript","json","less","nginx","scss","wasm","xml"]}' 

# Unzip the contents to the desired directory 
RUN unzip /tmp/highlightjs/highlightjs.zip -d ./static/

# Remove temp directory
RUN rm -rf /tmp/highlightjs

ENV OTEL_RESOURCE_ATTRIBUTES=service.name=codecoffee-home 
ENV OTEL_EXPORTER_OTLP_ENDPOINT="http://192.168.1.102:4317" 
ENV OTEL_EXPORTER_OTLP_PROTOCOL=grpc 
ENV OTEL_PYTHON_LOGGING_AUTO_INSTRUMENTATION_ENABLED=true
ENV OTEL_LOGS_EXPORTER=otlp
EXPOSE 8000

CMD ["opentelemetry-instrument", "gunicorn", "--config", "gunicorn.config.py", "app:app"]

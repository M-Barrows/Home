# Code And Coffee Blog
This is the main repo that I use to update my personal blog at [https://codecoffee.org](https://blog.codecoffee.org).

How to run the site 
```bash
OTEL_RESOURCE_ATTRIBUTES=service.name=codecoffee-home OTEL_EXPORTER_OTLP_ENDPOINT="http://192.168.1.102:4317" OTEL_EXPORTER_OTLP_PROTOCOL=grpc opentelemetry-instrument flask run
```


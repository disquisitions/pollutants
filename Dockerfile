# Base Image
FROM python:3.11.7-bookworm

# pip
RUN pip install --upgrade pip

# If the steps of a `Dockerfile` use files that are different from the `context` file, COPY the
# file of each step separately; and RUN the file immediately after COPY
WORKDIR /app
COPY requirements.txt /app
RUN pip install --requirement /app/requirements.txt --no-cache-dir && mkdir /app/warehouse && \
    mkdir /app/resources

# Specific COPY
COPY src /app/
COPY resources/s3_parameters.yaml /app/resources/
COPY config.py /app/config.py

# Port
EXPOSE 8050

# Create mountpoint
VOLUME /app/warehouse

# ENTRYPOINT
ENTRYPOINT ["python"]

# CMD
CMD ["src/main.py"]
# Base Image
FROM python:3.11.7-bookworm

# If the steps of a `Dockerfile` use files that are different from the `context` file, COPY the
# file of each step separately; and RUN the file immediately after COPY
WORKDIR /app
COPY .devcontainer/requirements.txt /app
RUN adduser --system --home /home/reader reader && pip install --upgrade pip && \
    pip install --requirement /app/requirements.txt --no-cache-dir

# Specific COPY
COPY src /app/src
COPY resources /app/resources
COPY config.py /app/config.py

# Reader
USER reader

# Port
EXPOSE 8050

# Create mountpoint
RUN mkdir /app/warehouse
VOLUME /app/warehouse

# ENTRYPOINT
ENTRYPOINT ["python"]

# CMD
CMD ["src/main.py"]
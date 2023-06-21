# Use a lightweight Linux distribution as the base image
FROM alpine:latest

# Install necessary dependencies
RUN apk update && \
    apk add --no-cache python3 && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt .
COPY ddns.py .
COPY .env .

# Install the dependencies from requirements.txt
RUN pip3 install -r requirements.txt

# Copy the ddns.py file to the container


# Run the ddns.py script
CMD ["sh", "-c", "python3 ddns.py && exit"]

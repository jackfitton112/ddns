#Use a lightweight Python base image
FROM python:3-alpine

# Install python-dotenv
RUN pip install python-dotenv requests

# Copy the ddns.py file to the container
COPY ddns.py /app/ddns.py

WORKDIR /app

# Run the ddns.py script and then exit with code 0
CMD ["python", "ddns.py"]















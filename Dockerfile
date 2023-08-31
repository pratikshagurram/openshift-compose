FROM ubuntu:latest  # Replace with appropriate base image

WORKDIR /app

# Copy your application files
COPY . .

# Copy the wrapper script
COPY run.sh .

# Make the wrapper script executable
RUN chmod +x run.sh

CMD ["./run.sh"]

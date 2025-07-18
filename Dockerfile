FROM flask:2.0.1
LABEL maintainer="shamim"
LABEL version="1.0"
LABEL description="Flask web application for converting roman numerals to integers and vice versa"
# Set the working directory
WORKDIR /app
# Create a non-root user and switch to it
RUN mkdir /app && chown -R flask:flask /app
USER flask

RUN apt-get update && apt-get install -y python3-pip
#create a virtual environment
RUN python3 -m venv venv
#activate the virtual environment
ENV PATH="/app/venv/bin:$PATH"

COPY  --chown=flask:flask requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["flask", "run"]
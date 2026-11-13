# Set the Django default project name
ARG PROJ_NAME="cicerone-backend"

# Set the python version as a build-time argument
# with Python 3.13 as the default
ARG PYTHON_VERSION=3.13-slim-bookworm
FROM python:${PYTHON_VERSION}

# Set Python-related environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install os dependencies for our mini vm
RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

# Create the mini vm's code directory
RUN mkdir -p /code

# Set the working directory to that same code directory
WORKDIR /code

# Upgrade pip and install pipenv
RUN pip install --no-cache-dir --upgrade pip pipenv

# Copy Pipfile and Pipfile.lock first (for caching)
COPY Pipfile Pipfile.lock /code/

# Install dependencies system-wide
RUN pipenv install --deploy --ignore-pipfile --system

# Copy the project code into the container's working directory
COPY ./src /code/src/

# Add our static files to container itself on build
RUN python src/manage.py collectstatic --noinput

# Copy the runtime script and make it executable
COPY run.sh /code/run.sh
RUN chmod +x /code/run.sh

# Expose the port at which the application server is run
EXPOSE 8000

# Run runtime script as container entrypoint
CMD ["/code/run.sh"]



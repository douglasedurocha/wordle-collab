FROM python:3.11.7-slim-bullseye

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH .
 
# Install dependencies
RUN set -xe \
    && apt-get update \
    && apt-get install -y --no-install-recommends build-essential \
    && pip install virtualenvwrapper poetry==1.7.1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY ["poetry.lock", "pyproject.toml", "./"]
RUN poetry install --no-root

# Copy project
COPY ["README.md", "Makefile", ".env",  "./"]
COPY wordle-collab wordle-collab 

# Expose port 8000
EXPOSE 8000

COPY scripts/entrypoint.sh entrypoint.sh
RUN chmod a+x entrypoint.sh

ENTRYPOINT ["bash", "entrypoint.sh"]


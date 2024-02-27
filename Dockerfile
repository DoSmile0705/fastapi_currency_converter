# Use Python 3.9 as the base image
FROM python:3.9

ARG LOCAL_DIR=.
ARG CONTAINER_PATH=/app

# Set the working directory to /app
WORKDIR ${CONTAINER_PATH}

# Copy the requirements file to the working directory
COPY ./requirements.txt /app/requirements.txt

# Install Python dependencies from the requirements file
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the working directory
COPY . /app

# Run Alembic migration to upgrade the database schema to the latest version,
# then run pytest for testing, and finally run the FastAPI app with uvicorn
CMD ["bash", "-c", "python -m alembic upgrade head && pytest && uvicorn app.main:app --host 0.0.0.0 --port 8000"]

FROM python:3

RUN mkdir /app

# Set the working directory in the container
############################################################################################################
# Ensure that Python output is sent straight to terminal (e.g. for logging)
ENV PYTHONUNBUFFERED 1

# Disable .pyc(cache) files
ENV PYTHONDONTWRITEBYTECODE 1

############################################################################################################

# Set the working directory in the container
WORKDIR /app

# Copy all files into the container at /app
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install django
RUN python manage.py makemigrations base
RUN python manage.py migrate

RUN python manage.py collectstatic --noinput
EXPOSE 8000
CMD ["python", "manage.py", "runserver"]

# Use the following command to build and run the Docker container
# docker build -t hackathon-portal .
# docker run -p 8000:8000 hackathon-portal
# Access the application at http://localhost:8000
# Note: Ensure that the Django settings are configured to allow connections from the host machine
# and that the database is set up correctly in settings.py.
# Make sure to have the necessary migrations and database setup before running the container
# You may need to adjust the Dockerfile based on your specific project requirements and dependencies.
# If you have additional dependencies, you can add them to the Dockerfile
# in the RUN pip install command.  
# For production use, consider using a more robust web server like Gunicorn or uWSGI
# and a reverse proxy like Nginx.
# Also, ensure that you have proper security settings in place for production environments.
# For development, you can use the Django development server as shown above.
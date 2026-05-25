#!/bin/bash

PORT=7700

# Find and kill any process running on port 7600
PID=$(lsof -t -i tcp:$PORT)

if [ -n "$PID" ]; then
    echo "Stopping service running on port $PORT (PID: $PID)..."
    kill -9 $PID
    echo "Service stopped."
else
    echo "No service is running on port $PORT."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Start the Django server (bind to all interfaces so it's accessible from other computers)
echo "Starting the server on 0.0.0.0:$PORT..."
python manage.py runserver 0.0.0.0:$PORT

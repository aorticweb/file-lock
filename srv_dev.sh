#!/bin/bash
# Start Api for development with automatic code updates
# To change permissions
# chmod 767 ./srv_dev.sh
uvicorn app.main:app --host 0.0.0.0 --port 5057 --reload
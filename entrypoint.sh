#!/bin/sh
exec python3 -m uvicorn main:app --host 0.0.0.0 --port 8012 --reload

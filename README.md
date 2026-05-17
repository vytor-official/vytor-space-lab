# Vytor Space Intelligence

Vytor is a modular space intelligence dashboard focused on live observation, cinematic visualization, and clean backend architecture.

## Current Version
V8 Cinematic Dashboard

## Features
- NASA APOD visualization
- ISS live stream embed
- ISS live position tracking
- Asteroid monitoring
- Animated glass UI
- Responsive dashboard layout
- Modular backend architecture

## Stack
- Python
- Flask
- Requests
- HTML
- CSS
- JavaScript

## Structure
- `app.py` for the Flask entrypoint
- `config/` for centralized settings
- `core/` for orchestration and validation
- `services/` for data retrieval
- `templates/` for the UI
- `static/` for styles and motion logic

## Run
Install dependencies and set `NASA_API_KEY` in your environment before launching the app.

```bash
pip install -r requirements.txt
python app.py
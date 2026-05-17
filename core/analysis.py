from core.validation import safe_text, safe_number

def build_dashboard_payload(apod_data, iss_data, asteroid_data):
    return {
        "title": safe_text(apod_data.get("title"), "NASA Astronomy Picture of the Day"),
        "image": safe_text(apod_data.get("url"), ""),
        "explanation": safe_text(apod_data.get("explanation"), "No explanation available."),
        "latitude": safe_text(iss_data.get("latitude"), "Unknown"),
        "longitude": safe_text(iss_data.get("longitude"), "Unknown"),
        "asteroid_date": safe_text(asteroid_data.get("date"), "Unknown"),
        "asteroid_count": safe_number(asteroid_data.get("count"), 0),
    } 
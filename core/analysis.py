from core.validation import safe_text, safe_number, safe_dict

def build_dashboard_payload(apod_data, iss_data, asteroid_data):
    apod_data = safe_dict(apod_data)
    iss_data = safe_dict(iss_data)
    asteroid_data = safe_dict(asteroid_data)

    return {
        "title": safe_text(apod_data.get("title"), "Vytor Space Intelligence"),
        "image": safe_text(apod_data.get("url"), ""),
        "explanation": safe_text(
            apod_data.get("explanation"),
            "Space data is currently unavailable."
        ),
        "latitude": safe_text(iss_data.get("latitude"), "Unknown"),
        "longitude": safe_text(iss_data.get("longitude"), "Unknown"),
        "asteroid_date": safe_text(asteroid_data.get("date"), "Unknown"),
        "asteroid_count": safe_number(asteroid_data.get("count"), 0),
        "hazardous_count": safe_number(asteroid_data.get("hazardous_count"), 0)
    }
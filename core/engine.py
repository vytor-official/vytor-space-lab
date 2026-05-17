from core.analysis import build_dashboard_payload
from services.nasa_service import get_apod
from services.iss_service import get_iss_position
from services.asteroid_service import get_asteroids


def get_dashboard_data():
    apod_data = get_apod()
    iss_data = get_iss_position()
    asteroid_data = get_asteroids()

    return build_dashboard_payload(
        apod_data,
        iss_data,
        asteroid_data
    )
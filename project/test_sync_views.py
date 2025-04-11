import httpx
import time

base_url = "http://localhost:8000"

endpoints = [
    "/",
    "/create/",
    "/login/",
    "/notes/",
    "/edit/1/",
    "/delete/1/",
]

def test_sync_views():
    total_time = 0

    for path in endpoints:
        url = base_url + path
        start = time.perf_counter()
        try:
            response = httpx.get(url)
            duration = time.perf_counter() - start
            print(f"{url} - {duration:.4f} seconds (status {response.status_code})")
            total_time += duration
        except Exception as e:
            print(f"Failed to fetch {url}: {e}")

    print(f"\nTotal time for sync requests: {total_time:.4f} seconds")

test_sync_views()

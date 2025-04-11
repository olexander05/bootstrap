import asyncio
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

async def fetch(url, client):
    start = time.perf_counter()
    try:
        response = await client.get(url)
        duration = time.perf_counter() - start
        print(f"{url} - {duration:.4f} seconds (status {response.status_code})")
        return duration
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return 0

async def test_async_views():
    total_time = 0
    async with httpx.AsyncClient(base_url=base_url) as client:
        tasks = [fetch(path, client) for path in endpoints]
        durations = await asyncio.gather(*tasks)
        total_time = sum(durations)

    print(f"\nTotal time for async parallel requests: {total_time:.4f} seconds")

asyncio.run(test_async_views())

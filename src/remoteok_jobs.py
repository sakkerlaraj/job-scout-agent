import requests


AI_KEYWORDS = [
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "genai engineer",
    "generative ai",
    "llm engineer",
    "prompt engineer",
    "rag engineer",
    "agentic ai",
    "ai developer",
    "python developer",
    "data scientist",
    "nlp engineer",
    "computer vision engineer",
    "applied scientist",
    "ai researcher",
    "research engineer",
    "mlops engineer"
]


def get_remoteok_jobs():

    url = "https://remoteok.com/api"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=30
    )

    data = response.json()

    jobs = []

    for job in data:

        if not isinstance(job, dict):
            continue

        title = job.get("position", "").lower()

        if any(keyword in title for keyword in AI_KEYWORDS):

            jobs.append({
                "id": f"remoteok_{job.get('id')}",
                "title": job.get("position"),
                "company": job.get("company"),
                "location": "Remote",
                "url": job.get("url"),
                "source": "RemoteOK"
            })

    return jobs
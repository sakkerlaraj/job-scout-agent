import requests

KEYWORDS = [
    "python",
    "ai",
    "artificial intelligence",
    "machine learning",
    "ml engineer",
    "data scientist",
    "genai",
    "llm"
]


def get_jobs():

    url = "https://www.arbeitnow.com/api/job-board-api"

    response = requests.get(url, timeout=30)

    data = response.json()

    filtered_jobs = []

    for job in data.get("data", []):

        title = job.get("title", "").lower()

        if any(keyword in title for keyword in KEYWORDS):

            filtered_jobs.append({
                "id": str(job.get("slug")),
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("location"),
                "url": job.get("url")
            })

    return filtered_jobs
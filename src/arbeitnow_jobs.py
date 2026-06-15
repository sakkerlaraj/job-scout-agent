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


def get_arbeitnow_jobs():

    url = "https://www.arbeitnow.com/api/job-board-api"

    response = requests.get(url, timeout=30)

    data = response.json()

    jobs = []

    for job in data.get("data", []):

        title = job.get("title", "").lower()

        if any(keyword in title for keyword in AI_KEYWORDS):

            jobs.append({
                "id": f"arbeitnow_{job.get('slug')}",
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("location"),
                "url": job.get("url"),
                "source": "Arbeitnow"
            })

    return jobs
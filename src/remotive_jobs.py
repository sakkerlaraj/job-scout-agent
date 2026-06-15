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


def get_remotive_jobs():

    url = "https://remotive.com/api/remote-jobs"

    response = requests.get(url, timeout=30)

    data = response.json()

    jobs = []

    for job in data.get("jobs", []):

        title = job.get("title", "").lower()

        if any(keyword in title for keyword in AI_KEYWORDS):

            jobs.append({
                "id": f"remotive_{job.get('id')}",
                "title": job.get("title"),
                "company": job.get("company_name"),
                "location": job.get("candidate_required_location"),
                "url": job.get("url"),
                "source": "Remotive"
            })

    return jobs
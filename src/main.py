import json

from arbeitnow_jobs import get_arbeitnow_jobs
from remotive_jobs import get_remotive_jobs
from remoteok_jobs import get_remoteok_jobs
from greenhouse_jobs import get_greenhouse_jobs
from lever_jobs import get_lever_jobs

from telegram_alert import send_telegram_message

SEEN_FILE = "seen_jobs.json"

# AI Keywords
AI_KEYWORDS = [
    "ai engineer",
    "machine learning",
    "ml engineer",
    "llm",
    "generative ai",
    "nlp",
    "deep learning",
    "artificial intelligence",
    "data scientist",
    "computer vision",
    "prompt engineer",
    "rag",
]

# Fresher Keywords
FRESHER_KEYWORDS = [
    "junior",
    "entry",
    "entry level",
    "graduate",
    "new grad",
    "intern",
    "internship",
    "trainee",
    "associate",
    "fresher",
    "early career",
]


def load_seen_jobs():
    try:
        with open(SEEN_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_seen_jobs(seen_jobs):
    with open(SEEN_FILE, "w") as file:
        json.dump(seen_jobs, file)


def is_ai_job(title):
    title = title.lower()
    return any(keyword in title for keyword in AI_KEYWORDS)


def is_fresher_job(title):
    title = title.lower()
    return any(keyword in title for keyword in FRESHER_KEYWORDS)


# Collect jobs from all sources
jobs = []

jobs.extend(get_arbeitnow_jobs())
jobs.extend(get_remotive_jobs())
jobs.extend(get_remoteok_jobs())
jobs.extend(get_greenhouse_jobs())
jobs.extend(get_lever_jobs())

print(f"Total Jobs Found: {len(jobs)}")

# AI Jobs
ai_jobs = [
    job for job in jobs
    if is_ai_job(job.get("title", ""))
]

# AI Fresher Jobs
fresher_jobs = [
    job for job in ai_jobs
    if is_fresher_job(job.get("title", ""))
]

print(f"AI Jobs Found: {len(ai_jobs)}")
print(f"AI Fresher Jobs Found: {len(fresher_jobs)}")

seen_jobs = load_seen_jobs()

for job in fresher_jobs:

    job_id = job.get("id")

    if job_id not in seen_jobs:

        message = f"""
🚀 AI Fresher Job Found

Source: {job.get('source', 'Unknown')}
Title: {job.get('title', 'N/A')}
Company: {job.get('company', 'N/A')}
Location: {job.get('location', 'Remote')}

Apply Here:
{job.get('url', '')}
"""

        result = send_telegram_message(message)

        if result:
            seen_jobs.append(job_id)

save_seen_jobs(seen_jobs)

print("Job Scout Completed")
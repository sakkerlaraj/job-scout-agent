import json

from telegram_alert import send_telegram_message

from arbeitnow_jobs import get_arbeitnow_jobs
from remotive_jobs import get_remotive_jobs
from remoteok_jobs import get_remoteok_jobs

SEEN_FILE = "seen_jobs.json"


def load_seen_jobs():

    try:
        with open(SEEN_FILE, "r") as file:
            return json.load(file)

    except:
        return []


def save_seen_jobs(seen_jobs):

    with open(SEEN_FILE, "w") as file:
        json.dump(seen_jobs, file)


jobs = []

jobs.extend(get_arbeitnow_jobs())
jobs.extend(get_remotive_jobs())
jobs.extend(get_remoteok_jobs())

seen_jobs = load_seen_jobs()

for job in jobs:

    if job["id"] not in seen_jobs:

        message = f"""
🚀 New AI Job Found

Source: {job['source']}
Title: {job['title']}
Company: {job['company']}
Location: {job['location']}

Apply:
{job['url']}
"""

        result = send_telegram_message(message)

        print(result)

        seen_jobs.append(job["id"])

save_seen_jobs(seen_jobs)

print(f"Total Jobs Found: {len(jobs)}")
print("Job Scout Completed")
import json
print("DEBUG VERSION 2")

from arbeitnow_jobs import get_arbeitnow_jobs
from remotive_jobs import get_remotive_jobs
from remoteok_jobs import get_remoteok_jobs
from telegram_alert import send_telegram_message

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

print(f"Total Jobs Found: {len(jobs)}")

seen_jobs = load_seen_jobs()

print("Seen Jobs:", seen_jobs)

for job in jobs:

    print("Checking:", job["title"])

    if job["id"] not in seen_jobs:

        print("Sending:", job["title"])

        message = f"""
🚀 New AI Job Found

Source: {job.get('source', 'Unknown')}
Title: {job['title']}
Company: {job['company']}
Location: {job['location']}

Apply:
{job['url']}
"""

        response = send_telegram_message(message)

        print(response)

        seen_jobs.append(job["id"])

save_seen_jobs(seen_jobs)

print("Job Scout Completed")
import requests

AI_KEYWORDS = [
    "ai",
    "machine learning",
    "ml",
    "llm",
    "genai",
    "data scientist",
    "python",
    "nlp"
]

COMPANIES = [
    "huggingface",
    "cohere",
    "ramp",
    "brex"
]


def get_lever_jobs():

    jobs = []

    for company in COMPANIES:

        try:

            url = f"https://api.lever.co/v0/postings/{company}"

            response = requests.get(url, timeout=30)

            if response.status_code != 200:
                continue

            data = response.json()

            if not isinstance(data, list):
                continue

            for job in data:

                if not isinstance(job, dict):
                    continue

                title = job.get("text", "").lower()

                if any(keyword in title for keyword in AI_KEYWORDS):

                    jobs.append({
                        "id": f"lever_{job.get('id')}",
                        "title": job.get("text"),
                        "company": company,
                        "location": job.get(
                            "categories",
                            {}
                        ).get(
                            "location",
                            "Unknown"
                        ),
                        "url": job.get("hostedUrl"),
                        "source": "Lever"
                    })

        except Exception as e:
            print(f"Lever Error ({company}):", e)

    return jobs
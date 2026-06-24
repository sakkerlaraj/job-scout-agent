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
    "openai",
    "scaleai",
    "databricks",
    "perplexity-ai"
]


def get_greenhouse_jobs():

    jobs = []

    for company in COMPANIES:

        try:

            url = f"https://boards-api.greenhouse.io/v1/boards/{company}/jobs"

            response = requests.get(url, timeout=30)

            data = response.json()

            for job in data.get("jobs", []):

                title = job.get("title", "").lower()

                if any(keyword in title for keyword in AI_KEYWORDS):

                    jobs.append({
                        "id": f"greenhouse_{job['id']}",
                        "title": job["title"],
                        "company": company,
                        "location": "Various",
                        "url": job["absolute_url"],
                        "source": "Greenhouse"
                    })

        except Exception as e:
            print(e)

    return jobs
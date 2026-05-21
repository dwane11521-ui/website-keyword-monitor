import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

# Websites and keywords to check
targets = [
    {
        "url": "https://www.python.org",
        "keyword": "Python"
    },
    {
        "url": "https://github.com",
        "keyword": "GitHub"
    }
]

results = []

for target in targets:
    url = target["url"]
    keyword = target["keyword"]

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        page_text = soup.get_text(" ", strip=True)

        keyword_found = keyword.lower() in page_text.lower()

        results.append({
            "url": url,
            "keyword": keyword,
            "keyword_found": keyword_found,
            "status": "success",
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    except Exception as error:
        results.append({
            "url": url,
            "keyword": keyword,
            "keyword_found": False,
            "status": f"error: {error}",
            "checked_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

df = pd.DataFrame(results)
df.to_csv("keyword_results.csv", index=False)

print("Keyword check completed.")
print(df)
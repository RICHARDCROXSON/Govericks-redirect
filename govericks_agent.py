import requests
import json

# ✅ Your LangSearch API key
API_KEY = "sk-bf2473b2f5dd4deb84ddc54bf1ca8d22"

# 🔍 LangSearch query setup
url = "https://api.langsearch.com/v1/web-search"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "query": "construction law UK",
    "freshness": "noLimit",
    "summary": True,
    "count": 25
}

# 🚀 Send request and print results
response = requests.post(url, headers=headers, data=json.dumps(payload))
results = response.json()
webpages = results.get("data", {}).get("webPages", {}).get("value", [])

for item in webpages:
    print("Title:", item.get("name"))
    print("URL:", item.get("url"))
    print("Summary:", item.get("summary"))
    print("-" * 40)

    print("Status Code:", response.status_code)
    print("Raw Response:", response.text)

    print("✅ Govericks Agent executed successfully.")

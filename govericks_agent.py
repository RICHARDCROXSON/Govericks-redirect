import requests
import json

# 🚧 TEMPORARY: Hardcoded API key for testing
API_KEY = "sk-bf2473b2f5dd4deb84ddc54bf1ca8d22"  # ← Replace this with your actual LangSearch key

# 🔍 LangSearch query setup
url = "https://api.langsearch.com/v1/web-search"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}
payload = {
    "query": "Donald Trump visit to the UK or immigration speach",
    "freshness": "noLimit",
    "summary": True,
    "count": 100
}

# 🚀 Send request and print results
response = requests.post(url, headers=headers, data=json.dumps(payload))

# ✅ Parse and display results
if response.status_code == 200:
    results = response.json()
    webpages = results.get("webPages", {}).get("value", [])

    if not webpages:
        print("No vector-related results found.")
    else:
        print(f"Found {len(webpages)} vector candidates:\n")
        for item in webpages:
            print("🔹 Title:", item.get("name"))
            print("🔗 URL:", item.get("url"))
            print("📝 Summary:", item.get("summary", "No summary available"))
            print("-" * 40)
else:
    print("LangSearch API error:", response.status_code)
    print("Raw Response:", response.text)

print("✅ Govericks Agent executed successfully.")

import requests
import os

# 🔑 Set your LangSearch API key here or via environment variable
LANGSEARCH_API_KEY = os.getenv("sk-bf2473b2f5dd4deb84ddc54bf1ca8d22") or "YOUR_API_KEY_HERE"

# 🧭 LangSearch API endpoint
url = "https://api.langsearch.com/v1/web-search"

# 📦 Request headers
headers = {
    "Authorization": f"Bearer {LANGSEARCH_API_KEY}",
    "Content-Type": "application/json"
}

# 📨 Query payload — adjust this to fit your focus
payload = {
    "query": "UK legal policy updates",
    "freshness": "sixMonths",
    "summary": True,
    "count": 100
}

# 🚀 Make the API call using proper JSON formatting
response = requests.post(url, headers=headers, json=payload)

# 📊 Print status and raw response text
print("Status Code:", response.status_code)
print("Raw Response:", response.text)

# 🧠 Parse results and summarize
try:
    data = response.json()
    results = data.get("webPages", {}).get("value", [])

    if results:
        print(f"\n✅ Found {len(results)} result(s):\n")
        for i, item in enumerate(results[:5], 1):  # Show first 5 results
            print(f"{i}. {item.get('name')}")
            print(f"   {item.get('snippet')}")
            print(f"   {item.get('url')}\n")
    else:
        print("\n⚠ No vector matches found. Try refining the query.")
except Exception as e:
    print("❌ Error parsing response:", str(e))

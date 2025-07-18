import requests

# 🔐 Insert your real LangSearch API key between the quotes below
LANGSEARCH_API_KEY = "sk-bf2473b2f5dd4deb84ddc54bf1ca8d22"  # ← Replace this with your actual key

# 🌐 LangSearch API endpoint
url = "https://api.langsearch.com/v1/web-search"

# 📦 Request headers — using your key
headers = {
    "Authorization": f"Bearer {LANGSEARCH_API_KEY}",
    "Content-Type": "application/json"
}

# 📨 Query payload
payload = {
    "query": "UK legal policy updates",
    "freshness": "sixMonths",
    "summary": True,
    "count": 100
}

# 🚀 Send the request and get the response
response = requests.post(url, headers=headers, json=payload)

# 📊 Print status code and response text before trying to parse
print("Status Code:", response.status_code)
print("Raw Response:", response.text)

# 🔍 Attempt to parse JSON — with error handling
try:
    data = response.json()
    results = data.get("webPages", {}).get("value", [])

    if results:
        print(f"\n✅ Found {len(results)} result(s):\n")
        for i, item in enumerate(results[:5], 1):  # Show top 5 matches
            print(f"{i}. {item.get('name')}")
            print(f"   {item.get('snippet')}")
            print(f"   {item.get('url')}\n")
    else:
        print("\n⚠ LangSearch ran successfully but returned no results. Try refining your query.")
except Exception as e:
    print("❌ LangSearch response could not be parsed as JSON.")
    print("Error:", str(e))

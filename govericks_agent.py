import requests

# 🔐 Your actual LangSearch API key goes here — replace the placeholder below
LANGSEARCH_API_KEY = "sk-bf2473b2f5dd4deb84ddc54bf1ca8d22"  # ✅ Replace with your real key — no quotes around spaces

# 🌐 LangSearch API endpoint
url = "https://api.langsearch.com/v1/web-search"

# 📦 Headers for request — including your API key and correct content type
headers = {
    "Authorization": f"Bearer {LANGSEARCH_API_KEY}",
    "Content-Type": "application/json"
}

# 📨 Query payload — structured exactly as LangSearch expects
payload = {
    "query": "UK legal policy updates",
    "freshness": "sixMonths",
    "summary": True,
    "count": 100
}

# 🚀 Send request and capture response
response = requests.post(url, headers=headers, json=payload)

# 📊 Print status code and raw response body
print("Status Code:", response.status_code)
print("Raw Response:", response.text)

# 🔍 Try to parse JSON response
try:
    data = response.json()
    results = data.get("webPages", {}).get("value", [])

    if results:
        print(f"\n✅ Found {len(results)} result(s):\n")
        for i, item in enumerate(results[:5], 1):  # Top 5
            print(f"{i}. {item.get('name')}")
            print(f"   {item.get('snippet')}")
            print(f"   {item.get('url')}\n")
    else:
        print("\n⚠ LangSearch responded successfully, but no results matched your query.")
except Exception as e:
    print("❌ LangSearch returned a response that couldn’t be parsed as JSON.")
    print("Error:", str(e))

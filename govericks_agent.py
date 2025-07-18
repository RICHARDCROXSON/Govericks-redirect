import requests

# 🔐 Your LangSearch API key — confirmed and locked
LANGSEARCH_API_KEY = "sk-bf2473b2f5dd4deb84ddc54bf1ca8d22"  # ← Replace with your exact key if not already in place

# 🌐 LangSearch API endpoint
url = "https://api.langsearch.com/v1/web-search"

# 📦 Headers needed by LangSearch
headers = {
    "Authorization": f"Bearer {LANGSEARCH_API_KEY}",
    "Content-Type": "application/json"
}

# 📝 The payload you tested manually and know returns results
payload = {
    "query": "UK legal policy updates",
    "freshness": "sixMonths",
    "summary": True,
    "count": 100
}

# 🚀 Send the request using proper JSON formatting
response = requests.post(url, headers=headers, json=payload)

# 📊 Print status and raw response — shows exactly what LangSearch replies
print("Status Code:", response.status_code)
print("Raw Response:", response.text)

# 🔍 Try to parse response — this will succeed or clearly show why it doesn't
try:
    data = response.json()
    results = data.get("webPages", {}).get("value", [])

    if results:
        print(f"\n✅ Found {len(results)} result(s):\n")
        for i, item in enumerate(results[:5], 1):  # Display top 5
            print(f"{i}. {item.get('name')}")
            print(f"   {item.get('snippet')}")
            print(f"   {item.get('url')}\n")
    else:
        print("\n⚠ No matches returned — LangSearch is working but found no vector content matching your query.")
except Exception as e:
    print("❌ Error parsing LangSearch response:", str(e))

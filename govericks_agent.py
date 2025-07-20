import requests

# 🔐 Your actual LangSearch API key — replace this with your real key
LANGSEARCH_API_KEY = "sk-bf2473b2f5dd4deb84ddc54bf1ca8d22"

# 🌐 LangSearch API endpoint
url = "https://api.langsearch.com/v1/web-search"

# 📦 Headers for the request
headers = {
    "Authorization": f"Bearer {LANGSEARCH_API_KEY}",
    "Content-Type": "application/json"
}

# 📨 Payload for the query
payload = {
    "query": "breach of construction contract"
 "construction agreements"
 "construction arbitration"
 "construction barrister"
 "construction claims"
 "construction contract advice"
 "construction contract expert witness"
 "construction contract expert"
 "construction contracts"
 "construction disputes"
 "delay analysis"
 "dispute avoidance in construction"
 "dispute avoidance"
 "engineering disputes"
 "EPC Contracts"
 "extensions of time"
 "Infrastructure contracts"
 "infrastructure disputes"
 "liquidated damages"
 "new engineering contract disputes"
 "prolongation costs"
 "quantum expert"
 "Society of Construction Law"
 "strategic construction contract advice"
 "time at large",
    "freshness": "freshness_window = timedelta(hours=6)
start_date = datetime.now() - freshness_window",
    "summary": True,
    "count": 20
}

# 🚀 Send the request
response = requests.post(url, headers=headers, json=payload)

# 📊 Print status and raw response
print("Status Code:", response.status_code)
print("Raw Response:", response.text)

# 🔍 Try to parse JSON safely
try:
    if response.headers.get("Content-Type", "").startswith("application/json"):
        data = response.json()
        results = data.get("webPages", {}).get("value", [])

        if results:
            print(f"\n✅ Found {len(results)} result(s):\n")
            for i, item in enumerate(results[:5], 1):
                print(f"{i}. {item.get('name')}")
                print(f"   {item.get('snippet')}")
                print(f"   {item.get('url')}\n")
        else:
            print("\n⚠ LangSearch responded successfully, but no results matched your query.")
    else:
        print("\n❌ LangSearch did not return JSON. Response type:", response.headers.get("Content-Type"))
except Exception as e:
    print("❌ LangSearch response could not be parsed as JSON.")
    print("Error:", str(e))

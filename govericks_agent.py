import requests

from datetime import datetime, timedelta

LANGSEARCH_API_KEY = "sk-bf2473b2f5dd4deb84ddc54bf1ca8d22"
url = "https://api.langsearch.com/v1/web-search"

headers = {
    "Authorization": f"Bearer {LANGSEARCH_API_KEY}",
    "Content-Type": "application/json"
}

# Construct a single string query from all terms
query_terms = [
    "breach of construction contract",
    "construction agreements",
    "construction arbitration",
    "construction barrister",
    "construction claims",
    "construction contract advice",
    "construction contract expert witness",
    "construction contract expert",
    "construction contracts",
    "construction disputes",
    "delay analysis",
    "dispute avoidance in construction",
    "dispute avoidance",
    "engineering disputes",
    "EPC Contracts",
    "extensions of time",
    "Infrastructure contracts",
    "infrastructure disputes",
    "liquidated damages",
    "new engineering contract disputes",
    "prolongation costs",
    "quantum expert",
    "Society of Construction Law",
    "strategic construction contract advice",
    "time-at-large"
]

combined_query = " OR ".join(query_terms)

# Freshness: posts from last 6 hours
start_time = (datetime.now() - timedelta(hours=6)).isoformat()

payload = {
    "query": combined_query,
    "freshness": start_time,  # depends on LangSearch expected format
    "summary": True,
    "count": 20
}

response = requests.post(url, headers=headers, json=payload)

print("Status Code:", response.status_code)
print("Raw Response:", response.text)

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
    print("Error:", str(e))

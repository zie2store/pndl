import requests

url = "https://thedaddy.top/schedule/schedule-generated.php"
output_file = "dlhd.json"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:141.0) Gecko/20100101 Firefox/141.0",
    "Referer": "https://thedaddy.top/"
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(response.text)

    print(f"✅ File saved: {output_file}")

except requests.RequestException as e:
    print(f"❌ Error: {e}")
    exit(1)

import http.client
import json

# Example payload (replace with your actual data)
payload = json.dumps({
    'loginId': 'leiz'
})

# Replace with your endpoint and adjust as necessary
conn = http.client.HTTPSConnection('www.smartplay.lcsd.gov.hk')

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-hk',
    'Connection': 'keep-alive',
    'Login-Token': 'eb68f208d1bc4917900230182851b7da',  # Replace with actual token
    'Origin': 'https://www.smartplay.lcsd.gov.hk',
    'Referer': 'https://www.smartplay.lcsd.gov.hk/home',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36',
    'channel': 'INTERNET',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}
try:
    # Send POST request
    conn.request('POST', '/rest/patron/api/v1/publ/queue', payload, headers)

    # Get response
    response = conn.getresponse()
    print(response.read().decode('utf-8'))

finally:
    conn.close()
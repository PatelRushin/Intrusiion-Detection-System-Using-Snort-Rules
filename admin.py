import requests

# alerting for TCP
payload_1 = {
  "action": "alert",
  "protocol": "tcp",
  "source_ip": "any",
  "source_port": "any",
  "dest_ip": "$HOME_NET",
  "dest_port": "22",
  "sid": "100002",
  "rev_num": "1",
  "msg": "SSH Attempt Detected!!"
}

# alerting for ICMP
payload_2 = {
  "action": "alert",
  "protocol": "icmp",
  "source_ip": "any",
  "source_port": "any",
  "dest_ip": "$HOME_NET",
  "dest_port": "any",
  "sid": "100001",
  "rev_num": "1",
  "msg": "Ping Detected!!"
}

# alerting for FTP/Port Scan
payload_3 = {
    "action": "alert",
    "protocol": "tcp",
    "source_ip": "any",
    "source_port": "8000",  
    "dest_ip": "$HOME_NET",
    "dest_port": "21",
    "sid": "100003",
    "rev_num": "1",
    "msg": "FTP Authentication Attempt Detected!!"
}
try:
    # Send HTTP POST request
    response = requests.post('http://127.0.0.1:8000/rule/', json=payload_2)
    # Check the response status code
    if response.status_code == 200:
        # Access the 'final_rule' key from the response JSON
        print(response.json().get('Rule created'))
    else:
        print(f" {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"An error occurred: {e}")
https://reqres.in/api/users
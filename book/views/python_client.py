import requests



resp = requests.get("http://127.0.0.1:8000/home_cbv/", data={"name": "Vinay"})
print(resp.content)  # idempotent requ
# s = requests.Session()

# Non idempotent -- 




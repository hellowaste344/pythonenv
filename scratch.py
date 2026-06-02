import requests

s = requests.Session()

url = "https://www.google.com/maps/vt/proto/bpb=CgsKBggDEAMYBMoBABIVCAASAW0Yv7q09AIiCAoDbmRsEgExGioSBWVuLVVTGgJUUigDYhsIRBIXCgNzZXQSEFJvYWRtYXBTYXRlbGxpdGUgATIZKAFYALgCAdgCAeACBOgCAbgDAdADAdgFAboBBOmOtBY&token=65716"

try: 
    resp = s.get(url)
    print(resp.status_code)
    if 200 <= resp.status_code < 400:
        print(resp.json()) 
except Exception as e:
    print(f"{e}")
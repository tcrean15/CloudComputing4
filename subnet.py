import requests
import json

url = "https://management.azure.com/subscriptions/5f55cf38-c1af-4122-808e-bee5767d3862/resourceGroups/lab4/providers/Microsoft.Network/virtualNetworks/net4/subnets/snet4?api-version=2023-05-01"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSIsImtpZCI6IjlHbW55RlBraGMzaE91UjIybXZTdmduTG83WSJ9.eyJhdWQiOiJodHRwczovL21hbmFnZW1lbnQuY29yZS53aW5kb3dzLm5ldCIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0Lzc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYS8iLCJpYXQiOjE3MDAxNTIwNzgsIm5iZiI6MTcwMDE1MjA3OCwiZXhwIjoxNzAwMTU3MDE4LCJhY3IiOiIxIiwiYWlvIjoiQVZRQXEvOFZBQUFBTEUwRE5nWktRY2JReFhHUlFIZWl2Vlc2VzdsSzRQc1g1bTJVZytkU3dDaWJxTzhSazlONGkwOXZiZ202THRiWGxHZlFDbXdGU1lieWs4b25BVnJNYUs0QjZyVzBLRVh4aDMyaTVFMGV5d1E9IiwiYW1yIjpbInB3ZCIsIm1mYSJdLCJhcHBpZCI6IjE4ZmJjYTE2LTIyMjQtNDVmNi04NWIwLWY3YmYyYjM5YjNmMyIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiQ3JlYW4iLCJnaXZlbl9uYW1lIjoiVGhvbWFzIiwiZ3JvdXBzIjpbIjgxMDhjNTAzLWQ2NTYtNDJjZi04ZWU0LTg5NDRhZWYwZmFkZSIsIjk3YWY4MTJkLTk2ZTktNGYwMS04YTExLTc1ODAzMzc2MjE3YSIsIjg3ZjYwMDNkLTk0NzAtNDM4Zi1iZmVmLTgxM2IzN2ZjMmI2OCIsIjgzOGEyODlhLTg0YTQtNGNhOC1hZWVjLWIzMWVjMWQ3MWQ0YSIsIjRkYzAzYjlmLTFiNmMtNDQxNS1hYzA1LTgyNDI3MTNjNzUyMCIsIjVhZDdkNmI0LWFkYWYtNGI5ZC05NTdmLTBmM2I2MTRiZWU2MCIsIjhhYzE1NGRkLWQ0NWYtNGM0Ni05NGU1LWJiNzhmZWZhM2FlZiIsIjhjODE4NmVhLTQyYTQtNDRhZi04YTc4LWFlOTE0MDExZTZiNCIsImQyYTZhOGVmLTRkMjYtNGQ5NS1iZDExLWFhMWVjNjE5ZjgxOCIsImFiZDQ5ZGZkLWNlZmItNGMzNi1hZDY3LTI1ZmQ5ZmZkMzM3ZiJdLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIxNDcuMjUyLjE5LjE5MCIsIm5hbWUiOiJDMjE0MTYwMTQgVGhvbWFzIENyZWFuIiwib2lkIjoiOTJlMzZjY2MtNzA4OC00ZGE0LThiZWMtNzlmZGZkZmYyYTczIiwib25wcmVtX3NpZCI6IlMtMS01LTIxLTQwMjI5ODg0OS0xNzM0NzA1MTMxLTMxMjAwMjQwMDEtNDQwMzYiLCJwdWlkIjoiMTAwMzIwMDE4MzFFQ0RCNSIsInJoIjoiMC5BVEVBeXhkamRranBYMDZNN05xOGppX1Yya1pJZjNrQXV0ZFB1a1Bhd2ZqMk1CTXhBRlEuIiwic2NwIjoidXNlcl9pbXBlcnNvbmF0aW9uIiwic3ViIjoiYVdmbmNuTkJCbi12QXoyeVdEYXY0YmxwQTQzbkZBZUNMYlpCdklwSHZfayIsInRpZCI6Ijc2NjMxN2NiLWU5NDgtNGU1Zi04Y2VjLWRhYmM4ZTJmZDVkYSIsInVuaXF1ZV9uYW1lIjoiQzIxNDE2MDE0QG15dHVkdWJsaW4uaWUiLCJ1cG4iOiJDMjE0MTYwMTRAbXl0dWR1Ymxpbi5pZSIsInV0aSI6InVVLWFOTUQ2UFVxNTBGazRaUTRpQUEiLCJ2ZXIiOiIxLjAiLCJ3aWRzIjpbImI3OWZiZjRkLTNlZjktNDY4OS04MTQzLTc2YjE5NGU4NTUwOSJdLCJ4bXNfY2FlIjoiMSIsInhtc190Y2R0IjoxNTI1MzM4OTQxfQ.lySAzlto0qaEeoxRsrX87G4bZ6J9BVHBnm2qBujyXcqm12sJahLM20Kdr5wDqjxu32-sT6PH5l8WHTsaAIAlTawxFRkhHlbqkuAsbh3OzpvyUxbBkDywOzkV6cn5REpNFHMhXHgyJf8SPw5UVPFDX9TSXmHQuR_5gebk4CZex_J_LtEE7FfH1iuD597iuMbZn3lKG3lx_HeOmwoWcsxYN0QcSlQ3Z0sMx-JDBxh3GX7tPShdljq49kcH731ZMcOrCeNootRba14FBp03BDNwbR6ixju-s6u87eqarE5P9sHH_RcnqmhAadOc0wskkehMuDv_xfJBT_6nD4Vf4EZMkQ
',
}

data = {

    'location': "westeurope"

}

response = requests.put(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
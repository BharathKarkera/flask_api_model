# flask_api_model

```
 1:22PM @Bharath  ~ curl -i "http://localhost:5000/users" \
-H "Accept: application/json" \
-H "Content-Type:application/json" \
--data @<(cat <<EOF
{
"name":"Maddy" ,
"JL": "SSE" ,
"Language": "Python" ,
"age":25
  }
EOF
)
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 89
Server: Werkzeug/2.0.2 Python/3.9.7
Date: Tue, 25 Jul 2023 18:22:31 GMT

{
  "JL": "SSE", 
  "Language": "Python", 
  "age": 25, 
  "id": 7, 
  "name": "Maddy"
}
 1:22PM @Bharath  ~ 
```



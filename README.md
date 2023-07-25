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


```
 1:22PM @Bharath  ~ curl -i -H "Accept: application/json"  -X GET http://127.0.0.1:5000/users
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 863
Server: Werkzeug/2.0.2 Python/3.9.7
Date: Tue, 25 Jul 2023 18:22:27 GMT

[
  {
    "JL": "TA", 
    "Language": "Python", 
    "age": "25", 
    "id": "0", 
    "name": "Bharath"
  }, 
  {
    "JL": "TL", 
    "Language": "Python", 
    "age": "28", 
    "id": "1", 
    "name": "Shrini"
  }, 
  {
    "JL": "TA", 
    "Language": "Java", 
    "age": "27", 
    "id": "2", 
    "name": "Naga"
  }, 
  {
    "JL": "TA", 
    "Language": "Java", 
    "age": "26", 
    "id": "3", 
    "name": "Hitha"
  }, 
  {
    "JL": "SSE", 
    "Language": "Python", 
    "age": "25", 
    "id": "4", 
    "name": "Aishwarya"
  }, 
  {
    "JL": "TL", 
    "Language": "Java", 
    "age": "35", 
    "id": "5", 
    "name": "Rohit"
  }, 
  {
    "JL": "TL", 
    "Language": "Java", 
    "age": "27", 
    "id": "6", 
    "name": "Anil"
  }, 
  {
    "JL": "TL", 
    "Language": "Python", 
    "age": "27", 
    "id": "6", 
    "name": "Anil"
  }
]
 1:22PM @Bharath  ~ 
```



#curl -i -H "Accept: application/json" -X POST -d "path=/AuthenticationSource/EXAMPLE.COM%20AD" http://localhost:8000/api/AuthenticationSources

#curl -i -H "Accept: application/json" -X DELETE http://localhost:8000/api/AuthenticationSources/EXAMPLE.COM%20AD
curl -i -H "Accept: application/json" -X DELETE http://localhost:8000/api/Containers

# AzureFunctionApp

## How to test your API Server:

curl -X POST "https://<Your Function App Name>.azurewebsites.net/api/http_trigger1?code=<Your API KEY>" \
     -H "Content-Type: application/json" \
     -d '{"name":"Maziar"}'

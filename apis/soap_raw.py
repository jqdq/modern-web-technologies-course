import requests

url = "https://www.w3schools.com/xml/tempconvert.asmx"

payload = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<soap12:Envelope xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:xsd=\"http://www.w3.org/2001/XMLSchema\" xmlns:soap12=\"http://www.w3.org/2003/05/soap-envelope\">\n  <soap12:Body>\n    <FahrenheitToCelsius xmlns=\"https://www.w3schools.com/xml/\">\n      <Fahrenheit>75</Fahrenheit>\n    </FahrenheitToCelsius>\n  </soap12:Body>\n</soap12:Envelope>"
headers = {
  'Content-Type': 'application/soap+xml; charset=utf-8'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
import zeep

url = "https://www.w3schools.com/xml/tempconvert.asmx?WSDL"
client = zeep.Client(url)

print(client.service.FahrenheitToCelsius(Fahrenheit=75))

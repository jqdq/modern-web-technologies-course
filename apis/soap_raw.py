import requests

url = "https://www.w3schools.com/xml/tempconvert.asmx"
soap_header = "application/soap+xml; charset=utf-8"

def xml_message(fahrenheit):
    return f"""
    <?xml version="1.0" encoding="utf-8"?>
    <soap12:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
    <soap12:Body>
        <FahrenheitToCelsius xmlns="https://www.w3schools.com/xml/">
        <Fahrenheit>{fahrenheit}</Fahrenheit>
        </FahrenheitToCelsius>
    </soap12:Body>
    </soap12:Envelope>
    """

req = requests.get("https://api.adviceslip.com/advice")
if req.ok:
    print(req.json()['slip']['advice'])
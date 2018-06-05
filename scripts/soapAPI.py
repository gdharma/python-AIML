from symbol import argument
from sys import argv
import xml.etree.ElementTree as E
import requests
import switch as switch


import urllib3
data= None
# project="GET CONTRACT"
project=argv[1].upper()
# username="243T40468"
username=argv[2].upper()
# soursesystem=argv[3].upper()
# dataneed=argv[4].upper()

if project in "GET CONTRACT":

    host = "https://sit4.internal2.eportal.wellpoint.com/services/eligibilityDomain/v1/eligibilityService"
    # request="<soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:ser=\"http://service.eligibility.middletier.ebiz.wellpoint.com/\">\n" + "<soapenv:Header>\n" + "<wsse:Security soapenv:mustUnderstand=\"0\" xmlns:wsse=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd\">\n" + "<wsse:UsernameToken wsu:Id=\"UsernameToken-62194613\" xmlns:wsu=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd\">\n" + "<wsse:Username>srcLDAPescWSSecurity</wsse:Username>\n" + "<wsse:Password Type=\"http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText\">St@rt100</wsse:Password>\n" + "</wsse:UsernameToken>\n" + "</wsse:Security>\n" + "</soapenv:Header>\n + <soapenv:Body>\n" + "<ser:getContract>\n" + "<sourceSystem>" "WGS" "</sourceSystem>\n" + "<cachingRequestHeader>\n" + "<forceLiveResponse>true</forceLiveResponse>\n" + "</cachingRequestHeader>\n" + "<hcid>""243T40468""</hcid>\n" + "</ser:getContract>\n" + "</soapenv:Body>\n" + "</soapenv:Envelope> \n"
    request="""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ser="http://service.eligibility.middletier.ebiz.wellpoint.com/">
   <soapenv:Header>
      <wsse:Security soapenv:mustUnderstand="0" xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd">
         <wsse:UsernameToken wsu:Id="UsernameToken-662A20200 " xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
            <wsse:Username>srcLDAPescWSSecurity</wsse:Username>
            <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">St@rt100</wsse:Password>
         </wsse:UsernameToken>
      </wsse:Security>
   </soapenv:Header>
   <soapenv:Body>
      <ser:getContract>
         <messageId>1</messageId>
         <correlationId>?</correlationId>
         <transactionId>?</transactionId>
         <serviceVersion>1.0</serviceVersion>
         <consumerRequestHeader>
            <userName>aaa</userName>
            <applicationId>?</applicationId>
            <cobrowse>Y</cobrowse>
         </consumerRequestHeader>
         <sourceSystem>WGS</sourceSystem>
         <cachingRequestHeader>
            <forceLiveResponse>true</forceLiveResponse>
         </cachingRequestHeader>
         <hcid>%s</hcid>
      </ser:getContract>
   </soapenv:Body>
</soapenv:Envelope>"""%(username)
    encoded_request = request.encode ('utf-8')
    headers = {"Content-Type": "text/xml; charset=UTF-8","SOAPAction": "http://eligibility.middletier.ebiz.wellpoint.com/EligibilityDomain/getContract/"}
    urllib3.disable_warnings (urllib3.exceptions.InsecureRequestWarning)
    response = requests.post(host,headers = headers,data = encoded_request,verify=False)

    status=response.status_code
    responseParse=E.fromstring(response.text)
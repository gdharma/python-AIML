#!/usr/bin/env python
# encoding: utf-8

import requests
from pyquery import PyQuery


def CompleteReturnRequest(Username, Password, merchantCode, storeCode, returnId):
    form = """
        <soapenv:Envelope
            xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
            xmlns:pos="http://testthis.com/xmlschema/pos">
            <soapenv:Header>
                <wsse:Security soapenv:mustUnderstand="1"
                    xmlns:wsse="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
                    xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
                    <wsse:UsernameToken>
                        <wsse:Username>%s</wsse:Username>
                        <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-username-token-profile-1.0#PasswordText">%s</wsse:Password>
                    </wsse:UsernameToken>
                </wsse:Security>
            </soapenv:Header>
            <soapenv:Body>
                <pos:CompleteReturnRequest>"
                    <!--Optional:-->
                    <pos:merchantCode>%s</pos:merchantCode>
                    <pos:storeCode>%s</pos:storeCode>
                    <pos:returnId>%d</pos:returnTrxId>
                </pos:CompleteReturnRequest>
            </soapenv:Body>
        </soapenv:Envelope>""" % (Username, Password, merchantCode, storeCode, returnId)

    encoded_request = form.encode('utf-8')
    headers = {"Content-Type": "text/xml; charset=UTF-8", "Content-Length": len(encoded_request)}
    response = requests.post(url="https://testthis.pos.com:443/pos/soap/pos", headers=headers, data=encoded_request,
                             verify=False)

    return response
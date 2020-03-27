#!/usr/bin/env python
"""
I made the assumption that the XML would be passed as a code in the url. In order to get this code to work I had to change the quotation marks as provided in the word file.

"""

import web
import xml.etree.ElementTree as ET

urls = (
    '/(.*)','parseXML'
)

app = web.application(urls, globals())

class parseXML:
    def GET(self,xmlString):
        try:

            root = ET.fromstring(xmlString)
            print("after tree")
            for item in root.iter():
                print("in loop")
                print(item.tag)
                if item.tag == "Declaration":
                    if item.get("Command")!="DEFAULT":
                        return -1

                if item.tag == 'SiteID':
                    if item.text!="DUB":
                        return -2
            print("t")
            return 0
        except:
            return "Error in reading XML, May not be correctly structured"

if __name__ == "__main__":
    app.run()

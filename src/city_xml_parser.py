import xml.etree.ElementTree as ET
root = ET.parse("./xml/burma14.xml").getroot()
nodes = root.find("graph").findall("vertex")
print(nodes)
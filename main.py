import re
import xml.etree.cElementTree as ET
import xml.dom.minidom

people_tag = ET.Element("people")

with open("file.txt") as textfile:
    textlines = textfile.readlines()

    for textline in textfile:
        textlines.append(textline.rstrip('\n'))

    prevline = ""

    for line in textlines:
        if line[0] == "P":
            person_names = re.search(r'\|.*', line)
            firstname = person_names[0].split('|')[1]
            lastname = person_names[0].split('|')[2]

            person_tag = ET.SubElement(people_tag, "person")
            ET.SubElement(person_tag, "firstname").text = firstname
            ET.SubElement(person_tag, "lastname").text = lastname

        elif line[0] == "A" and prevline[0] != "F":
            address_info = re.search(r'\|.*', line)
            street = address_info[0].split('|')[1]
            city = address_info[0].split('|')[2]
            postcode = address_info[0].split('|')[3]
            print("City: ", city)

            address = ET.SubElement(person_tag, "address")
            ET.SubElement(address, "street").text = street
            ET.SubElement(address, "city").text = city
            ET.SubElement(address, "postcode").text = postcode

        elif line[0] == "T" and prevline[0] != "F":
            phones = re.search(r'\|.*', line)
            mobile = phones[0].split('|')[1]
            landline = phones[0].split('|')[2]

            phone = ET.SubElement(person_tag, "phone")
            mobile = ET.SubElement(phone, "mobile").text = mobile
            landline = ET.SubElement(phone, "landline").text = landline

        elif line[0] == "F":
            family_info = re.search(r'\|.*', line)
            name = family_info[0].split('|')[1]
            born = family_info[0].split('|')[2]

            family = ET.SubElement(person_tag, "family")
            ET.SubElement(family, "name").text = name
            ET.SubElement(family, "born").text = born

        elif line[0] == "A" and prevline[0] == "F":
            address_info = re.search(r'\|.*', line)
            street = address_info[0].split('|')[1]
            city = address_info[0].split('|')[2]
            postcode = address_info[0].split('|')[3]

            address = ET.SubElement(family, "address")
            ET.SubElement(address, "street").text = street
            ET.SubElement(address, "city").text = city
            ET.SubElement(address, "postcode").text = postcode
        
        elif line[0] == "T" and prevline[0] == "F":
            phones = re.search(r'\|.*', line)
            mobile = phones[0].split('|')[1]
            landline = phones[0].split('|')[2]

            phone = ET.SubElement(family, "phone")
            mobile = ET.SubElement(phone, "mobile").text = mobile
            landline = ET.SubElement(phone, "landline").text = landline
        
        prevline = line

    tree = ET.ElementTree(people_tag)
    tree.write("file_xml.xml")

    with open('file_xml.xml') as xmldata:
        xml = xml.dom.minidom.parseString(xmldata.read())
        xml_pretty_str = xml.toprettyxml()

    print(xml_pretty_str)
from lxml import etree

if __name__ == '__main__':
    xml_content = '<?xml version="1.0" encoding="UTF-8"?>' \
                  '<info>Project B works !</info>'
    root = etree.fromstring(xml_content.encode())
    print(root.text)

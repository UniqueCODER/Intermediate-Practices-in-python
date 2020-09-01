import xml.etree.ElementTree as et
data = '''
<person>
<name> Ellysa </name>
<phone>+63 916 545 4758</phone>
<email hide="yes"/>
</person>
'''

tree = et.fromstring(data)
print('Name',tree.find('name').text)
print('Attr',tree.find('email').get('hide'))
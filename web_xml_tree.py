import xml.etree.ElementTree as et
input1 = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Kookie</name>
        </user>
    </users>

</stuff>
'''

stuff = et.fromstring(input1)
lst =stuff.findall('users/user')
print('User Count', len(lst))

for item in lst:
    print('Name',item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute',item.get("x"))
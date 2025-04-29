import re

def parse_link(string):
    match=re.fullmatch(r'<a href="(.*)">(.*)</a>',string)
    if not match:
        return None
    link,caption=match.groups()
    return caption,link

string='a href="www.gooogle.com" chicken nugget'
print(parse_link(string))
string='<a href="www.google.com">Google</a>'
print(parse_link(string))
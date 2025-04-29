# import re

# def collect_links(html):
#     pattern = r'<a[^>]+href=["\'](https?://[^"\']+)["\']'
#     return re.findall(pattern, html)

# html = '''
# <html>
#   <body>
#     <a href="https://example.com">Example</a>
#     <a href="http://test.com">Test</a>
#     <a>No link here</a>
#   </body>
# </html>
# '''

# print(collect_links(html))


import re
def collect_links(string):
    p = r'<a href=\"([^\"]*)\">[^<]*</a>'
    match = re.findall(p, string)
    return match


print(collect_links('<a href="https://www.example1.com">Link 1</a> <a href="https://www.example2.com">Link 2</a> <a href="https://www.example3.com">Link 3</a>'))
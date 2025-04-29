import re

def parse_time(string):
    match=re.fullmatch(r"(\d{2}):(\d{2}):(\d{2})(?:[.:](\d{3}))?",string)
    if not match:
        return None
    h,m,s,ms=match.groups()
    return int(h),int(m),int(s),int(ms or 0)

string="00:00:00:001"
print(parse_time(string))
string="11:12:13"
print(parse_time(string))
string="37:42:09.642"
print(parse_time(string))
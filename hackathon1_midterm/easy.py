# 1
from datetime import datetime
import re

def day_diff(release_date, code_complete_day):
    date_format_release = "%d/%m/%Y"
    date_format_complete = "%Y-%d-%m"
    release_date = datetime.strptime(release_date, date_format_release)
    code_complete_day = datetime.strptime(code_complete_day, date_format_complete)
    return  (release_date-code_complete_day).days
    pass
# 2
def alpha_num(sentence):
    a = re.findall('[a-zA-Z0-9]*\d', sentence)
    list = []
    for i in a:
        if i.isalnum():
            list.append(i)
    return list
    pass
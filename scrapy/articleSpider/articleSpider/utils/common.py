import hashlib
import re


def get_md5(url):
    if isinstance(url, str):
        url = url.encode('utf-8')
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()


def extract_num(text):
    nums = re.match('.*?(\d+).*', text)
    if nums:
        nums = int(nums.group(1))
    else:
        nums = 0
    return nums
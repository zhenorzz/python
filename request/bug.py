import urllib
import urllib.request
import re
def download_page(url):
    try:
        request = urllib.request.urlopen(url)
        return request.read()
    except urllib.error.HTTPError as e:
        pass

def get_image(html):
    regx = r'http://[\S]*\.jpg'
    pattern = re.compile(regx)
    get_img = re.findall(pattern, repr(html))
    num = 1
    for img in get_img:
        try:
            request = urllib.request.urlopen(img)
            image = request.read()
        except urllib.error.HTTPError as e:
            pass
        with open('%s.jpg'%num,'wb') as fp:
            fp.write(image)
            num += 1
            print('正在下载第%s张图片'%num)
    return
url = 'http://pic.yesky.com/451/106166451.shtml'
get_image(download_page(url))
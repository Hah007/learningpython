def get_headers(header_raw):
    """
    通过原生请求头获取请求头字典
    :param header_raw: {str} 浏览器请求头
    :return: {dict} headers
    """
    header_raw = header_raw.strip()  # 处理可能的空字符
    header_raw = header_raw.split("\n")  # 分割每行
    header_raw = [line.split(":", 1) for line in header_raw]  # 分割冒号
    # print(header_raw)
    header_raw = dict((k.strip(), v.strip()) for k, v in header_raw)  # 处理可能的空字符
    return header_raw
    # dict(line.split(": ", 1) for line in header_raw.split("\n"))


def get_cookies(cookie_raw):
    """
    通过原生cookie获取cookie字段
    :param cookie_raw: {str} 浏览器原始cookie
    :return: {dict} cookies
    """
    return dict(line.split("=", 1) for line in cookie_raw.split("; "))


if __name__ == '__main__':
    raw_headers = '''accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: max-age=0
content-length: 45
content-type: application/x-www-form-urlencoded
cookie: Hm_lvt_32da9a91d04e7f7f3eca588f6f08a0ae=1577601258; jieqiVisitId=article_articleviews%3D351; PHPSESSID=1b9d18e661bdf59dfe4c93ce94de24af; jieqiUserInfo=jieqiUserId%3D146194%2CjieqiUserName%3Dhah007%2CjieqiUserGroup%3D3%2CjieqiUserName_un%3Dhah007%2CjieqiUserLogin%3D1577601363; jieqiVisitInfo=jieqiUserLogin%3D1577601363%2CjieqiUserId%3D146194; Hm_lpvt_32da9a91d04e7f7f3eca588f6f08a0ae=1577601375
origin: https://www.xslou.com
referer: https://www.xslou.com/yuedu/351/
sec-fetch-mode: navigate
sec-fetch-site: same-origin
sec-fetch-user: ?1
upgrade-insecure-requests: 1'''

    raw_headers = '''
    username: hah007
password: hellohh
action: login
    '''
    
    
    # raw_headers = '''Host: open.tool.hexun.com
    # Pragma: no-cache
    # Cache-Control: no-cache
    # User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36
    # Accept: */*
    # Referer: http://stock.hexun.com/gsxw/
    # Accept-Encoding: gzip, deflate
    # Accept-Language: zh-CN,zh;q=0.9,en;q=0.8'''

    # raw_headers = '''Referer:http://s.ygdy8.com/plus/s.php?typeid=1&keyword=%CC%EC%CF%C2
    # Upgrade-Insecure-Requests:1
    # User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'''


    headers_js=get_headers(raw_headers)
    print(headers_js)

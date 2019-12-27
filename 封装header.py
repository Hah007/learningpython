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
    raw_headers = '''Accept: application/json, text/javascript, */*; q=0.01
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Connection: keep-alive
    Content-Length: 0
    Cookie: WWWID=WWW85B39E3AE7522AAA7411F2E057AC9874; Hm_lvt_22ea01af58ba2be0fec7c11b25e88e6c=1577248153; Hm_lpvt_22ea01af58ba2be0fec7c11b25e88e6c=1577248153
    Host: www.kuaidi100.com
    Origin: https://www.kuaidi100.com
    Referer: https://www.kuaidi100.com/?from=openv
    Sec-Fetch-Mode: cors
    Sec-Fetch-Site: same-origin
    User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36
    X-Requested-With: XMLHttpRequest'''
    
    
    
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

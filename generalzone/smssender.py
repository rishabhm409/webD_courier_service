from urllib.request import urlopen,Request
from urllib.parse import urlencode
user="BRIJESH"
key="ba24d737a5XX"
senderid="PRVRTN"
accusage="1"
def sentsms(mobile,message):
    value={
        'user':user,
        'key':key,
        'mobile':mobile,
        'message':message,
        'senderid':senderid,
        'accusage':accusage

    }
    url="http://sms.bulkssms.com/submitsms.jsp"
    postdata=urlencode(value).encode("utf-8")
    req=Request(url,postdata)
    response=urlopen(req)
    response.read()

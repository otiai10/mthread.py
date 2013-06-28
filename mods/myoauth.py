import time,random,urllib,cgi,hmac,hashlib
from conf import Conf

class MyOAuth:
  def __init__(self):
    pass

  @classmethod
  def get_oauth_token_and_secret(self):
    consumer_key    = Conf.consumer_key
    consumer_secret = Conf.consumer_secret
    method="GET"
    request_token_rul="https://api.twitter.com/oauth/request_token"
    params = {
      "oauth_consumer_key":    consumer_key,
      "oauth_signature_method":"HMAC-SHA1",
      "oauth_timestamp":       str(int(time.time())),
      "oauth_nonce":           str(random.getrandbits(64)),
      "oauth_version":         "1.0"
    }
    params_str = '&'.join(['%s=%s'%(urllib.quote(key,''),urllib.quote(params[key],'')) for key in sorted(params)])
    message = '%s&%s&%s' % (method, urllib.quote(request_token_rul,''), urllib.quote(params_str,''))
    key = '%s&%s' % (consumer_secret, '')
    signature = hmac.new(key,message,hashlib.sha1)
    digest_base64 = signature.digest().encode('base64').strip()
    params['oauth_signature'] = digest_base64
    _url = request_token_rul + '?' + urllib.urlencode(params)
    res = urllib.urlopen(_url).read()
    data = cgi.parse_qs(res)
    return data

  @classmethod
  def get_url(self):
    oa_token_and_secret = self.get_oauth_token_and_secret()

    return 'https://api.twitter.com/oauth/authorize?oauth_token='+oa_token_and_secret['oauth_token'][0]

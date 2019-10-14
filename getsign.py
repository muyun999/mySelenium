import hashlib
import base64


def get_sign(thekey):
    newkey = thekey+'1qaz2wsx'
    m = hashlib.md5()
    b = newkey.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.digest()
    bs64 = base64.b64encode(str_md5)
    print(str(bs64, 'utf-8'))


if __name__ == '__main__':
    get_sign("A2019092800004,A2019101400015")



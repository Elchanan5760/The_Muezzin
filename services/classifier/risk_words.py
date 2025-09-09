import base64


class DecryptWords:
    @staticmethod
    def decrypt(decrypted):
        decrypt = base64.b64decode(decrypted)
        return decrypt
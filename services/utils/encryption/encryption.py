import base64


class Encryption:
    @staticmethod
    def decrypt(decrypted):
        decrypt = base64.b64decode(decrypted)
        return decrypt
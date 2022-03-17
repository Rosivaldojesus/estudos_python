import hashlib

resultado = hashlib.md5(b'Python Security')

print(f'O hash string é: {resultado.hexdigest()}')
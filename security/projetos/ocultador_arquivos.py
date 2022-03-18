"""
BIBLIOTECA: 
- ctypes: Fornece tipos de dados compatíveis com C e permite funções de
 chamada de DLLs bibliotecas compartilhadas.
"""
import ctypes

atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW('arquivo01.txt', atributo_ocultar)

if retorno:
    print('Arquivo foi ocultado')
else: 
    print('Arquivo não foi ocultado')
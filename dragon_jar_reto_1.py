from scapy.layers.inet import IP
from scapy.layers.l2 import *
import pickle
import zlib
import base64


data_comprimida = b'eNprYEouTk4sqNTLSaxMLSrWyzHici3JSC3iKmRIjk/OT0lNLuZKzQMxuAoZI+wZGBgO70dABjDgYHBlYNBgYGRgcGBTPNQcenjaoZbSegaggAiLAwMUBDApMBg5MTAUMkWwAbk5iSWZeYaFzG2FLEGFrK2FbEGF7BrujjftBF4Gc6X6gUBJIUeSHgB54y28'

try:
    decodificado_base_64 = base64.b64decode(data_comprimida)
    print(decodificado_base_64)
    print('\n')
    decodificado_zlib = zlib.decompress(decodificado_base_64)
    print(decodificado_zlib)
    print('\n')
    deserializado_pickle = pickle.loads(decodificado_zlib)
    print(deserializado_pickle)
    print('\n')
    decodificado_scapy_ip = IP(decodificado_zlib)
    decodificado_scapy_ether = Ether(decodificado_zlib)
    print(decodificado_scapy_ip.show())
    print('\n')
    print( decodificado_scapy_ether.show())
except zlib.error:
    print("No se pudo descomprimir el dato zlib")
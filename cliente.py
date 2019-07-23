#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Feito em Python 2.7

import socket
import sys
import struct
import argparse
from timeit import default_timer as timer

parser = argparse.ArgumentParser(description='Menor preco')
parser.add_argument('ip', metavar='ip', type=str, help='IP do servidor.')
parser.add_argument('port', metavar='port', type=int, help='Porta do servidor.')
args = parser.parse_args()

HOST = args.ip
PORT = args.port
timeout = 10 #tempo em segundos, se ultrapassar vai indicar
udp = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_DGRAM):
    af, socktype, proto, canonname, sa = res
    try:
        udp = socket.socket(af, socktype, proto)
    except socket.error as msg:
        udp = None
        continue
    try:
        udp.connect(sa)
    except socket.error as msg:
        udp.close()
        udp = None
        continue
    break
if udp is None:
    print 'Nao foi possivel abrir o socket'
    sys.exit(1)


#parte do jogo, preciso mudar
while True:

    msg = raw_input('Escreva a mensagem: ')
     
    try :
        #Enviando a mensagem
        udp.send(msg)
         
        # Recebendo a resposta de volta (data, addr)
        start = timer() #inicia o timer (10 segundos)
        d = udp.recvfrom(1024)
        udp.settimeout(timeout) #termina o timer

        print 'Resposta do servidor: '
        print d 
     
    except socket.error, msg: # Tratamento de erros
        print 'Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()


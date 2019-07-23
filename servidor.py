#!/usr/bin/env python2
# -*- coding: utf-8 -*-

#Feito em Python 2.7
import socket
import struct
import sys
import string
import argparse
from random import *

parser = argparse.ArgumentParser(description='Servidor do programa melhor preço.')
parser.add_argument('port', metavar='port', type=int, help='Porta do servidor.')
args = parser.parse_args()

# Fonte: https://docs.python.org/2/library/socket.html
HOST = None # Endereco IP do Servidor
PORT = args.port # Porta que o Servidor esta
udp = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC,
                              socket.SOCK_DGRAM, 0, socket.AI_PASSIVE):
    af, socktype, proto, canonname, sa = res
    try:
        udp = socket.socket(af, socktype, proto)
    except socket.error as msg:
        udp = None
        continue
    try:
        udp.bind(sa)       
    except socket.error as msg:
        udp.close()
        udp = None
        continue
    break
if udp is None:
    print 'Nao foi possivel abrir o socket'
    sys.exit(1)
  
def buscarMenor(lista):
    i = float("inf")
    for nr in lst:
        if nr < i:
            i = nr
    return i

listPreco = []
 
while True:
    data, addr = udp.recvfrom(1024) # O tamanho do buffer é 1024 bytes
    print "mensagem recebida:", data
    if not data: 
        break
             
    if data[0] == "D":
        udp.sendto('Servidor confirma recebimento da mensagem: '+ data, addr)
        f = open('workfile.txt', 'a+') #atualizar o arquivo
        f.write(data[1:8])
        f.write('\n')
        f.close()
    else:
        f = open('workfile.txt', 'r+')
        for line in f:
            if line[0] == data[1]:
                preco = line[1:5]
                listPreco.append(preco)
        
        valor = min(map(lambda i: int(i), listPreco))    
        f.close() 
        udp.sendto(str(valor), addr)
        print 'O valor mímino é ' + str(valor)
     
udp.close()
        
#Fechando a conexão com o Cliente
con.close()
    

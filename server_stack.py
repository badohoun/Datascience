# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 00:48:15 2020

@author: BADOHOUN
"""


#!/usr/bin/python
import websocket
from threading import Thread
import timeLe constructeur de l'objet WebSocket prend deux paramètres :

- L'URL du service, composée de :
- Le protocole : ws:// ou wss:// pour une connexion sécurisée.
- L'IP ou le nom de l'hôte.
- Le port d'écoute du serveur.
- La page qui prend en charge le service WebSocket.
- Le sous-protocole utilisé (facultatif).



#Évènements de l'objet WebSocket

#- onopen : déclenché une fois la connexion établie.
#- onmessage : déclenché à la réception d'un message.
#- onerror : déclenché lors de l'apparition d'une erreur.
#- onclose : déclenché une fois la connexion fermée.

def on_message(ws, message):
    print (message)

def on_error(ws, error):
    print (error)

def on_close(ws):
    print ("### closed ###")

def on_open(ws):
    def run(*args):
        for i in range(30000):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print ("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("http://localhost:8888/",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
    ws.on_open = on_open

    ws.run_forever()
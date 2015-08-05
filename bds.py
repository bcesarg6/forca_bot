#Contem todo o gerenciamento do banco de dados

#Importa os BDs da Google

from google.appengine.ext import ndb

#BD que grava as palavras
class PeDs(ndb.Model):
    pecs = ndb.StringProperty(repeated=True)
    tams = ndb.IntegerProperty(repeated=True)

def getNPeD(rnd, rnd2):
    PeD = ndb.Key(PeDs, 'PeDs').get()
    matriz = []
    print len(PeD.tams)
    for i in range(len(PeD.tams)):
        pals = []
        x = PeD.tams[i] if i > 0 else 0
        for j in range(x, PeD.tams[i]):
            print PeD.tams[i]
            pals.append(PeD.pecs[j])
        matriz.append(pals)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print matriz[i][j]
    p = matriz[rnd][rnd2]
    d = matriz[rnd][0]
    ped = [p, d]
    return ped

def updateList(matriz):
    pec = []
    tam = []
    for i in range(len(matriz)):
        tam.append(len(matriz[i]))
        for j in range(len(matriz[i])):
            pec.append(matriz[i][j])
    PeD = PeDs(pecs = pec, tams = tam, id = 'PeDs')
    PeD.put()

class Game(ndb.Model):
    preState = ndb.BooleanProperty(indexed=False, default=False)
    state = ndb.BooleanProperty(indexed=False, default=False)
    jogadores = ndb.StringProperty(repeated=True)
    nomes = ndb.StringProperty(repeated=True)
    adm = ndb.StringProperty(default='noAdm')
    rnd = ndb.IntegerProperty(default=0)
    palavra = ndb.StringProperty(default='noPalavra')
    dica = ndb.StringProperty(default='noDica')
    mascara = ndb.StringProperty(default='noMascara')
    letras = ndb.StringProperty(repeated=True)
    vidas = ndb.IntegerProperty(default = 6)

def menosVida(chat_id):
    v = ndb.Key(Game, chat_id).get()
    v.vidas -= 1
    v.put()

def getVidas(chat_id):
    v = ndb.Key(Game, chat_id).get()
    return v.vidas

def setGame(chat_id):
    g = Game(id = chat_id)
    g.put()

def setPeD(chat_id, ped):
    PeD = ndb.Key(Game, chat_id).get()
    PeD.palavra = ped[0]
    PeD.dica = ped[1]
    PeD.put()

def getPeD(chat_id):
    PeD = ndb.Key(Game, chat_id).get()
    ped = [PeD.palavra, PeD.dica]
    return ped

def setMascara(chat_id, masc):
    msc = ndb.Key(Game, chat_id).get()
    msc.mascara = masc
    msc.put()

def getMascara(chat_id):
    msc = ndb.Key(Game, chat_id).get()
    return msc.mascara

def setLetra(chat_id, letra):
    let = ndb.Key(Game, chat_id).get()
    let.letras.append(letra)
    let.put()

def getLetras(chat_id):
    let = ndb.Key(Game, chat_id).get()
    return let.letras

def setPreGame(chat_id, status):
    GameState = ndb.Key(Game, chat_id).get()
    GameState.preState = status
    GameState.put()

def getPreGame(chat_id):
    GameState = ndb.Key(Game, chat_id).get()
    if GameState:
        return GameState.preState
    return False

def setInGame(chat_id, status):
    GameState = ndb.Key(Game, chat_id).get()
    GameState.state = status
    GameState.put()

def getInGame(chat_id):
    GameState = ndb.Key(Game, chat_id).get()
    if GameState:
        return GameState.state
    return False

def addPlayer(chat_id, uId, uName):
    players = ndb.Key(Game, chat_id).get()
    players.jogadores.append(uId)
    players.nomes.append(uName)
    players.put()

def setAdm(chat_id, uId):
    a = ndb.Key(Game, chat_id).get()
    a.adm = uId
    a.put()

def getuIds(chat_id):
    u = ndb.Key(Game, chat_id).get()
    return u.jogadores

def getPlayers(chat_id):
    p = ndb.Key(Game, chat_id).get()
    return p.nomes

def getAdm(chat_id):
    a = ndb.Key(Game, chat_id).get()
    return a.adm

def setRound(chat_id, rd):
    r = ndb.Key(Game, chat_id).get()
    r.rnd = rd
    r.put()

def getRound(chat_id):
    r = ndb.Key(Game, chat_id).get()
    return r.rnd

def cleanGame(chat_id):
    p = ndb.Key(Game, chat_id).get()
    p.key.delete()

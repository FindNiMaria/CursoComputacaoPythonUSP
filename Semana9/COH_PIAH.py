import re
from itertools import chain

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()

        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    listaconta = [ ]
    soma = sum(abs(a - b) for a, b in zip(as_a, as_b))
    final = soma / 6
    return final

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    tamfrase = 0
    tampal = 0
    tamsent = 0
    numfrases = 0
    numpal = 0
    
    palavras_totais = []
    frases = []
    palavras = []

    sentencas = separa_sentencas(texto)
    numsent = len(sentencas)

    for i in sentencas:
        tamsent = tamsent + len(i) 
        frases = separa_frases(i)
        numfrases = numfrases + len(frases)
        for j in frases:
            tamfrase = tamfrase + len(j)
            palavras = separa_palavras(j)
            for n in palavras:
                tampal = tampal + len(n)
            palavras_totais = palavras_totais + palavras

    palavras_diferentes = n_palavras_diferentes(palavras_totais)
    palavras_unicas = n_palavras_unicas(palavras_totais)
    numpal = len(palavras_totais)


    #Tamanho médio de palavra é a soma dos tamanhos das palavras dividida pelo número total de palavras.    
    TamMedPal = tampal / numpal #tmp = tam_p/nptot
    #Relação Type-Token é o número de palavras diferentes dividido pelo número total de palavras.
    TypeToken = palavras_diferentes / numpal #rTyp_Tok = npdif/nptot
    #Razão Hapax Legomana é o número de palavras que aparecem uma única vez dividido pelo total de palavras.
    HapaxLegomana = palavras_unicas / numpal #rHap_Leg = np_unic/nptot
    #Tamanho médio de sentença é a soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças.
    TamMedSent = tamsent / numsent
    #Complexidade de sentença é o número total de frases divido pelo número de sentenças
    complexsent = numfrases / numsent 
    #Tamanho médio de frase é a soma do número de caracteres em cada frase dividida pelo número de frases no texto
    TamMedFrase = tamfrase / numfrases
    
   
    return [TamMedPal, TypeToken, HapaxLegomana, TamMedSent, complexsent, TamMedFrase]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    coh_piah = []
    ass_tx = []
    for x in textos:
        ass_tx.append(calcula_assinatura(x))


    for x in ass_tx:
        coh_piah.append(compara_assinatura(ass_cp, x))
        
    minimo = float(min(coh_piah))

    resposta = coh_piah.index(minimo)
    return resposta + 1

def __main__():    
    ass_cp = le_assinatura()
    textos = le_textos()
    resultado = avalia_textos(textos, ass_cp)
    print("O autor do texto", resultado, "está infectado com COH-PIAH")

__main__()
palavra_secreta = 'programar'
letras_acertadas = ''
while True:

    letra_digitada = input('tente advinhar a palavra secreta :')


    
    if len(letra_digitada) > 1:
        print('digite apenas uma letra')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    
    palavra_formada = ''
    
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'      
    print('palavra formada' , palavra_formada)

    if palavra_formada == palavra_secreta:
        print('parabéns voce acertou a palavra do dia')
        print(f'a palavra formada era: {palavra_formada}')

        break
    

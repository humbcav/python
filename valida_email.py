def inicio_validação(email: str) -> None:
    print("========================================================================")
    print(f"Início da validação do e-mail: {email}")
    print("========================================================================")
    
def resultado_final(resultado: bool) -> None:
    """gera o resultado final da avaliação do e-mail

    Args:
        resultado (bool): true para e-mail valido
    """
    if resultado:
        escreve_verde("+++++++++++++++++++++++++++++++++++")
        escreve_verde("+      E-mail valido!             +")
        escreve_verde("+++++++++++++++++++++++++++++++++++")
    else:
        escreve_vermelho("+++++++++++++++++++++++++++++++++++")
        escreve_vermelho("+       E-mail inválido           +")
        escreve_vermelho("+++++++++++++++++++++++++++++++++++")
def escreve_vermelho(texto: str) -> None:
    """função para escrever em vermelho

    Args:
        texto (str): texto a ser impresso
    """
    VERMELHO = "\033[31m"
    RESET = "\033[0m"
    NEGRITO = "\033[1m"
    print(f"{VERMELHO}{NEGRITO}{texto}{RESET}")

def escreve_verde(texto: str) -> None:
    """função para escrever em verde

    Args:
        texto (str): texto a ser impresso
    """
    VERDE = "\033[32m"
    RESET = "\033[0m"
    NEGRITO = "\033[1m"
    print(f"{VERDE}{NEGRITO}{texto}{RESET}")
    
def validar_email(email: str) -> bool:
    """Fun

    Args:
        email (str): e-mail a ser validado

    Returns:
        bool: True se o e-mail for valido
    """
    retorno = False

    #print do ínicio da validação
    inicio_validação(email)
    
    #valida que não deve ter espaços
    if " " in email:
        escreve_vermelho("validação de espaços: falhou")
        ret2 = False
    else:
        escreve_verde("validação de espaços: ok")
        ret2 = True
 
    #valida se tem apenas um @.
    if email.count("@") !=1:
        escreve_vermelho("validação do @ único: falhou")
        ret1 = False
        escreve_vermelho("não é possível separar usuário e domínio sem o @")
        escreve_vermelho("teste suspenso!")
    else:
        escreve_verde("validação do @ único: ok")
        ret1 = True    
 
    #valida que usuários e domínio não podem estar vazios
    if ret1:
        usuario, dominio = email.split("@")

    if ret1:
        if not usuario or not dominio:
            escreve_vermelho("validação usuário e domínio não vazios: falhou")
            ret3 = False
        else:
            escreve_verde("validação usuário e domínio não vazios: ok")
            ret3 = True
    
    #domínio deve ter pelo menos um ponto
    if ret1:
        if dominio.count(".") < 1:
            escreve_vermelho("validação domínio com pelo menos um ponto: falhou")
            ret4 = False
        else:
            escreve_verde("validação domínio com pelo menos um ponto: ok")
            ret4 = True
    
    #usuário deve ter apenas letras, números e pontos
    if ret1:
        if not usuario.isalnum():
            escreve_vermelho("validação usuário só pode ter letras, números e pontos: falhou")
            ret5 = False
        else:
            escreve_verde("validação usuário só pode ter letras, números e pontos: ok")
            ret5 = True
    
    #domínio deve ter apenas letras, números, pontos e hífen
    if ret1:
        if not (dominio.isalpha or dominio.isdigit or dominio in ['.', '-']):
            escreve_vermelho("validação domínio deve ter apenas letras, números, pontos e hífen: falhou")
            ret6 = False
        else:
            escreve_verde("validação domínio deve ter apenas letras, números, pontos e hífen: ok")
            ret6 = True
    
    #domínio não pode iniciar ou terminar com ponto
    if ret1:
        if dominio.startswith(".") or dominio.endswith("."):
            escreve_vermelho("validação domínio não pode iniciar ou terminar com ponto: falhou")
            ret7 = False
        else:
            escreve_verde("validação domínio não pode iniciar ou terminar com ponto: ok")
            ret7 = True

    #usuário não pode iniciar ou terminar com ponto
    if ret1:
        if usuario.startswith(".") or usuario.endswith("."):
            escreve_vermelho("validação usuário não pode iniciar ou terminar com ponto: falhou") 
            ret8 = False
        else:
            escreve_verde("validação usuário não pode iniciar ou terminar com ponto: ok")
            ret8 = True

    if ret1 and ret2 and ret3 and ret4 and ret5 and ret6 and ret7 and ret8:
        retorno = True
        
    resultado_final(retorno)
    return retorno

validar_email("humbcavbr@gmail.com") 
validar_email("@gmail.com") 
validar_email(".humbcavbr@gmail.com") 
validar_email("humbcavbr@gmail.com.") 
validar_email("humbcavbr@gmail.com.br") 
validar_email("humbcavbr@") 
validar_email("humbcavbr_gmail.com") 
validar_email("humbcavbr_1@gmail.com") 
validar_email("humbcavbr123@gmail.com")    
validar_email("humbcav-br@gmail.com") 
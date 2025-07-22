#pip install types-requests
#pip install requests
#pip install httpx (evolução da biblioteca requests)

#import requests

import httpx

urlGET = "https://jsonplaceholder.typicode.com/posts/1"

def do_GET(url: str) -> None:
    """faz a chamada do GET para a url proposta no exercício

    Args:
        url (str): _endereço a ser chamado no GET, conforme descrição
    """
 
    response = httpx.get(url)
    dados = response.json()
    print(response.status_code, dados)    

urlPOST = "https://jsonplaceholder.typicode.com/posts"

bodyPOST = {
"title": "foo",
"body": "bar",
"userId": 1
}
def do_POST(url: str) -> None:
    """faz a chamada do POST para a url proposta no exercício

    Args:
        url (str): _endereço a ser chamado no POST, conforme descrição
    """
    response = httpx.post(url, data=bodyPOST)
    dados = response.json()
    print(response.status_code, dados)
    
def main() -> None:
    try:
        do_GET(urlGET)
        do_POST(urlPOST)
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    main()  
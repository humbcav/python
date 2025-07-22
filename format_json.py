import httpx
url = "https://assets.breatheco.de/apis/fake/sample/project1.php"

def faz_chamada(url: str) -> None:
    response = httpx.get(url)
    dados = response.json()
    name = dados["name"]
    first_image = dados["images"][0]    
    print(f"Projeto: {name}, Imagem: {first_image}")

def main() -> None:
    faz_chamada(url)

if __name__ == "__main__":
    main()  
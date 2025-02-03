# Escavador - API de Extração de Elementos HTML

Este projeto oferece uma API simples construída com Flask para extrair todos os elementos HTML de uma página web fornecida. Ele retorna os nomes das tags, IDs e textos de todos os elementos encontrados na página.

**Aviso**: Esta API é somente para fins de desenvolvimento e não deve ser usada em produção sem as devidas medidas de segurança e otimização.

## Como Iniciar o Projeto

### 1. Clonar o Repositório

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/escavador.git
cd escavador
```

### 2. Criar um Ambiente Virtual (opcional, mas recomendado)

Crie um ambiente virtual para isolar as dependências:

```
python3 -m venv .venv
source .venv/bin/activate  # No Windows use .venv\Scripts\activate
```

### 3. Instalar as Dependências

Instale as dependências necessárias:

```
pip install -r requirements.txt
```

### 4. Iniciar o Servidor

Para iniciar o servidor localmente, execute o seguinte comando:

```
python app.py
```

O servidor será iniciado em http://127.0.0.1:3000 por padrão.

### 5. Acessando a API

Você pode acessar a API no seguinte endpoint:

```
GET /escavar?url={URL_DA_PAGINA}
```

Exemplo:

```
http://127.0.0.1:3000/escavar?url=https://www.exemplo.com
```

A resposta será um JSON contendo os elementos encontrados na página HTML fornecida, com os campos tag, id e texto.

### 6. Usando o Servidor Remoto

Você também pode acessar a API através do servidor remoto:

```
https://escavador-a0li.onrender.com/escavar?url={URL_DA_PAGINA}
```

Exemplo:

```
https://escavador-a0li.onrender.com/escavar?url=https://www.exemplo.com
```

### Bibliotecas Usadas

	•	Flask: Framework web para Python, usado para criar a API.
	•	Requests: Biblioteca para fazer requisições HTTP.
	•	BeautifulSoup4: Biblioteca para parsing de HTML, usada para extrair os elementos da página.

### AVISO

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais informações.

### Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais informações.









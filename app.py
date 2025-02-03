from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/escavar', methods=['GET'])
def extrair_elementos():
    url = request.args.get('url') 
    
    if not url:
        return jsonify({'error': 'URL não fornecida'}), 400

    try:
        response = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0",
            "Accept-Encoding": "gzip, deflate, br",
        })
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        elementos = []

        for elemento in soup.find_all(True):  # Pega todos os elementos da página
            tag = elemento.name  # Nome da tag (ex: div, span, h1, etc.)
            id_elemento = elemento.get('id')  # ID do elemento (se existir)
            texto = elemento.get_text(strip=True)  # Texto dentro do elemento

            elementos.append({
                'tag': tag,
                'id': id_elemento if id_elemento else None,  # Evita IDs vazios
                'texto': texto if texto else None  # Evita textos vazios
            })

        return jsonify({
            'url': url,
            'elementos': elementos
        })

    except requests.exceptions.Timeout:
        return jsonify({'error': 'Tempo de resposta excedido'}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({'error': 'Erro ao buscar os dados', 'details': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=3000)
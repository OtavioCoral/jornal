from flask import Flask, render-template, request, redirect
import json


app = flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.rput('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        conteudo = request.form['conteudo'] #conteudo = noticias

    with open('noticias.json', 'r') as file:
            dados = json.load(file)

    noticias = dados.get('noticias',[])

    proximo_id = len(noticias) +1

    nova noticia = {
        'id': proximo_id,
        'titulo': titulo,
        'conteudo':conteudo
    }

    noticias_append(nova_noticia)

    dados['noticias'] = noticias 
    with open('noticias.json', 'w') as file:
                json.dump(dados, file, indent =4)

        return redirect('/cadastrar')

    return render_template('cadastrar.html')


@app.route('/noticias')
def noticias():
    with open('noticias.json', 'r') as file:
        dados = json.load(file)

    noticias = dados.get('noticias', [])

    return render_template('noticias.html', noticias = noticias)

if __name__== '__main__':
    app.run(debug = True)
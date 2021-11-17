from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Filme:
    def __init__(self, nome, categoria, ano):
        self.nome = nome
        self.categoria = categoria
        self.ano = ano

filme1 = Filme('Us', 'Terror', '2019')
filme2 = Filme('Booksmart', 'Comédia', '2019')
filme3 = Filme('Star Wars', 'Ficção', '1977')
filme4 = Filme('Legalmente Loira', 'Comédia', '2001')
filme5 = Filme('Um Lugar Silencioso', 'Terror', '2018')
lista = [filme1, filme2, filme3, filme4, filme5]

@app.route('/filmes', methods=['POST', 'GET',])

def retorna_filmes():   
    return render_template('lista.html', titulo='Filmes', filmes=lista)        

def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    ano = request.form['ano']
    filme = Filme(nome, categoria, ano)
    lista.append(filme)
    return redirect('/filmes')
    
app.run()
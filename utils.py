from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome="Rodrigues", idade=39)
    print(pessoa)
    pessoa.save()


def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(Pessoas)
    pessoa = Pessoas.query.filter_by(nome="Felipe").first()
    print(pessoa.idade)
    
            
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Rodrigues").first()
    pessoa.nome = "Felipe"
    pessoa.save()
    
    
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome="Felipe").first()
    pessoa.delete()
    
    
        

if __name__ == '__main__':
    # insere_pessoas()
    consulta_pessoas()
    # altera_pessoa()
    # exclui_pessoa()
    
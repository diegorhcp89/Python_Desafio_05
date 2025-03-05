'''
OPEN CLOSED PRINCIPLE

Imagine que uma clínica veterinária tem seu sistema próprio para aprovação de exames. No primeiro momento, ela tem um método para
verificar exame de sangue. Em outro ela adiciona exame por raio-x. Notamos no código que, conforme a clínica adiciona exames,
deverão adicionar uma validação para o exame. O que aumentaria a complexidade do código e a manutenção do mesmo.

A solução deste caso pode ser feita com o princípio aberto-fechado (Open Closed Principle). 
Utilizando do conceito do OCP, crie uma interface e classes que implementam a mesma para que, caso a clínica necessite de um novo
tipo de exame, uma nova classe seja adicionada, implementando métodos de uma interface padrão para exames.

'''


# Interface (ou classe abstrata) que define o contrato para todos os exames
class Exame:
    def verifica_condicoes(self):
        pass

# Implementação específica para exame de sangue
class ExameSangue(Exame):
    def verifica_condicoes(self):
        print("Verificando condições do exame de sangue...")
        return True  # Exemplo: sempre aprova o exame de sangue

# Implementação específica para exame de raio-x
class ExameRaioX(Exame):
    def verifica_condicoes(self):
        print("Verificando condições do exame de raio-x...")
        return True  # Exemplo: sempre aprova o exame de raio-x

# Implementação específica para exame de ultrassom
class ExameUltrassom(Exame):
    def verifica_condicoes(self):
        print("Verificando condições do exame de ultrassom...")
        return True  # Exemplo: sempre aprova o exame de ultrassom

# Classe que aprova exames
class AprovaExame:
    def do_work(self, exame: Exame) -> None:
        if exame.verifica_condicoes():
            print(f"Exame do tipo {exame.__class__.__name__} aprovado!")
        else:
            print(f"Exame do tipo {exame.__class__.__name__} reprovado.")

# Exemplo de uso
exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()
exame_ultrassom = ExameUltrassom()

aprovador = AprovaExame()

# Aprovação dos exames
aprovador.do_work(exame_sangue)
aprovador.do_work(exame_raio_x)
aprovador.do_work(exame_ultrassom)



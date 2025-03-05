# Python_Desafio_05

# Projeto de Gerenciamento de Tarefas e Aprovação de Exames

## Descrição
Este repositório contém duas implementações principais em Python aplicando os princípios SOLID:
1. **TaskHandler** - Sistema de gerenciamento de tarefas
2. **AprovaExame** - Sistema de verificação e aprovação de exames

## Princípios SOLID Aplicados

### 1. **Single Responsibility Principle (SRP)**
Cada classe tem uma única responsabilidade:
- `TaskHandler`: Gerencia tarefas e notificações.
- `Exame` e suas subclasses: Cada uma trata um tipo específico de exame.
- `AprovaExame`: Responsável apenas por aprovar exames.

### 2. **Open/Closed Principle (OCP)**
As classes podem ser estendidas sem modificação:
- Novos tipos de exames podem ser adicionados sem alterar `AprovaExame`.
- Novos métodos de gestão de tarefas podem ser adicionados sem modificar `TaskHandler`.

### 3. **Liskov Substitution Principle (LSP)**
As subclasses podem substituir a classe base sem alterar o comportamento esperado:
- `ExameSangue`, `ExameRaioX` e `ExameUltrassom` podem ser usadas no lugar de `Exame` sem impactar `AprovaExame`.

### 4. **Interface Segregation Principle (ISP)**
Cada classe tem apenas os métodos que realmente precisa:
- `TaskHandler` separa suas responsabilidades em diferentes métodos privados.
- `Exame` define apenas um método necessário para suas subclasses (`verifica_condicoes`).

### 5. **Dependency Inversion Principle (DIP)**
Módulos de alto nível dependem de abstrações e não de implementações concretas:
- `AprovaExame` depende da abstração `Exame`, permitindo flexibilidade na adção de novos tipos de exame sem modificar sua lógica.

## Tecnologias Utilizadas
- Python 3
- Programação Orientada a Objetos
- Princípios SOLID

## Como Executar
1. Clone este repositório:
   ```sh
   git clone https://github.com/seu-repositorio.git
   ```
2. Acesse o diretório do projeto:
   ```sh
   cd seu-repositorio
   ```
3. Execute os scripts conforme necessário:
   ```sh
   python3 task_handler.py
   python3 exame_aprovador.py
   ```

## Contribuição
Sinta-se à vontade para abrir issues e pull requests para melhorias e sugestões.

## Licença
Este projeto está sob a licença MIT.


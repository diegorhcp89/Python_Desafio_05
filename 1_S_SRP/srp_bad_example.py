'''
SINGLE RESPONSABILITY PRINCIPLE

Note que nessa classe, temos várias ações e responsabilidades. O que torna a manutenção, usabilidade e até a performance ruins.

Seguindo o conceito do Princípio da Responsabilidade única, organize essa classe e, se necessário, crie outras 
classes com suas devidas responsabilidades.

'''

class TaskHandler:
    def handle(self, task: str, task_id: int, new_task: str, message: str, data: str) -> None:
        """
        Método principal que orquestra todas as ações.
        """
        if self.__verify_input_data(task, task_id, new_task, message, data):
            self.__connect_to_api()
            self.__create_task(task)
            self.__update_task(task_id, new_task)
            self.__remove_task(task_id)
            self.__send_notification(message)
            report = self.__generate_report(data)
            self.__send_report(report)
        else:
            self.__raise_error('Dados inválidos')

    def __verify_input_data(self, task: str, task_id: int, new_task: str, message: str, data: str) -> bool:
        """
        Verifica se os dados de entrada são válidos.
        """
        return (
            isinstance(task, str) and
            isinstance(task_id, int) and
            isinstance(new_task, str) and
            isinstance(message, str) and
            isinstance(data, str)
        )

    def __connect_to_api(self) -> None:
        """
        Conecta à API.
        """
        print("Conectando à API...")
        # Lógica de conexão à API

    def __create_task(self, task: str) -> None:
        """
        Cria uma nova tarefa.
        """
        print(f"Criando tarefa: {task}")
        # Lógica para criar uma tarefa

    def __update_task(self, task_id: int, new_task: str) -> None:
        """
        Atualiza uma tarefa existente.
        """
        print(f"Atualizando tarefa {task_id} para: {new_task}")
        # Lógica para atualizar uma tarefa

    def __remove_task(self, task_id: int) -> None:
        """
        Remove uma tarefa existente.
        """
        print(f"Removendo tarefa: {task_id}")
        # Lógica para remover uma tarefa

    def __send_notification(self, message: str) -> None:
        """
        Envia uma notificação.
        """
        print(f"Enviando notificação: {message}")
        # Lógica para enviar notificações

    def __generate_report(self, data: str) -> str:
        """
        Gera um relatório com os dados fornecidos.
        """
        print(f"Gerando relatório com os dados: {data}")
        # Lógica para gerar relatórios
        return "Relatório gerado"

    def __send_report(self, report: str) -> None:
        """
        Envia o relatório gerado.
        """
        print(f"Enviando relatório: {report}")
        # Lógica para enviar relatórios

    def __raise_error(self, message: str) -> Exception:
        """
        Lança uma exceção com a mensagem de erro fornecida.
        """
        raise Exception(message)


# Exemplo de uso
if __name__ == "__main__":
    task_handler = TaskHandler()
    try:
        task_handler.handle(
            task="Nova tarefa",
            task_id=1,
            new_task="Tarefa atualizada",
            message="Notificação importante!",
            data="Dados para o relatório"
        )
    except Exception as e:
        print(f"Erro: {e}")

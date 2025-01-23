
## Implementação ruim
class Employee:
    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position

    def calculate_salary(self):
        # Calcula o salário com impostos e benefícios
        tax = self.salary * 0.2
        benefits = 1000 if self.position == "senior" else 500
        return self.salary - tax + benefits

    def save_employee_to_database(self):
        # Salva os dados do funcionário no banco de dados
        print(f"Salvando funcionário {self.name} no banco de dados...")
        # código para salvar no banco de dados

    def generate_employee_report(self):
        # Gera relatório em PDF do funcionário
        print(f"Gerando relatório PDF para {self.name}...")
        # código para gerar PDF

    def send_email(self, message):
        # Envia email para o funcionário
        print(f"Enviando email para {self.name}: {message}")
        # código para enviar email




## Implementação boa
class CaculatorSalary:
    def calculate_salary(self, employee):
        # Calcula o salário com impostos e benefícios
        tax = employee.salary * 0.2
        benefits = 1000 if employee.position == "senior" else 500
        return employee.salary - tax + benefits
    

class EmployeeRepository:
    def save(self, employee):
        # Salva os dados do funcionário no banco de dados
        print(f"Salvando funcionário {employee.name} no banco de dados...")
        # código para salvar no banco de dados

class ReportGenerator:
    def generate(self, employee):
        # Gera relatório em PDF do funcionário
        print(f"Gerando relatório PDF para {employee.name}...") 
        # código para gerar PDF

class EmailService:
    def send(self, message):
        # Envia email para o funcionário
        print(f"Enviando email para {self.name}: {message}")
        # código para enviar email

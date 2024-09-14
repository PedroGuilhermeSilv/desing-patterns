# Padrões de Design (Design Patterns) - Checklist

## 1. Padrões Criacionais (Creational Patterns)
- [ ] **Singleton**: Garante que uma classe tenha apenas uma instância e fornece um ponto global de acesso a ela. 
- [x] **Factory Method**: Define uma interface para criar objetos, permitindo que subclasses alterem o tipo de objeto criado. [API Para conversão de arquivos (csv,xslx, json)](https://github.com/PedroGuilhermeSilv/api-convert-files)
- [ ] **Abstract Factory**: Fornece uma interface para criar famílias de objetos relacionados sem especificar classes concretas.
- [ ] **Builder**: Separa a construção de um objeto complexo da sua representação, permitindo diferentes representações.
- [ ] **Prototype**: Cria novos objetos clonando uma instância existente.

## 2. Padrões Estruturais (Structural Patterns)
- [ ] **Adapter**: Permite que classes com interfaces incompatíveis trabalhem juntas, encapsulando a interface de uma classe existente.
- [ ] **Bridge**: Separa a abstração de sua implementação, permitindo que variem independentemente.
- [ ] **Composite**: Composição de objetos em estruturas de árvore para representar hierarquias parte-todo.
- [ ] **Decorator**: Adiciona responsabilidades a objetos dinamicamente, sem afetar outros objetos da mesma classe.
- [ ] **Facade**: Fornece uma interface simplificada para um subsistema complexo.
- [ ] **Flyweight**: Reduz o número de objetos criados reutilizando objetos que compartilham o mesmo estado.
- [ ] **Proxy**: Fornece um substituto ou ponto de acesso para controlar o acesso a um objeto.

## 3. Padrões Comportamentais (Behavioral Patterns)
- [ ] **Chain of Responsibility**: Permite que mais de um objeto tenha a oportunidade de tratar uma solicitação ao encadeá-los.
- [ ] **Command**: Encapsula uma solicitação como um objeto, permitindo filas, logs e operações reversíveis.
- [ ] **Interpreter**: Define uma representação para a gramática de uma linguagem e um interpretador para as sentenças.
- [ ] **Iterator**: Fornece uma maneira de acessar os elementos de um agregado de objetos sequencialmente sem expor sua estrutura.
- [ ] **Mediator**: Define um objeto que encapsula como um conjunto de objetos interage, promovendo acoplamento fraco.
- [ ] **Memento**: Captura e restaura o estado interno de um objeto sem violar o encapsulamento.
- [ ] **Observer**: Define uma dependência um-para-muitos entre objetos para notificar e atualizar automaticamente seus dependentes.
- [ ] **State**: Permite que um objeto altere seu comportamento quando seu estado interno muda.
- [ ] **Strategy**: Define uma família de algoritmos, encapsula cada um deles e os torna intercambiáveis.
- [ ] **Template Method**: Define o esqueleto de um algoritmo, delegando alguns passos para as subclasses.
- [ ] **Visitor**: Representa uma operação a ser realizada nos elementos de uma estrutura de objetos sem alterar suas classes.

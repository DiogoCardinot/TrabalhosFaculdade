# Classe para representar um estado do automato
class State:
    # Inicializa um estado com um nome e uma opção de ser estado de aceitação
    def __init__(self, name, is_accepting=False):
        self.name = name # nome do estado
        self.is_accepting = is_accepting # indica se é estado de aceitação
        self.transitions = {} # dicionario para armazenar transições (input_symbol -> next_state)
    

    # Adiciona uma transição ao estado
    def add_transition(self, input_symbol, next_state):
        # Verifica se o simbolo de entrada é uma lista
        if type(input_symbol) == list:
            # Itera sobre a lista de simbolos de entrada
            for i in input_symbol:
                # Adiciona cada transição ao estado
                self.transitions[i] = next_state
        else:
            # Adiciona a transição ao estado
            self.transitions[input_symbol] = next_state
    
    # Define a representação do objeto como string
    def __str__(self):
        return self.name

# Classe para representar o automato de pilha
class PushdownAutomata:
    # Inicializa um autômato de pilha com estado inicial, estados de aceitação, simbolos de entrada e simbolos de pilha
    def __init__(self, start_state, accept_states, input_symbols, stack_symbols):
        self.start_state = start_state # estado inicial
        self.accept_states = accept_states # estados de aceitação
        self.input_symbols = input_symbols # simbolos de entrada permitidos
        self.stack_symbols = stack_symbols # simbolos da pilha permitidos
        self.current_state = start_state # estado atual
        self.stack = ["$"] # pilha iniciada com o símbolo de fim de expressão

    # Verifica se o estado atual é um estado de aceitação
    def is_accepting(self):
        return self.current_state in self.accept_states

    # Efetua a transição para o próximo estado a partir do simbolo de entrada
    def next_state(self, input_symbol):
        # Verifica se há uma transição definida para o simbolo de entrada
        transition = self.current_state.transitions.get(input_symbol)
        if transition:
            self.current_state = transition
        else:
            raise Exception("Transicao Invalida")

    # Empilha um simbolo na pilha
    def push_stack(self, stack_symbol):
        self.stack.append(stack_symbol)

    # Desempilha um simbolo da pilha
    def pop_stack(self):
        return self.stack.pop()

    # Verifica se a expressão é reconhecida pelo automato
    def parse_expression(self, expression):
        # Remove espaços em branco da expressão
        expression = expression.strip()
        
        # Itera sobre a expressão
        for symbol in expression:
            # Verifica se o simbolo é válido
            if symbol not in self.input_symbols:
                # Lança uma exceção se o simbolo não for válido
                raise Exception(f"Simbolo de entrada invalido: {symbol}")
            # Efetua a transição para o próximo estado
            self.next_state(symbol)
            
            # Empilha um parênteses "("
            if symbol == "(":
                self.push_stack(symbol)
            elif symbol == ")":
                # Desempilha o último simbolo empilhado
                op = self.pop_stack()
                # Verifica se o simbolo desempilhado é o parênteses esperado "("
                if op != "(":
                    raise Exception("Parenteses Incompativeis")
        
        # Verifica se todos os parênteses foram corretamente fechados
        if len(self.stack) > 1:
            raise Exception("Parenteses Incompativeis")
        else:
            self.next_state(self.stack[0])
            
        # Verifica se o autômato está em um estado de aceitação
        if self.is_accepting():
            return True
        else:
            return False



start_state = State("Start")
accept_state = State("Accept", True)
int_state = State("See_INT")
op_state = State("See_OPERADOR")


operators = ["+", "-", "*", "/"]
operands = list(map(str, range(10)))
input_symbols = operators + operands + ["(", ")"]

stack_symbols = operators + ["$"]

start_state.add_transition("(", start_state)

start_state.add_transition(operands, int_state)

int_state.add_transition(operators, start_state)

int_state.add_transition(")", int_state)
int_state.add_transition("$", accept_state)


automata = PushdownAutomata(start_state, [accept_state], input_symbols, stack_symbols)

expression = "(2+1)"
result = automata.parse_expression(expression)
if result:
    print('Expressao reconhecida')
else:
    print('Expressao nao reconhecida')

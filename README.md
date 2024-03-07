# COPIAR-pyperclip.py

Funcionalidades
O aplicativo permite ao usuário manipular texto em três campos: "Texto", "Opção 1" e "Opção 2".

Bibliotecas Utilizadas
O aplicativo faz uso de tkinter para a interface gráfica e pyperclip para manipular a área de transferência.

> pip install pyperclip

> pip install tkinter

Interface Gráfica
A interface inclui campos de entrada e botões para copiar e colar texto.

Operações
Botões "Copiar Opção 1" e "Copiar Opção 2": Permitem copiar o texto das caixas de entrada correspondentes para a área de transferência.
Botão "Colar": Cola o texto da área de transferência na caixa de entrada "Texto".
Métodos Principais
copiar_opcao1(): Copia o texto da caixa de entrada "Opção 1".
copiar_opcao2(): Copia o texto da caixa de entrada "Opção 2".
colar(): Cola o texto da área de transferência na caixa de entrada "Texto".
Inicialização
O programa inicia a janela principal e inicia o loop de eventos do Tkinter.

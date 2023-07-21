
#! modularização = dividir um programa grande para aumentar a elegibilidade. Facilitar a manutenção

# Pacotes, em outras linguagens de programacao se chama biblioteca

# Pacote = pasta q contem modulos(arquivos.py), q podem serem separados por assuntos. Usamos isso quando o projeto ficar grande

# cada pasta com modulo ou o pacote precisa ter um arquivo __init__.py

# ? inicialmente eu n to sabendo para q serve esse __init__.py, o professor tá colando todos os codigos dentro desse arquivo, mas eu ja vi gente usando deixando ele em branco e usando outro arquivo

#! a gente coloca __init__ quando estiver fazendo pacotes
'''
Se você remover o __init__.pyarquivo, o Python não procurará mais submódulos dentro desse diretório; portanto, as tentativas de importar o módulo falharão.

O __init__.pyarquivo geralmente está vazio, mas pode ser usado para exportar partes selecionadas do pacote com um nome mais conveniente, manter funções de conveniência etc. etc. Dado o exemplo acima, o conteúdo do módulo init pode ser acessado como

no entanto, se você tiver setup.pye usar find_packages(), é necessário ter __init__.pyem todos os diretórios. Veja stackoverflow.com/a/56277323/7127824
'''

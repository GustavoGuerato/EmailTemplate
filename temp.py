from string import Template
from datetime import datetime
import os

try:

    diretorio_script = os.path.dirname(os.path.realpath(__file__))

    caminho_template = os.path.join(diretorio_script, 'email.html')

    if not os.path.exists(caminho_template):
        raise FileNotFoundError(f"Erro: O arquivo 'email.html' não foi encontrado em '{diretorio_script}'")

    with open(caminho_template, 'r') as html:
        template = Template(html.read())
        data_atual = datetime.now().strftime('%d/%m/%Y')
        corpo_msg = template.substitute(nome='Gustavo Guerato', data=data_atual)
        print("Mensagem gerada com sucesso:", corpo_msg)

except Exception as e:
    print(f"Ocorreu um erro: {e}")

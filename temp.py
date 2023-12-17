from string import Template
from datetime import datetime

with open('template.html', 'r') as html:
    template = Template(html.read())
    dia = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Gustavo Guerato', data=dia)

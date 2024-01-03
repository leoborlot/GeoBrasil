# GeoBrasil
import unicodedata
import re
from functools import wraps

def verifica_tipo(*tipos_permitidos):
    def decorator(func):
        @wraps(func)
        def wrapper(self, entrada, *args, **kwargs):
            # Se a entrada estiver vazia, retorna vazio
            if not entrada:
                return ""

            tipo_entrada = self.identificar_tipo(entrada)
            if tipo_entrada not in tipos_permitidos:
                return f"Erro: entrada do tipo '{tipo_entrada}' não é permitida para este método."
            return func(self, entrada, *args, **kwargs)
        return wrapper
    return decorator


class GeoBrasil:
    def __init__(self):

        self.regioes = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']

        self.estados = {
            'AC': 'Acre', 'AL': 'Alagoas', 'AP': 'Amapá', 'AM': 'Amazonas', 
            'BA': 'Bahia', 'CE': 'Ceará', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo',
            'GO': 'Goiás', 'MA': 'Maranhão', 'MT': 'Mato Grosso', 'MS': 'Mato Grosso do Sul',
            'MG': 'Minas Gerais', 'PA': 'Pará', 'PB': 'Paraíba', 'PR': 'Paraná', 
            'PE': 'Pernambuco', 'PI': 'Piauí', 'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte',
            'RS': 'Rio Grande do Sul', 'RO': 'Rondônia', 'RR': 'Roraima', 'SC': 'Santa Catarina',
            'SP': 'São Paulo', 'SE': 'Sergipe', 'TO': 'Tocantins'
        }

        self.ddd_to_estado = {
            '68': 'Acre', '82': 'Alagoas', '96': 'Amapá', '92': 'Amazonas',
            '71': 'Bahia', '73': 'Bahia', '74': 'Bahia', '75': 'Bahia', '77': 'Bahia',
            '85': 'Ceará', '88': 'Ceará', '61': 'Distrito Federal',
            '27': 'Espírito Santo', '28': 'Espírito Santo',
            '62': 'Goiás', '64': 'Goiás', '98': 'Maranhão', '99': 'Maranhão',
            '65': 'Mato Grosso', '66': 'Mato Grosso',
            '67': 'Mato Grosso do Sul', '31': 'Minas Gerais', '32': 'Minas Gerais',
            '33': 'Minas Gerais', '34': 'Minas Gerais', '35': 'Minas Gerais',
            '37': 'Minas Gerais', '38': 'Minas Gerais', '91': 'Pará', '93': 'Pará', '94': 'Pará',
            '83': 'Paraíba', '41': 'Paraná', '42': 'Paraná', '43': 'Paraná', '44': 'Paraná',
            '45': 'Paraná', '46': 'Paraná', '81': 'Pernambuco', '87': 'Pernambuco',
            '86': 'Piauí', '89': 'Piauí', '21': 'Rio de Janeiro', '22': 'Rio de Janeiro',
            '24': 'Rio de Janeiro', '84': 'Rio Grande do Norte',
            '54': 'Rio Grande do Sul', '55': 'Rio Grande do Sul', '51': 'Rio Grande do Sul',
            '53': 'Rio Grande do Sul', '69': 'Rondônia', '95': 'Roraima',
            '47': 'Santa Catarina', '48': 'Santa Catarina', '49': 'Santa Catarina',
            '11': 'São Paulo', '12': 'São Paulo', '13': 'São Paulo', '14': 'São Paulo',
            '15': 'São Paulo', '16': 'São Paulo', '17': 'São Paulo', '18': 'São Paulo',
            '19': 'São Paulo', '79': 'Sergipe', '63': 'Tocantins'
        }

        self.estado_to_ddd = {estado: [ddd for ddd, est in self.ddd_to_estado.items() if est == estado]
                              for estado in self.estados.values()}
        
        self.nome_to_uf = {nome: uf for uf, nome in self.estados.items()}

        self.ufc_to_estado = [
            {'codigo_uf': 12, 'uf': 'AC', 'unidade_federativa': 'Acre'},
            {'codigo_uf': 27, 'uf': 'AL', 'unidade_federativa': 'Alagoas'},
            {'codigo_uf': 13, 'uf': 'AM', 'unidade_federativa': 'Amazonas'},
            {'codigo_uf': 16, 'uf': 'AP', 'unidade_federativa': 'Amapá'},
            {'codigo_uf': 29, 'uf': 'BA', 'unidade_federativa': 'Bahia'},
            {'codigo_uf': 23, 'uf': 'CE', 'unidade_federativa': 'Ceará'},
            {'codigo_uf': 53, 'uf': 'DF', 'unidade_federativa': 'Distrito Federal'},
            {'codigo_uf': 32, 'uf': 'ES', 'unidade_federativa': 'Espírito Santo'},
            {'codigo_uf': 52, 'uf': 'GO', 'unidade_federativa': 'Goiás'},
            {'codigo_uf': 31, 'uf': 'MG', 'unidade_federativa': 'Minas Gerais'},
            {'codigo_uf': 50, 'uf': 'MS', 'unidade_federativa': 'Mato Grosso do Sul'},
            {'codigo_uf': 51, 'uf': 'MT', 'unidade_federativa': 'Mato Grosso'},
            {'codigo_uf': 15, 'uf': 'PA', 'unidade_federativa': 'Pará'},
            {'codigo_uf': 25, 'uf': 'PB', 'unidade_federativa': 'Paraíba'},
            {'codigo_uf': 26, 'uf': 'PE', 'unidade_federativa': 'Pernambuco'},
            {'codigo_uf': 22, 'uf': 'PI', 'unidade_federativa': 'Piauí'},
            {'codigo_uf': 41, 'uf': 'PR', 'unidade_federativa': 'Paraná'},
            {'codigo_uf': 33, 'uf': 'RJ', 'unidade_federativa': 'Rio de Janeiro'},
            {'codigo_uf': 24, 'uf': 'RN', 'unidade_federativa': 'Rio Grande do Norte'},
            {'codigo_uf': 43, 'uf': 'RS', 'unidade_federativa': 'Rio Grande do Sul'},
            {'codigo_uf': 42, 'uf': 'SC', 'unidade_federativa': 'Santa Catarina'},
            {'codigo_uf': 28, 'uf': 'SE', 'unidade_federativa': 'Sergipe'},
            {'codigo_uf': 35, 'uf': 'SP', 'unidade_federativa': 'São Paulo'},
            {'codigo_uf': 17, 'uf': 'TO', 'unidade_federativa': 'Tocantins'},
            {'codigo_uf': 21, 'uf': 'MA', 'unidade_federativa': 'Maranhão'},
            {'codigo_uf': 11, 'uf': 'RO', 'unidade_federativa': 'Rondônia'},
            {'codigo_uf': 14, 'uf': 'RR', 'unidade_federativa': 'Roraima'}
        ]

        self.estado_info = {
            'AC': {'Nome': 'Acre', 'Região': 'Norte'},
            'AL': {'Nome': 'Alagoas', 'Região': 'Nordeste'},
            'AP': {'Nome': 'Amapá', 'Região': 'Norte'},
            'AM': {'Nome': 'Amazonas', 'Região': 'Norte'},
            'BA': {'Nome': 'Bahia', 'Região': 'Nordeste'},
            'CE': {'Nome': 'Ceará', 'Região': 'Nordeste'},
            'DF': {'Nome': 'Distrito Federal', 'Região': 'Centro-Oeste'},
            'ES': {'Nome': 'Espírito Santo', 'Região': 'Sudeste'},
            'GO': {'Nome': 'Goiás', 'Região': 'Centro-Oeste'},
            'MA': {'Nome': 'Maranhão', 'Região': 'Nordeste'},
            'MT': {'Nome': 'Mato Grosso', 'Região': 'Centro-Oeste'},
            'MS': {'Nome': 'Mato Grosso do Sul', 'Região': 'Centro-Oeste'},
            'MG': {'Nome': 'Minas Gerais', 'Região': 'Sudeste'},
            'PA': {'Nome': 'Pará', 'Região': 'Norte'},
            'PB': {'Nome': 'Paraíba', 'Região': 'Nordeste'},
            'PR': {'Nome': 'Paraná', 'Região': 'Sul'},
            'PE': {'Nome': 'Pernambuco', 'Região': 'Nordeste'},
            'PI': {'Nome': 'Piauí', 'Região': 'Nordeste'},
            'RJ': {'Nome': 'Rio de Janeiro', 'Região': 'Sudeste'},
            'RN': {'Nome': 'Rio Grande do Norte', 'Região': 'Nordeste'},
            'RS': {'Nome': 'Rio Grande do Sul', 'Região': 'Sul'},
            'RO': {'Nome': 'Rondônia', 'Região': 'Norte'},
            'RR': {'Nome': 'Roraima', 'Região': 'Norte'},
            'SC': {'Nome': 'Santa Catarina', 'Região': 'Sul'},
            'SP': {'Nome': 'São Paulo', 'Região': 'Sudeste'},
            'SE': {'Nome': 'Sergipe', 'Região': 'Nordeste'},
            'TO': {'Nome': 'Tocantins', 'Região': 'Norte'}
        }

        self.reg_to_estados = {
            'Norte': ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 'Tocantins'],
            'Nordeste': ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe'],
            'Centro-Oeste': ['Distrito Federal', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul'],
            'Sudeste': ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 'São Paulo'],
            'Sul': ['Paraná', 'Rio Grande do Sul', 'Santa Catarina']
        }

    @verifica_tipo('sigla')
    def estado_from_uf(self, uf):
        if self.identificar_tipo(uf) != 'sigla':
            return "Erro: entrada deve ser uma sigla"
        return self.estados.get(uf.upper(), "Estado não encontrado")

    @verifica_tipo('extenso')
    def uf_from_estado(self, estado_nome):
        return self.nome_to_uf.get(estado_nome, "Sigla não encontrada")

    @verifica_tipo('ddd')
    def estado_from_ddd(self, ddd):
         if not ddd.isdigit():
            return "Erro: entrada deve ser um DDD numérico"

    @verifica_tipo('ddd')
    def ddd_from_estado(self, estado_nome):
        return self.estado_to_ddd.get(estado_nome, [])

    @verifica_tipo('ddd')
    def ufc_from_uf(self, uf):
        for estado in self.ufc_to_estado:
            if estado['uf'] == uf.upper():
                return estado['codigo_uf']
        return "Código UF não encontrado"

    @verifica_tipo('regiao')
    def reg_from_estado(self, uf):
        uf = uf.upper()
        return self.estado_info.get(uf, {}).get('Região', 'Região não encontrada')

    @verifica_tipo('sigla', 'extenso')
    def estados_from_reg(self, regiao):
        return self.reg_to_estados.get(regiao, [])

    @verifica_tipo('sigla', 'extenso')
    def estado_info(self, uf):
        uf = uf.upper()
        return self.estado_info.get(uf, "Informação não encontrada")

    @verifica_tipo('sigla', 'extenso')
    def short_up(self, entrada):
        tipo = self.identificar_tipo(entrada)
        if tipo == 'sigla':
            return entrada.upper()
        elif tipo == 'extenso':
            sigla = self.uf_from_estado(entrada)
            return sigla.upper() if sigla != "Sigla não encontrada" else sigla
        else:
            return "Não encontrado"

    @verifica_tipo('sigla', 'extenso')
    def short_low(self, entrada):
        tipo = self.identificar_tipo(entrada)
        if tipo == 'sigla':
            return entrada.lower()
        elif tipo == 'extenso':
            sigla = self.uf_from_estado(entrada)
            return sigla.lower() if sigla != "Sigla não encontrada" else sigla
        else:
            return "Não encontrado"

    @verifica_tipo('sigla', 'extenso')
    def extend_up(self, entrada):
        tipo = self.identificar_tipo(entrada)
        if tipo == 'sigla':
            estado = self.estado_from_uf(entrada)
            return estado.upper() if estado != "Estado não encontrado" else estado
        elif tipo == 'extenso':
            return entrada.upper()
        else:
            return "Não encontrado"

    @verifica_tipo('sigla', 'extenso')
    def extend_low(self, entrada):
        tipo = self.identificar_tipo(entrada)
        if tipo == 'sigla':
            estado = self.estado_from_uf(entrada)
            return estado.lower() if estado != "Estado não encontrado" else estado
        elif tipo == 'extenso':
            return entrada.lower()
        else:
            return "Não encontrado"

    @verifica_tipo('sigla', 'extenso')
    def extend_slug(self, entrada):
        tipo = self.identificar_tipo(entrada)
        if tipo in ['sigla', 'extenso']:
            nome_estado = self.estado_from_uf(entrada) if tipo == 'sigla' else entrada
            nome_estado = unicodedata.normalize('NFD', nome_estado).encode('ascii', 'ignore').decode('utf-8')
            return nome_estado.replace(' ', '_').lower()
        else:
            return "Não encontrado"

    
    def identificar_tipo(self, entrada):
        entrada_normalizada = unicodedata.normalize('NFD', entrada).encode('ascii', 'ignore').decode('utf-8')
        if re.fullmatch(r'[A-Z]{2}', entrada):
            return 'sigla'
        elif re.fullmatch(r'\d{2}', entrada):
            return 'DDD'
        elif entrada.title() in self.regioes:
            return 'regiao'
        elif entrada.title() in self.estados.values():
            return 'extenso'
        elif entrada_normalizada.replace(' ', '_').lower() == entrada:
            return 'slug'
        return 'desconhecido'
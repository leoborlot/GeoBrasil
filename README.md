# GeoBrasil - Manual do Usuário

Este documento serve como um guia para a utilização da classe `EstadosBrasil`, que oferece métodos para acessar e transformar informações sobre os estados do Brasil.

## Métodos Disponíveis

### 1. `estado_from_uf(self, uf)`
Retorna o nome completo do estado com base na sua sigla (UF).
- **Parâmetros**: `uf` (string) - A sigla do estado.
- **Retorno**: Nome completo do estado ou "Estado não encontrado".

**Exemplo**:
```python
print(GeoBrasil.estado_from_uf("RJ"))
# Saída: Rio de Janeiro
```

### 2. `estado_from_ddd(self, ddd)`
Retorna o nome do estado com base no DDD fornecido.
- **Parâmetros**: `ddd` (string) - O DDD do estado.
- **Retorno**: Nome do estado ou "DDD não encontrado".

**Exemplo**:
```python
print(GeoBrasil.estado_from_ddd("21"))
# Saída: Rio de Janeiro
```

### 3. `ddd_from_estado(self, estado_nome)`
Retorna os códigos DDD associados ao nome do estado.
- **Parâmetros**: `estado_nome` (string) - O nome completo do estado.
- **Retorno**: Lista de códigos DDD ou lista vazia.

**Exemplo**:
```python
print(GeoBrasil.ddd_from_estado("Bahia"))
# Saída: ['71', '73', '74', '75', '77']
```

### 4. `ufc_from_uf(self, uf)`
Retorna o código de identificação da UF com base na sigla.
- **Parâmetros**: `uf` (string) - A sigla do estado.
- **Retorno**: Código de identificação da UF ou "Código UF não encontrado".

**Exemplo**:
```python
print(GeoBrasil.ufc_from_uf("SP"))
# Saída: 35
```

### 5. `reg_from_estado(self, uf)`
Retorna a região do Brasil a que o estado pertence.
- **Parâmetros**: `uf` (string) - A sigla do estado.
- **Retorno**: Nome da região ou "Região não encontrada".

**Exemplo**:
```python
print(GeoBrasil.reg_from_estado("MG"))
# Saída: Sudeste
```

### 6. `estados_from_reg(self, regiao)`
Retorna uma lista de estados pertencentes a uma região específica.
- **Parâmetros**: `regiao` (string) - O nome da região.
- **Retorno**: Lista de estados ou lista vazia.

**Exemplo**:
```python
print(GeoBrasil.estados_from_reg("Sul"))
# Saída: ['Paraná', 'Rio Grande do Sul', 'Santa Catarina']
```

### 7. `estado_info(self, uf)`
Retorna informações detalhadas sobre o estado.
- **Parâmetros**: `uf` (string) - A sigla do estado.
- **Retorno**: Dicionário com informações do estado ou "Informação não encontrada".

**Exemplo**:
```python
print(GeoBrasil.estado_info("PR"))
# Saída: {'Nome': 'Paraná', 'Região': 'Sul'}
```

### 8. `short_up(self, entrada)`
Converte a entrada para a sigla do estado em letras maiúsculas.
- **Parâmetros**: `entrada` (string) - Nome ou sigla do estado.
- **Retorno**: Sigla do estado em maiúsculas.

**Exemplo**:
```python
print(GeoBrasil.short_up("paraná"))
# Saída: PR
```

### 9. `short_low(self, entrada)`
Converte a entrada para a sigla do estado em letras minúsculas.
- **Parâmetros**: `entrada` (string) - Nome ou sigla do estado.
- **Retorno**: Sigla do estado em minúsculas.

**Exemplo**:
```python
print(GeoBrasil.short_low("RJ"))
# Saída: rj
```

### 10. `extend_up(self, entrada)`
Converte a entrada para o nome completo do estado em letras maiúsculas.
- **Parâmetros**: `entrada` (string) - Nome ou sigla do estado.
- **Retorno**: Nome do estado em maiúsculas.

**Exemplo**:
```python
print(GeoBrasil.extend_up("sc"))
# Saída: SANTA CATARINA
```

### 11. `extend_low(self, entrada)`
Converte a entrada para o nome completo do estado em letras minúsculas.
- **Parâmetros**: `entrada` (string) - Nome ou sigla do estado.
- **Retorno**: Nome do estado em minúsculas.

**Exemplo**:
```python
print(GeoBrasil.extend_low("PA"))
# Saída: pará
```

### 12. `extend_slug(self, entrada)`
Converte a entrada para uma versão 'slug' do nome do estado: em minúsculas, sem acentos e com espaços substituídos por '_'.
- **Parâmetros**: `entrada` (string) - Nome ou sigla do estado.
- **Retorno**: Versão 'slug' do nome do estado.

**Exemplo**:
```python
print(GeoBrasil.extend_slug("Rio de Janeiro"))
# Saída: rio_de_janeiro
```

## Conclusão
A classe `EstadosBrasil` oferece uma variedade de métodos para acessar e transformar informações sobre os estados do Brasil de maneiras úteis e práticas, facilitando o manejo de dados geográficos e de telecomunicações em aplicações diversas.

## 📋 Sumário

- [📋 Sumário](#-sumário)

- [🔎 Sobre](#-sobre)

- [🛠 Tecnologias usadas](#-tecnologias-usadas)

- [⚙ Como executar este projeto](#-como-executar-este-projeto)

- [🛠 Execução dos Testes Unitários](#-execução-dos-testes-unitários)

- [📚 Documentação](#-documentação)

- [📁 Estrutura do projeto](#-estrutura-do-projeto)



## 🔎 Sobre

O presente projeto consiste da implementação de uma simples api para executar operações matemáticas de somar e dividir.

## 🛠 Tecnologias usadas

Para o desenvolvimento deste projeto, as seguintes tecnologias foram utilizadas:

- python 3.11
- FastAPI (Desenvolvimento de API REST)
- Poetry (gerenciador de pacotes python)
- Pytest (gerenciador de testes)
- Docker e docker-compose (gerenciador de containers)

## ⚙ Como executar este projeto
PS: por ser um projeto simples, não é necessário informar variáveis de ambiente.

Let's Borah Nessa!!!
- Clone o repositório:

```sh
$ git clone https://github.com/lucasousa/calc.git
```

- Entre na pasta:

```sh
$ cd calc/
```

Configurando com docker-compose

``` bash
$ docker-compose build
```

``` bash
$ docker-compose up -d
```

``` bash
$ docker-compose logs -f
```

Ou se preferir usar com ambiente virtual venv
- Crie o ambiente virtual:

``` sh
$ python3.11 -m venv env
#você pode adicionar seu Interpreter Settings, caso use o PyCharm
```

- Atualize o pip e instale o poetry:

``` sh
$ pip install --upgrade pip
$ pip install poetry
```

- Instale as dependências:

```sh
$ poetry install
```


Por fim, execute a aplicação:
- Se você estiver usando docker, na etapa anterior já deve ter subido a aplicação, assim basta mostrar os logs:
```sh
docker-compose logs -f
```

- Executando com env:

```sh
python src/main.py
```

## 🛠 Execução dos Testes Unitários
Garanta que as etapas anteriores estejam funcionando. Em seguida, basta executar o seguinte comando:

```sh
$ pytest src/tests
```

## 📚 Documentação
A documentação deste projeto e especificação da api está disponível em:
Ao acessar algum dos links abaixo é possível obter os detalhes de como consumir a API.

```sh
$ http://localhost:8000/redoc/ #ou
$ http://localhost:8000/docs/
```

## 📁 Estrutura do projeto

Este projeto está estruturado de modo que todos os arquivos python estão dentro de uma pasta chamada de src. Abaixo temos algumas definições:

- tests: deve conter os testes unitários de toda a aplicação;
- schemas: contém os esquemas de dados de entradas e os serializers para dados de saída;
- services: contém as implementações de regras de negócio dos endpoints;
- controllers: contém a definição dos endpoints
# Projeto de Automações

Automação desenvolvida em Python para integração com o Google Sheets utilizando as APIs do Google, uma conta de serviço e a biblioteca `gspread`.

O projeto tem como objetivo automatizar a leitura, processamento e atualização de dados de uma planilha do Google Sheets utilizando Python e Pandas.

## Objetivo

O projeto realiza a integração entre Python e Google Sheets para:

* Conectar uma aplicação Python a uma planilha do Google Sheets;
* Autenticar utilizando uma conta de serviço;
* Ler dados da planilha;
* Transformar os dados em um DataFrame do Pandas;
* Filtrar alunos de acordo com o status;
* Criar e atualizar uma segunda aba com os resultados filtrados.

## Tecnologias utilizadas

* Python 3.10+
* Pandas
* gspread
* Google Auth
* python-dotenv
* Google Sheets API
* Google Drive API

## Estrutura do projeto

```text
projeto-automacoes/
│
├── main.py
├── .env
├── credenciais.json
├── .gitignore
└── README.md
```

### `main.py`

Arquivo principal responsável pela execução da automação.

### `.env`

Arquivo utilizado para armazenar configurações do projeto, como o caminho das credenciais e o ID da planilha.

Exemplo:

```env
GOOGLE_CREDENTIALS=credenciais.json
GOOGLE_SHEETS_ID=SEU_ID_DA_PLANILHA
```

> Os valores reais não devem ser publicados no repositório.

### `credenciais.json`

Arquivo de credenciais da conta de serviço utilizada para autenticação com os serviços do Google.

Por motivos de segurança, esse arquivo não deve ser versionado.

### `.gitignore`

Responsável por impedir que arquivos sensíveis ou desnecessários sejam enviados ao repositório.

## Configuração

### 1. Instalar as dependências

Execute:

```bash
pip install gspread pandas google-auth python-dotenv
```

Caso seja necessário utilizar um proxy:

```bash
pip install gspread pandas google-auth python-dotenv --proxy http://10.15.54.158:8080
```

### 2. Configurar o Google Cloud

No Google Cloud, é necessário possuir um projeto com as seguintes APIs habilitadas:

* Google Sheets API
* Google Drive API

O projeto utiliza uma conta de serviço chamada `robo-python`.

### 3. Configurar as credenciais

O arquivo JSON gerado para a conta de serviço deve ser colocado na raiz do projeto.

O caminho do arquivo deve ser informado no `.env`:

```env
GOOGLE_CREDENTIALS=credenciais.json
```

### 4. Configurar a planilha

O ID da planilha deve ser informado no `.env`:

```env
GOOGLE_SHEETS_ID=SEU_ID_DA_PLANILHA
```

A planilha também precisa ser compartilhada com o endereço de e-mail da conta de serviço `robo-python`.

## Funcionamento

O fluxo da automação é:

```text
Google Sheets
      │
      ▼
Conta de serviço
robo-python
      │
      ▼
Google APIs
      │
      ▼
gspread
      │
      ▼
DataFrame Pandas
      │
      ▼
Filtragem dos dados
      │
      ▼
Aba "Pendentes"
```

## Execução

Para executar a automação:

```bash
python main.py
```

Se a conexão estiver funcionando corretamente, o programa exibirá uma mensagem semelhante a:

```text
Conexão realizada com sucesso!
Nome da planilha: Nome da sua planilha
```

## Segurança

As credenciais do Google não devem ser compartilhadas ou versionadas.

Os seguintes arquivos devem permanecer fora do Git:

```text
.env
credenciais.json
```

Por isso, eles devem estar presentes no `.gitignore`.

## Próximas etapas

O projeto será evoluído para:

* Leitura completa dos alunos;
* Conversão dos dados para DataFrame;
* Filtro de alunos com status `Pendente`;
* Criação da aba `Pendentes`;
* Atualização automática dos resultados no Google Sheets;
* Melhorias de tratamento de erros;
* Organização e reutilização das funções de automação.

## Autor

**André Heber Azeredo Coutinho**

Projeto acadêmico/prático desenvolvido para estudo de automação, integração com APIs e manipulação de dados utilizando Python.

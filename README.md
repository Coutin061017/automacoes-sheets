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
├── requirements.txt
└── README.md
```

### `main.py`

Arquivo principal responsável pela execução da automação.

Os arquivos `.env`, `credenciais.json` e `.gitignore` são mantidos **apenas localmente** e não fazem parte dos arquivos publicados neste repositório.

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

### `.gitignore` (somente local)

Responsável por impedir que arquivos sensíveis ou desnecessários sejam enviados ao repositório. Por preferência do autor, ele é mantido na máquina, sem publicação no GitHub.

## Configuração

### 1. Instalar as dependências

Execute:

```bash
pip install -r requirements.txt
```

Caso seja necessário utilizar um proxy:

```bash
pip install -r requirements.txt --proxy http://SEU_PROXY:PORTA
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

## Validações existentes

- Confere as configurações necessárias no `.env` local e a existência do JSON de credenciais.
- Verifica se a aba de origem contém dados e uma coluna chamada `Status`.
- Identifica `Pendente` mesmo com diferenças de maiúsculas e espaços.
- Mantém o cabeçalho mesmo quando não há pendências.
- Ajusta o tamanho da aba de saída e evita imprimir dados pessoais no terminal.

A atualização usa argumentos nomeados `values` e `range_name`, compatíveis com o `gspread` 6.

## Próximas melhorias

Testes de integração com planilha fictícia, logging e tratamento detalhado de falhas de rede.

## Dados de demonstração

Use uma planilha de testes com dados fictícios. O link de uma planilha específica foi retirado da documentação pública por precaução com a privacidade.


# Dockerfile Python para utilizar com oracle ADB

Exemplo de Dockfile para criar um container que roda código python com a biblioteca cx_oracle.

Esse é um exemplo de Dockerfile que utiliza uma imagem python:3.8-slim como base para a criação da imagem pedrochristo/pythonoracle que já tem as configurações do Instant CLient da Oracle, que possibilida a conexão ao banco através de JDBC.

A imagem pedrochristo/pythonoracle já tem o TNS_ADMIN criado e o arquivo sqlnet.ora, que é necessário para a conexão com o Autonomous Database.

## Como utilizar:

Na mesma pasta do seu Dockerfile é necessário ter a Wallet do ADB em formato .zip, seu código python e o arquivo de requiremtes.

Esse arquivo é um exemplo de multistage para criar uma imagem mais leve.

É necessário apenas substituir o nome do arquivo.py e o nome da Waller.zip.

## Recomendações

Para não expor o usuário e senha do banco, recomendo a utilização dos mesmos, não direto no código, mas sim nas variáveis de ambiente.

Podem ser setados direto no Dockerfile ou executando o docker passando essas variáveis através da tag --env.
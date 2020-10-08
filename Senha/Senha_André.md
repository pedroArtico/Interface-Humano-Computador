# Senha
 



## *id:[SENH_ANDR_74]* Problema 74: Falta de verifica��o de formul�rio.
**Ocorre na p�gina**: *Senha > Cadastre aqui > Caso voc� n�o tenha recebido a senha inicial clique aqui.*

Falta de verifica��o do que foi digitado em todos os campos.
## Fotos
![https://drive.google.com/open?id=12v61bxr4LjJkJ0vz_9tFMvuHyAQZ4GOL](../../imgs/ANDR�_12v61bxr4LjJkJ0vz_9tFMvuHyAQZ4GOL.png)

## Considera��es

### Heur�stica ferida: 5�
**Heur�stica ferida**: 5 - Preven��o de erro

**Justificativa**: Como os campos n�o s�o verificados antes da submiss�o o usu�rio n�o � impedido de causar erros no sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SENH_ANDR_75]* Problema 75: Mensagem de erro pouco esclarecedora.
**Ocorre na p�gina**: *Senha > Cadastre aqui > Caso voc� n�o tenha recebido a senha inicial clique aqui.*

A mensagem de erro n�o esclarece quais s�o os campos num�ricos, ou se os campos de data s�o num�ricos ou de data, um usu�rio mais leigo n�o entenderia o que � um erro de convers�o �o sistema quer converter o que no que?�
Outro exemplo � que posso colocar letras em campos ditos num�ricos - se o sistema me permite isso por que ocorreria um erro se fosse colocado �mil novecentos e noventa e sete� ao inv�s de �1997�?.
## Fotos
![https://drive.google.com/open?id=1W6rGbaDI4d6wKv7cx122dq9pbdph0nyU](../../imgs/ANDR�_1W6rGbaDI4d6wKv7cx122dq9pbdph0nyU.png)

## Considera��es

### Heur�stica ferida: 9�
**Heur�stica ferida**: 9 - Auxiliar usu�rios a reconhecer, diagnosticar e recuperar a��es erradas

**Justificativa**: A mensagem de erro n�o � clara e n�o aponta para solu��es de forma direta.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_ANDR_76]* Problema 76: Mensagem de erro incorreta.
**Ocorre na p�gina**: *Senha > Cadastre aqui > Caso voc� n�o tenha recebido a senha inicial clique aqui.*

Ao tentar submeter um formul�rio vazio o erro mostrado � de convers�o de campos num�ricos, a mensagem n�o ajuda o usu�rio.
## Fotos
![https://drive.google.com/open?id=1kqUqhmA7Qexvwfpq167n7yq9OG0S7EDV](../../imgs/ANDR�_1kqUqhmA7Qexvwfpq167n7yq9OG0S7EDV.png)

## Considera��es

### Heur�stica ferida: 9�
**Heur�stica ferida**: 9 - Auxiliar usu�rios a reconhecer, diagnosticar e recuperar a��es erradas

**Justificativa**: A mensagem de erro n�o reflete o que ocorreu realmente, confundindo o usu�rio.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastr�fico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SENH_ANDR_77]* Problema 77: P�gina de ajuda n�o ajuda.
**Ocorre na p�gina**: *Senha > Cadastre aqui > Caso voc� n�o tenha recebido a senha inicial clique aqui > D�vidas.*

A ajuda fala apenas sobre como preencher nomes, n�o explica demais campos ou o que o sistema faz..
## Fotos
![https://drive.google.com/open?id=1gk0KKlLL_Tc7LLIvJAUaa3zZhU8rKobN](../../imgs/ANDR�_1gk0KKlLL_Tc7LLIvJAUaa3zZhU8rKobN.png)

![https://drive.google.com/open?id=1EoaEwsG7dVG9i3FEl3pIT9XyYutMdSyl](../../imgs/ANDR�_1EoaEwsG7dVG9i3FEl3pIT9XyYutMdSyl.png)

## Considera��es

### Heur�stica ferida: 10�
**Heur�stica ferida**: 10 - Ajuda e documenta��o

**Justificativa**: A p�gina de ajuda � insuficiente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_ANDR_78]* Problema 78: P�gina inexistente.
**Ocorre na p�gina**: *Senha > Alterar senha > Alunos > Orienta��es gerais sobre senha.*

Ao clicar no link o usu�rio � levado para uma p�gina dizendo que a p�gina que queria encontrar n�o foi encontrada.
## Fotos
![https://drive.google.com/open?id=1vAw22T9YgCbfDdTluHngKfbWPQzqABxr](../../imgs/ANDR�_1vAw22T9YgCbfDdTluHngKfbWPQzqABxr.png)

![https://drive.google.com/open?id=1lpV1o4X7U0X4sc3pu-66UYePV5YmlD_E](../../imgs/ANDR�_1lpV1o4X7U0X4sc3pu-66UYePV5YmlD_E.png)

![https://drive.google.com/open?id=1ExUjV7dYwsU6u8rPBM8fHmr7YQ7fsgDN](../../imgs/ANDR�_1ExUjV7dYwsU6u8rPBM8fHmr7YQ7fsgDN.png)

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: O usu�rio perde liberdade visto que certos links levam para p�ginas que n�o existem.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_ANDR_79]* Problema 79: Baixo contraste quando alto contraste � ativado.
**Ocorre na p�gina**: *Senha > Alterar senha > Alunos > Onde retirar ou trocar senha > Alto contraste.*

� dif�cil ler a tabela mostrada caso a p�gina esteja no modo alto contraste.
## Fotos
![https://drive.google.com/open?id=1PldOc3yXruoZs0J0q-O2giFtQ3-uInxx](../../imgs/ANDR�_1PldOc3yXruoZs0J0q-O2giFtQ3-uInxx.png)

![https://drive.google.com/open?id=1v9QZNwZh7YUtvy5TqcPD9yKRa4Ns-qzT](../../imgs/ANDR�_1v9QZNwZh7YUtvy5TqcPD9yKRa4Ns-qzT.png)

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: O design da p�gina quando em alto contraste impede a visualiza��o do conte�do.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)


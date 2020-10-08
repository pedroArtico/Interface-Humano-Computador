# Senha
 



## *id:[SENH_GRUP_20]* Problema 20: P�gina de ajuda n�o ajuda
**Ocorre na p�gina**: *Senha > cadastre aqui > caso voc� n�o tenha recebido a senha inicial clique aqui > d�vidas*

A ajuda fala apenas sobre como preencher nomes, n�o explica demais campos ou o que o sistema faz.
## Fotos
![https://drive.google.com/open?id=1gk0KKlLL_Tc7LLIvJAUaa3zZhU8rKobN](../../imgs/GRUPO_1gk0KKlLL_Tc7LLIvJAUaa3zZhU8rKobN.png)

![https://drive.google.com/open?id=1EoaEwsG7dVG9i3FEl3pIT9XyYutMdSyl](../../imgs/GRUPO_1EoaEwsG7dVG9i3FEl3pIT9XyYutMdSyl.png)

## Considera��es

### Heur�stica ferida: 10�
**Heur�stica ferida**: 10 - Ajuda e documenta��o

**Justificativa**: A p�gina de ajuda � insuficiente.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SENH_GRUP_21]* Problema 21: Mensagem de erro incorreta
**Ocorre na p�gina**: *Senha > cadastre aqui > caso voc� n�o tenha recebido a senha inicial clique aqui*

Ao tentar submeter um formul�rio vazio o erro mostrado � de convers�o de campos num�ricos, a mensagem n�o ajuda o usu�rio.
## Fotos
![https://drive.google.com/open?id=1kqUqhmA7Qexvwfpq167n7yq9OG0S7EDV](../../imgs/GRUPO_1kqUqhmA7Qexvwfpq167n7yq9OG0S7EDV.png)

## Considera��es

### Heur�stica ferida: 9�
**Heur�stica ferida**: 9 - Auxiliar usu�rios a reconhecer, diagnosticar e recuperar a��es erradas

**Justificativa**: A mensagem de erro n�o reflete o que ocorreu realmente, confundindo o usu�rio.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastr�fico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SENH_GRUP_22]* Problema 22: Mensagem de erro pouco esclarecedora
**Ocorre na p�gina**: *Senha > cadastre aqui > caso voc� n�o tenha recebido a senha inicial clique aqui*


A mensagem de erro n�o esclarece quais s�o os campos num�ricos, ou se os campos de data s�o num�ricos ou de data um usu�rio leigo n�o entenderia o que � um erro de convers�o.
Outro exemplo � a possibilidade de colocar letras em campos num�ricos.
## Fotos
![https://drive.google.com/open?id=1W6rGbaDI4d6wKv7cx122dq9pbdph0nyU](../../imgs/GRUPO_1W6rGbaDI4d6wKv7cx122dq9pbdph0nyU.png)

## Considera��es

### Heur�stica ferida: 9�
**Heur�stica ferida**: 9 - Auxiliar usu�rios a reconhecer, diagnosticar e recuperar a��es erradas

**Justificativa**: A mensagem de erro n�o � clara e n�o aponta para solu��es de forma direta.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastr�fico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SENH_GRUP_23]* Problema 23: Falta de verifica��o de formul�rio
**Ocorre na p�gina**: *Senha > cadastre aqui > caso voc� n�o tenha recebido a senha inicial clique aqui*

Falta de verifica��o do que foi digitado em todos os campos.
## Fotos
![https://drive.google.com/open?id=12v61bxr4LjJkJ0vz_9tFMvuHyAQZ4GOL](../../imgs/GRUPO_12v61bxr4LjJkJ0vz_9tFMvuHyAQZ4GOL.png)

## Considera��es

### Heur�stica ferida: 5�
**Heur�stica ferida**: 5 - Preven��o de erro

**Justificativa**: Como os campos n�o s�o verificados antes da submiss�o o usu�rio n�o � impedido de causar erros no sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastr�fico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SENH_GRUP_34]* Problema 34: Falta de verifica��o de campos.
**Ocorre na p�gina**: *Senha > Alterar Senha.*

Ao tentar alterar a senha, inserindo um username com caracteres emoji, n�o h� verifica��o de teste para valida��o.
## Fotos
![https://drive.google.com/open?id=1HmTIB4a9zdkAt2iQBN4qSVNQZIvbnUuW](../../imgs/GRUPO_1HmTIB4a9zdkAt2iQBN4qSVNQZIvbnUuW.png)

## Considera��es

### Heur�stica ferida: 5�
**Heur�stica ferida**: 5 - Preven��o de erro

**Justificativa**:  A heuristica correta � a 5, pois n�o foram tomadas iniciativas por parte dos desenvolvedores para evitar que os usu�rios digitassem caracteres indesejados.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastr�fico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SENH_GRUP_35]* Problema 35: Erro de processamento ao tentar alterar senha.
**Ocorre na p�gina**: *Senha > Alterar Senha.*

Ao tentar realizar a troca de senha, caso o usu�rio insira caracteres do tipo emoji no username, ocorre um erro de processamento do qual n�o se tem informa��es.
## Fotos
![https://drive.google.com/open?id=1wFLgggGlkSuAVbaF42eagL1FQ8vgq1y0](../../imgs/GRUPO_1wFLgggGlkSuAVbaF42eagL1FQ8vgq1y0.png)

## Considera��es

### Heur�stica ferida: 9�
**Heur�stica ferida**: 9 - Auxiliar usu�rios a reconhecer, diagnosticar e recuperar a��es erradas

**Justificativa**: O usu�rio cometeu um erro e n�o h� indica��o de como soluciona-lo de maneira r�pida e efetiva.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastr�fico (Muito grave, deve ser reparado de qualquer forma -)


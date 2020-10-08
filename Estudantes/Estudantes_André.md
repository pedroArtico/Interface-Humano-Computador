# Estudantes
 



## *id:[ESTU_ANDR_1]* Problema 1: Op��es com conte�dos amb�guos.
**Ocorre na p�gina**: *Estudantes > Menu Estudantes.*

No menu estudantes existem v�rias op��es amb�guas, o que dificulta para o usu�rio descobrir qual sistema precisa acessar para fazer sua tarefa. Por exemplo: existem menus diferentes com os itens "Relat�rio de matr�cula" e "Atestado de Matr�cula", seriam a mesma coisa ou n�o? 
O item de "Relat�rio de Matr�cula" est� na se��o "Altera��o de matr�cula", em "Servi�os Acad�micos" h� o item "Matr�cula", nesse caso o sistema de altera��o de matr�cula tamb�m gera relat�rios? No quadro com a op��o "Matr�cula", alterar a matr�cula n�o faria parte j� de um sistema "Matr�cula"? Existe uma separa��o que confunde o usu�rio.
O sistema SIGA tamb�m tem op��es referentes � matr�cula, o usu�rio n�o tem como saber qual op��o precisa usar.
## Fotos
![https://drive.google.com/open?id=17TRAvl8CIB4wThbZYKkBrO3mkLdybmoT](../../imgs/ANDR�_17TRAvl8CIB4wThbZYKkBrO3mkLdybmoT.png)

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: Existe na mesma tela quadros com informa��es repetidas/inconsistentes/incoerentes dificultando com que o usu�rio encontre a op��o que deseja.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ESTU_ANDR_2]* Problema 2: Nomes semelhantes.
**Ocorre na p�gina**: *Estudantes > Menu Estudantes.*

N�o deixa claro a diferen�a entre desist�ncia de matr�cula e cancelamento de matr�cula, ao cancelar minha matr�cula numa disciplina estou desistindo dela?.
## Fotos
![https://drive.google.com/open?id=1QfvM-IRONMgKKKxvHuATL6-x4FR3BkKE](../../imgs/ANDR�_1QfvM-IRONMgKKKxvHuATL6-x4FR3BkKE.png)

![https://drive.google.com/open?id=1JMYd_dUuMtxJDaQJE1GeB_13gvf4Eliz](../../imgs/ANDR�_1JMYd_dUuMtxJDaQJE1GeB_13gvf4Eliz.png)

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: Op��es amb�guas confundem o usu�rio em termos de qual sistema ele deve acessar.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTU_ANDR_3]* Problema 3: Menu separado para "Altera��o de Matr�cula."
**Ocorre na p�gina**: *Estudantes > Menu Estudantes.*

Coisas relacionadas com a matr�cula s�o servi�os acad�micos, por que existe um menu a parte apenas para a altera��o da matr�cula? 
N�o se pode fazer uma altera��o de matr�cula pelo servi�o em "Servi�os Acad�micos"?
Um usu�rio que fez uma matr�cula pelos "Servi�os Acad�micos" precisa ir em um outro menu caso queira fazer uma altera��o logo em seguida.
## Fotos
![https://drive.google.com/open?id=1slEBIJy-uGprwTpV0KPM1uUnSAKRq1i7](../../imgs/ANDR�_1slEBIJy-uGprwTpV0KPM1uUnSAKRq1i7.png)

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: Op��es relacionadas com matr�cula est�o dispersas em v�rios menus que acessam v�rios sistemas, com toda essa informa��o o usu�rio n�o consegue saber de fato o que cada sistema faz ou n�o faz.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTU_ANDR_4]* Problema 4: Janela de login.
**Ocorre na p�gina**: *Estudantes > Menu Estudantes > Intranet.*

Ao clicar em �intranet� o uma caixa de di�logo aparece.
N�o � informado qual login e senha s�o requeridos.
N�o � informado se trata-se da mesma intranet que os alunos acessam pelo site da FT.
Caso essa seja uma ferramenta de administra��o por que existe um link no site onde qualquer um poderia tentar o acesso sem saber do que se trata.
## Fotos
![https://drive.google.com/open?id=1HW6qdDhQW0SbZvdStAY49stNxIqkzdvp](../../imgs/ANDR�_1HW6qdDhQW0SbZvdStAY49stNxIqkzdvp.png)

## Coment�rios
Acredito que seja um link para um sistema de gerenciamento da administra��o do site, se for o caso acredito que seria melhor que este link n�o estivesse dispon�vel em todas as p�ginas do portal e que ao exibir a janela de login existisse uma mensagem como "Esta � uma tela de login para a administra��o do site, caso voc� seja um administrador utilize seu login e senha ... no formato ...".

## Considera��es

### Heur�stica ferida: 5�
**Heur�stica ferida**: 5 - Preven��o de erro

**Justificativa**: N�o existem explica��es sobre o que se trata a tela de login, formato de login ou em qual sistema est� sendo feito o acesso, assim o usu�rio pode cometer erros ao tentar inserir os campos e acessar o sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[ESTU_ANDR_5]* Problema 5: Erro ao acessar intranet.
**Ocorre na p�gina**: *Estudantes > Menu Estudantes  > Intranet.*

Ao acessar o menu intranet, inserir um login e senha na caixa de di�logo e clicar em entrar a caixa de di�logo fecha e uma nova aparece, sem os dados inseridos e sem dizer qual foi o erro no login, ao clicar em cancelar sou redirecionado para  uma p�gina de erro.
## Fotos
![https://drive.google.com/open?id=12dygWgWM6AyVqwssAsX8oFRkwWSFNx0H](../../imgs/ANDR�_12dygWgWM6AyVqwssAsX8oFRkwWSFNx0H.png)

![https://drive.google.com/open?id=1SVyNqcAxYIjBqEUR9fy4d4cqKNFG1ezo](../../imgs/ANDR�_1SVyNqcAxYIjBqEUR9fy4d4cqKNFG1ezo.png)

## Considera��es

### Heur�stica ferida: 9�
**Heur�stica ferida**: 9 - Auxiliar usu�rios a reconhecer, diagnosticar e recuperar a��es erradas

**Justificativa**: N�o existem mensagens de erro ao tentar fazer um login com credenciais incorretas.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ESTU_ANDR_6]* Problema 6: Bot�es que n�o levam a lugar algum.
**Ocorre na p�gina**: *Estudantes > Menu Estudantes > Intranet > Cancelar.*

Ao acessar o menu intranet, inserir um login e senha na caixa de di�logo e clicar em entrar a caixa de di�logo fecha e uma nova aparece, sem os dados inseridos e sem dizer qual foi o erro no login, ao clicar em cancelar sou redirecionado para  uma p�gina de erro.
## Fotos
![https://drive.google.com/open?id=1NtX2WUpi6km0-sBnWam-1OcbBSCKJ1rS](../../imgs/ANDR�_1NtX2WUpi6km0-sBnWam-1OcbBSCKJ1rS.png)

![https://drive.google.com/open?id=1fygN_5fA9AigAellO7-kr0lU-YiAr2OJ](../../imgs/ANDR�_1fygN_5fA9AigAellO7-kr0lU-YiAr2OJ.png)

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: Caso o usu�rio entre nessa janela por engano clicar em "Ok" ir� abrir uma outra janela de di�logo e clicar em "Cancelar" ir� redirecion�-lo a uma p�gina de erro sem o bot�o "Voltar", portanto ele perde a liberdade durante a navega��o no portal.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ESTU_ANDR_7]* Problema 7: Mensagem de erro em ingl�s.
**Ocorre na p�gina**: *Estudantes > Menu Estudantes > Intranet > Cancelar.*

Ao acessar o menu intranet, inserir um login e senha na caixa de di�logo e clicar em entrar a caixa de di�logo fecha e uma nova aparece, sem os dados inseridos e sem dizer qual foi o erro no login, ao clicar em cancelar sou redirecionado para  uma p�gina de erro.
A p�gina de erro est� em ingl�s e a mensagem n�o � assertiva o suficiente para o usu�rio conseguir diagnosticar o que fez de errado, al�m disso a p�gina n�o possui um bot�o "Voltar".
## Fotos
![https://drive.google.com/open?id=1LypYzK2QECeQZzZauxrtRK3gtYw7uMa8](../../imgs/ANDR�_1LypYzK2QECeQZzZauxrtRK3gtYw7uMa8.png)

## Considera��es

### Heur�stica ferida: 9�
**Heur�stica ferida**: 9 - Auxiliar usu�rios a reconhecer, diagnosticar e recuperar a��es erradas

**Justificativa**: A mensagem de erro em ingl�s e pouco clara n�o ajuda o usu�rio a saber o que fez de errado.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTU_ANDR_8]* Problema 8: Falta de bot�o "Voltar" em p�gina de erro.
**Ocorre na p�gina**: *Estudantes > Menu Estudantes > Intranet > Cancelar.*

Ao acessar o menu intranet, inserir um login e senha na caixa de di�logo e clicar em entrar a caixa de di�logo fecha e uma nova aparece, sem os dados inseridos e sem dizer qual foi o erro no login, ao clicar em cancelar sou redirecionado para  uma p�gina de erro.
A p�gina de erro est� em ingl�s e a mensagem n�o � assertiva o suficiente para o usu�rio conseguir diagnosticar o que fez de errado, al�m disso a p�gina n�o possui um bot�o "Voltar".
## Fotos
![https://drive.google.com/open?id=1oZQbTyGpzD6femsr1oaCL3feYKntyn-L](../../imgs/ANDR�_1oZQbTyGpzD6femsr1oaCL3feYKntyn-L.png)

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: A falta do bot�o "Voltar" faz com que o usu�rio tenha uma perda do controle que tinha ao utilizar o sistema j� que a p�gina de erro n�o apresenta nenhum link ou bot�o que o direcione para o pr�ximo passo em seu objetivo.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ESTU_ANDR_9]* Problema 9: Bot�o "Entrar" n�o faz nada.
**Ocorre na p�gina**: *Estudantes > Menu Estudantes > Intranet.*

Ao acessar o menu intranet, inserir um login e senha na caixa de di�logo e clicar em entrar a caixa de di�logo fecha e uma nova aparece, sem os dados inseridos e sem dizer qual foi o erro no login, ao clicar em cancelar o usu�rio � redirecionado para  uma p�gina de erro.
## Fotos
![https://drive.google.com/open?id=1j238H3M1zFRikrzuzIkuzefzPxsiFGDT](../../imgs/ANDR�_1j238H3M1zFRikrzuzIkuzefzPxsiFGDT.png)

## Considera��es

### Heur�stica ferida: 1�
**Heur�stica ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: O sistema n�o oferece qualquer feedback ao tentar fazer o login, em casos onde o login est� incorreto a mesma janela � mostrada novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[ESTU_ANDR_10]* Problema 10: �cone n�o muda em alto contraste.
**Ocorre na p�gina**: *Estudantes > Menu Estudantes > Bot�o "Alto Contraste".*

Ao usar a op��o alto contraste do site um dos �cones n�o muda de cor.
## Fotos
![https://drive.google.com/open?id=1NqJoAIeRFbXTmxBv_89EeYnECRflcTwz](../../imgs/ANDR�_1NqJoAIeRFbXTmxBv_89EeYnECRflcTwz.png)

## Considera��es

### Heur�stica ferida: 4�
**Heur�stica ferida**: 4 - Consist�ncia e padr�es

**Justificativa**: Um dos �cones sai do padr�o ao ativar o modo de alto contraste, o usu�rio pode ser levado a pensar que � uma op��o diferenciada, mais importante ou em destaque.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[ESTU_ANDR_17]* Problema 17: Problemas na utiliza��o com o teclado.
**Ocorre na p�gina**: *Estudantes > Ao navegar pelo menu "Estudantes".*

Era esperado que pudesse navegar entre os quadros utilizando a tecla tab ou as teclas direcionais, isso n�o � poss�vel.
## Fotos
![https://drive.google.com/open?id=171dRhdUupMesWyKAxoT9CmPqRHn9-dD6](../../imgs/ANDR�_171dRhdUupMesWyKAxoT9CmPqRHn9-dD6.png)

## Considera��es

### Heur�stica ferida: 7�
**Heur�stica ferida**: 7 - Flexibilidade e efici�ncia de uso

**Justificativa**: A falta de atalhos de teclado e funcionalidades simples com o teclado dificultam o manuseio do sistema para usu�rios experientes.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTU_ANDR_116]* Problema 116: Formata��o diferente.
**Ocorre na p�gina**: *Estudantes > Microsoft Office Online.*

Nos outros quadros os itens s�o separados em t�picos, aqui est�o sendo separados com v�rgulas e est�o todos no mesmo t�pico.
## Fotos
![https://drive.google.com/open?id=1KgxQrX5UFczNzDS8LpTmzSoklaL6KVv2](../../imgs/ANDR�_1KgxQrX5UFczNzDS8LpTmzSoklaL6KVv2.png)

## Considera��es

### Heur�stica ferida: 4�
**Heur�stica ferida**: 4 - Consist�ncia e padr�es

**Justificativa**: O sistema est� inconsistente pois um dos quadros est� diferente dos outros.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)


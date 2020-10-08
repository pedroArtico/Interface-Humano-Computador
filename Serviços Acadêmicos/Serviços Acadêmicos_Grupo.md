# Servi�os Acad�micos
 



## *id:[SRVACAD_GRUP_4]* Problema 4: Problemas de Processamento
**Ocorre na p�gina**: *Servi�os Acad�micos > Login do usu�rio, ao clicar em "acessar"*

Ao tentar logar utilizando caracteres do tipo emoji (n�o permitidos pelo sistema, entretanto, a informa��o n�o � explicitada) o sistema encaminha o usu�rio para um erro de processamento com uma mensagem contendo trechos de c�digo SQL.
## Fotos
![https://drive.google.com/open?id=1O0c6hzbqEOSK4yfSvRpr6Bi_y5x6CH0x](../../imgs/GRUPO_1O0c6hzbqEOSK4yfSvRpr6Bi_y5x6CH0x.png)

## Coment�rios
O grau de severidade � grave, pois o usu�rio n�o consegue ter acesso a uma parte fundamental do sistema, por esse motivo � de suma import�ncia a r�pida resolu��o.

## Considera��es

### Heur�stica ferida: 9�
**Heur�stica ferida**: 9 - Auxiliar usu�rios a reconhecer, diagnosticar e recuperar a��es erradas

**Justificativa**: A heur�stica aplicada ao problema � a 9, pois em nenhum momento foi dito como o usu�rio poderia resolver o problema, apenas � solicitado que ele copie o c�digo SQL e envie � DAC. O usu�rio n�o tem entendimento do tipo de problema cometido, e como ele poderia ser facilmente resolvido.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastr�fico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SRVACAD_GRUP_5]* Problema 5: Carregamento da p�gina
**Ocorre na p�gina**: *Servi�os Acad�micos > Ao clicar em "cursos regulares" no t�pico REQUERIMENTO DE MATR�CULA*

A p�gina que aparece est� apenas em modo texto, a pagina n�o � carregada. Al�m disso, apresenta caracteres fora do padr�o utf8.
## Fotos
![https://drive.google.com/open?id=1RZIfWJnIpO1YVtNeDsPPWGgJKrOoznt8](../../imgs/GRUPO_1RZIfWJnIpO1YVtNeDsPPWGgJKrOoznt8.png)

## Coment�rios
Grau de severidade � 2, pois n�o � um problema grave, apesar de n�o condizer com a linguagem por meio da qual o usu�rio esta acostumado, ainda assim � poss�vel extrair algumas informa��es da p�gina.

## Considera��es

### Heur�stica ferida: 2�
**Heur�stica ferida**: 2 - Equival�ncia entre o sistema e o mundo real

**Justificativa**: A p�gina apresenta conte�do que n�o � coerente com o conhecimento do usu�rio leigo, n�o faz parte do que ele est� habituado a encontrar. N�o faz parte da "linguagem" do usu�rio.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_GRUP_6]* Problema 6: Falta de verifica��o de campos
**Ocorre na p�gina**: *Servi�os Acad�micos > Ao tentar redirecionar o e-mail da DAC*

O usu�rio pode digitar combina��es de caracteres que n�o condizem com um endere�o de e-mail v�lido. N�o h� verifica��o se o usu�rio realmente digitou um e-mail ou caracteres aleat�rios, como o exemplo da imagem.
## Fotos
![https://drive.google.com/open?id=1knwfBLJO2jTwsIbFq5LoCxtHwZm6U6po](../../imgs/GRUPO_1knwfBLJO2jTwsIbFq5LoCxtHwZm6U6po.png)

## Coment�rios
O grau de severidade � m�ximo, pois o usu�rio pode n�o receber mais e-mails da DAC, por conta de uma redirecionamento indevido.

## Considera��es

### Heur�stica ferida: 5�
**Heur�stica ferida**: 5 - Preven��o de erro

**Justificativa**: A heur�stica correta � a 5, pois os desenvolvedores n�o pensaram em formas de circuncidar o sistema para que o usu�rio n�o pudesse inserir endere�os de e-mail inv�lidos.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastr�fico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SRVACAD_GRUP_7]* Problema 7: Falta de bot�o na interface
**Ocorre na p�gina**: *Servi�os Acad�micos > Ocorre na Desist�ncia de Matr�cula*

O usu�rio n�o tem a op��o de Voltar, j� que o bot�o n�o existe. Ele pode apenas sair do sistema, n�o garantindo que a a��o foi desfeita.
## Fotos
![https://drive.google.com/open?id=1O0G0a-oFC3-tcR_S8SAITlL_LxZBdUrt](../../imgs/GRUPO_1O0G0a-oFC3-tcR_S8SAITlL_LxZBdUrt.png)

## Coment�rios
O grau de severidade � 3, ou seja, � necess�rio corrigir esse problema, pois caso o usu�rio n�o consiga retornar a um menu anterior, e seja obrigado a sair do sistema, o mesmo pode perder informa��es n�o-salvas.

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: A heur�stica correta � a 3, pois o usu�rio � impedido de voltar � p�gina anterior, desfazendo uma a��o, por conta da falta de um bot�o voltar.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_GRUP_9]* Problema 9: Problema de Codifica��o de caracteres
**Ocorre na p�gina**: *Servi�os Acad�micos > Integraliza��o Curricular*

Problema com a codifica��o dos caracteres especiais.
## Fotos
![https://drive.google.com/open?id=1OE_BL1MHjrxycAOCTUWf5mpW69XO1GqC](../../imgs/GRUPO_1OE_BL1MHjrxycAOCTUWf5mpW69XO1GqC.png)

## Considera��es

### Heur�stica ferida: 2�
**Heur�stica ferida**: 2 - Equival�ncia entre o sistema e o mundo real

**Justificativa**: Usu�rio n�o � capaz de identificar que � um problema de codifica��o para caracteres especiais portanto n�o � capaz de entender a informa��o escrita.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_GRUP_28]* Problema 28: Falha de seguran�a ao usar navegador.
**Ocorre na p�gina**: *Servi�os Acad�micos > Ap�s o login.*

Ao fazer o login no sistema � mostrada uma mensagem dizendo que dependendo do navegador utilizado e de sua vers�o o usu�rio corre riscos relacionados com a seguran�a. 
O teste foi feito em um navegador fora da lista e a ferramenta funcionou normalmente, aparentemente � aceit�vel que os usu�rios do sistema corram riscos de seguran�a.
## Fotos
![https://drive.google.com/open?id=12aySqRu-gGf9jVow_c7lnUWr2rf-3jZ6](../../imgs/GRUPO_12aySqRu-gGf9jVow_c7lnUWr2rf-3jZ6.png)

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: O sistema funciona normalmente em um navegador que n�o � recomendado, � dito que s�o problemas de seguran�a - mas a mensagem � mostrada ap�s o usu�rio inserir seus dados em um navegador dito inseguro e fazer o login. 
Isso pode causar medo em alguns usu�rios ou d�vidas se precisam ou n�o utilizar os navegadores ditos j� que o sistema funciona normalmente em um outro navegador.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_GRUP_29]* Problema 29: Fun��es est�o em outro sistema.
**Ocorre na p�gina**: *Servi�os Acad�micos > Ap�s fazer o login na ferramenta.*

� exibida uma mensagem dizendo que para fazer certas altera��es de dados existe um novo sistema. N�o � esclarecido se tais fun��es continuam no sistema atual, al�m disso, essa mensagem poderia aparecer antes do usu�rio efetuar o login j� que ele � obrigado a se autenticar para ent�o descobrir que ter� que sair do sistema para acessar outro.
## Fotos
![https://drive.google.com/open?id=1BG4NLRn1rOMCM_WPBJk8NODpo_7tjxb-](../../imgs/GRUPO_1BG4NLRn1rOMCM_WPBJk8NODpo_7tjxb-.png)

## Considera��es

### Heur�stica ferida: 2�
**Heur�stica ferida**: 2 - Equival�ncia entre o sistema e o mundo real

**Justificativa**: N�o existe l�gica nas a��es ao requerer que um usu�rio j� tenha feito o login para mostrar que as op��es que quer podem n�o estar mais no portal que ele conhece.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_GRUP_30]* Problema 30: Op��es de p�s-gradua��o para aluno da gradua��o apenas.
**Ocorre na p�gina**: *Servi�os Acad�micos > P�s-gradua��o.*

Mesmo logado como aluno que cursa apenas Gradua��o o sistema mostra bot�es clic�veis indicando que poderia acessar op��es que n�o correspondem com o perfil do usu�rio. .
## Fotos
![https://drive.google.com/open?id=146lb6TTR3bVI6MXscRo-dalH5rqIRbhv](../../imgs/GRUPO_146lb6TTR3bVI6MXscRo-dalH5rqIRbhv.png)

## Considera��es

### Heur�stica ferida: 2�
**Heur�stica ferida**: 2 - Equival�ncia entre o sistema e o mundo real

**Justificativa**: A heur�stica violada � a 2, pois um aluno de gradua��o n�o deve ter acesso � informa��es de p�s-gradua��o. N�o faz parte da "realidade" dele.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_GRUP_31]* Problema 31: Mensagem sem sentido no contexto.
**Ocorre na p�gina**: *Servi�os Acad�micos > Relat�rio Final de Matr�cula.*

O sistema mostra uma mensagem de  �campos obrigat�rios� mesmo sem haver qualquer campo que possa ser preenchido.
## Fotos
![https://drive.google.com/open?id=1Jw9xGvEBQc5WsShRCgSlJqOtk52ck6uT](../../imgs/GRUPO_1Jw9xGvEBQc5WsShRCgSlJqOtk52ck6uT.png)

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: A informa��o n�o tem utilidade e s� adiciona conte�do in�til � carga visual do usu�rio.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_GRUP_32]* Problema 32: Bot�es com design diferente.
**Ocorre na p�gina**: *Servi�os Acad�micos > Integraliza��o Curricular.*

Os bot�es imprimir e voltar tem tamanhos, cores, comportamentos, ... diferentes, diminuindo a consist�ncia do sistema.
## Fotos
![https://drive.google.com/open?id=1j8_TBaJ3nVPgfgMrOeREnoL8ZMyr88kb](../../imgs/GRUPO_1j8_TBaJ3nVPgfgMrOeREnoL8ZMyr88kb.png)

## Considera��es

### Heur�stica ferida: 4�
**Heur�stica ferida**: 4 - Consist�ncia e padr�es

**Justificativa**: O sistema � inconsistente pois os bot�es deveriam seguir um mesmo padr�o.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))


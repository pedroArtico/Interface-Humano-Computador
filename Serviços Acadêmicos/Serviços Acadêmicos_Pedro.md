# Servi�os Acad�micos
 



## *id:[SRVACAD_PEDR_1]* Problema 1: Problemas de Processamento.
**Ocorre na p�gina**: *Servi�os Acad�micos > Login do usu�rio, ao clicar em "Acessar".*

Ao tentar logar utilizando caracteres do tipo emoji (n�o permitidos pelo sistema, entretanto, a informa��o n�o � explicitada) o sistema encaminha o usu�rio para um erro de processamento com uma mensagem contendo trechos de c�digo SQL.
## Fotos
![https://drive.google.com/open?id=1O0c6hzbqEOSK4yfSvRpr6Bi_y5x6CH0x](../../imgs/PEDRO_1O0c6hzbqEOSK4yfSvRpr6Bi_y5x6CH0x.png)

## Coment�rios
O grau de severidade � grave, pois o usu�rio n�o consegue ter acesso a uma parte fundamental do sistema, por esse motivo � de suma import�ncia a r�pida resolu��o.

## Considera��es

### Heur�stica ferida: 9�
**Heur�stica ferida**: 9 - Auxiliar usu�rios a reconhecer, diagnosticar e recuperar a��es erradas

**Justificativa**: A heur�stica aplicada ao problema � a 9, pois em nenhum momento foi dito como o usu�rio poderia resolver o problema, apenas � solicitado que ele copie o c�digo SQL e envie � DAC. O usu�rio n�o tem entendimento do tipo de problema cometido, e como ele poderia ser facilmente resolvido.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_PEDR_2]* Problema 2: Carregamento da p�gina.
**Ocorre na p�gina**: *Servi�os Acad�micos > Ao clicar em "Cursos Regulares" no t�pico "Requerimento de Matr�cula".*

A p�gina que aparece est� apenas em modo texto, a pagina n�o � carregada. Al�m disso, apresenta caracteres fora do padr�o utf8.
## Fotos
![https://drive.google.com/open?id=1RZIfWJnIpO1YVtNeDsPPWGgJKrOoznt8](../../imgs/PEDRO_1RZIfWJnIpO1YVtNeDsPPWGgJKrOoznt8.png)

## Coment�rios
Grau de severidade � 2, pois n�o � um problema grave, apesar de n�o condizer com a linguagem por meio da qual o usu�rio esta acostumado, ainda assim � poss�vel extrair algumas informa��es da p�gina.

## Considera��es

### Heur�stica ferida: 2�
**Heur�stica ferida**: 2 - Equival�ncia entre o sistema e o mundo real

**Justificativa**: A p�gina apresenta conte�do que n�o � coerente com o conhecimento do usu�rio leigo, n�o faz parte do que ele est� habituado a encontrar. N�o faz parte da "linguagem" do usu�rio.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_PEDR_3]* Problema 3: Falta de verifica��o de campos.
**Ocorre na p�gina**: *Servi�os Acad�micos > Ao tentar redirecionar o e-mail da DAC.*

O usu�rio pode digitar combina��es de caracteres que n�o condizem com um endere�o de e-mail v�lido. N�o h� verifica��o se o usu�rio realmente digitou um e-mail ou caracteres aleat�rios, como o exemplo da imagem.
## Fotos
![https://drive.google.com/open?id=1knwfBLJO2jTwsIbFq5LoCxtHwZm6U6po](../../imgs/PEDRO_1knwfBLJO2jTwsIbFq5LoCxtHwZm6U6po.png)

## Coment�rios
O grau de severidade � m�ximo, pois o usu�rio pode n�o receber mais e-mails da DAC, por conta de uma redirecionamento indevido.

## Considera��es

### Heur�stica ferida: 5�
**Heur�stica ferida**: 5 - Preven��o de erro

**Justificativa**: A heur�stica correta � a 5, pois os desenvolvedores n�o pensaram em formas de circuncidar o sistema para que o usu�rio n�o pudesse inserir endere�os de e-mail inv�lidos.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_PEDR_5]* Problema 5: Inconsist�ncia no menu.
**Ocorre na p�gina**: *Servi�os Acad�micos > Menu Principal de Servi�os Acad�micos.*

A op��o CERTIFICADO PED � apresentada na parte de Gradua��o do Menu Principal, entretanto, um aluno de gradua��o n�o pode ser PED.
## Fotos
![https://drive.google.com/open?id=15cfCIlW8FVhSaHt8xB_K8B21BPPXjMWG](../../imgs/PEDRO_15cfCIlW8FVhSaHt8xB_K8B21BPPXjMWG.png)

## Coment�rios
O grau de severidade � baixo, pois n�o afeta o desempenho do sistema, e poss�veis a��es erradas do usu�rio n�o levariam a erros complexos.

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: A heur�stica correta � a 8, pois o sistema apresenta uma inconsist�ncia de informa��es acad�micas na parte de Estudantes (contida no Menu Principal), ou seja, houve uma falha conceitual na diferencia��o de bot�es da gradua��o e da p�s-gradua��o.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_PEDR_6]* Problema 6: Falta de bot�o na interface.
**Ocorre na p�gina**: *Servi�os Acad�micos > Ocorre na "Desist�ncia de Matr�cula".*

O usu�rio n�o tem a op��o de Voltar, j� que o bot�o n�o existe. Ele pode apenas sair do sistema, n�o garantindo que a a��o foi desfeita.
## Fotos
![https://drive.google.com/open?id=1O0G0a-oFC3-tcR_S8SAITlL_LxZBdUrt](../../imgs/PEDRO_1O0G0a-oFC3-tcR_S8SAITlL_LxZBdUrt.png)

## Coment�rios
O grau de severidade � 3, ou seja, � necess�rio corrigir esse problema, pois caso o usu�rio n�o consiga retornar a um menu anterior, e seja obrigado a sair do sistema, o mesmo pode perder informa��es n�o-salvas.

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: A heur�stica correta � a 3, pois o usu�rio � impedido de voltar � p�gina anterior, desfazendo uma a��o, por conta da falta de um bot�o voltar.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_PEDR_7]* Problema 7: Inconsist�ncia em "Requerimento de Matricula".
**Ocorre na p�gina**: *Servi�os Acad�micos > Ao submeter login e senha na se��o "Requerimento de Matr�cula".*

O relat�rio de matricula n�o est� no menu anterior, e sim no menu principal/inicial j� que no menu anterior est�o os campos de login e senha.
## Fotos
![https://drive.google.com/open?id=1Rij8I3KxQDLHvL0BchI7JNT6ruLv1aUv](../../imgs/PEDRO_1Rij8I3KxQDLHvL0BchI7JNT6ruLv1aUv.png)

## Coment�rios
Grau de severidade baixo, pode causar certa confus�o para o usu�rio, mas n�o implicar� em erros de sistema.

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: A heur�stica correta � a 8, pois h� informa��o in�til e incorreta na tela, ao dizer que o relat�rio est� em um menu, quando na realidade esta em outro.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem import�ncia (N�o afeta a opera��o da interface (n�o � um problema de usabilidade))





## *id:[SRVACAD_PEDR_8]* Problema 8: Falta de bot�o na interface de "Servi�os Acad�micos".
**Ocorre na p�gina**: *Servi�os Acad�micos > Ao tentar gerar o relat�rio de matr�cula.*

O usu�rio n�o tem a op��o de acessar o menu anterior, neste caso em que a busca retornou sem ocorr�ncias. Ele acaba por ser obrigado a sair do sistema e logar novamente.
## Fotos
![https://drive.google.com/open?id=1HhWVkAV_M5b0UYCPUu6YvRC4xy3wiRwE](../../imgs/PEDRO_1HhWVkAV_M5b0UYCPUu6YvRC4xy3wiRwE.png)

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: O usu�rio n�o tem a liberdade de voltar ao menu anterior e refazer a a��o. N�o pode consultar novamente seu relat�rio final de matr�cula, sem ter que sair do sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_PEDR_10]* Problema 10: Decodifica��o de caracteres.
**Ocorre na p�gina**: *Servi�os Acad�micos > Integraliza��o Curricular.*

Ao clicar em "Integraliza��o Curricular", aparecem varias informa��es sobre o aluno, entretanto, h� erros de codifica��o de Caracteres UTF-8. O conte�do est� com sentido comprometido.
## Fotos
![https://drive.google.com/open?id=1pzBGaZ37qE30lMISGowt86ICxLsfBm9_](../../imgs/PEDRO_1pzBGaZ37qE30lMISGowt86ICxLsfBm9_.png)

## Considera��es

### Heur�stica ferida: 2�
**Heur�stica ferida**: 2 - Equival�ncia entre o sistema e o mundo real

**Justificativa**: A informa��o n�o � apresentado na mesma linguagem que o usu�rio est� habituado. N�o � poss�vel compreender o conte�do da p�gina.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_PEDR_42]* Problema 42: P�gina em branco.
**Ocorre na p�gina**: *Servi�os Acad�micos > Ao clicar no bot�o "Confirmar", em PED.*

O usu�rio � redirecionado para uma p�gina em branco.
## Fotos
![https://drive.google.com/open?id=10xRVG11Wl6msHft6Q94BAKD1ydKP8aGZ](../../imgs/PEDRO_10xRVG11Wl6msHft6Q94BAKD1ydKP8aGZ.png)

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: O usu�rio � estudante de gradua��o, e tenta emitir um certificado n�o existente. Ele n�o tem a op��o de voltar a a��o.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_PEDR_43]* Problema 43: P�gina n�o encontrada.
**Ocorre na p�gina**: *Servi�os Acad�micos > Ao clicar em "Caderno de Horarios da Gradua��o".*

O usu�rio � redirecionado para uma p�gina n�o encontrada.
## Fotos
![https://drive.google.com/open?id=1AYqEyvbHo4eBrMyekl4FfC_eD70JSmLT](../../imgs/PEDRO_1AYqEyvbHo4eBrMyekl4FfC_eD70JSmLT.png)

## Considera��es

### Heur�stica ferida: 0�
**Heur�stica ferida**: 0 - A heur�stica n�o foi identificada: este t�pico n�o se encaixa em nenhuma das heur�sticas ou ser� discutido posteriormente para a defini��o de sua heur�stica

**Justificativa**: O usu�rio n�o � levado a uma p�gina v�lida.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)


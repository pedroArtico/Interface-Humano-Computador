# Servi�os Acad�micos
 



## *id:[SRVACAD_ANDR_11]* Problema 11: Nome do sistema muda de acordo com a p�gina.
**Ocorre na p�gina**: *Servi�os Acad�micos > No caminho de login em "Servi�os Acad�micos".*

Em cada etapa do login um t�tulo diferente com um formato diferente � colocado na tela, primeiramente "Servi�os Acad�micos", depois "Sistema de Senha �nica e Permiss�es" (nesse ponto o usu�rio j� pode estar confuso pois esperava entrar num sistema de servi�os acad�micos e n�o de senhas, mas pode ser que interprete que � uma etapa passar pelo sistema de login) por fim "Sistemas Acad�micos - Servi�os". 
� f�cil para um usu�rio se confundir sem saber se est� acessando o sistema correto.
## Fotos
![https://drive.google.com/open?id=1jF7Y9DWpc0sfd_j7eKve5GTn1pnrWws3](../../imgs/ANDR�_1jF7Y9DWpc0sfd_j7eKve5GTn1pnrWws3.png)

![https://drive.google.com/open?id=1Zwcqm1rAxFjqecFKxbEQZQckt8PyD2FS](../../imgs/ANDR�_1Zwcqm1rAxFjqecFKxbEQZQckt8PyD2FS.png)

![https://drive.google.com/open?id=1Sx6XGLruaMqrZjIx5BBWimDaBEGhf2zg](../../imgs/ANDR�_1Sx6XGLruaMqrZjIx5BBWimDaBEGhf2zg.png)

## Considera��es

### Heur�stica ferida: 4�
**Heur�stica ferida**: 4 - Consist�ncia e padr�es

**Justificativa**: O sistema n�o tem consist�ncia, a cada passo do acesso o usu�rio passa por um sistema com nome diferente e design diferente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_12]* Problema 12: Caracteres especiais.
**Ocorre na p�gina**: *Servi�os Acad�micos > Ao tentar fazer login em "Servi�os Acad�micos."*

O sistema em quest�o tem problemas em diferenciar um caractere emoji em unicode da sua representa��o em html, assim, deveria impedir que os mesmos fossem inseridos, ao tentar fazer login usando esses caracteres um erro � gerado.
## Fotos
![https://drive.google.com/open?id=1J0TJ0ISI_mU8iuwaPUr9LdL6IaFTy0i7](../../imgs/ANDR�_1J0TJ0ISI_mU8iuwaPUr9LdL6IaFTy0i7.png)

![https://drive.google.com/open?id=1yWNM-QZ2JIBH5AHceMAYajORZnGowHK3](../../imgs/ANDR�_1yWNM-QZ2JIBH5AHceMAYajORZnGowHK3.png)

## Considera��es

### Heur�stica ferida: 5�
**Heur�stica ferida**: 5 - Preven��o de erro

**Justificativa**: O sistema n�o evita que o usu�rio cometa erros permitindo que insira caracteres especiais nos campos de login.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_ANDR_13]* Problema 13: Erro com termos t�cnicos e sem ajuda.
**Ocorre na p�gina**: *Servi�os Acad�micos > Quando um erro no login ocorre na p�gina.*

Ao tentar fazer login na p�gina usando caracteres especiais a p�gina gera um erro com termos t�cnicos, detalhes de programa��o sem indicar de fato o que ocorreu de errado.
## Fotos
![https://drive.google.com/open?id=1O5qlu588YZ35NPu_6Y5LH5q-PQCSQQPL](../../imgs/ANDR�_1O5qlu588YZ35NPu_6Y5LH5q-PQCSQQPL.png)

## Considera��es

### Heur�stica ferida: 9�
**Heur�stica ferida**: 9 - Auxiliar usu�rios a reconhecer, diagnosticar e recuperar a��es erradas

**Justificativa**: A mensagem de erro n�o � clara pois n�o diz o que ocorreu de errado usa termos t�cnicos e mostra detalhes da programa��o do sistema. Nenhuma solu��o � sugerida.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastr�fico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SRVACAD_ANDR_14]* Problema 14: Bot�o "Sair" amb�guo.
**Ocorre na p�gina**: *Servi�os Acad�micos > Ao clicar em "Sair" quando um erro de login ocorre.*

O usu�rio � posto em d�vida se o bot�o "Sair" se refere a "sair desta tela de erro" ou "sair do sistema". Ele fecha o sistema o que faz com que o usu�rio tenha que procurar e abrir novamente a p�gina do sistema.
## Fotos
![https://drive.google.com/open?id=1IRR-o1Wx3CqAhhINI9znbmtK5CUocJ3b](../../imgs/ANDR�_1IRR-o1Wx3CqAhhINI9znbmtK5CUocJ3b.png)

## Considera��es

### Heur�stica ferida: 2�
**Heur�stica ferida**: 2 - Equival�ncia entre o sistema e o mundo real

**Justificativa**: Se houve um erro no sistema de login o usu�rio ir� pensar em tentar fazer o login novamente, n�o em fechar o sistema. Em outros sistemas quando uma mensagem de erro aparece um bot�o "Sair" normalmente se refere a fechar a p�gina de erro e n�o fechar o sistema como um todo.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_15]* Problema 15: Falha de seguran�a ao usar navegador.
**Ocorre na p�gina**: *Servi�os Acad�micos > Ap�s o login.*

Ao fazer o login no sistema � mostrada uma mensagem dizendo que dependendo do navegador utilizado e de sua vers�o o usu�rio corre riscos relacionados com a seguran�a. 
No caso o teste foi feito num navegador fora da lista e a ferramenta funcionou normalmente, aparentemente � aceit�vel que os usu�rios do sistema corram riscos de seguran�a.
## Fotos
![https://drive.google.com/open?id=12aySqRu-gGf9jVow_c7lnUWr2rf-3jZ6](../../imgs/ANDR�_12aySqRu-gGf9jVow_c7lnUWr2rf-3jZ6.png)

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: O sistema funciona normalmente em um navegador que n�o � recomendado, � dito que s�o problemas de seguran�a - mas a mensagem � mostrada ap�s o usu�rio inserir seus dados em um navegador dito inseguro e fazer o login. 
Isso pode causar medo em alguns usu�rios ou d�vidas se precisam ou n�o utilizar os navegadores ditos j� que o sistema funciona normalmente em um outro navegador.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_ANDR_16]* Problema 16: Mensagens conflitantes.
**Ocorre na p�gina**: *Servi�os Acad�micos > Ao ir para a p�gina de baixar os navegadores recomendados.*

Ao fazer o login no sistema � mostrada uma mensagem dizendo que dependendo do navegador utilizado e de sua vers�o o usu�rio corre riscos relacionados com a seguran�a. 
Existe um link para uma p�gina de download dos navegadores recomendados, nela uma mensagem de aviso semelhante aparece mas com mais navegadores e em outras vers�es.
O usu�rio n�o tem como saber em qual mensagem deve confiar.
## Fotos
![https://drive.google.com/open?id=1q9dWQ_rn0YC5OdyVPX15_N9ftelwoDRa](../../imgs/ANDR�_1q9dWQ_rn0YC5OdyVPX15_N9ftelwoDRa.png)

![https://drive.google.com/open?id=1-pNuMicD3mHIe9kQttEAvD3PSvYlOF5c](../../imgs/ANDR�_1-pNuMicD3mHIe9kQttEAvD3PSvYlOF5c.png)

## Considera��es

### Heur�stica ferida: 4�
**Heur�stica ferida**: 4 - Consist�ncia e padr�es

**Justificativa**: O sistema est� inconsistente pois existem duas mensagens para a solu��o do mesmo problema com solu��es diferentes.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_18]* Problema 18: Falta de informa��o ao baixar navegadores.
**Ocorre na p�gina**: *Servi�os Acad�micos > Baixar navegadores recomendados.*

Na p�gina de baixar os navegadores recomendados � dado apenas o link para o arquivo instalador na maior parte dos casos. Usu�rios mais leigos com bastante certeza se sentiriam mais seguros se tivessem acesso aos tutoriais de instala��o e acesso ao site da empresa que desenvolveu o navegador.
## Fotos
![https://drive.google.com/open?id=1K4MinxD3_9HyYaumhFpGV8gR5pmIeavn](../../imgs/ANDR�_1K4MinxD3_9HyYaumhFpGV8gR5pmIeavn.png)

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: Usu�rios leigos podem ter dificuldades com a instala��o e conhecimento do software que ir�o instalar em seus computadores. O usu�rio acaba perdendo controle nesse caso.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_19]* Problema 19: Fun��es est�o em outro sistema.
**Ocorre na p�gina**: *Servi�os Acad�micos > Ap�s fazer o login na ferramenta.*

� exibida uma mensagem dizendo que para fazer certas altera��es de dados existe um novo sistema. N�o � esclarecido se tais fun��es continuam no sistema atual, al�m disso, essa mensagem poderia aparecer antes do usu�rio efetuar o login j� que ele � obrigado a se autenticar para ent�o descobrir que ter� que sair do sistema para acessar outro.
## Fotos
![https://drive.google.com/open?id=1BG4NLRn1rOMCM_WPBJk8NODpo_7tjxb-](../../imgs/ANDR�_1BG4NLRn1rOMCM_WPBJk8NODpo_7tjxb-.png)

## Considera��es

### Heur�stica ferida: 2�
**Heur�stica ferida**: 2 - Equival�ncia entre o sistema e o mundo real

**Justificativa**: N�o existe l�gica nas a��es ao requerer que um usu�rio j� tenha feito o login para mostrar que as op��es que quer podem n�o estar mais no portal que ele conhece.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_ANDR_20]* Problema 20: Op��es de p�s-gradua��o para aluno da gradua��o apenas.
**Ocorre na p�gina**: *Servi�os Acad�micos > P�s-gradua��o.*

Mesmo logado como aluno que cursa apenas Gradua��o o sistema mostra bot�es clic�veis indicando que poderia acessar op��es que n�o correspondem com o perfil do usu�rio. .
## Fotos
![https://drive.google.com/open?id=146lb6TTR3bVI6MXscRo-dalH5rqIRbhv](../../imgs/ANDR�_146lb6TTR3bVI6MXscRo-dalH5rqIRbhv.png)

## Coment�rios
Poderia haver uma divis�o melhor das se��es e apenas a parte importante para o usu�rio deve aparecer.

## Considera��es

### Heur�stica ferida: 5�
**Heur�stica ferida**: 5 - Preven��o de erro

**Justificativa**: Visto que ao escolher uma op��o que n�o corresponde com o perfil do usu�rio um erros s�o gerados, o fato dessas op��es estarem dispon�veis mesmo com o conhecimento pr�vio de que os erros acontecer�o caracteriza o problema em tal heur�stica.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_ANDR_21]* Problema 21: Muitos bot�es com e sem funcionalidade juntos.
**Ocorre na p�gina**: *Servi�os Acad�micos > Tela de usu�rio logado.*

Mesmo logado como aluno que cursa apenas Gradua��o o sistema mostra bot�es clic�veis indicando que poderia acessar op��es que n�o correspondem com o perfil do usu�rio. .
## Fotos
![https://drive.google.com/open?id=1-ORpeSVpGpnf_UJs3vreIP4XaIs90gzx](../../imgs/ANDR�_1-ORpeSVpGpnf_UJs3vreIP4XaIs90gzx.png)

![https://drive.google.com/open?id=135eeXsTY7RnnDcQsbGJJTJM_e6rzrlA8](../../imgs/ANDR�_135eeXsTY7RnnDcQsbGJJTJM_e6rzrlA8.png)

## Coment�rios
Seria melhor que o sistema mostrasse aos usu�rios que s�o s� da gradua��o ou s� da p�s gradua��o seus respectivos menus e marcar bot�es que levam a op��es que n�o est�o dispon�veis no momento como n�o clic�veis.

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: O sistema mostra uma se��o inteira sem necessidade e em alguns casos bot�es para op��es que n�o est�o dispon�veis no momento.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_ANDR_22]* Problema 22: P�gina indispon�vel.
**Ocorre na p�gina**: *Servi�os Acad�micos > Desist�ncia de Matr�cula em Disciplinas.*

Ao acessar "Desist�ncia de Matr�cula em Disciplinas" � mostrada uma mensagem dizendo que a op��o est� indispon�vel, isso poderia estar marcado j� no bot�o.
## Fotos
![https://drive.google.com/open?id=1dvSmVvpdU0VWPdF6spVmaiXbDb1u3uV7](../../imgs/ANDR�_1dvSmVvpdU0VWPdF6spVmaiXbDb1u3uV7.png)

![https://drive.google.com/open?id=1KL9H4iiU2zyed2ufSjTaNHCwA4rt5m3x](../../imgs/ANDR�_1KL9H4iiU2zyed2ufSjTaNHCwA4rt5m3x.png)

## Considera��es

### Heur�stica ferida: 2�
**Heur�stica ferida**: 2 - Equival�ncia entre o sistema e o mundo real

**Justificativa**: O usu�rio perde liberdade ao acessar uma fun��o indispon�vel que � mostrada como se estivesse dispon�vel.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_ANDR_23]* Problema 23: Bot�o "Sair" amb�guo.
**Ocorre na p�gina**: *Servi�os Acad�micos > Desist�ncia de Matr�cula em Disciplinas.*

A mensagem exibida n�o tem um bot�o "Voltar", apenas um bot�o "Sair" que � mais facilmente interpretado como "Sair desta mensagem e voltar ao menu principal" do que "Sair do sistema". O bot�o fecha o sistema.
## Fotos
![https://drive.google.com/open?id=1lcDACS32yRRkIIeorOuUT5hZ2me3VY78](../../imgs/ANDR�_1lcDACS32yRRkIIeorOuUT5hZ2me3VY78.png)

![https://drive.google.com/open?id=1zgjoN8jt_URazkOIHFK3x1AjY_Rl638I](../../imgs/ANDR�_1zgjoN8jt_URazkOIHFK3x1AjY_Rl638I.png)

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: Ao entrar em tal op��o o bot�o sair n�o ajuda o usu�rio a retornar ao menu que queria, tirando sua liberdade.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_24]* Problema 24: Falta de bot�o "Voltar" em p�gina de erro.
**Ocorre na p�gina**: *Servi�os Acad�micos > Desist�ncia de Matr�cula em Disciplinas.*

O sistema apresenta apenas um bot�o "Sair" e n�o um bot�o "Voltar".
## Fotos
![https://drive.google.com/open?id=1wcIF_CpKgRva2V0PbZakyRa3wnB_pwEq](../../imgs/ANDR�_1wcIF_CpKgRva2V0PbZakyRa3wnB_pwEq.png)

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: A falta do bot�o tira a liberdade do usu�rio ao utilizar o portal.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_ANDR_25]* Problema 25: Falta de link para o calend�rio.
**Ocorre na p�gina**: *Servi�os Acad�micos > Desist�ncia de Matr�cula em Disciplinas.*

Ao acessar a p�gina "Desist�ncia de Matr�cula" em Disciplinas a mensagem diz ao usu�rio que consulte o calend�rio da DAC, sem dizer como fazer isso ou sequer o que � o calend�rio da DAC (Caso seja a primeira vez que o usu�rio acessa tal sistema).
## Fotos
![https://drive.google.com/open?id=1QNCXhDEq1W2QJQLhgGRLH7lYE2jY1V7Q](../../imgs/ANDR�_1QNCXhDEq1W2QJQLhgGRLH7lYE2jY1V7Q.png)

![https://drive.google.com/open?id=1c2k_FXruDnTSVuN0ivzIe6nESt1L5W2r](../../imgs/ANDR�_1c2k_FXruDnTSVuN0ivzIe6nESt1L5W2r.png)

## Considera��es

### Heur�stica ferida: 7�
**Heur�stica ferida**: 7 - Flexibilidade e efici�ncia de uso

**Justificativa**: O usu�rio perde efici�ncia pois para consultar o calend�rio da DAC ter� que ir por um caminho que a princ�pio � desconhecido j� que a mensagem n�o o auxilia a fazer tal opera��o.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_26]* Problema 26: Falta de bot�o "Voltar".
**Ocorre na p�gina**: *Servi�os Acad�micos > Desist�ncia de Matr�cula em Disciplinas.*

O site apresenta apenas um bot�o que fecha o sistema, falta um bot�o para voltar ao menu anterior.
## Fotos
![https://drive.google.com/open?id=1EA0vO73r_KLWr_enHSYPtIOms_6SbK0P](../../imgs/ANDR�_1EA0vO73r_KLWr_enHSYPtIOms_6SbK0P.png)

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: Sem um bot�o "Voltar" a opera��o de sair da mensagem mostrada e voltar ao menu anterior fica dificultada.
O usu�rio pode ainda se confundir com o bot�o "Sair" achando que vai sair da tela da mensagem par ao menu principal e acabar selecionando essa op��o, o que ir� fechar o sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_27]* Problema 27: Bot�o "Voltar" n�o "volta" corretamente.
**Ocorre na p�gina**: *Servi�os Acad�micos > Acompanhar requerimentos processados.*

A mensagem de erro est� incorreta j� que no menu anterior foi feita a escolha de visualizar tal relat�rio.
Se o relat�rio est� dispon�vel em outro menu por que n�o pode ser mostrado quando for selecionado no menu corrente?.
## Fotos
![https://drive.google.com/open?id=1OWjS-yIuCC2HTjbXhv3IrYBt1npsOCPa](../../imgs/ANDR�_1OWjS-yIuCC2HTjbXhv3IrYBt1npsOCPa.png)

![https://drive.google.com/open?id=1P8hZq-kKMXjUxHkiMz14EpfNfcgXtg7h](../../imgs/ANDR�_1P8hZq-kKMXjUxHkiMz14EpfNfcgXtg7h.png)

![https://drive.google.com/open?id=1kCYp-RQETozpf02wBhGGSiQv1XeD__WJ](../../imgs/ANDR�_1kCYp-RQETozpf02wBhGGSiQv1XeD__WJ.png)

## Coment�rios
Acredito que a mensagem correta seria exibir o relat�rio na p�gina atual afinal, segundo o sistema ele est� dispon�vel, mas em outra parte do sistema - se o usu�rio j� fez todo o percurso at� aquela tela por que obrig�-lo a voltar?.

## Considera��es

### Heur�stica ferida: 2�
**Heur�stica ferida**: 2 - Equival�ncia entre o sistema e o mundo real

**Justificativa**: O sistema est� inconsistente com o mundo real pois estou acessando uma p�gina com relat�rios, posso escolher o relat�rio que quero ter acesso na lista mas este n�o est� dispon�vel no menu em quest�o, tem um menu pr�prio.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_ANDR_28]* Problema 28: Mensagem sem sentido no contexto.
**Ocorre na p�gina**: *Servi�os Acad�micos > Relat�rio Final de Matr�cula.*

O sistema mostra uma mensagem de  �Campos Obrigat�rios� mesmo sem haver qualquer campo que possa ser preenchido.
## Fotos
![https://drive.google.com/open?id=1Jw9xGvEBQc5WsShRCgSlJqOtk52ck6uT](../../imgs/ANDR�_1Jw9xGvEBQc5WsShRCgSlJqOtk52ck6uT.png)

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: A informa��o n�o tem utilidade e s� adiciona conte�do in�til � carga visual do usu�rio.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_ANDR_29]* Problema 29: Coluna sem valor em PDF.
**Ocorre na p�gina**: *Servi�os Acad�micos > Gera��o do "Relat�rio Final de Matr�cula".*

Ao gerar um relat�rio de matr�cula  existe uma coluna "Mensagem" sem qualquer valor dentro, a visualiza��o seria melhorada se ela fosse removida para os usu�rios em que n�o tem valor algum.
## Fotos
![https://drive.google.com/open?id=1pS8QKhL4qkhM10qMK661LRL7yHa1kmmb](../../imgs/ANDR�_1pS8QKhL4qkhM10qMK661LRL7yHa1kmmb.png)

![https://drive.google.com/open?id=1vHm6nAjfMzW_M06ysKiEgR3a-YvXun-7](../../imgs/ANDR�_1vHm6nAjfMzW_M06ysKiEgR3a-YvXun-7.png)

![https://drive.google.com/open?id=1HWBveeM5tKmRZTQEevyu7CV1iqmWV9xJ](../../imgs/ANDR�_1HWBveeM5tKmRZTQEevyu7CV1iqmWV9xJ.png)

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: A coluna sem dados "rouba" espa�o das outras dificultando ao usu�rio a visualiza��o das informa��es.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_ANDR_30]* Problema 30: Falta do bot�o "Voltar".
**Ocorre na p�gina**: *Servi�os Acad�micos > Relat�rio Final de Matr�cula  > F�rias / Recupera��o.*

Ao consultar modalidades onde n�o existem relat�rios a �nica opera��o dispon�vel � o bot�o "Sair", deveria haver um bot�o "Voltar". Sair deixa em d�vida se estou �saindo desta tela do sistema� ou �saindo do sistema�.
Isso � v�lido para os campos F�rias e Recupera��o.
## Fotos
![https://drive.google.com/open?id=1cuPIpmdvvR2efzRPqZ-gYaBX76vc4WTW](../../imgs/ANDR�_1cuPIpmdvvR2efzRPqZ-gYaBX76vc4WTW.png)

![https://drive.google.com/open?id=1IS4gUaH9SXkAxEMoNG0Y2bviIYXAex-S](../../imgs/ANDR�_1IS4gUaH9SXkAxEMoNG0Y2bviIYXAex-S.png)

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: O usu�rio perde liberdade ao n�o ter a op��o de voltar.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_31]* Problema 31: Erro confuso.
**Ocorre na p�gina**: *Servi�os Acad�micos > Integraliza��o Curricular.*

Algumas vezes ao tentar visualizar a integra��o curricular um erro surge.
## Fotos
![https://drive.google.com/open?id=17SoCiXjdKqr9HJmGx67U8FNo-zyWatjA](../../imgs/ANDR�_17SoCiXjdKqr9HJmGx67U8FNo-zyWatjA.png)

![https://drive.google.com/open?id=1bRtxgb2Gp-h-T9p2t9QoeaZJtWPw-l4s](../../imgs/ANDR�_1bRtxgb2Gp-h-T9p2t9QoeaZJtWPw-l4s.png)

## Considera��es

### Heur�stica ferida: 9�
**Heur�stica ferida**: 9 - Auxiliar usu�rios a reconhecer, diagnosticar e recuperar a��es erradas

**Justificativa**: A mensagem de erro n�o foi clara, usa termos t�cnicos e mensagens de erro n�o formatadas e n�o diz o que fazer para resolver o erro.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_ANDR_32]* Problema 32: Falta do bot�o voltar
**Ocorre na p�gina**: *Servi�os Acad�micos > Erro em Integraliza��o Curricular*

A mensagem de erro mostrada tem apenas o bot�o que sai do sistema, mas � natural de qualquer usu�rio querer voltar para a p�gina anterior quando um erro ocorre.
## Fotos
![https://drive.google.com/open?id=1w5Pup1dSXeNtc1HV23IVC9AySoJXJwdr](../../imgs/ANDR�_1w5Pup1dSXeNtc1HV23IVC9AySoJXJwdr.png)

## Considera��es

### Heur�stica ferida: 3�
**Heur�stica ferida**: 3 - Liberdade e controle do usu�rio

**Justificativa**: Usu�rios perdem a liberdade pois n�o podem voltar ao sistema ap�s lidar com um erro.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_33]* Problema 33: Erro de codifica��o de caracteres.
**Ocorre na p�gina**: *Servi�os Acad�micos > Integraliza��o Curricular.*

Ao acessar a p�gina "Integraliza��o Curricular" o conte�do gerado tem v�rios problemas de codifica��o de caracteres o que faz os caracteres errados aparecerem no texto.
## Fotos
![https://drive.google.com/open?id=1j11ermi0PSoU7xHbO_VS1TZCwkwaUXsw](../../imgs/ANDR�_1j11ermi0PSoU7xHbO_VS1TZCwkwaUXsw.png)

![https://drive.google.com/open?id=1TaRndVfZjtTs38wWJyd2-6YLkG502wlg](../../imgs/ANDR�_1TaRndVfZjtTs38wWJyd2-6YLkG502wlg.png)

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: O fato do texto estar com caracteres trocados dificulta que o usu�rio interprete a informa��o na tela e se o usu�rio n�o consegue entender a informa��o ela n�o � de utilidade para ele.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_ANDR_34]* Problema 34: Bot�es com design diferente.
**Ocorre na p�gina**: *Servi�os Acad�micos > Integraliza��o Curricular.*

Os bot�es "Imprimir" e "Voltar" tem tamanhos, cores, comportamentos, ... diferentes, diminuindo a consist�ncia do sistema.
## Fotos
![https://drive.google.com/open?id=1j8_TBaJ3nVPgfgMrOeREnoL8ZMyr88kb](../../imgs/ANDR�_1j8_TBaJ3nVPgfgMrOeREnoL8ZMyr88kb.png)

## Considera��es

### Heur�stica ferida: 4�
**Heur�stica ferida**: 4 - Consist�ncia e padr�es

**Justificativa**: O sistema � inconsistente pois os bot�es deveriam seguir um mesmo padr�o.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_ANDR_35]* Problema 35: Mensagem de sucesso � igual a de erro.
**Ocorre na p�gina**: *Servi�os Acad�micos > Integraliza��o Curricular > Solicitar Hist�rico Atualizado > Confirmar.*

Na p�gina em quest�o uma mensagem de que a opera��o foi realizada com sucesso tem exatamente o mesmo design que uma mensagem de erro, o que pode confundir o usu�rio, a primeira vista � f�cil dizer que houve algo de errado.
## Fotos
![https://drive.google.com/open?id=1lks81Oh9TsEE2nKRJzu_BatMmtj4Krlm](../../imgs/ANDR�_1lks81Oh9TsEE2nKRJzu_BatMmtj4Krlm.png)

![https://drive.google.com/open?id=1HtCDrfJjKMVmzZav9cql-NcvxXAADgZO](../../imgs/ANDR�_1HtCDrfJjKMVmzZav9cql-NcvxXAADgZO.png)

## Considera��es

### Heur�stica ferida: 4�
**Heur�stica ferida**: 4 - Consist�ncia e padr�es

**Justificativa**: O sistema est� inconsistente pois mensagens com o mesmo visual querem dizer coisas diferentes.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_ANDR_36]* Problema 36: Mensagens de erro com design inconsistente.
**Ocorre na p�gina**: *Servi�os Acad�micos > Todo o sistema de "Servi�os Acad�micos".*

Existem diferentes estilos de mensagens para mostrar que houve algo de errado no sistema.
## Fotos
![https://drive.google.com/open?id=12lUjBvxTPWtUov3v3fY15iiIdXwDFE6a](../../imgs/ANDR�_12lUjBvxTPWtUov3v3fY15iiIdXwDFE6a.png)

![https://drive.google.com/open?id=1FEYXEAynESh6ZrAnGK76ynXA6915AWcL](../../imgs/ANDR�_1FEYXEAynESh6ZrAnGK76ynXA6915AWcL.png)

![https://drive.google.com/open?id=1s7uiDtjDLTPWMDrD2wlAiqSFXE2BChrE](../../imgs/ANDR�_1s7uiDtjDLTPWMDrD2wlAiqSFXE2BChrE.png)

![https://drive.google.com/open?id=1nCqgJjEWkfhMJ9PthuxBPSYrYZgk7X0U](../../imgs/ANDR�_1nCqgJjEWkfhMJ9PthuxBPSYrYZgk7X0U.png)

## Considera��es

### Heur�stica ferida: 4�
**Heur�stica ferida**: 4 - Consist�ncia e padr�es

**Justificativa**: Como um padr�o para as mensagens de erro n�o � seguido a heur�stica � adequada.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosm�tico (N�o h� necessidade imediata de solu��o)





## *id:[SRVACAD_ANDR_37]* Problema 37: Bot�o n�o deveria estar ativo.
**Ocorre na p�gina**: *Servi�os Acad�micos > Atestado de Matr�cula.*

� poss�vel tentar acessar um "Atestado de Matr�cula" mesmo que n�o haja arquivo para visualizar, o sistema deveria desabilitar a op��o nesses casos. Clicar no bot�o gera um erro.
## Fotos
![https://drive.google.com/open?id=1RkmjPccuRS8ik-HLpuQQxqFUmDvczywg](../../imgs/ANDR�_1RkmjPccuRS8ik-HLpuQQxqFUmDvczywg.png)

![https://drive.google.com/open?id=1vlvheqGscfVhtd653lgzppAebHc2f-LB](../../imgs/ANDR�_1vlvheqGscfVhtd653lgzppAebHc2f-LB.png)

![https://drive.google.com/open?id=1KlbbNQZ5fWLmX2UzB6YSv4yBeZ3H3Jzx](../../imgs/ANDR�_1KlbbNQZ5fWLmX2UzB6YSv4yBeZ3H3Jzx.png)

## Considera��es

### Heur�stica ferida: 5�
**Heur�stica ferida**: 5 - Preven��o de erro

**Justificativa**: Como j� � sabido que n�o h� arquivo a abrir e que tentar acessar relat�rios inexistentes causa um erro os desenvolvedores n�o preveniram que o usu�rio causasse esse erro pois o bot�o est� habilitado mesmo que n�o haja relat�rio a visualizar.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_ANDR_38]* Problema 38: Mensagem de erro confusa.
**Ocorre na p�gina**: *Servi�os Acad�micos > Atestado de Matr�cula.*

� poss�vel tentar acessar um "Atestado de Matr�cula" mesmo que n�o haja arquivo para visualizar, a mensagem de erro n�o � clara j� que diz que o arquivo � inv�lido sendo que n�o existe arquivo.
## Fotos
![https://drive.google.com/open?id=1HK98LnHLLh6fWp_pNrHRjvZnxYVfxOqX](../../imgs/ANDR�_1HK98LnHLLh6fWp_pNrHRjvZnxYVfxOqX.png)

## Considera��es

### Heur�stica ferida: 9�
**Heur�stica ferida**: 9 - Auxiliar usu�rios a reconhecer, diagnosticar e recuperar a��es erradas

**Justificativa**: A mensagem de erro n�o ajuda o usu�rio a diagnosticar o que ocorreu.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_39]* Problema 39: T�tulos repetidos.
**Ocorre na p�gina**: *Servi�os Acad�micos > Todos os itens em "Servi�os Acad�micos".*

As p�ginas em "Servi�os Acad�micos" tem dois campos com o mesmo t�tulo.
## Fotos
![https://drive.google.com/open?id=1-EF1fxwqKGbaXJrjNfYSKxeOEdrzCQCp](../../imgs/ANDR�_1-EF1fxwqKGbaXJrjNfYSKxeOEdrzCQCp.png)

![https://drive.google.com/open?id=11G-RyWW4y10beG8AR0wBHc6O0I6kE4SD](../../imgs/ANDR�_11G-RyWW4y10beG8AR0wBHc6O0I6kE4SD.png)

## Considera��es

### Heur�stica ferida: 8�
**Heur�stica ferida**: 8 - Est�tica e design minimalista

**Justificativa**: A presen�a de dois t�tulos apenas sobrecarrega a mem�ria visual do usu�rio.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_40]* Problema 40: P�gina de busca confusa.
**Ocorre na p�gina**: *Servi�os Acad�micos > Programas de Interc�mbio.*

A p�gina � confusa, faltam explica��es.
Estou buscando est�gios em faculdades?
Como vou saber de antem�o as cidades/universidades que t�m os programas? Preciso pesquisar uma a uma? Se sim, n�o poderia haver uma lista apenas com as cidades/faculdades cadastradas?.
## Fotos
![https://drive.google.com/open?id=1FQxz0q9YDTFP8PVj3CAaClqfbL1Nd5zl](../../imgs/ANDR�_1FQxz0q9YDTFP8PVj3CAaClqfbL1Nd5zl.png)

![https://drive.google.com/open?id=1u7FMxQqCagyo_6Kkx-fq2rTtjIRRaMBB](../../imgs/ANDR�_1u7FMxQqCagyo_6Kkx-fq2rTtjIRRaMBB.png)

## Considera��es

### Heur�stica ferida: 2�
**Heur�stica ferida**: 2 - Equival�ncia entre o sistema e o mundo real

**Justificativa**: No mundo real uma situa��o como essa n�o seria representada como foi no sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))


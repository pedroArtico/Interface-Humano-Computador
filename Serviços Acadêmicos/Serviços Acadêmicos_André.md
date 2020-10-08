# Serviços Acadêmicos
 



## *id:[SRVACAD_ANDR_11]* Problema 11: Nome do sistema muda de acordo com a página.
**Ocorre na página**: *Serviços Acadêmicos > No caminho de login em "Serviços Acadêmicos".*

Em cada etapa do login um título diferente com um formato diferente é colocado na tela, primeiramente "Serviços Acadêmicos", depois "Sistema de Senha Única e Permissões" (nesse ponto o usuário já pode estar confuso pois esperava entrar num sistema de serviços acadêmicos e não de senhas, mas pode ser que interprete que é uma etapa passar pelo sistema de login) por fim "Sistemas Acadêmicos - Serviços". 
É fácil para um usuário se confundir sem saber se está acessando o sistema correto.
## Fotos
![https://drive.google.com/open?id=1jF7Y9DWpc0sfd_j7eKve5GTn1pnrWws3](../../imgs/ANDRÉ_1jF7Y9DWpc0sfd_j7eKve5GTn1pnrWws3.png)

![https://drive.google.com/open?id=1Zwcqm1rAxFjqecFKxbEQZQckt8PyD2FS](../../imgs/ANDRÉ_1Zwcqm1rAxFjqecFKxbEQZQckt8PyD2FS.png)

![https://drive.google.com/open?id=1Sx6XGLruaMqrZjIx5BBWimDaBEGhf2zg](../../imgs/ANDRÉ_1Sx6XGLruaMqrZjIx5BBWimDaBEGhf2zg.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema não tem consistência, a cada passo do acesso o usuário passa por um sistema com nome diferente e design diferente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_12]* Problema 12: Caracteres especiais.
**Ocorre na página**: *Serviços Acadêmicos > Ao tentar fazer login em "Serviços Acadêmicos."*

O sistema em questão tem problemas em diferenciar um caractere emoji em unicode da sua representação em html, assim, deveria impedir que os mesmos fossem inseridos, ao tentar fazer login usando esses caracteres um erro é gerado.
## Fotos
![https://drive.google.com/open?id=1J0TJ0ISI_mU8iuwaPUr9LdL6IaFTy0i7](../../imgs/ANDRÉ_1J0TJ0ISI_mU8iuwaPUr9LdL6IaFTy0i7.png)

![https://drive.google.com/open?id=1yWNM-QZ2JIBH5AHceMAYajORZnGowHK3](../../imgs/ANDRÉ_1yWNM-QZ2JIBH5AHceMAYajORZnGowHK3.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: O sistema não evita que o usuário cometa erros permitindo que insira caracteres especiais nos campos de login.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_ANDR_13]* Problema 13: Erro com termos técnicos e sem ajuda.
**Ocorre na página**: *Serviços Acadêmicos > Quando um erro no login ocorre na página.*

Ao tentar fazer login na página usando caracteres especiais a página gera um erro com termos técnicos, detalhes de programação sem indicar de fato o que ocorreu de errado.
## Fotos
![https://drive.google.com/open?id=1O5qlu588YZ35NPu_6Y5LH5q-PQCSQQPL](../../imgs/ANDRÉ_1O5qlu588YZ35NPu_6Y5LH5q-PQCSQQPL.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A mensagem de erro não é clara pois não diz o que ocorreu de errado usa termos técnicos e mostra detalhes da programação do sistema. Nenhuma solução é sugerida.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SRVACAD_ANDR_14]* Problema 14: Botão "Sair" ambíguo.
**Ocorre na página**: *Serviços Acadêmicos > Ao clicar em "Sair" quando um erro de login ocorre.*

O usuário é posto em dúvida se o botão "Sair" se refere a "sair desta tela de erro" ou "sair do sistema". Ele fecha o sistema o que faz com que o usuário tenha que procurar e abrir novamente a página do sistema.
## Fotos
![https://drive.google.com/open?id=1IRR-o1Wx3CqAhhINI9znbmtK5CUocJ3b](../../imgs/ANDRÉ_1IRR-o1Wx3CqAhhINI9znbmtK5CUocJ3b.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Se houve um erro no sistema de login o usuário irá pensar em tentar fazer o login novamente, não em fechar o sistema. Em outros sistemas quando uma mensagem de erro aparece um botão "Sair" normalmente se refere a fechar a página de erro e não fechar o sistema como um todo.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_15]* Problema 15: Falha de segurança ao usar navegador.
**Ocorre na página**: *Serviços Acadêmicos > Após o login.*

Ao fazer o login no sistema é mostrada uma mensagem dizendo que dependendo do navegador utilizado e de sua versão o usuário corre riscos relacionados com a segurança. 
No caso o teste foi feito num navegador fora da lista e a ferramenta funcionou normalmente, aparentemente é aceitável que os usuários do sistema corram riscos de segurança.
## Fotos
![https://drive.google.com/open?id=12aySqRu-gGf9jVow_c7lnUWr2rf-3jZ6](../../imgs/ANDRÉ_12aySqRu-gGf9jVow_c7lnUWr2rf-3jZ6.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O sistema funciona normalmente em um navegador que não é recomendado, é dito que são problemas de segurança - mas a mensagem é mostrada após o usuário inserir seus dados em um navegador dito inseguro e fazer o login. 
Isso pode causar medo em alguns usuários ou dúvidas se precisam ou não utilizar os navegadores ditos já que o sistema funciona normalmente em um outro navegador.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_ANDR_16]* Problema 16: Mensagens conflitantes.
**Ocorre na página**: *Serviços Acadêmicos > Ao ir para a página de baixar os navegadores recomendados.*

Ao fazer o login no sistema é mostrada uma mensagem dizendo que dependendo do navegador utilizado e de sua versão o usuário corre riscos relacionados com a segurança. 
Existe um link para uma página de download dos navegadores recomendados, nela uma mensagem de aviso semelhante aparece mas com mais navegadores e em outras versões.
O usuário não tem como saber em qual mensagem deve confiar.
## Fotos
![https://drive.google.com/open?id=1q9dWQ_rn0YC5OdyVPX15_N9ftelwoDRa](../../imgs/ANDRÉ_1q9dWQ_rn0YC5OdyVPX15_N9ftelwoDRa.png)

![https://drive.google.com/open?id=1-pNuMicD3mHIe9kQttEAvD3PSvYlOF5c](../../imgs/ANDRÉ_1-pNuMicD3mHIe9kQttEAvD3PSvYlOF5c.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema está inconsistente pois existem duas mensagens para a solução do mesmo problema com soluções diferentes.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_18]* Problema 18: Falta de informação ao baixar navegadores.
**Ocorre na página**: *Serviços Acadêmicos > Baixar navegadores recomendados.*

Na página de baixar os navegadores recomendados é dado apenas o link para o arquivo instalador na maior parte dos casos. Usuários mais leigos com bastante certeza se sentiriam mais seguros se tivessem acesso aos tutoriais de instalação e acesso ao site da empresa que desenvolveu o navegador.
## Fotos
![https://drive.google.com/open?id=1K4MinxD3_9HyYaumhFpGV8gR5pmIeavn](../../imgs/ANDRÉ_1K4MinxD3_9HyYaumhFpGV8gR5pmIeavn.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Usuários leigos podem ter dificuldades com a instalação e conhecimento do software que irão instalar em seus computadores. O usuário acaba perdendo controle nesse caso.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_19]* Problema 19: Funções estão em outro sistema.
**Ocorre na página**: *Serviços Acadêmicos > Após fazer o login na ferramenta.*

É exibida uma mensagem dizendo que para fazer certas alterações de dados existe um novo sistema. Não é esclarecido se tais funções continuam no sistema atual, além disso, essa mensagem poderia aparecer antes do usuário efetuar o login já que ele é obrigado a se autenticar para então descobrir que terá que sair do sistema para acessar outro.
## Fotos
![https://drive.google.com/open?id=1BG4NLRn1rOMCM_WPBJk8NODpo_7tjxb-](../../imgs/ANDRÉ_1BG4NLRn1rOMCM_WPBJk8NODpo_7tjxb-.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Não existe lógica nas ações ao requerer que um usuário já tenha feito o login para mostrar que as opções que quer podem não estar mais no portal que ele conhece.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_ANDR_20]* Problema 20: Opções de pós-graduação para aluno da graduação apenas.
**Ocorre na página**: *Serviços Acadêmicos > Pós-graduação.*

Mesmo logado como aluno que cursa apenas Graduação o sistema mostra botões clicáveis indicando que poderia acessar opções que não correspondem com o perfil do usuário. .
## Fotos
![https://drive.google.com/open?id=146lb6TTR3bVI6MXscRo-dalH5rqIRbhv](../../imgs/ANDRÉ_146lb6TTR3bVI6MXscRo-dalH5rqIRbhv.png)

## Comentários
Poderia haver uma divisão melhor das seções e apenas a parte importante para o usuário deve aparecer.

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: Visto que ao escolher uma opção que não corresponde com o perfil do usuário um erros são gerados, o fato dessas opções estarem disponíveis mesmo com o conhecimento prévio de que os erros acontecerão caracteriza o problema em tal heurística.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_ANDR_21]* Problema 21: Muitos botões com e sem funcionalidade juntos.
**Ocorre na página**: *Serviços Acadêmicos > Tela de usuário logado.*

Mesmo logado como aluno que cursa apenas Graduação o sistema mostra botões clicáveis indicando que poderia acessar opções que não correspondem com o perfil do usuário. .
## Fotos
![https://drive.google.com/open?id=1-ORpeSVpGpnf_UJs3vreIP4XaIs90gzx](../../imgs/ANDRÉ_1-ORpeSVpGpnf_UJs3vreIP4XaIs90gzx.png)

![https://drive.google.com/open?id=135eeXsTY7RnnDcQsbGJJTJM_e6rzrlA8](../../imgs/ANDRÉ_135eeXsTY7RnnDcQsbGJJTJM_e6rzrlA8.png)

## Comentários
Seria melhor que o sistema mostrasse aos usuários que são só da graduação ou só da pós graduação seus respectivos menus e marcar botões que levam a opções que não estão disponíveis no momento como não clicáveis.

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: O sistema mostra uma seção inteira sem necessidade e em alguns casos botões para opções que não estão disponíveis no momento.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_ANDR_22]* Problema 22: Página indisponível.
**Ocorre na página**: *Serviços Acadêmicos > Desistência de Matrícula em Disciplinas.*

Ao acessar "Desistência de Matrícula em Disciplinas" é mostrada uma mensagem dizendo que a opção está indisponível, isso poderia estar marcado já no botão.
## Fotos
![https://drive.google.com/open?id=1dvSmVvpdU0VWPdF6spVmaiXbDb1u3uV7](../../imgs/ANDRÉ_1dvSmVvpdU0VWPdF6spVmaiXbDb1u3uV7.png)

![https://drive.google.com/open?id=1KL9H4iiU2zyed2ufSjTaNHCwA4rt5m3x](../../imgs/ANDRÉ_1KL9H4iiU2zyed2ufSjTaNHCwA4rt5m3x.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O usuário perde liberdade ao acessar uma função indisponível que é mostrada como se estivesse disponível.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_ANDR_23]* Problema 23: Botão "Sair" ambíguo.
**Ocorre na página**: *Serviços Acadêmicos > Desistência de Matrícula em Disciplinas.*

A mensagem exibida não tem um botão "Voltar", apenas um botão "Sair" que é mais facilmente interpretado como "Sair desta mensagem e voltar ao menu principal" do que "Sair do sistema". O botão fecha o sistema.
## Fotos
![https://drive.google.com/open?id=1lcDACS32yRRkIIeorOuUT5hZ2me3VY78](../../imgs/ANDRÉ_1lcDACS32yRRkIIeorOuUT5hZ2me3VY78.png)

![https://drive.google.com/open?id=1zgjoN8jt_URazkOIHFK3x1AjY_Rl638I](../../imgs/ANDRÉ_1zgjoN8jt_URazkOIHFK3x1AjY_Rl638I.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Ao entrar em tal opção o botão sair não ajuda o usuário a retornar ao menu que queria, tirando sua liberdade.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_24]* Problema 24: Falta de botão "Voltar" em página de erro.
**Ocorre na página**: *Serviços Acadêmicos > Desistência de Matrícula em Disciplinas.*

O sistema apresenta apenas um botão "Sair" e não um botão "Voltar".
## Fotos
![https://drive.google.com/open?id=1wcIF_CpKgRva2V0PbZakyRa3wnB_pwEq](../../imgs/ANDRÉ_1wcIF_CpKgRva2V0PbZakyRa3wnB_pwEq.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: A falta do botão tira a liberdade do usuário ao utilizar o portal.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_ANDR_25]* Problema 25: Falta de link para o calendário.
**Ocorre na página**: *Serviços Acadêmicos > Desistência de Matrícula em Disciplinas.*

Ao acessar a página "Desistência de Matrícula" em Disciplinas a mensagem diz ao usuário que consulte o calendário da DAC, sem dizer como fazer isso ou sequer o que é o calendário da DAC (Caso seja a primeira vez que o usuário acessa tal sistema).
## Fotos
![https://drive.google.com/open?id=1QNCXhDEq1W2QJQLhgGRLH7lYE2jY1V7Q](../../imgs/ANDRÉ_1QNCXhDEq1W2QJQLhgGRLH7lYE2jY1V7Q.png)

![https://drive.google.com/open?id=1c2k_FXruDnTSVuN0ivzIe6nESt1L5W2r](../../imgs/ANDRÉ_1c2k_FXruDnTSVuN0ivzIe6nESt1L5W2r.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: O usuário perde eficiência pois para consultar o calendário da DAC terá que ir por um caminho que a princípio é desconhecido já que a mensagem não o auxilia a fazer tal operação.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_26]* Problema 26: Falta de botão "Voltar".
**Ocorre na página**: *Serviços Acadêmicos > Desistência de Matrícula em Disciplinas.*

O site apresenta apenas um botão que fecha o sistema, falta um botão para voltar ao menu anterior.
## Fotos
![https://drive.google.com/open?id=1EA0vO73r_KLWr_enHSYPtIOms_6SbK0P](../../imgs/ANDRÉ_1EA0vO73r_KLWr_enHSYPtIOms_6SbK0P.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Sem um botão "Voltar" a operação de sair da mensagem mostrada e voltar ao menu anterior fica dificultada.
O usuário pode ainda se confundir com o botão "Sair" achando que vai sair da tela da mensagem par ao menu principal e acabar selecionando essa opção, o que irá fechar o sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_27]* Problema 27: Botão "Voltar" não "volta" corretamente.
**Ocorre na página**: *Serviços Acadêmicos > Acompanhar requerimentos processados.*

A mensagem de erro está incorreta já que no menu anterior foi feita a escolha de visualizar tal relatório.
Se o relatório está disponível em outro menu por que não pode ser mostrado quando for selecionado no menu corrente?.
## Fotos
![https://drive.google.com/open?id=1OWjS-yIuCC2HTjbXhv3IrYBt1npsOCPa](../../imgs/ANDRÉ_1OWjS-yIuCC2HTjbXhv3IrYBt1npsOCPa.png)

![https://drive.google.com/open?id=1P8hZq-kKMXjUxHkiMz14EpfNfcgXtg7h](../../imgs/ANDRÉ_1P8hZq-kKMXjUxHkiMz14EpfNfcgXtg7h.png)

![https://drive.google.com/open?id=1kCYp-RQETozpf02wBhGGSiQv1XeD__WJ](../../imgs/ANDRÉ_1kCYp-RQETozpf02wBhGGSiQv1XeD__WJ.png)

## Comentários
Acredito que a mensagem correta seria exibir o relatório na página atual afinal, segundo o sistema ele está disponível, mas em outra parte do sistema - se o usuário já fez todo o percurso até aquela tela por que obrigá-lo a voltar?.

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O sistema está inconsistente com o mundo real pois estou acessando uma página com relatórios, posso escolher o relatório que quero ter acesso na lista mas este não está disponível no menu em questão, tem um menu próprio.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_ANDR_28]* Problema 28: Mensagem sem sentido no contexto.
**Ocorre na página**: *Serviços Acadêmicos > Relatório Final de Matrícula.*

O sistema mostra uma mensagem de  “Campos Obrigatórios” mesmo sem haver qualquer campo que possa ser preenchido.
## Fotos
![https://drive.google.com/open?id=1Jw9xGvEBQc5WsShRCgSlJqOtk52ck6uT](../../imgs/ANDRÉ_1Jw9xGvEBQc5WsShRCgSlJqOtk52ck6uT.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A informação não tem utilidade e só adiciona conteúdo inútil à carga visual do usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_ANDR_29]* Problema 29: Coluna sem valor em PDF.
**Ocorre na página**: *Serviços Acadêmicos > Geração do "Relatório Final de Matrícula".*

Ao gerar um relatório de matrícula  existe uma coluna "Mensagem" sem qualquer valor dentro, a visualização seria melhorada se ela fosse removida para os usuários em que não tem valor algum.
## Fotos
![https://drive.google.com/open?id=1pS8QKhL4qkhM10qMK661LRL7yHa1kmmb](../../imgs/ANDRÉ_1pS8QKhL4qkhM10qMK661LRL7yHa1kmmb.png)

![https://drive.google.com/open?id=1vHm6nAjfMzW_M06ysKiEgR3a-YvXun-7](../../imgs/ANDRÉ_1vHm6nAjfMzW_M06ysKiEgR3a-YvXun-7.png)

![https://drive.google.com/open?id=1HWBveeM5tKmRZTQEevyu7CV1iqmWV9xJ](../../imgs/ANDRÉ_1HWBveeM5tKmRZTQEevyu7CV1iqmWV9xJ.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A coluna sem dados "rouba" espaço das outras dificultando ao usuário a visualização das informações.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_ANDR_30]* Problema 30: Falta do botão "Voltar".
**Ocorre na página**: *Serviços Acadêmicos > Relatório Final de Matrícula  > Férias / Recuperação.*

Ao consultar modalidades onde não existem relatórios a única operação disponível é o botão "Sair", deveria haver um botão "Voltar". Sair deixa em dúvida se estou “saindo desta tela do sistema” ou “saindo do sistema”.
Isso é válido para os campos Férias e Recuperação.
## Fotos
![https://drive.google.com/open?id=1cuPIpmdvvR2efzRPqZ-gYaBX76vc4WTW](../../imgs/ANDRÉ_1cuPIpmdvvR2efzRPqZ-gYaBX76vc4WTW.png)

![https://drive.google.com/open?id=1IS4gUaH9SXkAxEMoNG0Y2bviIYXAex-S](../../imgs/ANDRÉ_1IS4gUaH9SXkAxEMoNG0Y2bviIYXAex-S.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde liberdade ao não ter a opção de voltar.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_31]* Problema 31: Erro confuso.
**Ocorre na página**: *Serviços Acadêmicos > Integralização Curricular.*

Algumas vezes ao tentar visualizar a integração curricular um erro surge.
## Fotos
![https://drive.google.com/open?id=17SoCiXjdKqr9HJmGx67U8FNo-zyWatjA](../../imgs/ANDRÉ_17SoCiXjdKqr9HJmGx67U8FNo-zyWatjA.png)

![https://drive.google.com/open?id=1bRtxgb2Gp-h-T9p2t9QoeaZJtWPw-l4s](../../imgs/ANDRÉ_1bRtxgb2Gp-h-T9p2t9QoeaZJtWPw-l4s.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A mensagem de erro não foi clara, usa termos técnicos e mensagens de erro não formatadas e não diz o que fazer para resolver o erro.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_ANDR_32]* Problema 32: Falta do botão voltar
**Ocorre na página**: *Serviços Acadêmicos > Erro em Integralização Curricular*

A mensagem de erro mostrada tem apenas o botão que sai do sistema, mas é natural de qualquer usuário querer voltar para a página anterior quando um erro ocorre.
## Fotos
![https://drive.google.com/open?id=1w5Pup1dSXeNtc1HV23IVC9AySoJXJwdr](../../imgs/ANDRÉ_1w5Pup1dSXeNtc1HV23IVC9AySoJXJwdr.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Usuários perdem a liberdade pois não podem voltar ao sistema após lidar com um erro.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_33]* Problema 33: Erro de codificação de caracteres.
**Ocorre na página**: *Serviços Acadêmicos > Integralização Curricular.*

Ao acessar a página "Integralização Curricular" o conteúdo gerado tem vários problemas de codificação de caracteres o que faz os caracteres errados aparecerem no texto.
## Fotos
![https://drive.google.com/open?id=1j11ermi0PSoU7xHbO_VS1TZCwkwaUXsw](../../imgs/ANDRÉ_1j11ermi0PSoU7xHbO_VS1TZCwkwaUXsw.png)

![https://drive.google.com/open?id=1TaRndVfZjtTs38wWJyd2-6YLkG502wlg](../../imgs/ANDRÉ_1TaRndVfZjtTs38wWJyd2-6YLkG502wlg.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: O fato do texto estar com caracteres trocados dificulta que o usuário interprete a informação na tela e se o usuário não consegue entender a informação ela não é de utilidade para ele.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_ANDR_34]* Problema 34: Botões com design diferente.
**Ocorre na página**: *Serviços Acadêmicos > Integralização Curricular.*

Os botões "Imprimir" e "Voltar" tem tamanhos, cores, comportamentos, ... diferentes, diminuindo a consistência do sistema.
## Fotos
![https://drive.google.com/open?id=1j8_TBaJ3nVPgfgMrOeREnoL8ZMyr88kb](../../imgs/ANDRÉ_1j8_TBaJ3nVPgfgMrOeREnoL8ZMyr88kb.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema é inconsistente pois os botões deveriam seguir um mesmo padrão.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_ANDR_35]* Problema 35: Mensagem de sucesso é igual a de erro.
**Ocorre na página**: *Serviços Acadêmicos > Integralização Curricular > Solicitar Histórico Atualizado > Confirmar.*

Na página em questão uma mensagem de que a operação foi realizada com sucesso tem exatamente o mesmo design que uma mensagem de erro, o que pode confundir o usuário, a primeira vista é fácil dizer que houve algo de errado.
## Fotos
![https://drive.google.com/open?id=1lks81Oh9TsEE2nKRJzu_BatMmtj4Krlm](../../imgs/ANDRÉ_1lks81Oh9TsEE2nKRJzu_BatMmtj4Krlm.png)

![https://drive.google.com/open?id=1HtCDrfJjKMVmzZav9cql-NcvxXAADgZO](../../imgs/ANDRÉ_1HtCDrfJjKMVmzZav9cql-NcvxXAADgZO.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema está inconsistente pois mensagens com o mesmo visual querem dizer coisas diferentes.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_ANDR_36]* Problema 36: Mensagens de erro com design inconsistente.
**Ocorre na página**: *Serviços Acadêmicos > Todo o sistema de "Serviços Acadêmicos".*

Existem diferentes estilos de mensagens para mostrar que houve algo de errado no sistema.
## Fotos
![https://drive.google.com/open?id=12lUjBvxTPWtUov3v3fY15iiIdXwDFE6a](../../imgs/ANDRÉ_12lUjBvxTPWtUov3v3fY15iiIdXwDFE6a.png)

![https://drive.google.com/open?id=1FEYXEAynESh6ZrAnGK76ynXA6915AWcL](../../imgs/ANDRÉ_1FEYXEAynESh6ZrAnGK76ynXA6915AWcL.png)

![https://drive.google.com/open?id=1s7uiDtjDLTPWMDrD2wlAiqSFXE2BChrE](../../imgs/ANDRÉ_1s7uiDtjDLTPWMDrD2wlAiqSFXE2BChrE.png)

![https://drive.google.com/open?id=1nCqgJjEWkfhMJ9PthuxBPSYrYZgk7X0U](../../imgs/ANDRÉ_1nCqgJjEWkfhMJ9PthuxBPSYrYZgk7X0U.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: Como um padrão para as mensagens de erro não é seguido a heurística é adequada.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_ANDR_37]* Problema 37: Botão não deveria estar ativo.
**Ocorre na página**: *Serviços Acadêmicos > Atestado de Matrícula.*

É possível tentar acessar um "Atestado de Matrícula" mesmo que não haja arquivo para visualizar, o sistema deveria desabilitar a opção nesses casos. Clicar no botão gera um erro.
## Fotos
![https://drive.google.com/open?id=1RkmjPccuRS8ik-HLpuQQxqFUmDvczywg](../../imgs/ANDRÉ_1RkmjPccuRS8ik-HLpuQQxqFUmDvczywg.png)

![https://drive.google.com/open?id=1vlvheqGscfVhtd653lgzppAebHc2f-LB](../../imgs/ANDRÉ_1vlvheqGscfVhtd653lgzppAebHc2f-LB.png)

![https://drive.google.com/open?id=1KlbbNQZ5fWLmX2UzB6YSv4yBeZ3H3Jzx](../../imgs/ANDRÉ_1KlbbNQZ5fWLmX2UzB6YSv4yBeZ3H3Jzx.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: Como já é sabido que não há arquivo a abrir e que tentar acessar relatórios inexistentes causa um erro os desenvolvedores não preveniram que o usuário causasse esse erro pois o botão está habilitado mesmo que não haja relatório a visualizar.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_ANDR_38]* Problema 38: Mensagem de erro confusa.
**Ocorre na página**: *Serviços Acadêmicos > Atestado de Matrícula.*

É possível tentar acessar um "Atestado de Matrícula" mesmo que não haja arquivo para visualizar, a mensagem de erro não é clara já que diz que o arquivo é inválido sendo que não existe arquivo.
## Fotos
![https://drive.google.com/open?id=1HK98LnHLLh6fWp_pNrHRjvZnxYVfxOqX](../../imgs/ANDRÉ_1HK98LnHLLh6fWp_pNrHRjvZnxYVfxOqX.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A mensagem de erro não ajuda o usuário a diagnosticar o que ocorreu.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_39]* Problema 39: Títulos repetidos.
**Ocorre na página**: *Serviços Acadêmicos > Todos os itens em "Serviços Acadêmicos".*

As páginas em "Serviços Acadêmicos" tem dois campos com o mesmo título.
## Fotos
![https://drive.google.com/open?id=1-EF1fxwqKGbaXJrjNfYSKxeOEdrzCQCp](../../imgs/ANDRÉ_1-EF1fxwqKGbaXJrjNfYSKxeOEdrzCQCp.png)

![https://drive.google.com/open?id=11G-RyWW4y10beG8AR0wBHc6O0I6kE4SD](../../imgs/ANDRÉ_11G-RyWW4y10beG8AR0wBHc6O0I6kE4SD.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A presença de dois títulos apenas sobrecarrega a memória visual do usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_40]* Problema 40: Página de busca confusa.
**Ocorre na página**: *Serviços Acadêmicos > Programas de Intercâmbio.*

A página é confusa, faltam explicações.
Estou buscando estágios em faculdades?
Como vou saber de antemão as cidades/universidades que têm os programas? Preciso pesquisar uma a uma? Se sim, não poderia haver uma lista apenas com as cidades/faculdades cadastradas?.
## Fotos
![https://drive.google.com/open?id=1FQxz0q9YDTFP8PVj3CAaClqfbL1Nd5zl](../../imgs/ANDRÉ_1FQxz0q9YDTFP8PVj3CAaClqfbL1Nd5zl.png)

![https://drive.google.com/open?id=1u7FMxQqCagyo_6Kkx-fq2rTtjIRRaMBB](../../imgs/ANDRÉ_1u7FMxQqCagyo_6Kkx-fq2rTtjIRRaMBB.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: No mundo real uma situação como essa não seria representada como foi no sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))


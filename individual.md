# Documento de avaliação segundo as Heurísticas de Nielsen
## Avaliação individual
**Página Avaliada**: [https://www.dac.unicamp.br/portal/acesso/estudantes](https://www.dac.unicamp.br/portal/acesso/estudantes)


![data/paginaavaliada.png](data/paginaavaliada.png)
O procedimento de avaliação das heurísticas foi feito em dois momentos distintos. Primeiro, cada um dos quatro integrantes do grupo avaliou individualmente o site da Diretoria Acadêmica. Foi criado um documento no GOOGLE FORMS contendo cada uma das questões referentes aos problemas, tais como: nome,  seção onde o problema aparece, descrição do problema, imagem, heurísticas, justificativa e grau de severidade. O documento foi preenchido para cada problema individualmente, gerando um documento do Google Sheets como resultado. Esse documento foi processado por um programa escrito em Python para colocar os dados da tabela em um documento de texto.

Após a avaliação ter sido feita individualmente (os alunos não trocaram informações sobre os problemas encontrados durante o período de análise), o grupo se uniu para definir quais problemas em comum foram encontrados. Os problemas que foram encontrados individualmente foram avaliados, e alguns erros na definição de heurísticas e graus de severidade foram corrigidos.


**Formulário utilizado**

![data/form.png](data/form.png)



* **Link para o formulário utilizado**: [Formulário](https://docs.google.com/forms/d/e/1FAIpQLScmZ_LzhXA_dx5XmhWrQjtcYFNG7xgcjER1TXufxEPOvflIjQ/viewform)
* **Link para o software desenvolvido**: [GitHub](https://github.com/ALREstevam/Gsheet-IHC/)

---------------


# Problemas levantados por: *André*




## *id:[ESTU_ANDR_1]* Problema 1: Opções com conteúdos ambíguos.
**Ocorre na página**: *Estudantes > Menu Estudantes.*

No menu estudantes existem várias opções ambíguas, o que dificulta para o usuário descobrir qual sistema precisa acessar para fazer sua tarefa. Por exemplo: existem menus diferentes com os itens "Relatório de matrícula" e "Atestado de Matrícula", seriam a mesma coisa ou não? 
O item de "Relatório de Matrícula" está na seção "Alteração de matrícula", em "Serviços Acadêmicos" há o item "Matrícula", nesse caso o sistema de alteração de matrícula também gera relatórios? No quadro com a opção "Matrícula", alterar a matrícula não faria parte já de um sistema "Matrícula"? Existe uma separação que confunde o usuário.
O sistema SIGA também tem opções referentes à matrícula, o usuário não tem como saber qual opção precisa usar.
## Fotos
![https://drive.google.com/open?id=17TRAvl8CIB4wThbZYKkBrO3mkLdybmoT](./imgs/ANDRÉ_17TRAvl8CIB4wThbZYKkBrO3mkLdybmoT.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Existe na mesma tela quadros com informações repetidas/inconsistentes/incoerentes dificultando com que o usuário encontre a opção que deseja.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ESTU_ANDR_2]* Problema 2: Nomes semelhantes.
**Ocorre na página**: *Estudantes > Menu Estudantes.*

Não deixa claro a diferença entre desistência de matrícula e cancelamento de matrícula, ao cancelar minha matrícula numa disciplina estou desistindo dela?.
## Fotos
![https://drive.google.com/open?id=1QfvM-IRONMgKKKxvHuATL6-x4FR3BkKE](./imgs/ANDRÉ_1QfvM-IRONMgKKKxvHuATL6-x4FR3BkKE.png)

![https://drive.google.com/open?id=1JMYd_dUuMtxJDaQJE1GeB_13gvf4Eliz](./imgs/ANDRÉ_1JMYd_dUuMtxJDaQJE1GeB_13gvf4Eliz.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Opções ambíguas confundem o usuário em termos de qual sistema ele deve acessar.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTU_ANDR_3]* Problema 3: Menu separado para "Alteração de Matrícula."
**Ocorre na página**: *Estudantes > Menu Estudantes.*

Coisas relacionadas com a matrícula são serviços acadêmicos, por que existe um menu a parte apenas para a alteração da matrícula? 
Não se pode fazer uma alteração de matrícula pelo serviço em "Serviços Acadêmicos"?
Um usuário que fez uma matrícula pelos "Serviços Acadêmicos" precisa ir em um outro menu caso queira fazer uma alteração logo em seguida.
## Fotos
![https://drive.google.com/open?id=1slEBIJy-uGprwTpV0KPM1uUnSAKRq1i7](./imgs/ANDRÉ_1slEBIJy-uGprwTpV0KPM1uUnSAKRq1i7.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Opções relacionadas com matrícula estão dispersas em vários menus que acessam vários sistemas, com toda essa informação o usuário não consegue saber de fato o que cada sistema faz ou não faz.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTU_ANDR_4]* Problema 4: Janela de login.
**Ocorre na página**: *Estudantes > Menu Estudantes > Intranet.*

Ao clicar em “intranet” o uma caixa de diálogo aparece.
Não é informado qual login e senha são requeridos.
Não é informado se trata-se da mesma intranet que os alunos acessam pelo site da FT.
Caso essa seja uma ferramenta de administração por que existe um link no site onde qualquer um poderia tentar o acesso sem saber do que se trata.
## Fotos
![https://drive.google.com/open?id=1HW6qdDhQW0SbZvdStAY49stNxIqkzdvp](./imgs/ANDRÉ_1HW6qdDhQW0SbZvdStAY49stNxIqkzdvp.png)

## Comentários
Acredito que seja um link para um sistema de gerenciamento da administração do site, se for o caso acredito que seria melhor que este link não estivesse disponível em todas as páginas do portal e que ao exibir a janela de login existisse uma mensagem como "Esta é uma tela de login para a administração do site, caso você seja um administrador utilize seu login e senha ... no formato ...".

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: Não existem explicações sobre o que se trata a tela de login, formato de login ou em qual sistema está sendo feito o acesso, assim o usuário pode cometer erros ao tentar inserir os campos e acessar o sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ESTU_ANDR_5]* Problema 5: Erro ao acessar intranet.
**Ocorre na página**: *Estudantes > Menu Estudantes  > Intranet.*

Ao acessar o menu intranet, inserir um login e senha na caixa de diálogo e clicar em entrar a caixa de diálogo fecha e uma nova aparece, sem os dados inseridos e sem dizer qual foi o erro no login, ao clicar em cancelar sou redirecionado para  uma página de erro.
## Fotos
![https://drive.google.com/open?id=12dygWgWM6AyVqwssAsX8oFRkwWSFNx0H](./imgs/ANDRÉ_12dygWgWM6AyVqwssAsX8oFRkwWSFNx0H.png)

![https://drive.google.com/open?id=1SVyNqcAxYIjBqEUR9fy4d4cqKNFG1ezo](./imgs/ANDRÉ_1SVyNqcAxYIjBqEUR9fy4d4cqKNFG1ezo.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: Não existem mensagens de erro ao tentar fazer um login com credenciais incorretas.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ESTU_ANDR_6]* Problema 6: Botões que não levam a lugar algum.
**Ocorre na página**: *Estudantes > Menu Estudantes > Intranet > Cancelar.*

Ao acessar o menu intranet, inserir um login e senha na caixa de diálogo e clicar em entrar a caixa de diálogo fecha e uma nova aparece, sem os dados inseridos e sem dizer qual foi o erro no login, ao clicar em cancelar sou redirecionado para  uma página de erro.
## Fotos
![https://drive.google.com/open?id=1NtX2WUpi6km0-sBnWam-1OcbBSCKJ1rS](./imgs/ANDRÉ_1NtX2WUpi6km0-sBnWam-1OcbBSCKJ1rS.png)

![https://drive.google.com/open?id=1fygN_5fA9AigAellO7-kr0lU-YiAr2OJ](./imgs/ANDRÉ_1fygN_5fA9AigAellO7-kr0lU-YiAr2OJ.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Caso o usuário entre nessa janela por engano clicar em "Ok" irá abrir uma outra janela de diálogo e clicar em "Cancelar" irá redirecioná-lo a uma página de erro sem o botão "Voltar", portanto ele perde a liberdade durante a navegação no portal.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ESTU_ANDR_7]* Problema 7: Mensagem de erro em inglês.
**Ocorre na página**: *Estudantes > Menu Estudantes > Intranet > Cancelar.*

Ao acessar o menu intranet, inserir um login e senha na caixa de diálogo e clicar em entrar a caixa de diálogo fecha e uma nova aparece, sem os dados inseridos e sem dizer qual foi o erro no login, ao clicar em cancelar sou redirecionado para  uma página de erro.
A página de erro está em inglês e a mensagem não é assertiva o suficiente para o usuário conseguir diagnosticar o que fez de errado, além disso a página não possui um botão "Voltar".
## Fotos
![https://drive.google.com/open?id=1LypYzK2QECeQZzZauxrtRK3gtYw7uMa8](./imgs/ANDRÉ_1LypYzK2QECeQZzZauxrtRK3gtYw7uMa8.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A mensagem de erro em inglês e pouco clara não ajuda o usuário a saber o que fez de errado.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTU_ANDR_8]* Problema 8: Falta de botão "Voltar" em página de erro.
**Ocorre na página**: *Estudantes > Menu Estudantes > Intranet > Cancelar.*

Ao acessar o menu intranet, inserir um login e senha na caixa de diálogo e clicar em entrar a caixa de diálogo fecha e uma nova aparece, sem os dados inseridos e sem dizer qual foi o erro no login, ao clicar em cancelar sou redirecionado para  uma página de erro.
A página de erro está em inglês e a mensagem não é assertiva o suficiente para o usuário conseguir diagnosticar o que fez de errado, além disso a página não possui um botão "Voltar".
## Fotos
![https://drive.google.com/open?id=1oZQbTyGpzD6femsr1oaCL3feYKntyn-L](./imgs/ANDRÉ_1oZQbTyGpzD6femsr1oaCL3feYKntyn-L.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: A falta do botão "Voltar" faz com que o usuário tenha uma perda do controle que tinha ao utilizar o sistema já que a página de erro não apresenta nenhum link ou botão que o direcione para o próximo passo em seu objetivo.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ESTU_ANDR_9]* Problema 9: Botão "Entrar" não faz nada.
**Ocorre na página**: *Estudantes > Menu Estudantes > Intranet.*

Ao acessar o menu intranet, inserir um login e senha na caixa de diálogo e clicar em entrar a caixa de diálogo fecha e uma nova aparece, sem os dados inseridos e sem dizer qual foi o erro no login, ao clicar em cancelar o usuário é redirecionado para  uma página de erro.
## Fotos
![https://drive.google.com/open?id=1j238H3M1zFRikrzuzIkuzefzPxsiFGDT](./imgs/ANDRÉ_1j238H3M1zFRikrzuzIkuzefzPxsiFGDT.png)

## Considerações

### Heurística ferida: 1ª
**Heurística ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: O sistema não oferece qualquer feedback ao tentar fazer o login, em casos onde o login está incorreto a mesma janela é mostrada novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ESTU_ANDR_10]* Problema 10: Ícone não muda em alto contraste.
**Ocorre na página**: *Estudantes > Menu Estudantes > Botão "Alto Contraste".*

Ao usar a opção alto contraste do site um dos ícones não muda de cor.
## Fotos
![https://drive.google.com/open?id=1NqJoAIeRFbXTmxBv_89EeYnECRflcTwz](./imgs/ANDRÉ_1NqJoAIeRFbXTmxBv_89EeYnECRflcTwz.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: Um dos ícones sai do padrão ao ativar o modo de alto contraste, o usuário pode ser levado a pensar que é uma opção diferenciada, mais importante ou em destaque.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_ANDR_11]* Problema 11: Nome do sistema muda de acordo com a página.
**Ocorre na página**: *Serviços Acadêmicos > No caminho de login em "Serviços Acadêmicos".*

Em cada etapa do login um título diferente com um formato diferente é colocado na tela, primeiramente "Serviços Acadêmicos", depois "Sistema de Senha Única e Permissões" (nesse ponto o usuário já pode estar confuso pois esperava entrar num sistema de serviços acadêmicos e não de senhas, mas pode ser que interprete que é uma etapa passar pelo sistema de login) por fim "Sistemas Acadêmicos - Serviços". 
É fácil para um usuário se confundir sem saber se está acessando o sistema correto.
## Fotos
![https://drive.google.com/open?id=1jF7Y9DWpc0sfd_j7eKve5GTn1pnrWws3](./imgs/ANDRÉ_1jF7Y9DWpc0sfd_j7eKve5GTn1pnrWws3.png)

![https://drive.google.com/open?id=1Zwcqm1rAxFjqecFKxbEQZQckt8PyD2FS](./imgs/ANDRÉ_1Zwcqm1rAxFjqecFKxbEQZQckt8PyD2FS.png)

![https://drive.google.com/open?id=1Sx6XGLruaMqrZjIx5BBWimDaBEGhf2zg](./imgs/ANDRÉ_1Sx6XGLruaMqrZjIx5BBWimDaBEGhf2zg.png)

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
![https://drive.google.com/open?id=1J0TJ0ISI_mU8iuwaPUr9LdL6IaFTy0i7](./imgs/ANDRÉ_1J0TJ0ISI_mU8iuwaPUr9LdL6IaFTy0i7.png)

![https://drive.google.com/open?id=1yWNM-QZ2JIBH5AHceMAYajORZnGowHK3](./imgs/ANDRÉ_1yWNM-QZ2JIBH5AHceMAYajORZnGowHK3.png)

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
![https://drive.google.com/open?id=1O5qlu588YZ35NPu_6Y5LH5q-PQCSQQPL](./imgs/ANDRÉ_1O5qlu588YZ35NPu_6Y5LH5q-PQCSQQPL.png)

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
![https://drive.google.com/open?id=1IRR-o1Wx3CqAhhINI9znbmtK5CUocJ3b](./imgs/ANDRÉ_1IRR-o1Wx3CqAhhINI9znbmtK5CUocJ3b.png)

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
![https://drive.google.com/open?id=12aySqRu-gGf9jVow_c7lnUWr2rf-3jZ6](./imgs/ANDRÉ_12aySqRu-gGf9jVow_c7lnUWr2rf-3jZ6.png)

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
![https://drive.google.com/open?id=1q9dWQ_rn0YC5OdyVPX15_N9ftelwoDRa](./imgs/ANDRÉ_1q9dWQ_rn0YC5OdyVPX15_N9ftelwoDRa.png)

![https://drive.google.com/open?id=1-pNuMicD3mHIe9kQttEAvD3PSvYlOF5c](./imgs/ANDRÉ_1-pNuMicD3mHIe9kQttEAvD3PSvYlOF5c.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema está inconsistente pois existem duas mensagens para a solução do mesmo problema com soluções diferentes.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTU_ANDR_17]* Problema 17: Problemas na utilização com o teclado.
**Ocorre na página**: *Estudantes > Ao navegar pelo menu "Estudantes".*

Era esperado que pudesse navegar entre os quadros utilizando a tecla tab ou as teclas direcionais, isso não é possível.
## Fotos
![https://drive.google.com/open?id=171dRhdUupMesWyKAxoT9CmPqRHn9-dD6](./imgs/ANDRÉ_171dRhdUupMesWyKAxoT9CmPqRHn9-dD6.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: A falta de atalhos de teclado e funcionalidades simples com o teclado dificultam o manuseio do sistema para usuários experientes.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_ANDR_18]* Problema 18: Falta de informação ao baixar navegadores.
**Ocorre na página**: *Serviços Acadêmicos > Baixar navegadores recomendados.*

Na página de baixar os navegadores recomendados é dado apenas o link para o arquivo instalador na maior parte dos casos. Usuários mais leigos com bastante certeza se sentiriam mais seguros se tivessem acesso aos tutoriais de instalação e acesso ao site da empresa que desenvolveu o navegador.
## Fotos
![https://drive.google.com/open?id=1K4MinxD3_9HyYaumhFpGV8gR5pmIeavn](./imgs/ANDRÉ_1K4MinxD3_9HyYaumhFpGV8gR5pmIeavn.png)

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
![https://drive.google.com/open?id=1BG4NLRn1rOMCM_WPBJk8NODpo_7tjxb-](./imgs/ANDRÉ_1BG4NLRn1rOMCM_WPBJk8NODpo_7tjxb-.png)

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
![https://drive.google.com/open?id=146lb6TTR3bVI6MXscRo-dalH5rqIRbhv](./imgs/ANDRÉ_146lb6TTR3bVI6MXscRo-dalH5rqIRbhv.png)

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
![https://drive.google.com/open?id=1-ORpeSVpGpnf_UJs3vreIP4XaIs90gzx](./imgs/ANDRÉ_1-ORpeSVpGpnf_UJs3vreIP4XaIs90gzx.png)

![https://drive.google.com/open?id=135eeXsTY7RnnDcQsbGJJTJM_e6rzrlA8](./imgs/ANDRÉ_135eeXsTY7RnnDcQsbGJJTJM_e6rzrlA8.png)

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
![https://drive.google.com/open?id=1dvSmVvpdU0VWPdF6spVmaiXbDb1u3uV7](./imgs/ANDRÉ_1dvSmVvpdU0VWPdF6spVmaiXbDb1u3uV7.png)

![https://drive.google.com/open?id=1KL9H4iiU2zyed2ufSjTaNHCwA4rt5m3x](./imgs/ANDRÉ_1KL9H4iiU2zyed2ufSjTaNHCwA4rt5m3x.png)

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
![https://drive.google.com/open?id=1lcDACS32yRRkIIeorOuUT5hZ2me3VY78](./imgs/ANDRÉ_1lcDACS32yRRkIIeorOuUT5hZ2me3VY78.png)

![https://drive.google.com/open?id=1zgjoN8jt_URazkOIHFK3x1AjY_Rl638I](./imgs/ANDRÉ_1zgjoN8jt_URazkOIHFK3x1AjY_Rl638I.png)

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
![https://drive.google.com/open?id=1wcIF_CpKgRva2V0PbZakyRa3wnB_pwEq](./imgs/ANDRÉ_1wcIF_CpKgRva2V0PbZakyRa3wnB_pwEq.png)

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
![https://drive.google.com/open?id=1QNCXhDEq1W2QJQLhgGRLH7lYE2jY1V7Q](./imgs/ANDRÉ_1QNCXhDEq1W2QJQLhgGRLH7lYE2jY1V7Q.png)

![https://drive.google.com/open?id=1c2k_FXruDnTSVuN0ivzIe6nESt1L5W2r](./imgs/ANDRÉ_1c2k_FXruDnTSVuN0ivzIe6nESt1L5W2r.png)

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
![https://drive.google.com/open?id=1EA0vO73r_KLWr_enHSYPtIOms_6SbK0P](./imgs/ANDRÉ_1EA0vO73r_KLWr_enHSYPtIOms_6SbK0P.png)

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
![https://drive.google.com/open?id=1OWjS-yIuCC2HTjbXhv3IrYBt1npsOCPa](./imgs/ANDRÉ_1OWjS-yIuCC2HTjbXhv3IrYBt1npsOCPa.png)

![https://drive.google.com/open?id=1P8hZq-kKMXjUxHkiMz14EpfNfcgXtg7h](./imgs/ANDRÉ_1P8hZq-kKMXjUxHkiMz14EpfNfcgXtg7h.png)

![https://drive.google.com/open?id=1kCYp-RQETozpf02wBhGGSiQv1XeD__WJ](./imgs/ANDRÉ_1kCYp-RQETozpf02wBhGGSiQv1XeD__WJ.png)

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
![https://drive.google.com/open?id=1Jw9xGvEBQc5WsShRCgSlJqOtk52ck6uT](./imgs/ANDRÉ_1Jw9xGvEBQc5WsShRCgSlJqOtk52ck6uT.png)

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
![https://drive.google.com/open?id=1pS8QKhL4qkhM10qMK661LRL7yHa1kmmb](./imgs/ANDRÉ_1pS8QKhL4qkhM10qMK661LRL7yHa1kmmb.png)

![https://drive.google.com/open?id=1vHm6nAjfMzW_M06ysKiEgR3a-YvXun-7](./imgs/ANDRÉ_1vHm6nAjfMzW_M06ysKiEgR3a-YvXun-7.png)

![https://drive.google.com/open?id=1HWBveeM5tKmRZTQEevyu7CV1iqmWV9xJ](./imgs/ANDRÉ_1HWBveeM5tKmRZTQEevyu7CV1iqmWV9xJ.png)

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
![https://drive.google.com/open?id=1cuPIpmdvvR2efzRPqZ-gYaBX76vc4WTW](./imgs/ANDRÉ_1cuPIpmdvvR2efzRPqZ-gYaBX76vc4WTW.png)

![https://drive.google.com/open?id=1IS4gUaH9SXkAxEMoNG0Y2bviIYXAex-S](./imgs/ANDRÉ_1IS4gUaH9SXkAxEMoNG0Y2bviIYXAex-S.png)

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
![https://drive.google.com/open?id=17SoCiXjdKqr9HJmGx67U8FNo-zyWatjA](./imgs/ANDRÉ_17SoCiXjdKqr9HJmGx67U8FNo-zyWatjA.png)

![https://drive.google.com/open?id=1bRtxgb2Gp-h-T9p2t9QoeaZJtWPw-l4s](./imgs/ANDRÉ_1bRtxgb2Gp-h-T9p2t9QoeaZJtWPw-l4s.png)

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
![https://drive.google.com/open?id=1w5Pup1dSXeNtc1HV23IVC9AySoJXJwdr](./imgs/ANDRÉ_1w5Pup1dSXeNtc1HV23IVC9AySoJXJwdr.png)

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
![https://drive.google.com/open?id=1j11ermi0PSoU7xHbO_VS1TZCwkwaUXsw](./imgs/ANDRÉ_1j11ermi0PSoU7xHbO_VS1TZCwkwaUXsw.png)

![https://drive.google.com/open?id=1TaRndVfZjtTs38wWJyd2-6YLkG502wlg](./imgs/ANDRÉ_1TaRndVfZjtTs38wWJyd2-6YLkG502wlg.png)

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
![https://drive.google.com/open?id=1j8_TBaJ3nVPgfgMrOeREnoL8ZMyr88kb](./imgs/ANDRÉ_1j8_TBaJ3nVPgfgMrOeREnoL8ZMyr88kb.png)

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
![https://drive.google.com/open?id=1lks81Oh9TsEE2nKRJzu_BatMmtj4Krlm](./imgs/ANDRÉ_1lks81Oh9TsEE2nKRJzu_BatMmtj4Krlm.png)

![https://drive.google.com/open?id=1HtCDrfJjKMVmzZav9cql-NcvxXAADgZO](./imgs/ANDRÉ_1HtCDrfJjKMVmzZav9cql-NcvxXAADgZO.png)

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
![https://drive.google.com/open?id=12lUjBvxTPWtUov3v3fY15iiIdXwDFE6a](./imgs/ANDRÉ_12lUjBvxTPWtUov3v3fY15iiIdXwDFE6a.png)

![https://drive.google.com/open?id=1FEYXEAynESh6ZrAnGK76ynXA6915AWcL](./imgs/ANDRÉ_1FEYXEAynESh6ZrAnGK76ynXA6915AWcL.png)

![https://drive.google.com/open?id=1s7uiDtjDLTPWMDrD2wlAiqSFXE2BChrE](./imgs/ANDRÉ_1s7uiDtjDLTPWMDrD2wlAiqSFXE2BChrE.png)

![https://drive.google.com/open?id=1nCqgJjEWkfhMJ9PthuxBPSYrYZgk7X0U](./imgs/ANDRÉ_1nCqgJjEWkfhMJ9PthuxBPSYrYZgk7X0U.png)

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
![https://drive.google.com/open?id=1RkmjPccuRS8ik-HLpuQQxqFUmDvczywg](./imgs/ANDRÉ_1RkmjPccuRS8ik-HLpuQQxqFUmDvczywg.png)

![https://drive.google.com/open?id=1vlvheqGscfVhtd653lgzppAebHc2f-LB](./imgs/ANDRÉ_1vlvheqGscfVhtd653lgzppAebHc2f-LB.png)

![https://drive.google.com/open?id=1KlbbNQZ5fWLmX2UzB6YSv4yBeZ3H3Jzx](./imgs/ANDRÉ_1KlbbNQZ5fWLmX2UzB6YSv4yBeZ3H3Jzx.png)

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
![https://drive.google.com/open?id=1HK98LnHLLh6fWp_pNrHRjvZnxYVfxOqX](./imgs/ANDRÉ_1HK98LnHLLh6fWp_pNrHRjvZnxYVfxOqX.png)

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
![https://drive.google.com/open?id=1-EF1fxwqKGbaXJrjNfYSKxeOEdrzCQCp](./imgs/ANDRÉ_1-EF1fxwqKGbaXJrjNfYSKxeOEdrzCQCp.png)

![https://drive.google.com/open?id=11G-RyWW4y10beG8AR0wBHc6O0I6kE4SD](./imgs/ANDRÉ_11G-RyWW4y10beG8AR0wBHc6O0I6kE4SD.png)

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
![https://drive.google.com/open?id=1FQxz0q9YDTFP8PVj3CAaClqfbL1Nd5zl](./imgs/ANDRÉ_1FQxz0q9YDTFP8PVj3CAaClqfbL1Nd5zl.png)

![https://drive.google.com/open?id=1u7FMxQqCagyo_6Kkx-fq2rTtjIRRaMBB](./imgs/ANDRÉ_1u7FMxQqCagyo_6Kkx-fq2rTtjIRRaMBB.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: No mundo real uma situação como essa não seria representada como foi no sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ALTEMATR_ANDR_41]* Problema 41: Erro confuso.
**Ocorre na página**: *Alteração de Matrícula > Alteração de Matrícula.*

Um erro ocorre ao digitar certos caracteres especiais. O motivo do erro não é indicado e não é feita verificação antes do envio dos dados.
## Fotos
![https://drive.google.com/open?id=14hdzFcm3Oe0X1okzH99PiAbgRfr_32JQ](./imgs/ANDRÉ_14hdzFcm3Oe0X1okzH99PiAbgRfr_32JQ.png)

![https://drive.google.com/open?id=1rdgDU-cvmg_LYeLj2unmCTP7XvTN91Ao](./imgs/ANDRÉ_1rdgDU-cvmg_LYeLj2unmCTP7XvTN91Ao.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A mensagem de erro não auxilia em nada o usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ALTEMATR_ANDR_42]* Problema 42: Campos não verificados.
**Ocorre na página**: *Alteração de Matrícula > Alteração de Matrícula.*

Um erro ocorre ao digitar certos caracteres especiais, não é feita a verificação antes do envio dos dados.
## Fotos
![https://drive.google.com/open?id=1kLQGj0D5SdZHvjubxMO6VEWxv_0Ltzxa](./imgs/ANDRÉ_1kLQGj0D5SdZHvjubxMO6VEWxv_0Ltzxa.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: Como não há verificação o sistema não impede que o usuário deliberadamente cometa o erro.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_ANDR_43]* Problema 43: Cliques não permitidos.
**Ocorre na página**: *Alteração de Matrícula > Todo o sistema.*

Uma caixa de diálogo aparece quando o usuário tenta clicar com o botão direito do mouse ou com o scroll dizendo que tal função é inválida.
## Fotos
![https://drive.google.com/open?id=1YXXNTkk0q4Cr9aILxW3HURYgcZU7Onsq](./imgs/ANDRÉ_1YXXNTkk0q4Cr9aILxW3HURYgcZU7Onsq.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema impede o usuário de utilizar funções disponíveis na maioria dos sistemas.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ALTEMATR_ANDR_44]* Problema 44: Botões do mouse são bloqueados.
**Ocorre na página**: *Alteração de Matrícula > Todo o sistema*

Uma caixa de diálogo aparece quando o usuário tenta clicar com o botão direito do mouse ou com o scroll dizendo que tal função é inválida.
## Fotos
![https://drive.google.com/open?id=1VL1s7HADBieNBNWkB8_SAeNNtjZkHZGQ](./imgs/ANDRÉ_1VL1s7HADBieNBNWkB8_SAeNNtjZkHZGQ.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: O sistema impede que o usuário utilize a função "abrir em uma nova guia" ao clicar em um link com o scroll do mouse.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_ANDR_45]* Problema 45: Mensagem de erro não auxilia o usuário.
**Ocorre na página**: *Alteração de Matrícula > Informar Pedido de Alteração de Matrícula e Acompanhar Pedido de Alteração de Matrícula validado.*

A mensagem de erro exibida ao acessar certas funções diz que o usuário precisa consultar o calendário da DAC mas sem fornecer o caminho para isso.
## Fotos
![https://drive.google.com/open?id=1IrX8V6w2KxE0Sq1X9ngmL2atSOG72H8b](./imgs/ANDRÉ_1IrX8V6w2KxE0Sq1X9ngmL2atSOG72H8b.png)

![https://drive.google.com/open?id=1X2GO8kYLUorp6tU1vhoyYXSUvkmWmWki](./imgs/ANDRÉ_1X2GO8kYLUorp6tU1vhoyYXSUvkmWmWki.png)

![https://drive.google.com/open?id=1vFMaJZzfV0UfBMYrK8hax2JTNrroGSz2](./imgs/ANDRÉ_1vFMaJZzfV0UfBMYrK8hax2JTNrroGSz2.png)

![https://drive.google.com/open?id=1BT8Zi5HI0Pj9qDvvTr958fOw00oNOfPF](./imgs/ANDRÉ_1BT8Zi5HI0Pj9qDvvTr958fOw00oNOfPF.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: As mensagens de erro dizem o que deve ser feito mas não como fazê-lo.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ALTEMATR_ANDR_46]* Problema 46: Mensagens de erro inconsistentes.
**Ocorre na página**: *Alteração de Matrícula > Várias mensagens de erro do sistema.*

No sistema nem todas as mensagens de erro tem um botão "Voltar", algumas apresentam apenas a opção de sair do sistema.
## Fotos
![https://drive.google.com/open?id=18idZFLsfFozMUiyRW-lAA-HkPesTGNhl](./imgs/ANDRÉ_18idZFLsfFozMUiyRW-lAA-HkPesTGNhl.png)

![https://drive.google.com/open?id=19V15DWQazHY4kee-qOElA2p_BI2kuJ4w](./imgs/ANDRÉ_19V15DWQazHY4kee-qOElA2p_BI2kuJ4w.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema está inconsistente visto que interfaces que deveriam seguir um mesmo padrão não o seguem.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_ANDR_47]* Problema 47: Problema com texto de ajuda.
**Ocorre na página**: *Alteração de Matrícula > Seção de ajuda.*

A página de ajuda está com problema na codificação dos caracteres.
## Fotos
![https://drive.google.com/open?id=1DRFt-T6yzmtMo7z3D60bLTZqMRoyIEIq](./imgs/ANDRÉ_1DRFt-T6yzmtMo7z3D60bLTZqMRoyIEIq.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: O problema de codificação leva o usuário a ter dificuldade na leitura, tornando a página de ajuda bem menos útil.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ALTEMATR_ANDR_48]* Problema 48: Mensagem de erro inconsistente.
**Ocorre na página**: *Alteração de Matrícula > Serviços do Aluno.*

O portal diz que um acesso indevido está sendo feito sendo que esse não é o caso.
## Fotos
![https://drive.google.com/open?id=104hpHkWG8d0JvUe-oYt3EIZ9g4KCztok](./imgs/ANDRÉ_104hpHkWG8d0JvUe-oYt3EIZ9g4KCztok.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O sistema tira a liberdade do usuário ao mostrar mensagens de erro fora de situações de erro.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ALTEMATR_ANDR_49]* Problema 49:  Erros de codificação de caracteres.
**Ocorre na página**: *Alteração de Matrícula > Relatório de Integralização.*


A página acessada têm diferentes erros de codificação de caracteres em diferentes lugares.
## Fotos
![https://drive.google.com/open?id=1lRkPhxZmt8vewIUal76wwJMwyOXEu680](./imgs/ANDRÉ_1lRkPhxZmt8vewIUal76wwJMwyOXEu680.png)

![https://drive.google.com/open?id=11QksqG9iUq83S5K0Zpc8Rn5pZax_KAGD](./imgs/ANDRÉ_11QksqG9iUq83S5K0Zpc8Rn5pZax_KAGD.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema está inconsistente visto que caracteres mal formatados só atrapalham o uso.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ALTEMATR_ANDR_50]* Problema 50:  Falta do botão "Voltar".
**Ocorre na página**: *Alteração de Matrícula > Várias partes do sistema - exemplo: Relatório de Integralização.*

No exemplo existem apenas os botões para imprimir e sair do sistema.
## Fotos
![https://drive.google.com/open?id=1lQ5TF5UW_dyLWORXcB3ybeNZNHo7TE7f](./imgs/ANDRÉ_1lQ5TF5UW_dyLWORXcB3ybeNZNHo7TE7f.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A estética do sistema é afetada pois texto que o usuário não consegue ler atrapalha a visualização da parte que ele consegue.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_ANDR_51]* Problema 51: Inconsistência no relatório a imprimir.
**Ocorre na página**: *Alteração de Matrícula > Relatório de integralização > Imprimir.*

A opção imprimir não imprime o relatório mas toda a página, não há sentido nisso visto que um usuário não iria querer imprimir o botão “imprimir”, por exemplo.
## Fotos
![https://drive.google.com/open?id=1XdITYqjmKn-Bx_eHsClUk1Q4fhKyDiL_](./imgs/ANDRÉ_1XdITYqjmKn-Bx_eHsClUk1Q4fhKyDiL_.png)

![https://drive.google.com/open?id=1ps4nZijpMQu8RIW1qHvgufLn-mGXeXQX](./imgs/ANDRÉ_1ps4nZijpMQu8RIW1qHvgufLn-mGXeXQX.png)

![https://drive.google.com/open?id=18JAFT2x7dypQsOeKChceRW_QddDKG_S5](./imgs/ANDRÉ_18JAFT2x7dypQsOeKChceRW_QddDKG_S5.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: No mundo real um relatório impresso não deveria vir com a interface do sistema que o gerou.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_ANDR_52]* Problema 52: Opções inválidas disponíveis.
**Ocorre na página**: *Alteração de Matrícula > Histórico Escolar.*


O sistema mostra uma opção que não se aplica ao perfil do usuário que não faz Pós-Graduação.
## Fotos
![https://drive.google.com/open?id=13hxjWpeDMq1B8ER3tNmJlgLpGvGi8joz](./imgs/ANDRÉ_13hxjWpeDMq1B8ER3tNmJlgLpGvGi8joz.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Botões que quando clicados não levam a nenhuma ação redundante atrapalham a visualização dos que realmente importam.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_ANDR_53]* Problema 53: Falta do botão "Voltar".
**Ocorre na página**: *Alteração de Matrícula > Em várias partes do sistema.*

Falta do botão "Voltar" em várias partes do sistema.
## Fotos
![https://drive.google.com/open?id=1fkOip4cHrAHtZPLQurUqr3j6y6M8dwKg](./imgs/ANDRÉ_1fkOip4cHrAHtZPLQurUqr3j6y6M8dwKg.png)

![https://drive.google.com/open?id=1QQac1gcHLZUdqS5lA5SOYeCCRi0Yol_I](./imgs/ANDRÉ_1QQac1gcHLZUdqS5lA5SOYeCCRi0Yol_I.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Usuário perde liberdade quando não tem disponível o botão de voltar.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_ANDR_54]* Problema 54: Relatório com erro visual.
**Ocorre na página**: *Alteração de Matrícula > Relatório de Matrícula > Normal > Exibir relatório de matrícula.*

O relatório gerado tem um erro de formatação, o que dificulta a visualização por parte do usuário.
## Fotos
![https://drive.google.com/open?id=1kFqt-_GE-mgzSbY_AZlDXt5ivsztFEgj](./imgs/ANDRÉ_1kFqt-_GE-mgzSbY_AZlDXt5ivsztFEgj.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A visualização é prejudicada pelo erro do formulário.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ALTEMATR_ANDR_55]* Problema 55: Relatório com coluna sem valor.
**Ocorre na página**: *Alteração de Matrícula > Relatório de Matrícula > Normal > Exibir relatório de matrícula.*

Existe uma coluna para mensagens que não tem nenhum valor, isso toma espaço dos outros itens sem necessidade, o que dificulta a visualização do relatório.
## Fotos
![https://drive.google.com/open?id=13hz4cGmGRVgJUC7oYDUcB02W03o-Q5UJ](./imgs/ANDRÉ_13hz4cGmGRVgJUC7oYDUcB02W03o-Q5UJ.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A presença de uma coluna sem motivo atrapalha a visualização das demais.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_ANDR_56]* Problema 56: Mensagem de erro insuficiente.
**Ocorre na página**: *Alteração de Matrícula > Relatório de Matrícula > Férias / Recuperação.*

O sistema não diferencia se o relatório de matrícula não está disponível porque nenhuma matrícula foi feita (o que é o caso) ou se houve algum erro ou outro motivo para o relatório não estar disponível no momento.
## Fotos
![https://drive.google.com/open?id=1MtEBJx2InR6NGOa8yrIbe4qLFGaY6-NV](./imgs/ANDRÉ_1MtEBJx2InR6NGOa8yrIbe4qLFGaY6-NV.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: Como a mensagem de erro não é clara o suficiente o usuário não consegue se recuperar da situação de erro facilmente.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ALTEMATR_ANDR_57]* Problema 57: Página confusa.
**Ocorre na página**: *Alteração de Matrícula > Situação de vagas por disciplina.*

A página precisa de um tópico de ajuda pois é confusa: existe a possibilidade de escolher valores para graduação e pós graduação por exemplo, isso pode levar o usuário a acreditar que está procurando disciplinas disponibilizadas para ambos os grupos.
## Fotos
![https://drive.google.com/open?id=1Oq_qnQPD1gGvQkWNaoztshvDZ0ZtJplv](./imgs/ANDRÉ_1Oq_qnQPD1gGvQkWNaoztshvDZ0ZtJplv.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: Não existe opção de ajuda na página.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ALTEMATR_ANDR_58]* Problema 58: Código da disciplina precisa ser lembrado.
**Ocorre na página**: *Alteração de Matrícula > Situação de vagas por disciplina.*

A página espera que o usuário já saiba qual o código da disciplina que quer pesquisar, como isso é bastante incomum o usuário terá que usar uma outra página para consultar as disciplinas e seus códigos.
## Fotos
![https://drive.google.com/open?id=1w5XVO2ZjVV44ImfXzDIJ6a6De9PQfk6l](./imgs/ANDRÉ_1w5XVO2ZjVV44ImfXzDIJ6a6De9PQfk6l.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: O sistema requer que o usuário lembre de cada código de cada disciplina que quiser consultar no sistema sendo que poderia ser feita uma busca pela disciplina em questão.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ALTEMATR_ANDR_59]* Problema 59: Página não previne erro do usuário.
**Ocorre na página**: *Alteração de Matrícula > Situação de vagas por disciplina.*

A página espera que a opção “Oferecimento” tenha apenas um dos campos preenchidos: Graduação OU Pós-Graduação. Não é feita verificação, ou é dito isso ao usuário e um erro é gerado.
## Fotos
![https://drive.google.com/open?id=14kV-aGA-NOI3FusSKKgT69y6xq8ktk8c](./imgs/ANDRÉ_14kV-aGA-NOI3FusSKKgT69y6xq8ktk8c.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: A página não evita que o usuário cause erros na página sendo que poderia fazê-lo facilmente.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ALTEMATR_ANDR_60]* Problema 60: Página não previne erro do usuário.
**Ocorre na página**: *Alteração de Matrícula > Situação de vagas por disciplina.*

A verificação só é feita após o envio. Ao digitar caracteres inválidos nos campos de texto um erro ocorre, o motivo não é mostrado e a única opção é sair do sistema.
## Fotos
![https://drive.google.com/open?id=1nRhc3y6TMGlKixx4X1pmbv4Vckq1OdZL](./imgs/ANDRÉ_1nRhc3y6TMGlKixx4X1pmbv4Vckq1OdZL.png)

![https://drive.google.com/open?id=1MsrcSQ2Pq8dHO5cy22w_hfZ3BHpevyM7](./imgs/ANDRÉ_1MsrcSQ2Pq8dHO5cy22w_hfZ3BHpevyM7.png)

## Comentários
A página não evita que o usuário cause erros na página sendo que poderia fazê-lo facilmente.

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A mensagem de erro é insuficiente para ajudar o usuário a evitá-lo.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ALTEMATR_ANDR_61]* Problema 61: Sistema não se recupera após erro.
**Ocorre na página**: *Alteração de Matrícula > Todo o sistema.*

Quando um erro ocorre a única opção disponível é um botão para sair do sistema, mas o botão não faz essa tarefa e uma mensagem de erro diferente é gerada.
## Fotos
![https://drive.google.com/open?id=1Z8AKBwJBcXP9CELTEq5GK2N-KpjffzYY](./imgs/ANDRÉ_1Z8AKBwJBcXP9CELTEq5GK2N-KpjffzYY.png)

![https://drive.google.com/open?id=1Z2PClT4njofHOaF8sH3lwnZ2AIz94ZtA](./imgs/ANDRÉ_1Z2PClT4njofHOaF8sH3lwnZ2AIz94ZtA.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: As mensagens de erro e o comportamento do sistema levam o usuário a cometer mais erros.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[ALTEMATR_ANDR_62]* Problema 62: Botões do mouse bloqueados.
**Ocorre na página**: *Alteração de Matrícula > Todo o sistema.*

Ao clicar com o botão direito do mouse ou com o scroll uma caixa de diálogo aparece. O texto não ajuda a entender o que está acontecendo. São geradas duas caixas de diálogo idênticas sobrepostas, para voltar a usar a página é preciso clicar em “OK” nas duas, ou seja, duas vezes, a mesma caixa, com a mesma mensagem.
## Fotos
![https://drive.google.com/open?id=1M0v7EIybKPm4zeo8o9DOaP363RU7eh9C](./imgs/ANDRÉ_1M0v7EIybKPm4zeo8o9DOaP363RU7eh9C.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: O sistema impede o usuário de utilizar funções muito comuns ao qual já estaria acostumado.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SIGA_ANDR_63]* Problema 63: Legendas em inglês.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Ao usar o menu “Legenda”.*

As legendas no sistema estão em inglês sendo que o sistema é voltado para usuários brasileiros e o restante dele está em português.
## Fotos
![https://drive.google.com/open?id=1Ew_LHJi2mYY0V1mRGx56gBJ_xsRHQMlU](./imgs/ANDRÉ_1Ew_LHJi2mYY0V1mRGx56gBJ_xsRHQMlU.png)

![https://drive.google.com/open?id=19uzfoVx8oHy6XBOjANAve7TyyU4pXDdY](./imgs/ANDRÉ_19uzfoVx8oHy6XBOjANAve7TyyU4pXDdY.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: A ajuda em inglês é de pouca utilidade visto que a maioria dos usuários fala português.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SIGA_ANDR_64]* Problema 64: Ícones inconsistentes.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Ao acessar as legendas.*

Existem ícones diferentes para as mesmas ações e ícones semelhantes para ações diferentes.
## Fotos
![https://drive.google.com/open?id=1WFEEobv4vm_KipLwWO4d46wxcyQPRDq5](./imgs/ANDRÉ_1WFEEobv4vm_KipLwWO4d46wxcyQPRDq5.png)

![https://drive.google.com/open?id=1i-5aDzedBCTaOQat-hbxDBgWG-nFC-o3](./imgs/ANDRÉ_1i-5aDzedBCTaOQat-hbxDBgWG-nFC-o3.png)

![https://drive.google.com/open?id=189OPmRGNmHFhDuCMaiz-A5goJLjuxQ0v](./imgs/ANDRÉ_189OPmRGNmHFhDuCMaiz-A5goJLjuxQ0v.png)

![https://drive.google.com/open?id=1gJrIyRVYEPFLEvUBirXErTmYdKUje6ST](./imgs/ANDRÉ_1gJrIyRVYEPFLEvUBirXErTmYdKUje6ST.png)

![https://drive.google.com/open?id=1C2IsqXgrfSZHgnoR9QHrzWU2Y2slEFEE](./imgs/ANDRÉ_1C2IsqXgrfSZHgnoR9QHrzWU2Y2slEFEE.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema não segue um padrão nos botões, tanto que uma legenda é requerida e nela botões diferentes fazem a mesma coisa e botões semelhantes fazem coisas diferentes.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SIGA_ANDR_65]* Problema 65: Opção sem utilidade.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Ao usar o menu para anexar foto do aluno.*

O sistema não diz como fazer a solicitação a DAC e de certa forma o sistema já seria um modo de fazer essa solicitação.
## Fotos
![https://drive.google.com/open?id=1OGpfXUGx9g3NBIpwBb6wm06Y1xtEHMLr](./imgs/ANDRÉ_1OGpfXUGx9g3NBIpwBb6wm06Y1xtEHMLr.png)

![https://drive.google.com/open?id=1ye95_I342ZMN2FCEOBFm_Oqhcn30hFPv](./imgs/ANDRÉ_1ye95_I342ZMN2FCEOBFm_Oqhcn30hFPv.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Da forma como o sistema é feito é passada a impressão de que a opção está presente no sistema sendo que não está.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SIGA_ANDR_66]* Problema 66: Conteúdo some.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Ao ativar e desativar a opção de alto contraste.*

Ao trocar o modo alto contraste o conteúdo apresentado some.
## Fotos
![https://drive.google.com/open?id=1buSVF9bJpKS38Xyu-NRgXtbyc3DfPe1v](./imgs/ANDRÉ_1buSVF9bJpKS38Xyu-NRgXtbyc3DfPe1v.png)

![https://drive.google.com/open?id=1Tm4uhQ1vsF0_wbh9wIbl_LD6mQkAkkPz](./imgs/ANDRÉ_1Tm4uhQ1vsF0_wbh9wIbl_LD6mQkAkkPz.png)

## Considerações

### Heurística ferida: 1ª
**Heurística ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: Durante o uso o usuário perde qual o estado atual do sistema caso ative e desative a opção de alto contraste.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SIGA_ANDR_67]* Problema 67: Mensagens de campo inválido longe dos campos.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Cadastros > Documentos.*

As mensagens de erro aparecem no topo da página, seria melhor que estivessem ao lado ou próximo dos campos aos quais correspondem.
## Fotos
![https://drive.google.com/open?id=1KnR4ZvqoXemWY5ETgJ01fAEAdpdq4yIr](./imgs/ANDRÉ_1KnR4ZvqoXemWY5ETgJ01fAEAdpdq4yIr.png)

## Considerações

### Heurística ferida: 1ª
**Heurística ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: Como as mensagens de erro estão longe dos campos com valores errados o usuário pode não ver tais mensagens.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SIGA_ANDR_68]* Problema 68: Validação de CEP incorreta.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Endereço > Localizar CEP.*

Houve uma mudança nos números do CEP em minha cidade, o site da DAC não foi atualizado de acordo com essa mudança, dessa forma não é possível colocar o CEP atualizado. Pesquisando no site dos Correios é possível ver que o CEP em questão é válido.
## Fotos
![https://drive.google.com/open?id=1q3JMDuUlfS7TG7k7TvMhuIkgGm_9i1qx](./imgs/ANDRÉ_1q3JMDuUlfS7TG7k7TvMhuIkgGm_9i1qx.png)

![https://drive.google.com/open?id=1rQi8yDstnguP0kU0i3QT7fsZ45ZBHkgx](./imgs/ANDRÉ_1rQi8yDstnguP0kU0i3QT7fsZ45ZBHkgx.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O sistema está desalinhado com o mundo real pois diz que um CEP que existe é inexistente.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SIGA_ANDR_69]* Problema 69: Mensagem de confirmação sem motivo.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Em atualizar (sem nenhuma alteração nos dados).*

A mensagem de confirmação de alteração nos dados cadastrais é exibida mesmo que nenhum dado tenha sido alterado.
## Fotos
![https://drive.google.com/open?id=1ucYpnMn_4eZkP1mcnbYDviwnGqC8hjyZ](./imgs/ANDRÉ_1ucYpnMn_4eZkP1mcnbYDviwnGqC8hjyZ.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: O sistema mostra uma tela que não tem necessidade de ser mostrada.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SIGA_ANDR_70]* Problema 70: Ajuda só é mostrada antes do login.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Ao fazer login.*

A opção de ajuda no topo direito da página não é mostrada depois do usuário estar logado.
## Fotos
![https://drive.google.com/open?id=1FPqSSgrQrJCCMZFtoxp6eOscVPyl7tWO](./imgs/ANDRÉ_1FPqSSgrQrJCCMZFtoxp6eOscVPyl7tWO.png)

![https://drive.google.com/open?id=1GpNKJefHXRV3RB3fjSkRYJluWkEXEPM2](./imgs/ANDRÉ_1GpNKJefHXRV3RB3fjSkRYJluWkEXEPM2.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: O botão de ajuda some ao fazer o login.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[EDAC_ANDR_71]* Problema 71: Tela de login confusa.
**Ocorre na página**: *e-DAC > Identificação do usuário.*


Na tela de login não é informado qual o formato do usuário e da senha: os mesmos do login no sistema da dac, no webmail da dac, as credenciais do google classroom, apenas os números do RA, RA com a inicial do nome, as credenciais para login na rede Wi-Fi, as credenciais para login nos computadores....
## Fotos
![https://drive.google.com/open?id=1vsNbNnTV3devV8z-oLwnOqlotBrJvdNf](./imgs/ANDRÉ_1vsNbNnTV3devV8z-oLwnOqlotBrJvdNf.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: O sistema não informa o formato do login, desta forma não previne o usuário de cometer o erro de usar as credenciais erradas.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[EDAC_ANDR_72]* Problema 72: Visualização ruim.
**Ocorre na página**: *e-DAC > Notas/Conceitos.*

A visualização da nota seria melhor se utilizassem um formato como “9,5” ao invés de “09.5”, da forma como está a visualização fica dificultada.
## Fotos
![https://drive.google.com/open?id=1FBVCxqoRDr6FoGDPgVKsKM9614YxW4OP](./imgs/ANDRÉ_1FBVCxqoRDr6FoGDPgVKsKM9614YxW4OP.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A representação dos números seria melhor se fosse menor.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[EDAC_ANDR_73]* Problema 73: Falta do nome da disciplina.
**Ocorre na página**: *e-DAC > Notas/Conceitos.*

Apenas é listado o código da disciplina e não o seu nome, dificilmente um aluno irá lembrar qual código corresponde a qual disciplina no seu primeiro semestre por exemplo.
.
## Fotos
![https://drive.google.com/open?id=13WOj-pwymYy9X3vzqrxYtp8_f7-0OFPs](./imgs/ANDRÉ_13WOj-pwymYy9X3vzqrxYtp8_f7-0OFPs.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: O sistema obriga o usuário a lembrar ou pesquisar o código da disciplina em algum outro lugar para descobrir o respectivo nome.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SENH_ANDR_74]* Problema 74: Falta de verificação de formulário.
**Ocorre na página**: *Senha > Cadastre aqui > Caso você não tenha recebido a senha inicial clique aqui.*

Falta de verificação do que foi digitado em todos os campos.
## Fotos
![https://drive.google.com/open?id=12v61bxr4LjJkJ0vz_9tFMvuHyAQZ4GOL](./imgs/ANDRÉ_12v61bxr4LjJkJ0vz_9tFMvuHyAQZ4GOL.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: Como os campos não são verificados antes da submissão o usuário não é impedido de causar erros no sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SENH_ANDR_75]* Problema 75: Mensagem de erro pouco esclarecedora.
**Ocorre na página**: *Senha > Cadastre aqui > Caso você não tenha recebido a senha inicial clique aqui.*

A mensagem de erro não esclarece quais são os campos numéricos, ou se os campos de data são numéricos ou de data, um usuário mais leigo não entenderia o que é um erro de conversão “o sistema quer converter o que no que?”
Outro exemplo é que posso colocar letras em campos ditos numéricos - se o sistema me permite isso por que ocorreria um erro se fosse colocado “mil novecentos e noventa e sete” ao invés de “1997”?.
## Fotos
![https://drive.google.com/open?id=1W6rGbaDI4d6wKv7cx122dq9pbdph0nyU](./imgs/ANDRÉ_1W6rGbaDI4d6wKv7cx122dq9pbdph0nyU.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A mensagem de erro não é clara e não aponta para soluções de forma direta.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_ANDR_76]* Problema 76: Mensagem de erro incorreta.
**Ocorre na página**: *Senha > Cadastre aqui > Caso você não tenha recebido a senha inicial clique aqui.*

Ao tentar submeter um formulário vazio o erro mostrado é de conversão de campos numéricos, a mensagem não ajuda o usuário.
## Fotos
![https://drive.google.com/open?id=1kqUqhmA7Qexvwfpq167n7yq9OG0S7EDV](./imgs/ANDRÉ_1kqUqhmA7Qexvwfpq167n7yq9OG0S7EDV.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A mensagem de erro não reflete o que ocorreu realmente, confundindo o usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SENH_ANDR_77]* Problema 77: Página de ajuda não ajuda.
**Ocorre na página**: *Senha > Cadastre aqui > Caso você não tenha recebido a senha inicial clique aqui > Dúvidas.*

A ajuda fala apenas sobre como preencher nomes, não explica demais campos ou o que o sistema faz..
## Fotos
![https://drive.google.com/open?id=1gk0KKlLL_Tc7LLIvJAUaa3zZhU8rKobN](./imgs/ANDRÉ_1gk0KKlLL_Tc7LLIvJAUaa3zZhU8rKobN.png)

![https://drive.google.com/open?id=1EoaEwsG7dVG9i3FEl3pIT9XyYutMdSyl](./imgs/ANDRÉ_1EoaEwsG7dVG9i3FEl3pIT9XyYutMdSyl.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: A página de ajuda é insuficiente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_ANDR_78]* Problema 78: Página inexistente.
**Ocorre na página**: *Senha > Alterar senha > Alunos > Orientações gerais sobre senha.*

Ao clicar no link o usuário é levado para uma página dizendo que a página que queria encontrar não foi encontrada.
## Fotos
![https://drive.google.com/open?id=1vAw22T9YgCbfDdTluHngKfbWPQzqABxr](./imgs/ANDRÉ_1vAw22T9YgCbfDdTluHngKfbWPQzqABxr.png)

![https://drive.google.com/open?id=1lpV1o4X7U0X4sc3pu-66UYePV5YmlD_E](./imgs/ANDRÉ_1lpV1o4X7U0X4sc3pu-66UYePV5YmlD_E.png)

![https://drive.google.com/open?id=1ExUjV7dYwsU6u8rPBM8fHmr7YQ7fsgDN](./imgs/ANDRÉ_1ExUjV7dYwsU6u8rPBM8fHmr7YQ7fsgDN.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde liberdade visto que certos links levam para páginas que não existem.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_ANDR_79]* Problema 79: Baixo contraste quando alto contraste é ativado.
**Ocorre na página**: *Senha > Alterar senha > Alunos > Onde retirar ou trocar senha > Alto contraste.*

É difícil ler a tabela mostrada caso a página esteja no modo alto contraste.
## Fotos
![https://drive.google.com/open?id=1PldOc3yXruoZs0J0q-O2giFtQ3-uInxx](./imgs/ANDRÉ_1PldOc3yXruoZs0J0q-O2giFtQ3-uInxx.png)

![https://drive.google.com/open?id=1v9QZNwZh7YUtvy5TqcPD9yKRa4Ns-qzT](./imgs/ANDRÉ_1v9QZNwZh7YUtvy5TqcPD9yKRa4Ns-qzT.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: O design da página quando em alto contraste impede a visualização do conteúdo.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[WEBM_ANDR_80]* Problema 80: Página não encontrada.
**Ocorre na página**: *Webmail > Login > Em caso de esquecimento de senha clique aqui.*

Ao clicar no link de esquecimento de senha a página mostra uma mensagem de página não encontrada.
## Fotos
![https://drive.google.com/open?id=12fJiFtgsPoc1Efgby154Yhk9ysHhJvmA](./imgs/ANDRÉ_12fJiFtgsPoc1Efgby154Yhk9ysHhJvmA.png)

![https://drive.google.com/open?id=1xFEhQcK2dwiv1H4QfjT_QfxnZDv8Bsrh](./imgs/ANDRÉ_1xFEhQcK2dwiv1H4QfjT_QfxnZDv8Bsrh.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde liberdade ao clicar em um link e não acessar a ferramenta que lhe foi prometida.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[WEBM_ANDR_81]* Problema 81: Erro ao fazer login.
**Ocorre na página**: *Webmail > Após login.*

Os campos são marcados como com erro, com mensagens em inglês.
## Fotos
![https://drive.google.com/open?id=1BhifwNqXiKKny--BQkTQQbHYIcMHzmYq](./imgs/ANDRÉ_1BhifwNqXiKKny--BQkTQQbHYIcMHzmYq.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: Os erros que aparecem não auxiliam o usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[WEBM_ANDR_82]* Problema 82: Ajuda em inglês.
**Ocorre na página**: *Webmail > Login > Entrar > Ajuda.*

A página de ajuda do webmail está em inglês.
## Fotos
![https://drive.google.com/open?id=1DiBDH1aa0MgsYjszv6s7dKqS6Tt3_Nd4](./imgs/ANDRÉ_1DiBDH1aa0MgsYjszv6s7dKqS6Tt3_Nd4.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: A página em inglês é pouco útil para usuários com a primeira língua sendo o português.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[WEBM_ANDR_83]* Problema 83: Página confusa.
**Ocorre na página**: *Webmail > Preferências > Categorias e nomenclaturas.*

A página não deixa claro o que são categorias e nomenclaturas.
## Fotos
![https://drive.google.com/open?id=11R_QvadsAcQWuMBgKv9LmXwCM_f4Scev](./imgs/ANDRÉ_11R_QvadsAcQWuMBgKv9LmXwCM_f4Scev.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O sistema falha ao tentar estabelecer relação com o mundo real pois não explica o que são as cores e nomenclaturas naquele contexto.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[WEBM_ANDR_84]* Problema 84: Termos técnicos em configurações.
**Ocorre na página**: *Webmail > Preferências.*

São utilizados termos técnicos como um número em pixels para a largura e “Menu de Elementos Dinâmicos” sem que isso seja explicado ao usuário.
## Fotos
![https://drive.google.com/open?id=1br71T1De9YnHY9VpyyDypYnrf7-H1xup](./imgs/ANDRÉ_1br71T1De9YnHY9VpyyDypYnrf7-H1xup.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O sistema não estabelece conexão com o mundo real e não explica o que significam os conceitos internos ao sistema na parte de configurações.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[WEBM_ANDR_85]* Problema 85: Corretor ortográfico não mostra que não encontrou substituto.
**Ocorre na página**: *Webmail > Nova Mensagem.*

Quanto o corretor ortográfico não encontra uma opção para substituir uma palavra errada nada é mostrado, nenhum menu dizendo algo como “substituição não encontrada” quando o usuário insiste em clicar na palavra para ver alternativas o sistema sai da opção de correção ortográfica.
## Fotos
![https://drive.google.com/open?id=1Mw-yTzce3YoNUDyFfenCKl3sTq9hkeht](./imgs/ANDRÉ_1Mw-yTzce3YoNUDyFfenCKl3sTq9hkeht.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: O comportamento do sistema não impede que o usuário erre.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[WEBM_ANDR_86]* Problema 86: Mudar idioma do corretor difícil de encontrar.
**Ocorre na página**: *Webmail > Nova Mensagem  > Verificar ortografia.*

A opção de mudar a língua do corretor está pouco visível, é uma pequena seta ao lado do botão “Corretor ortográfico”, botões não costumam abrir submenus.
## Fotos
![https://drive.google.com/open?id=1PVIEtLZ63zHExapQwU7XzK5CGMOe1Hrg](./imgs/ANDRÉ_1PVIEtLZ63zHExapQwU7XzK5CGMOe1Hrg.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: O sistema confunde o usuário ao fazer um botão (com ação) que tem um sub menu.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[WEBM_ANDR_87]* Problema 87: Sistema não avisa o que ocorrerá.
**Ocorre na página**: *Webmail > Nova Mensagem > Enviar.*

Ao enviar uma mensagem sem um destinatário e sem um assunto, apenas a falta do campo assunto é questionado, o e-mail é enviado para o próprio usuário e isso não é dito.
## Fotos
![https://drive.google.com/open?id=1TLEAAePUyjU3lBhxQAZmj51s_Aw0YMm8](./imgs/ANDRÉ_1TLEAAePUyjU3lBhxQAZmj51s_Aw0YMm8.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: Por não avisar o usuário de que o campo destinatário está vazio e que nesse caso o destinatário é o próprio usuário o sistema não impede que o usuário cometa o erro de deixar o campo vazio.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[CADEHORR_ANDR_88]* Problema 88: Busca difícil.
**Ocorre na página**: *Caderno de Horários > Continência/Equivalência (Graduação) > Alguma Letra.*

Durante uma busca não é possível trocar de letra inicial do código da disciplina buscada, a página sugere voltar na página inicial, mas falta o botão para isso, se o usuário tiver clicado em vários dos links na página terá que passar por todos eles de novo se utilizar a opção de voltar do navegador.
## Fotos
![https://drive.google.com/open?id=1dt_A6z6CPruVCMqeuBEZYKw5EpvySfZB](./imgs/ANDRÉ_1dt_A6z6CPruVCMqeuBEZYKw5EpvySfZB.png)

![https://drive.google.com/open?id=1zY3OdDiuctpZHVbqqdf0Kh1026CEKJw9](./imgs/ANDRÉ_1zY3OdDiuctpZHVbqqdf0Kh1026CEKJw9.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde liberdade no sistema ao não ter como voltar facilmente.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[CADEHORR_ANDR_89]* Problema 89: Página confusa.
**Ocorre na página**: *Caderno de Horários > Continência/Equivalência (Graduação).*

Faltam explicações, texto e notações são confusos.
A pesquisa é feita com letras de início do código da disciplina, isso dificulta o trabalho, poderia ter algo como um campo de pesquisa textual ou seleção da disciplina pelo nome ou código.
## Fotos
![https://drive.google.com/open?id=1NE6h0M7RfvebSOgStYvP6qbV1s8ZNJnN](./imgs/ANDRÉ_1NE6h0M7RfvebSOgStYvP6qbV1s8ZNJnN.png)

![https://drive.google.com/open?id=1eOPv93UxR_kgVdit2rmZBPsnMYMjgbpy](./imgs/ANDRÉ_1eOPv93UxR_kgVdit2rmZBPsnMYMjgbpy.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: As ações para encontrar as disciplinas não seguem uma lógica fácil de assimilar.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[CADEHORR_ANDR_90]* Problema 90: Barra de navegação some.
**Ocorre na página**: *Caderno de Horários > Continência/Equivalência (Graduação) > Alguma Letra.*

Ao clicar em “Continências iniciadas em [...]” a barra de navegação do site some.
Clicar no mesmo lugar não faz a barra voltar, é preciso insistir várias vezes fazendo o scroll para cima com o mouse para que a barra volte a ser mostrada.
## Fotos
![https://drive.google.com/open?id=1w1Z2skxG0--_Xl9nqM8LUt-DZQub0dWH](./imgs/ANDRÉ_1w1Z2skxG0--_Xl9nqM8LUt-DZQub0dWH.png)

![https://drive.google.com/open?id=1edGXQceRkgZPH4muHl6989eOERT1rNg1](./imgs/ANDRÉ_1edGXQceRkgZPH4muHl6989eOERT1rNg1.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: É difícil para o usuário voltar o sistema ao estado anterior depois de ter clicado no link.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[CADEHORR_ANDR_91]* Problema 91: Botão home confuso.
**Ocorre na página**: *Caderno de Horários > Continência/Equivalência (Graduação).*

A página sugere voltar para a página inicial das continências e tem um símbolo de casa, normalmente utilizado como link para a página inicial do site, nesse caso, o usuário fica em dúvida se irá para a página inicial do site ou página inicial das continências.
## Fotos
![https://drive.google.com/open?id=103xgsxMU66d9wQLmZTEwuqINBMbgjdkf](./imgs/ANDRÉ_103xgsxMU66d9wQLmZTEwuqINBMbgjdkf.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: O sistema põe o usuário em dúvida fazendo com que precise lembrar o que cada botão realmente faz;.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[CADEHORR_ANDR_92]* Problema 92: Falta de link para alterar senha.
**Ocorre na página**: *Caderno de Horários > Alunos de EL774: Lista de Projetos de Estágio em Licenciatura / Alunos de EL874: Lista de Projetos de Estágio em Licenciatura.*

Um usuário que chega na página que de fato quiser alterar a senha da DAC não é redirecionado na mensagem.
## Fotos
![https://drive.google.com/open?id=19GNmgQpTXtqJhGU_xsHMGA9sOUwJBTr2](./imgs/ANDRÉ_19GNmgQpTXtqJhGU_xsHMGA9sOUwJBTr2.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: O sistema não proporciona um atalho para mudança de senha ao tratar desse assunto.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[CADEHORR_ANDR_93]* Problema 93: Falta de página de dúvidas.
**Ocorre na página**: *Caderno de Horários > Alunos de EL774: Lista de Projetos de Estágio em Licenciatura / Alunos de EL874: Lista de Projetos de Estágio em Licenciatura.*

Não existe página de dúvidas, caso o usuário tenha, é dito que ligue em um telefone ou envie um e-mail.
## Fotos
![https://drive.google.com/open?id=1LSVQ92SNgNQuWOgVUvxirMH5xGwqixnq](./imgs/ANDRÉ_1LSVQ92SNgNQuWOgVUvxirMH5xGwqixnq.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: Não existe página de dúvidas.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[CADEHORR_ANDR_94]* Problema 94: Campos em inglês.
**Ocorre na página**: *Caderno de Horários > Alunos de EL774: Lista de Projetos de Estágio em Licenciatura / Alunos de EL874: Lista de Projetos de Estágio em Licenciatura > Disciplinas > Estágio …*

Parte dos resultados estão em inglês.
## Fotos
![https://drive.google.com/open?id=1a3BwZkEO6I4n3TJHLDfALY6IUDnMAvmP](./imgs/ANDRÉ_1a3BwZkEO6I4n3TJHLDfALY6IUDnMAvmP.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: A página está inconsistente pois parte está em português e parte em inglês.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[CADEHORR_ANDR_95]* Problema 95: Falta de nome de disciplinas.
**Ocorre na página**: *Caderno de Horários > Alunos de EL774: Lista de Projetos de Estágio em Licenciatura / Alunos de EL874: Lista de Projetos de Estágio em Licenciatura > Disciplinas > Estágio …*

Não é possível saber quais são as disciplinas com cada código no campo “Prerequisites”.
## Fotos
![https://drive.google.com/open?id=10H1RTTUj-zH5QIYWV7HdDFpJbCfcMhnQ](./imgs/ANDRÉ_10H1RTTUj-zH5QIYWV7HdDFpJbCfcMhnQ.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: O usuário perde flexibilidade ao ter que pesquisar quais são as disciplinas pois o site mostra apenas o código das mesmas.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[CADEHORR_ANDR_96]* Problema 96: Tabela que pode confundir.
**Ocorre na página**: *Caderno de Horários > Alunos de EL774: Lista de Projetos de Estágio em Licenciatura / Alunos de EL874: Lista de Projetos de Estágio em Licenciatura > Processos > Em andamento.*

Mensagem dizendo que o usuário pode clicar em um processo da lista, mas não há processo listado.
Na lista o único resultado é o texto “Nada.”, Algo assim pode confundir o usuário, seria melhor escrever algo como “Nenhum processo em andamento para mostrar” sem que esse texto fizesse parte da tabela com os processos.
## Fotos
![https://drive.google.com/open?id=1xaEKftutCXcZ_JHhTawX4Fq1RGyJQde-](./imgs/ANDRÉ_1xaEKftutCXcZ_JHhTawX4Fq1RGyJQde-.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O sistema está em desacordo com o mundo real já que uma tabela sem conteúdo não teria uma linha dizendo "nada".

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[CADEHORR_ANDR_97]* Problema 97: Campos obrigatórios não ditos.
**Ocorre na página**: *Caderno de Horários > Alunos de EL774: Lista de Projetos de Estágio em Licenciatura / Alunos de EL874: Lista de Projetos de Estágio em Licenciatura.*

Os nomes das opções estão seguidos de um asterisco, isso deve indicar que são campos obrigatórios, mas isso não é dito em nenhum lugar.
## Fotos
![https://drive.google.com/open?id=1yn08BVJRsynbMjaqqmxeKxYHBp2DWy1E](./imgs/ANDRÉ_1yn08BVJRsynbMjaqqmxeKxYHBp2DWy1E.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema está inconsistente pois põe o usuário em dúvida sobre o significado do asterisco.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[CADEHORR_ANDR_98]* Problema 98: Botão de informação não faz nada.
**Ocorre na página**: *Caderno de Horários > Caderno de Horários.*

Normalmente ícones com um “i” significam “informação” mas nada acontece ao passar o mouse ou clicar sobre eles.
## Fotos
![https://drive.google.com/open?id=1jMy3520pT-PTpij7t31843Iw53G4415x](./imgs/ANDRÉ_1jMy3520pT-PTpij7t31843Iw53G4415x.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema não segue o padrão de fornecer informações em botões com um "i".

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[CADEHORR_ANDR_99]* Problema 99: Página muito cheia.
**Ocorre na página**: *Caderno de Horários > Links a partir da primeira seção da página.*

Falta de ordem e falta de ferramenta de busca. A página é muito cheia visualmente, difícil encontrar o que o usuário procura, deveria, existir divisões de uma forma melhor busca.
## Fotos
![https://drive.google.com/open?id=1P23g9fMtnbPsY1RkWTPaJcPrEL0zstRu](./imgs/ANDRÉ_1P23g9fMtnbPsY1RkWTPaJcPrEL0zstRu.png)

![https://drive.google.com/open?id=1vtzb0uSCJ7UGtTNy2RptCEg6-sGP8rQO](./imgs/ANDRÉ_1vtzb0uSCJ7UGtTNy2RptCEg6-sGP8rQO.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A estética do sistema dificulta a utilização do mesmo.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[ESTR_ANDR_100]* Problema 100: Página inexistente.
**Ocorre na página**: *Estrangeiro > Registro de Visto.*

O link redireciona para uma página inexistente.
## Fotos
![https://drive.google.com/open?id=1b00t55rntffMQL1wAaRqpzdDFzwzCmii](./imgs/ANDRÉ_1b00t55rntffMQL1wAaRqpzdDFzwzCmii.png)

![https://drive.google.com/open?id=1VkWNS6ZdpMajbS9TPHwl8bR-jomRe1Nv](./imgs/ANDRÉ_1VkWNS6ZdpMajbS9TPHwl8bR-jomRe1Nv.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde liberdade pois é direcionado a uma página que não esperava.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTR_ANDR_101]* Problema 101: Caminho incorreto.
**Ocorre na página**: *Estrangeiro > Toda a página.*

O caminho mostrado está incorreto, cheguei a esta página por Estudantes > Estrangeiro  > Documentos produzidos no exterior.
## Fotos
![https://drive.google.com/open?id=1rIORhca5op-J9MW1vezD6L-4jdfUmKBz](./imgs/ANDRÉ_1rIORhca5op-J9MW1vezD6L-4jdfUmKBz.png)

## Considerações

### Heurística ferida: 1ª
**Heurística ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: O caminho errado confunde o usuário quando ele precisa saber o caminho que percorreu para chegar na página que está.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ESTR_ANDR_102]* Problema 102: Link para página errada.
**Ocorre na página**: *Estrangeiro > Ao clicar em Estudantes.*

Ao clicar no link “Estudantes” volto para uma página que não era a que esperava.
## Fotos
![https://drive.google.com/open?id=1kPzngFvgcLWdahvw8BZmf59_7pHiE8Fs](./imgs/ANDRÉ_1kPzngFvgcLWdahvw8BZmf59_7pHiE8Fs.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O usuário perde a liberdade pois uma opção não faz o que ele esperava.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[TRANINTE_ANDR_103]* Problema 103: Sistema não fala como encontrar regimento.
**Ocorre na página**: *Transferência Interna > No fim da página.*

O site não diz como conseguir regimento, se é disponibilizado na web, na biblioteca ou na secretaria, por exemplo.
## Fotos
![https://drive.google.com/open?id=1kdNYcrBdYcxdguWWSrmlUVfCGP54goyK](./imgs/ANDRÉ_1kdNYcrBdYcxdguWWSrmlUVfCGP54goyK.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: O usuário não tem a opção de saber mais sobre o regimento.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[PASSESCO_ANDR_104]* Problema 104: Link Inválido.
**Ocorre na página**: *Passe Escolar > Ao clicar em “O site da EMTU”.*

O link redireciona para uma página dizendo que o recurso que seria acessado está indisponível.
## Fotos
![https://drive.google.com/open?id=1aH6To-aDckL93zr62tJUk8dxYn9NOl1u](./imgs/ANDRÉ_1aH6To-aDckL93zr62tJUk8dxYn9NOl1u.png)

![https://drive.google.com/open?id=1g4H_k9E3jTykGWNbM9x4VEwOUd9dbD2K](./imgs/ANDRÉ_1g4H_k9E3jTykGWNbM9x4VEwOUd9dbD2K.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde liberdade pois não consegue acessar um recurso que pensou estar disponível.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[PASSESCO_ANDR_105]* Problema 105: Falta de atalho.
**Ocorre na página**: *Passe Escolar > Na seção “Endereço e Lei de Funcionamento da Unicamp”.*

A página diz ao usuário que acesse o catálogo ou o histórico escolar mas não diz como fazer isso.
## Fotos
![https://drive.google.com/open?id=1VMHLCwana3cXOIQA6pvEUceH6QJ6gBNo](./imgs/ANDRÉ_1VMHLCwana3cXOIQA6pvEUceH6QJ6gBNo.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: A página não disponibiliza atalhos para as ferramentas referenciadas.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ENSIABER_ANDR_106]* Problema 106: Problema visual.
**Ocorre na página**: *Ensino Aberto > Todo o sistema.*

Existe um problema visual com o rodapé da página: letra branca encontra fundo branco e impossibilita a leitura.
## Fotos
![https://drive.google.com/open?id=1sOVGDJbxW94WGF0Kj2Ijen01SZH0MFLW](./imgs/ANDRÉ_1sOVGDJbxW94WGF0Kj2Ijen01SZH0MFLW.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A forma como a página foi feita impede a leitura do texto.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ENSIABER_ANDR_107]* Problema 107: Páginas inexistentes.
**Ocorre na página**: *Ensino Aberto > Página inicial.*

Os links “orientações para o desenvolvimento de disciplinas no ambiente virtual” e “preparação de conteúdos” levam para páginas inexistentes.
## Fotos
![https://drive.google.com/open?id=1Fqyv0UUZpU_xKwAjPAESCDAWOoRi3RNt](./imgs/ANDRÉ_1Fqyv0UUZpU_xKwAjPAESCDAWOoRi3RNt.png)

![https://drive.google.com/open?id=1LQneoTYd0IO6vr5x_Ce8F7QS7ZZFKJlw](./imgs/ANDRÉ_1LQneoTYd0IO6vr5x_Ce8F7QS7ZZFKJlw.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Usuário perde liberdade pois não consegue acessar um conteúdo que achava estar disponível.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ENSIABER_ANDR_108]* Problema 108: Links levam a erro interno.
**Ocorre na página**: *Ensino Aberto > Listas de disciplinas de Graduação e Tecnologia > Todos os links.*

Links levam para uma página com “erro interno do sistema”.
## Fotos
![https://drive.google.com/open?id=1aWTInUEVzMddwiJGwu3A3tdKX7ylGsU2](./imgs/ANDRÉ_1aWTInUEVzMddwiJGwu3A3tdKX7ylGsU2.png)

![https://drive.google.com/open?id=19SIJ8vag4L25zeSK9YIANvOD5Cku8ull](./imgs/ANDRÉ_19SIJ8vag4L25zeSK9YIANvOD5Cku8ull.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: Os erros mostrados não ajudam o usuário a entender o que ele fez de errado sendo que o erro está no sistema - páginas inexistentes.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ENSIABER_ANDR_109]* Problema 109: Links não suportam clique com scroll.
**Ocorre na página**: *Ensino Aberto > Listas de disciplinas de Graduação e Tecnologia.*

Links não suportam o clique com o scroll do mouse, ao invés de abrir o link numa nova aba apenas redirecionam para a própria página.
## Fotos
![https://drive.google.com/open?id=1BlfbBzAJsCqg1lLovLD7OBRIHlGntfN8](./imgs/ANDRÉ_1BlfbBzAJsCqg1lLovLD7OBRIHlGntfN8.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Sistema impede usuário de usarem o atalho com o mouse.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ENSIABER_ANDR_110]* Problema 110: Link leva para página sem conteúdo.
**Ocorre na página**: *Ensino Aberto > Listas de disciplinas de Graduação e Tecnologia  > Registrar informações complementares.*

Link leva para uma página sem conteúdo: na página a única coisa escrita é "it works!".
## Fotos
![https://drive.google.com/open?id=1gu0wo8DCSch-J35kppABnMbxnHeXago2](./imgs/ANDRÉ_1gu0wo8DCSch-J35kppABnMbxnHeXago2.png)

![https://drive.google.com/open?id=17VC-EPtkZf3dioiFz1s9l3eOjcaq0qeT](./imgs/ANDRÉ_17VC-EPtkZf3dioiFz1s9l3eOjcaq0qeT.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Usuário perde liberdade ao acessar uma página em que o conteúdo não tem sentido.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[ENSIABER_ANDR_111]* Problema 111: Imagem de verificação muito pequena.
**Ocorre na página**: *Ensino Aberto > Contato.*

Na seção de contato a imagem de validação é muito pequena e dificulta a visualização.
## Fotos
![https://drive.google.com/open?id=1dgu2FofKp6p-Tu1OnA8_vPIBOc8P7z5-](./imgs/ANDRÉ_1dgu2FofKp6p-Tu1OnA8_vPIBOc8P7z5-.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A forma como a página foi feita dificulta a visualização de certas partes.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ENSIABER_ANDR_112]* Problema 112: Falta de verificação.
**Ocorre na página**: *Ensino Aberto > Contato.*

Nenhuma verificação de dados é feita, o usuário pode colocar um e-mail inválido inclusive.
## Fotos
![https://drive.google.com/open?id=1V5AQr1RQVmqsD8jjTSRP-EZScCxBpmsE](./imgs/ANDRÉ_1V5AQr1RQVmqsD8jjTSRP-EZScCxBpmsE.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: A falta de verificação não impede que o usuário cometa erros no preenchimento do formulário.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[ENSIABER_ANDR_113]* Problema 113: Falta de verificação.
**Ocorre na página**: *Ensino Aberto > Esqueci minha senha de colaborador externo.*

Não há validação dos dados do formulário antes do envio.
## Fotos
![https://drive.google.com/open?id=1xopupa0pi-lWzoryiCBjlPiXMzDdklkG](./imgs/ANDRÉ_1xopupa0pi-lWzoryiCBjlPiXMzDdklkG.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: A falta de verificação faz com que o usuário consiga cometer erros no preenchimento do formulário.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ENSIABER_ANDR_114]* Problema 114: Erro de codificação de caracteres.
**Ocorre na página**: *Ensino Aberto > Relação das disciplinas ativas por unidade de ensino.*

Os caracteres da página estão com uma formatação fora do padrão.
## Fotos
![https://drive.google.com/open?id=1J8UDhXa7yQjETYP_Tn7aWWgQub9-7L_6](./imgs/ANDRÉ_1J8UDhXa7yQjETYP_Tn7aWWgQub9-7L_6.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A forma como o texto foi codificado dificulta a leitura, texto que não pode ser lido não tem utilidade.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[TESTPROF_ANDR_115]* Problema 115: Login leva a página em branco.
**Ocorre na página**: *Teste de Proficiência > Ao fazer login.*

Ao fazer login no sistema uma página em branco é mostrada.
## Fotos
![https://drive.google.com/open?id=158PYwb0-SUDJxrk9Y5Ga_ABzCZ7F4Up2](./imgs/ANDRÉ_158PYwb0-SUDJxrk9Y5Ga_ABzCZ7F4Up2.png)

![https://drive.google.com/open?id=18Sal9Zm7Vq1sGsJM9BiZFiC7X0iDolnj](./imgs/ANDRÉ_18Sal9Zm7Vq1sGsJM9BiZFiC7X0iDolnj.png)

## Considerações

### Heurística ferida: 1ª
**Heurística ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: O sistema não retorna um feedback satisfatório quando o usuário faz o login.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[ESTU_ANDR_116]* Problema 116: Formatação diferente.
**Ocorre na página**: *Estudantes > Microsoft Office Online.*

Nos outros quadros os itens são separados em tópicos, aqui estão sendo separados com vírgulas e estão todos no mesmo tópico.
## Fotos
![https://drive.google.com/open?id=1KgxQrX5UFczNzDS8LpTmzSoklaL6KVv2](./imgs/ANDRÉ_1KgxQrX5UFczNzDS8LpTmzSoklaL6KVv2.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema está inconsistente pois um dos quadros está diferente dos outros.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[GDE_ANDR_117]* Problema 117: Página inexistente.
**Ocorre na página**: *GDE > Ao clicar em GDE.*

Ao clicar no link o usuário é levado para uma página dizendo “Página não encontrada”.
## Fotos
![https://drive.google.com/open?id=1rWjGtpwZj6sMaEXIU4iqPkZJY0K54bYf](./imgs/ANDRÉ_1rWjGtpwZj6sMaEXIU4iqPkZJY0K54bYf.png)

![https://drive.google.com/open?id=1aYMjRhADfO9ypgb6fuJCFAmiRxeS8IyO](./imgs/ANDRÉ_1aYMjRhADfO9ypgb6fuJCFAmiRxeS8IyO.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde liberdade ao não conseguir acessar um conteúdo que achou que estava disponível.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[TESTPROF_ANDR_118]* Problema 118: Informações dificeis de encontrar.
**Ocorre na página**: *Teste de Proficiência > Proficiência.*

Não há o caminho para encontrar onde estão as informações.
## Fotos
![https://drive.google.com/open?id=1UJwBL1289bQPt7b5twSQLOdfJqwPyW8Y](./imgs/ANDRÉ_1UJwBL1289bQPt7b5twSQLOdfJqwPyW8Y.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: A instrução de uso não esta clara.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))




---------

# Problemas levantados por: *Caroline*




## *id:[ALTEMATR_CARO_1]* Problema 1: Funções ocultas.
**Ocorre na página**: *Alteração de Matrícula > Consultas .*

Além da alteração de matrícula é possível fazer consultas de relatório de integralização, histórico escolar (pós) e situação de vaga por disciplina. Porém não há um lugar informando que existem essas funções na parte de "Alteração de Matrícula".
## Fotos
![https://drive.google.com/open?id=1p_0Bx1MK70Rt_gx91gqfPwVK8kQWevjp](./imgs/CAROLINE_1p_0Bx1MK70Rt_gx91gqfPwVK8kQWevjp.png)

## Considerações

### Heurística ferida: 1ª
**Heurística ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: Não há feedback da opção "Consultas".

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_CARO_2]* Problema 2: Aparecer histórico da Pós-Graduação.
**Ocorre na página**: *Alteração de Matrícula > Consultas.*

Há a opção de ver o histórico escolar de Pós-Graduação, se faço login como aluna de graduação não deveria aparecer funções da pós para mim.
## Fotos
![https://drive.google.com/open?id=1-RJHCgvZ8GvMzWKqnZeqN087OHrUAiOX](./imgs/CAROLINE_1-RJHCgvZ8GvMzWKqnZeqN087OHrUAiOX.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A informação de histórico escolar de pós graduando é inútil para alunos de graduação.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_CARO_3]* Problema 3: Falta de retorno em Situação.
**Ocorre na página**: *Alteração de Matrícula > Situação de Vaga por Disciplina.*

Ao clicar nessa seção aparecerá uma nova aba onde contém opção de semestre, ano e disciplina. Ao ser colocado as informações é aberta uma outra aba com a situação da vaga da disciplina escolhida porém não aparece em qual situação ela está, o campo está vazio.
## Fotos
![https://drive.google.com/open?id=17jywEh-_C8M6PWtY1c1SexC4ZpjPV5Ki](./imgs/CAROLINE_17jywEh-_C8M6PWtY1c1SexC4ZpjPV5Ki.png)

## Considerações

### Heurística ferida: 1ª
**Heurística ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: Não da o feedback da situação das vagas.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_CARO_4]* Problema 4: Falta do botão "Voltar".
**Ocorre na página**: *Alteração de Matrícula > Relatório de Matrícula.*

Falta botão "Voltar" no "Relatório de Matrícula" e na página referente a qualquer uma das opções de tipo de matrícula. Se apertar fechar, fecha toda a aba e o aluno terá que logar novamente para escolher outra opção.
## Fotos
![https://drive.google.com/open?id=1TIpJdQ8-Up17HozzYoT7rRSAZ0UPQesz](./imgs/CAROLINE_1TIpJdQ8-Up17HozzYoT7rRSAZ0UPQesz.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho voltar na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_CARO_5]* Problema 5: Falta do botão "Voltar".
**Ocorre na página**: *Alteração de Matrícula > Acompanhar Pedido de Alteração.*

Falta o botão "Voltar" na opção "Acompanhar Pedido de Alteração". .
## Fotos
![https://drive.google.com/open?id=1pIVJd0MLIoDbQ6-4cURdwqU90u5_TzFx](./imgs/CAROLINE_1pIVJd0MLIoDbQ6-4cURdwqU90u5_TzFx.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho voltar na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_CARO_6]* Problema 6: Falta do botão "Voltar".
**Ocorre na página**: *Alteração de Matrícula > Relatório de Integralização.*

Falta botão "Voltar" no "Relatório de Integralização".
## Fotos
![https://drive.google.com/open?id=1Vvs3YSKim3VYt9aDU6MID23pnUSPOAuz](./imgs/CAROLINE_1Vvs3YSKim3VYt9aDU6MID23pnUSPOAuz.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho voltar na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_CARO_7]* Problema 7: Falta do botão "Voltar".
**Ocorre na página**: *Alteração de Matrícula > Histórico Escolar (pós-graduação).*

Falta botão "Voltar" no "Histórico Escolar (Pós-Graduação)".
## Fotos
![https://drive.google.com/open?id=1Ax3DqEeIxk683i4Sluog7IFrkMaZMeRE](./imgs/CAROLINE_1Ax3DqEeIxk683i4Sluog7IFrkMaZMeRE.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho voltar na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_CARO_8]* Problema 8: Botão não parece um botão.
**Ocorre na página**: *Alteração de Matrícula > No "Relátorio de Integralização".*

Existe um botão "Serviços aluno", porém ele não tem a forma de uma botão, parece mais um texto.
## Fotos
![https://drive.google.com/open?id=1CSydOZPMS7yUvFStmm5p80k7WjZ95utM](./imgs/CAROLINE_1CSydOZPMS7yUvFStmm5p80k7WjZ95utM.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O botão não esta intuitivo para o usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: )





## *id:[ALTEMATR_CARO_9]* Problema 9: Erro UTF-8.
**Ocorre na página**: *Alteração de Matrícula > Quando clicado em "Ajuda" no "Relatório de Integralização".*

A página contém erros UTF-8 o que dificulta a leitura do usuário.
## Fotos
![https://drive.google.com/open?id=1-BUkRJQocG6KtTEAvW6fnca83_4bn94V](./imgs/CAROLINE_1-BUkRJQocG6KtTEAvW6fnca83_4bn94V.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: A heurística não foi identificada.

### Grau de Serveridade do problema
**Grau de Severidade**: )





## *id:[SRVACAD_CARO_10]* Problema 10: Mensagem difícil.
**Ocorre na página**: *Serviços Acadêmicos > Pagina inicial dos servições acadêmicos.*

Um usuário com pouca experiencia com os nomes técnicos e tecnologia, pode ficar confuso com a mensagem exibida.
## Fotos
![https://drive.google.com/open?id=1JZ8LVqYKDfKnq8FD_LQUmKbhQLXk4iLd](./imgs/CAROLINE_1JZ8LVqYKDfKnq8FD_LQUmKbhQLXk4iLd.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Termos muitos técnicos para usuários inexperientes.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_CARO_11]* Problema 11: Falta do botão "Voltar".
**Ocorre na página**: *Serviços Acadêmicos > Em "Desistencia de Matrícula".*

Falta o botão "Voltar" na "Desistencia de Matrícula".
## Fotos
![https://drive.google.com/open?id=1kpHHL7yoCD7T-sLNRB5OFiwLkzimadjG](./imgs/CAROLINE_1kpHHL7yoCD7T-sLNRB5OFiwLkzimadjG.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Voltar" na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_CARO_12]* Problema 12: Link com problema.
**Ocorre na página**: *Serviços Acadêmicos > Requerimento de Matrícula.*

Ao clicar no link que disponível, a aba do requerimento é fechada automaticamente, se o aluno quiser voltar terá que logar novamente.
## Fotos
![https://drive.google.com/open?id=1WHI6Mgr5UvnzxrL1Yo-_lisSaWs5ls0G](./imgs/CAROLINE_1WHI6Mgr5UvnzxrL1Yo-_lisSaWs5ls0G.png)

## Considerações

### Heurística ferida: 1ª
**Heurística ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: Falha ao clicar no link a página do requerimento é fechada.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_CARO_13]* Problema 13: Probelmas emoji.
**Ocorre na página**: *Serviços Acadêmicos > Autenticação -> Username ou RA.*

Ao colocar caractere tipo emoji o usuário não é impedido. E ao clicar em acessar aparece uma página de erro.
## Fotos
![https://drive.google.com/open?id=1SPmHcZl0zEG4Oi0cVYO0Ct9g1LNMbu82](./imgs/CAROLINE_1SPmHcZl0zEG4Oi0cVYO0Ct9g1LNMbu82.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: O sistema não evita que o usuário coloque emoji .

### Grau de Serveridade do problema
**Grau de Severidade**: )





## *id:[SRVACAD_CARO_14]* Problema 14: Valor das emissões.
**Ocorre na página**: *Serviços Acadêmicos > Atestado de Matrícula.*

Ao clicar em "Atestado de Matrícula" aparece que o pode solicitar 9 de 10 emissões, porém logo em baixo está escrito que para graduação são apenas 5 documentos disponíveis e para pós outros 5.
## Fotos
![https://drive.google.com/open?id=1agaImFsBHB1v9etNIMb6MJBbB8JU_DZT](./imgs/CAROLINE_1agaImFsBHB1v9etNIMb6MJBbB8JU_DZT.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Falta lógica, pois como está disponível 9 emissões se graduação só tem 5.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_CARO_15]* Problema 15: Certificado PED.
**Ocorre na página**: *Serviços Acadêmicos > Relatórios.*

Aparece a opção de certificado PED para alunos de graduação, no entanto apenas alunos de Pós-Graduação podem ser PED.
## Fotos
![https://drive.google.com/open?id=1iIBpCOuqDffL3Dd_DAw6HC4MvIq_dliE](./imgs/CAROLINE_1iIBpCOuqDffL3Dd_DAw6HC4MvIq_dliE.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Não há utilidade da opção PED para graduandos.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_CARO_16]* Problema 16: Página sem informação.
**Ocorre na página**: *Serviços Acadêmicos > Consultar Inscrição.*

Quando clicado nessa seção, abre outra página porém sem informação alguma.
## Fotos
![https://drive.google.com/open?id=1ErAyX5fKZMgc0_krepkN5KlcALw3Mnex](./imgs/CAROLINE_1ErAyX5fKZMgc0_krepkN5KlcALw3Mnex.png)

## Considerações

### Heurística ferida: 1ª
**Heurística ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: A página não tem informações.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SIGA_CARO_17]* Problema 17: Como anexar foto.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Cadastro.*

Ao colocar o mouse sobre a opção cadastro e clicar na opção anexar foto, aparece uma mensagem dizendo que é necessário solicitar na DAC, mas não tem a instrução de como fazer essa solicitação.
## Fotos
![https://drive.google.com/open?id=1vc3BpIE7rgm_gwmFZIcnU4f4HwqcUy7-](./imgs/CAROLINE_1vc3BpIE7rgm_gwmFZIcnU4f4HwqcUy7-.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: Não tem instruções de como fazer a solicitação.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SIGA_CARO_18]* Problema 18: Graduação como formação acadêmica anterior.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Consultar dados cadastrais do aluno.*

Na opção de Consultar dados cadastrais do aluno, quando clicado em Formação Acadêmica, mostra o curso da Unicamp como concluído e no nível de 2º grau, mas na verdade era para aparecer o nome da escola anterior ao ingresso na Unicamp.
## Fotos
![https://drive.google.com/open?id=1AxFGUnBxyu1Dr4r2jZeZCabYDoYRxZyI](./imgs/CAROLINE_1AxFGUnBxyu1Dr4r2jZeZCabYDoYRxZyI.png)

## Considerações

### Heurística ferida: 1ª
**Heurística ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: Esta dando feedback de informação errada.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[EDAC_CARO_19]* Problema 19: Falta o botão "Voltar".
**Ocorre na página**: *e-DAC > e-DAC.*

Falta a opção de um botão "Voltar".
## Fotos
![https://drive.google.com/open?id=1HpkeFogdLo4ycQmNhmjIpJgG5of9gOiA](./imgs/CAROLINE_1HpkeFogdLo4ycQmNhmjIpJgG5of9gOiA.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho voltar na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[EDAC_CARO_20]* Problema 20: Conceito.
**Ocorre na página**: *e-DAC > Notas/Conceitos.*

Ao ver Notas/Conceitos, aparecem Aprovado por Nota / Conceito e Frequência, porém não fica claro ao usuário o que significa o conceito.
## Fotos
![https://drive.google.com/open?id=1E8xdFRSoftZ9towsBbI6cT0facqQhlDn](./imgs/CAROLINE_1E8xdFRSoftZ9towsBbI6cT0facqQhlDn.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O usuário pode não entender o significado de conceito.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[EDAC_CARO_21]* Problema 21: Informações não carregam.
**Ocorre na página**: *e-DAC > Acompanhar Protocolo.*

Ao clicar em Acompanhar Protocolo e em seguida clicar em "Mais Informação", a página fica carregando porém não abre as informações, houve uma espera de 5 minutos e a página não abriu.
## Fotos
![https://drive.google.com/open?id=1b_9fbBYCRbtPlPMkx90F3vRVsh5xI99S](./imgs/CAROLINE_1b_9fbBYCRbtPlPMkx90F3vRVsh5xI99S.png)

## Considerações

### Heurística ferida: 1ª
**Heurística ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: Não houve retorno da função.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[EDAC_CARO_22]* Problema 22: Botão "Sair" escondido.
**Ocorre na página**: *e-DAC > e-DAC.*

Não fica claro que temos que apertar no G para sair.
## Fotos
![https://drive.google.com/open?id=1zFZpQ0Veg96r6rNhY7Zfqaqyn3shDeqG](./imgs/CAROLINE_1zFZpQ0Veg96r6rNhY7Zfqaqyn3shDeqG.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: A ação de sair não esta visível.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[EDAC_CARO_23]* Problema 23: Informação repetida.
**Ocorre na página**: *e-DAC > Efetuar Solicitação->Entrega de Documentos.*

Ao clicar em entrega de documentos aparece um pop-up e se fechar ele veremos que existe a mesma informação na página.
## Fotos
![https://drive.google.com/open?id=1W7PedLo-JRf6HoGZbQhNFxyNwahmlgOr](./imgs/CAROLINE_1W7PedLo-JRf6HoGZbQhNFxyNwahmlgOr.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Duas vezes a mesma informação não é útil.

### Grau de Serveridade do problema
**Grau de Severidade**: )





## *id:[SENH_CARO_24]* Problema 24: Falta o botão "Voltar".
**Ocorre na página**: *Senha > Senha.*

Falta o botão "Voltar" na página.
## Fotos
![https://drive.google.com/open?id=1Z5kVILoxkwhpQrXTcQp8yn5MrM2ls0q6](./imgs/CAROLINE_1Z5kVILoxkwhpQrXTcQp8yn5MrM2ls0q6.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Voltar" na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_CARO_25]* Problema 25: Falta o botão voltar.
**Ocorre na página**: *Senha > Cadastre Aqui.*

Falta a opção de voltar na página.
## Fotos
![https://drive.google.com/open?id=1lDQoAKfbC26LK_QJJenXssEpYVN8p5J6](./imgs/CAROLINE_1lDQoAKfbC26LK_QJJenXssEpYVN8p5J6.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Voltar" na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_CARO_26]* Problema 26: Voltar com outro nome.
**Ocorre na página**: *Senha > Alterar Senha.*

A opção voltar está com o nome "Sair".
## Fotos
![https://drive.google.com/open?id=1pEZT-vDMVhtGMQhvV0_WWy8bjQQvEEZM](./imgs/CAROLINE_1pEZT-vDMVhtGMQhvV0_WWy8bjQQvEEZM.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O botão "Sair" tem funcionalidade diferente em relação aos de outras páginas.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_CARO_27]* Problema 27: Voltar com outro nome.
**Ocorre na página**: *Senha > Esquecimento de senha.*

A opção voltar está com nome "Sair".
## Fotos
![https://drive.google.com/open?id=1qiwrjuuVy5UeQGeKZ8I815h5BmWItI85](./imgs/CAROLINE_1qiwrjuuVy5UeQGeKZ8I815h5BmWItI85.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O botão "Sair" tem funcionalidade diferente em relação aos de outras páginas.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_CARO_28]* Problema 28: Página não encontrada.
**Ocorre na página**: *Senha > Alterar Senha -> Orientações gerais sobre senha.*

Ao clicar em Alterar Senha o aluno é redirecionado para uma página para que a ação possa ser feita. Nessa página há um link escrito "Orientações Gerais Sobre a Senha". Porém ao clicá-lo aparece a mensagem "Página Não Encontrada.".
## Fotos
![https://drive.google.com/open?id=1-V9HnRVkXthT6Pj1nDgaHxizaMRRqe3v](./imgs/CAROLINE_1-V9HnRVkXthT6Pj1nDgaHxizaMRRqe3v.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: A página não foi encontrada.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SENH_CARO_29]* Problema 29: Mensagem de erro incorreta.
**Ocorre na página**: *Senha > Cadastra Aqui -> Caso você não tenha recebido a senha inicial, clique aqui.*

Ao deixar todos os campos em branco e clicar em "Cadastrar Senha" aparece a mensagem de erro "Erro de conversão. Campos numéricos devem ser preenchidos corretamente", porém a mensagem não ajuda o usuário.
## Fotos
![https://drive.google.com/open?id=1rSJw8ugD1XgIG3BReDFaAlhTOFkQNKeX](./imgs/CAROLINE_1rSJw8ugD1XgIG3BReDFaAlhTOFkQNKeX.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A mensagem de erro pode confundir o usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: )





## *id:[SENH_CARO_30]* Problema 30: Informações idênticas.
**Ocorre na página**: *Senha > Alterar senha -> Demais alunos.*

Ao clicar nas opções referentes aos demais alunos, os links grifados em vermelho tem instruções (idênticas) porém não fica claro como segui-las e achá-las. O mesmo ocorre com o esquecimento de senha.
## Fotos
![https://drive.google.com/open?id=1WI7xVd9j8C_pQZiN6spzP36Z6UKgY5Q_](./imgs/CAROLINE_1WI7xVd9j8C_pQZiN6spzP36Z6UKgY5Q_.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: O usuário tem que lembrar dos passos para realizar a atividade desejada.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_CARO_31]* Problema 31: Falta de verificação de campo.
**Ocorre na página**: *Senha > Cadastra Aqui -> Caso você não tenha recebido a senha inicial, clique aqui.*

Não é verificado se os dados são ou não válidos.
## Fotos
![https://drive.google.com/open?id=1Lluf5Yt2RSwycIGHjly9ir07Nts2ETnx](./imgs/CAROLINE_1Lluf5Yt2RSwycIGHjly9ir07Nts2ETnx.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: O sistema não evita que o usuário cometa erros.

### Grau de Serveridade do problema
**Grau de Severidade**: )





## *id:[WEBM_CARO_32]* Problema 32: Falta o botão "Voltar".
**Ocorre na página**: *Webmail > Webmail.*

Falta na página a opção de voltar.
## Fotos
![https://drive.google.com/open?id=12dkdc11clL4RlFfuJokyRG2lEGNrhZxl](./imgs/CAROLINE_12dkdc11clL4RlFfuJokyRG2lEGNrhZxl.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Voltar" na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[WEBM_CARO_33]* Problema 33: Falta informação.
**Ocorre na página**: *Webmail > Notas e Avisos.*

Logo de início já aparece do lado direito da página "Notas e Avisos", e lá tem instruções de como solicitar senha. Porém ao clicar no link o aluno é redirecionado para a página inicial da DAC e não está explícito onde ele deve ir para achar “Atendimento e Contato”.
## Fotos
![https://drive.google.com/open?id=18rOkov6gaTlUuWe__9yh3Z3Wj8juoQt9](./imgs/CAROLINE_18rOkov6gaTlUuWe__9yh3Z3Wj8juoQt9.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: A instrução de uso não esta visível.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[WEBM_CARO_34]* Problema 34: "Clique aqui" não funciona.
**Ocorre na página**: *Webmail > Webmail.*

Ao clicar em “Em caso de esquecimento de senha, clique aqui”, aparece uma página escrito “Página não encontrada”.
## Fotos
![https://drive.google.com/open?id=15M3rJ_IY8KuJKVX9_yPTbB6LLiVq_ka6](./imgs/CAROLINE_15M3rJ_IY8KuJKVX9_yPTbB6LLiVq_ka6.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: A página não foi encontrada.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[WEBM_CARO_35]* Problema 35: Ajuda em inglês.
**Ocorre na página**: *Webmail > Ajuda.*

Ajuda está em inglês, usuário que não tem conhecimento do idioma pode ter dificuldade.
## Fotos
![https://drive.google.com/open?id=1Z_rCgTVTIygziSu0LC4Tuqs5hkBJWHmj](./imgs/CAROLINE_1Z_rCgTVTIygziSu0LC4Tuqs5hkBJWHmj.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: A página não condiz com a lingua nativa da maioria dos usuários.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[WEBM_CARO_36]* Problema 36: Sem informação de como tirar dúvida.
**Ocorre na página**: *Webmail > Webmail.*

Ao fim da página aparece a mensagem com um link "Dúvidas? Acesse o Portal DAC", porém ao apertar no link o usuário é levado para página inicial da DAC e não fica claro de onde tirar dúvidas.
## Fotos
![https://drive.google.com/open?id=1-LXo216SWRJmW4Pv4YaeOkcBW361a0at](./imgs/CAROLINE_1-LXo216SWRJmW4Pv4YaeOkcBW361a0at.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: Instruções não estão visíveis.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[CADEHORR_CARO_37]* Problema 37: Falta o botão "Voltar".
**Ocorre na página**: *Caderno de Horários > Página inicial do Caderno de Horários*

Falta na página a opção "Voltar".
## Fotos
![https://drive.google.com/open?id=1wnUh0NhiDbfmfAqi3dzI8124iYNF0fAm](./imgs/CAROLINE_1wnUh0NhiDbfmfAqi3dzI8124iYNF0fAm.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Voltar" na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[CADEHORR_CARO_38]* Problema 38: Página confusa.
**Ocorre na página**: *Caderno de Horários > Continência/ Equivalência (Graduação).*

Difícil entender a finalidade da página.
## Fotos
![https://drive.google.com/open?id=1p2ADptPIr2L4mwtNs3SlkDPZ1c5V1I95](./imgs/CAROLINE_1p2ADptPIr2L4mwtNs3SlkDPZ1c5V1I95.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Não dá para entender de forma visual a finalidade das informações.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTR_CARO_39]* Problema 39: Link para página não corresponde com página esperada.
**Ocorre na página**: *Estrangeiro > Estudantes.*

Ao clicar em “Estudantes” o usuário é redirecionado para uma página indevida.
## Fotos
![https://drive.google.com/open?id=1kPzngFvgcLWdahvw8BZmf59_7pHiE8Fs](./imgs/CAROLINE_1kPzngFvgcLWdahvw8BZmf59_7pHiE8Fs.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O usuário perde a liberdade pois uma opção não faz o que ele esperava.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ESTR_CARO_40]* Problema 40: Sem o botão "Voltar".
**Ocorre na página**: *Estrangeiro > Página inicial Estrangeiro.*

Falta na página a opção "Voltar".
## Fotos
![https://drive.google.com/open?id=1EoRTpnMpB_DTFIsZEwiZXTR6uNuy7cS8](./imgs/CAROLINE_1EoRTpnMpB_DTFIsZEwiZXTR6uNuy7cS8.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Voltar" na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[TRANINTE_CARO_41]* Problema 41: Falta o botão "Voltar".
**Ocorre na página**: *Transferência Interna > Página inicial da Transferência Interna*

Falta na página a opção de voltar.
## Fotos
![https://drive.google.com/open?id=13nSrwKGEQT2H4o_-ElSnxwkwsWgg4eTG](./imgs/CAROLINE_13nSrwKGEQT2H4o_-ElSnxwkwsWgg4eTG.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Voltar" na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[PASSESCO_CARO_42]* Problema 42: Sem botão "Voltar"
**Ocorre na página**: *Passe Escolar > Página Inicial do Passe Escolar*

Falta na página a opção de voltar.
## Fotos
![https://drive.google.com/open?id=1KZfaNlzql_18NIsLy_QV2DPwxjLVk0Rh](./imgs/CAROLINE_1KZfaNlzql_18NIsLy_QV2DPwxjLVk0Rh.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Voltar" na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[PASSESCO_CARO_43]* Problema 43: Erro no link.
**Ocorre na página**: *Passe Escolar > Link EMTU.*

Quando o aluno clicar no link da EMTU aparece página com erro.
## Fotos
![https://drive.google.com/open?id=1Yqk4BSyIup9G01zEZbiXzJlAGreh6k2v](./imgs/CAROLINE_1Yqk4BSyIup9G01zEZbiXzJlAGreh6k2v.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: Mensagem de erro em linguagem complexa.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ENSIABER_CARO_44]* Problema 44: Sem o botão "Voltar".
**Ocorre na página**: *Ensino Aberto > Página inicial do Ensino Aberto.*

Falta na página uma opção para voltar.
## Fotos
![https://drive.google.com/open?id=1pBJUq_Z6c1QkSZP4NW_tOUG8UWf5b9yv](./imgs/CAROLINE_1pBJUq_Z6c1QkSZP4NW_tOUG8UWf5b9yv.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Voltar" na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ENSIABER_CARO_45]* Problema 45: Erro de codificação de caracteres.
**Ocorre na página**: *Ensino Aberto > Relação das disciplinas ativas por unidade de ensino.*

Ao clicar no link de relação das disciplinas ativas por unidade de ensino a página que será aberta contém erros de codificação UTF-8.
## Fotos
![https://drive.google.com/open?id=1hGT_wOycTf7ESm7hkKnpyYKpy-nUQuxY](./imgs/CAROLINE_1hGT_wOycTf7ESm7hkKnpyYKpy-nUQuxY.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: Não se encaixa em nenhuma heurística.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ENSIABER_CARO_46]* Problema 46: Erro na página.
**Ocorre na página**: *Ensino Aberto > Links: "Orientações para o desenvolvimento de disciplinas no ambiente virtual" e "Preparação de conteúdos".*

Ao clicar em um desses links abre uma página com erro.
## Fotos
![https://drive.google.com/open?id=1k6R4isdsjqGHNi_kYZEYuYsCn_2OfBko](./imgs/CAROLINE_1k6R4isdsjqGHNi_kYZEYuYsCn_2OfBko.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: Não se encaixa em nenhuma.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[TESTPROF_CARO_47]* Problema 47: "Voltar" com outro nome.
**Ocorre na página**: *Teste de Proficiência. > Página inicial do Teste de Proficiência.*

A opção voltar está com nome "Sair".
## Fotos
![https://drive.google.com/open?id=1AmeuijRRznL8o1m_Wwq4l0WDc8keyVJF](./imgs/CAROLINE_1AmeuijRRznL8o1m_Wwq4l0WDc8keyVJF.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O botão "Sair" tem funcionalidade diferente em relação aos de outras páginas.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[TESTPROF_CARO_48]* Problema 48: Erro de página não encontrada.
**Ocorre na página**: *Teste de Proficiência > Em caso de esquecimento de senha, clique aqui*

“Em caso de esquecimento de senha, clique aqui”, ao clicar o aluno é redirecionado a uma página com a seguinte mensagem “página não encontrada”.
## Fotos
![https://drive.google.com/open?id=1D7TibCUjQFoVPfaVGEJC6D62PTDW8R0w](./imgs/CAROLINE_1D7TibCUjQFoVPfaVGEJC6D62PTDW8R0w.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: A página não foi encontrada.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ESTU_CARO_49]* Problema 49: Alteração de matrícula em outro lugar.
**Ocorre na página**: *Estudantes > Estudantes -> Alteração de Matrícula.*

Alteração de matrícula é um serviço acadêmico e por isso deveria estar no menu de "Serviços Acadêmicos".
## Fotos
![https://drive.google.com/open?id=1dVWvPlrL-ca04jrr2OHXZQ0kavJg9qrw](./imgs/CAROLINE_1dVWvPlrL-ca04jrr2OHXZQ0kavJg9qrw.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A página tem uma opção de serviços acadêmicos e um menu de alteração de matrícula, não há necessidade do menu de alteração por ser um serviço acadêmico.

### Grau de Serveridade do problema
**Grau de Severidade**: )





## *id:[CADEHORR_CARO_50]* Problema 50: Pré Requisitos só com código.
**Ocorre na página**: *Caderno de Horários > Caderno de Horários -> Aluno de EL774: Lista de Projetos de Estágio em Licenciatura.*

Ao clicar em estágio supervisionado I, é mostrado os pré requisitos referente a disciplina, porém o usuário pode não saber a qual matérias as siglas se referem.
## Fotos
![https://drive.google.com/open?id=1eLPSRXzzCslevoG1BjjuGD326Qb-_e1n](./imgs/CAROLINE_1eLPSRXzzCslevoG1BjjuGD326Qb-_e1n.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Usuário fica sem flexibilidade ao ter que ir em outra página para pesquisar os significados.

### Grau de Serveridade do problema
**Grau de Severidade**: )





## *id:[WEBM_CARO_51]* Problema 51: Erro fatal.
**Ocorre na página**: *Webmail > Login do Webmail.*

Ao colocar emoji no usuário e clicar em "Conectar" aparece uma página de erro com a mensagem "erro fatal".
## Fotos
![https://drive.google.com/open?id=1K_znjf38csDieN7Ft5pZQMG_LZhfgFSK](./imgs/CAROLINE_1K_znjf38csDieN7Ft5pZQMG_LZhfgFSK.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: O usuário não é informado de como corrigir esse erro.

### Grau de Serveridade do problema
**Grau de Severidade**: )





## *id:[TESTPROF_CARO_52]* Problema 52: Difícil achar informações.
**Ocorre na página**: *Teste de Proficiência > Proficiência.*

Não é claro a onde tem que ir para achar as informações.
## Fotos
![https://drive.google.com/open?id=1UJwBL1289bQPt7b5twSQLOdfJqwPyW8Y](./imgs/CAROLINE_1UJwBL1289bQPt7b5twSQLOdfJqwPyW8Y.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: A instrução de uso não esta clara.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[EMAIFERRGOOG_CARO_53]* Problema 53: Como achar as outras funções.
**Ocorre na página**: *E-mail e ferramentas Google > Email e ferramentas Google.*

O aluno é direcionado a página para acesso ao e-mail “@g.unicamp.br” mas não mostra como ele acha as outras funções(Google apps for education, email-estudante especial).
## Fotos
![https://drive.google.com/open?id=1xxanAdI8AVRf5EU_JeRuT23DHeMg_FV2](./imgs/CAROLINE_1xxanAdI8AVRf5EU_JeRuT23DHeMg_FV2.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: Instruções de como achar as outras opções não estão visíveis.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[EMAIFERRGOOG_CARO_54]* Problema 54: Falta o botão "Voltar".
**Ocorre na página**: *E-mail e ferramentas Google > Página inicial do E-mail e ferramentas.*

Falta na página a opção para voltar.
## Fotos
![https://drive.google.com/open?id=1BdBGG6Wpr_dZbvEoMIRlgsHvREBHseT5](./imgs/CAROLINE_1BdBGG6Wpr_dZbvEoMIRlgsHvREBHseT5.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Voltar" na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[MICROFFIONLI_CARO_55]* Problema 55: Falta o botão "Voltar".
**Ocorre na página**: *Microsoft Office Online > Página inicial da Microsoft Office Online.*

Falta na página a opção de voltar.
## Fotos
![https://drive.google.com/open?id=1QNwa_PhjgN4DKX2w6YElb-igPf7tt0Uz](./imgs/CAROLINE_1QNwa_PhjgN4DKX2w6YElb-igPf7tt0Uz.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Voltar" na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[PIF_CARO_56]* Problema 56: Falta o botão "Voltar".
**Ocorre na página**: *PIF - Programa Integrado de Formação > Página inicial do PIF.*

Falta na página a opção de voltar.
## Fotos
![https://drive.google.com/open?id=1lJEkyvRlcNGJ8MYnN-GukQdNGo28vabU](./imgs/CAROLINE_1lJEkyvRlcNGJ8MYnN-GukQdNGo28vabU.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Voltar" na página, o usuário tem que fechar e abrir novamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[GDE_CARO_57]* Problema 57: Página não encontrada.
**Ocorre na página**: *GDE > Página inicial GDE.*

Ao clicar na opção do GDE aparece a mensagem "Página não encontrada".
## Fotos
![https://drive.google.com/open?id=1jAgOgwkMG10qqyQdsufwGy_wmRoEM70W](./imgs/CAROLINE_1jAgOgwkMG10qqyQdsufwGy_wmRoEM70W.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: Não se encaixa em nenhuma.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ALTEMATR_CARO_58]* Problema 58: Erro UTF-8.
**Ocorre na página**: *Alteração de Matrícula > Relatório de Integralização.*

O relatório contém erros de codificação UTF-8.
## Fotos
![https://drive.google.com/open?id=1X81fr_UcWbibV_YOCUz1L4bR7v3JQ5yz](./imgs/CAROLINE_1X81fr_UcWbibV_YOCUz1L4bR7v3JQ5yz.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: A heurística não foi identificada.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_CARO_59]* Problema 59: Falta botão "Fechar".
**Ocorre na página**: *Serviços Acadêmicos > Relatório de Matrícula.*

Falta no relatório a opção "Fechar".
## Fotos
![https://drive.google.com/open?id=1KpGlIisu44sDGOHHPqaCsrNIWRLocQeN](./imgs/CAROLINE_1KpGlIisu44sDGOHHPqaCsrNIWRLocQeN.png)

## Considerações

### Heurística ferida: 7ª
**Heurística ferida**: 7 - Flexibilidade e eficiência de uso

**Justificativa**: Falta botão de atalho "Fechar" na página.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[EDAC_CARO_60]* Problema 60: Disciplina só com o código.
**Ocorre na página**: *e-DAC > Notas/Conceito.*

O aluno pode não lembrar qual disciplina a nota se refere só com o código.
## Fotos
![https://drive.google.com/open?id=1d3WAHLtjnqKYM24nUk1QzGi-P9ozaxDF](./imgs/CAROLINE_1d3WAHLtjnqKYM24nUk1QzGi-P9ozaxDF.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: O usuário é obrigado a lembrar a qual disciplina o código pertence.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_CARO_61]* Problema 61: Página em modo texto.
**Ocorre na página**: *Serviços Acadêmicos > Requerimento de Matrícula -> Cursos Regulares.*

Ao clicar em cursos regulares aparece uma página em modo texto.
## Fotos
![https://drive.google.com/open?id=1lOwRUHc2DHqLmJHIQ_4FKkyuBnVuYFY5](./imgs/CAROLINE_1lOwRUHc2DHqLmJHIQ_4FKkyuBnVuYFY5.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O usuário não esta acostumado com páginas assim.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ALTEMATR_CARO_62]* Problema 62: Erro Página não encontrada.
**Ocorre na página**: *Alteração de Matrícula > Requerimento de Matrícula.*

Ao clicar em "Caderno de Horário da Graduação" ou "Caderno de Horário da Pós-Graduação" aparece uma página com a mensagem "Página Não Encontrada".
## Fotos
![https://drive.google.com/open?id=1POO_P2nJE35eRRKIxNWRNULrS8qQzUJ6](./imgs/CAROLINE_1POO_P2nJE35eRRKIxNWRNULrS8qQzUJ6.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: A página não foi encontrada.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))




---------

# Problemas levantados por: *Mayara*




## *id:[SRVACAD_MAYA_1]* Problema 1: Sem opção voltar.
**Ocorre na página**: *Serviços Acadêmicos > Desistência de Matrícula em Disciplinas.*

Não tem botão de voltar, portanto não tem como voltar para a página anterior (dos serviços acadêmicos) sem ser pelo botão do navegador. .
## Fotos
![https://drive.google.com/open?id=1hpn4_R_54yaakNScU-_82eM10pPNjBP3](./imgs/MAYARA_1hpn4_R_54yaakNScU-_82eM10pPNjBP3.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário não tem a opção de voltar para a página anterior, se não fizer isso pelo botão do navegador, terá que sair e entrar de novo nos serviços acadêmicos.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_MAYA_2]* Problema 2: Mensagem Complicada.
**Ocorre na página**: *Serviços Acadêmicos > Serviços Acadêmicos.*

Mensagem com palavras que um usuário leigo teria dificuldade de entender.
## Fotos
![https://drive.google.com/open?id=1vxhgIVN8xvYqtGZ9l8vZnnftPBNDVeNN](./imgs/MAYARA_1vxhgIVN8xvYqtGZ9l8vZnnftPBNDVeNN.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Mensagem com conceitos e palavras que um usuário leigo não está acostumado.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_MAYA_3]* Problema 3: Opções sem sentido.
**Ocorre na página**: *Serviços Acadêmicos > Relatórios.*

Opção de "Certificado PED" para graduação e "Certificado PAD" para pós-graduação, sendo que não há possibilidade de ser PED na graduação nem PAD na pós-graduação.
## Fotos
![https://drive.google.com/open?id=19Zp4MnHrvawhbvkd-MCbv-HUhRCvYYcI](./imgs/MAYARA_19Zp4MnHrvawhbvkd-MCbv-HUhRCvYYcI.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: A opção de "Ceritificado PED" na graduação e "Certificado PAD" na Pós-Graduação não condiz com a realidade.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[SRVACAD_MAYA_4]* Problema 4: Não tem como voltar.
**Ocorre na página**: *Serviços Acadêmicos > Relatório Final de Matrícula.*

Ao clicar em relatório final de matrícula e inserir os dados, a página carrega um PDF na mesma guia, ao invés de abrir o pdf em outra página/guia, se clicar pra fechar, fecha a página e para consultar qualquer outro serviço acadêmico é necessário clicar novamente no site da DAC.
## Fotos
![https://drive.google.com/open?id=1wl1PeKtvHQ0zLPEU94FLytDW5wNhNwHa](./imgs/MAYARA_1wl1PeKtvHQ0zLPEU94FLytDW5wNhNwHa.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde a liberdade e controle de poder selecionar outro serviço acadêmico sem ter de fazer todo o processo de novo (clicar em serviços acadêmicos no site da dac e inserir dados de autenticação).

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_MAYA_5]* Problema 5: Sem opção voltar.
**Ocorre na página**: *Alteração de Matrícula > Consultar Pedido de Alteração de Matrícula.*

Na página de consulta de pedido de alteração de matrícula não tem um botão para voltar pra página anterior.
## Fotos
![https://drive.google.com/open?id=1YNeuP8x-U2qHf-oc5wamZEvkZJuAfKkY](./imgs/MAYARA_1YNeuP8x-U2qHf-oc5wamZEvkZJuAfKkY.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Usuário não tem a liberdade de voltar para a página anterior sem ser pelo botão do navegador ou saindo e entrando de novo.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ALTEMATR_MAYA_6]* Problema 6: Sem opção voltar.
**Ocorre na página**: *Alteração de Matrícula > Consultar Relatório de Integralização.*

Na consulta de relatório de integralização não tem um botão "Voltar" para que o usuário possa voltar para a página anterior e selecionar outro serviço.
## Fotos
![https://drive.google.com/open?id=1gARXJZw8iv1SAABGarZwMZ_DI1zpquBm](./imgs/MAYARA_1gARXJZw8iv1SAABGarZwMZ_DI1zpquBm.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Usuário não tem a liberdade e controle de voltar para página anterior.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ALTEMATR_MAYA_7]* Problema 7: Botão que não parece botão.
**Ocorre na página**: *Alteração de Matrícula > Consultar Relatório de Integralização.*

Na parte superior da página há um botão "serviços aluno", que não parece ser um botão, que volta para a página anterior. Não tem a aparência de um botão que o usuário já está familiarizado e não deixa claro qual a sua função.
## Fotos
![https://drive.google.com/open?id=1e2ddXftavr9RKS5KRRAjdj84upv6cV7P](./imgs/MAYARA_1e2ddXftavr9RKS5KRRAjdj84upv6cV7P.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: Não segue o design já conhecido de um botão e não deixa claro qual sua função.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[PIF_MAYA_8]* Problema 8: Explicação confusa.
**Ocorre na página**: *PIF - Programa Integrado de Formação > PIF.*

O texto está confuso. Não é explicado onde estão as demais exigências.
## Fotos
![https://drive.google.com/open?id=1v-fRrfiaowN_hakHuXEf1gxRUSDnn7NG](./imgs/MAYARA_1v-fRrfiaowN_hakHuXEf1gxRUSDnn7NG.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Existe informação confusa para o usuário. Deveria estar mais detalhado quais são as exigências para participar do programa e as durações minima e máxima do curso.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SIGA_MAYA_9]* Problema 9: Botão "Sair" difícil de encontrar.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Página inicial.*

Botão com opção de sair do sistema difícil de ser encontrado.
## Fotos
![https://drive.google.com/open?id=12DUfsI_WwqKs7gOWxbjR3kJVWl1yUeFR](./imgs/MAYARA_12DUfsI_WwqKs7gOWxbjR3kJVWl1yUeFR.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: Botão de difícil reconhecimento, o usuário não encontra em uma primeira vista.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[EDAC_MAYA_10]* Problema 10: Design confuso.
**Ocorre na página**: *e-DAC > Declarações.*

Na seção de declarações há caixas de texto e um espaço para adicionar arquivo, os 3 com designs diferentes. Principalmente as caixas de texto, uma somente com uma linha, outra um quadrado, as duas para inserir informações diferentes.. Disposição dos espaços desorganizada.
## Fotos
![https://drive.google.com/open?id=1Min6STv-p6j-V-v5e4f-aFIc_l1TpzMG](./imgs/MAYARA_1Min6STv-p6j-V-v5e4f-aFIc_l1TpzMG.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Design desorganizado, confunde o usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[EDAC_MAYA_11]* Problema 11: Informação repetida.
**Ocorre na página**: *e-DAC > Entrega de documentos.*

Ao clicar em entrega de documentos abre um pop-up e logo em seguida na página contém a mesma informação da janela pop-up que o usuário teria acabado de fechar. .
## Fotos
![https://drive.google.com/open?id=1CuxqnY7bYpu6BF1NRboa_rLQc_0CeA7b](./imgs/MAYARA_1CuxqnY7bYpu6BF1NRboa_rLQc_0CeA7b.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A mesma informação exibida duas vezes, uma das vezes em uma janela pop-up, atrapalha e confunde o usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[CADEHORR_MAYA_12]* Problema 12: Sem botão "Voltar".
**Ocorre na página**: *Caderno de Horários > Caderno Horários.*

Não há um botão para voltar para a página anterior (seção estudantes).
## Fotos
![https://drive.google.com/open?id=1q3iuAmiiktdDrapjrKhEf2rAubUKxN7e](./imgs/MAYARA_1q3iuAmiiktdDrapjrKhEf2rAubUKxN7e.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Usuário perde liberdade e facilidade de poder voltar para a página anterior se por exemplo foi para uma página errada.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[CADEHORR_MAYA_13]* Problema 13: Não tem botão para voltar.
**Ocorre na página**: *Caderno de Horários > Continências.*

Na página de continências iniciadas em qualquer uma das letras não há um botão para voltar para a página anterior (Continência/Equivalência).
## Fotos
![https://drive.google.com/open?id=17CN414bDIzz_t_qIyhLIpr9hqFjMcXAV](./imgs/MAYARA_17CN414bDIzz_t_qIyhLIpr9hqFjMcXAV.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Usuário não tem a liberdade e facilidade de voltar para página anterior.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[CADEHORR_MAYA_14]* Problema 14: Página confusa.
**Ocorre na página**: *Caderno de Horários > Continência/ Equivalência.*

É difícil entender qual a finalidade da página.
## Fotos
![https://drive.google.com/open?id=1p2ADptPIr2L4mwtNs3SlkDPZ1c5V1I95](./imgs/MAYARA_1p2ADptPIr2L4mwtNs3SlkDPZ1c5V1I95.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Não dá para entender para que serve a página. Falta alguma informação explicando o que é continência/equivalência, pra que serve...

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[PASSESCO_MAYA_15]* Problema 15: Erro no link.
**Ocorre na página**: *Passe Escolar > link EMTU.*

Quando o aluno clicar no link da EMTU aparece página com erro.
## Fotos
![https://drive.google.com/open?id=1Yqk4BSyIup9G01zEZbiXzJlAGreh6k2v](./imgs/MAYARA_1Yqk4BSyIup9G01zEZbiXzJlAGreh6k2v.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: Mensagem de erro em linguagem diferente da linguagem compreendida pelo usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[GDE_MAYA_16]* Problema 16: Página inexistente.
**Ocorre na página**: *GDE > GDE.*

Existe uma seção dedicada ao GDE mas a página dessa seção não existe mais.
## Fotos
![https://drive.google.com/open?id=1rJ1iaFOoRGJmtgiKTMr2g10SRKO87pkO](./imgs/MAYARA_1rJ1iaFOoRGJmtgiKTMr2g10SRKO87pkO.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: A página dedicada ao GDE dentro do site da DAC não existe mais, sendo que a página do GDE continua existindo, o que tira a liberdade do usuário de ter as informações que a página diz ter.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTU_MAYA_17]* Problema 17: Vários designs.
**Ocorre na página**: *Estudantes > Estudantes.*

As seções dos serviços usam designs diferentes, cada página com uma aparência totalmente diferente. Dando a impressão, às vezes, de estar em uma página que não é da DAC.
## Fotos
![https://drive.google.com/open?id=1hIb4wmAnZhfNVwiy12iI0MrpK_yVd5Fr](./imgs/MAYARA_1hIb4wmAnZhfNVwiy12iI0MrpK_yVd5Fr.png)

![https://drive.google.com/open?id=1WG_SzHpekELeGk0ZqRRTpz2GQTqk1XxE](./imgs/MAYARA_1WG_SzHpekELeGk0ZqRRTpz2GQTqk1XxE.png)

![https://drive.google.com/open?id=1e9bIjY9UkR1BQqBClArcpgnnjgTHZqOv](./imgs/MAYARA_1e9bIjY9UkR1BQqBClArcpgnnjgTHZqOv.png)

![https://drive.google.com/open?id=1C6L5eOdrQESAu3nJoO1kueF9nv0fEF-8](./imgs/MAYARA_1C6L5eOdrQESAu3nJoO1kueF9nv0fEF-8.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: Não tem consistência nos designs/aparência das páginas DAC.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[TRANINTE_MAYA_18]* Problema 18: Texto confuso.
**Ocorre na página**: *Transferência Interna > Transferência Interna.*

Não é explicado como o estudante precisa compor os 50% dos créditos aproveitáveis .
## Fotos
![https://drive.google.com/open?id=1qpr-zNiLSThq7d032Je5Lpo3Kgq_OWtf](./imgs/MAYARA_1qpr-zNiLSThq7d032Je5Lpo3Kgq_OWtf.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Existe informação inútil na tela que confunde e atrapalha o usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[TRANINTE_MAYA_19]* Problema 19: Texto dificil de compreender.
**Ocorre na página**: *Transferência Interna > Transferência Interna.*

Não fica claro como a somatória de créditos é feita.
## Fotos
![https://drive.google.com/open?id=1Kxq0i728IrXUWwYIjmW1MfDY1QErSzXh](./imgs/MAYARA_1Kxq0i728IrXUWwYIjmW1MfDY1QErSzXh.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Existe informação inútil na tela que confunde e atrapalha o usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ALTEMATR_MAYA_20]* Problema 20: Codificação de caracteres UTF-8.
**Ocorre na página**: *Alteração de Matrícula > Relatório de Integralização.*

A página contém problemas com a codificação de caracteres especiais.
## Fotos
![https://drive.google.com/open?id=1C4w5PB4rKTSBQsEHtax-LmYhF9dXSdzV](./imgs/MAYARA_1C4w5PB4rKTSBQsEHtax-LmYhF9dXSdzV.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Com o problema, os caracteres especiais (acentuados e cedilhas, por exemplo) não aparecem da forma correta. Caso o usuário não tenha conhecimento de codificação de caracteres UTF-8, não conseguirá entender a informação que precisa da página.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_MAYA_21]* Problema 21: Página não existe.
**Ocorre na página**: *Senha > Alterar senha -> Alunos -> Orientações gerais sobre senha.*

Ao clicar no link o usuário é informado de que a página não existe.
## Fotos
![https://drive.google.com/open?id=1vAw22T9YgCbfDdTluHngKfbWPQzqABxr](./imgs/MAYARA_1vAw22T9YgCbfDdTluHngKfbWPQzqABxr.png)

![https://drive.google.com/open?id=1lpV1o4X7U0X4sc3pu-66UYePV5YmlD_E](./imgs/MAYARA_1lpV1o4X7U0X4sc3pu-66UYePV5YmlD_E.png)

![https://drive.google.com/open?id=1ExUjV7dYwsU6u8rPBM8fHmr7YQ7fsgDN](./imgs/MAYARA_1ExUjV7dYwsU6u8rPBM8fHmr7YQ7fsgDN.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde a liberdade, já que uma página que o sistema diz estar disponível, não está.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTU_MAYA_22]* Problema 22: Menu de Alteração de Matrícula separado.
**Ocorre na página**: *Estudantes > Estudantes.*

A alteração de matrícula faz parte de serviços acadêmicos, assim deveria estar nesse menu e não ter um menu separado.
## Fotos
![https://drive.google.com/open?id=1c8995WWNdruIljJADwsQYjVYNHLk_vrR](./imgs/MAYARA_1c8995WWNdruIljJADwsQYjVYNHLk_vrR.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Confunde o usuário com a existência de um menu só para alteração de matrícula, sendo que essa opção deveria estar no menu de serviços acadêmicos.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[SRVACAD_MAYA_23]* Problema 23: Problema de Codificação de Caracteres.
**Ocorre na página**: *Serviços Acadêmicos > Integralização Curricular.*

Problema com a codificação dos caracteres especiais.
## Fotos
![https://drive.google.com/open?id=1OE_BL1MHjrxycAOCTUWf5mpW69XO1GqC](./imgs/MAYARA_1OE_BL1MHjrxycAOCTUWf5mpW69XO1GqC.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Usuário não é capaz de identificar que é um problema de codificação para caracteres especiais portanto não é capaz de entender a informação escrita.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ENSIABER_MAYA_24]* Problema 24: Página que não existe.
**Ocorre na página**: *Ensino Aberto > "Orientações para o desevolvimento de disciplinas no ambiente virtual".*

Ao clicar no link o usuário é levado para uma página inexistente.
## Fotos
![https://drive.google.com/open?id=1Fqyv0UUZpU_xKwAjPAESCDAWOoRi3RNt](./imgs/MAYARA_1Fqyv0UUZpU_xKwAjPAESCDAWOoRi3RNt.png)

![https://drive.google.com/open?id=1LQneoTYd0IO6vr5x_Ce8F7QS7ZZFKJlw](./imgs/MAYARA_1LQneoTYd0IO6vr5x_Ce8F7QS7ZZFKJlw.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Usuário perde liberdade já que, é impedido de acessar um conteúdo que o site diz estar disponível.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SENH_MAYA_25]* Problema 25: Mensagem de erro incorreta.
**Ocorre na página**: *Senha > Cadastre aqui -> Caso você não tenha recebido a senha inicial clique aqui.*

Ao deixar os campos vazios e enviar assim, é exibido um erro de conversão de campos numéricos, sendo que não é esse o erro. .
## Fotos
![https://drive.google.com/open?id=1kqUqhmA7Qexvwfpq167n7yq9OG0S7EDV](./imgs/MAYARA_1kqUqhmA7Qexvwfpq167n7yq9OG0S7EDV.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A mensagem de erro não ajuda o usuário, já que mostra um erro diferente do que realmente ocorreu.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[TESTPROF_MAYA_26]* Problema 26: Informações inconsistentes.
**Ocorre na página**: *Teste de Proficiência > Proficiência.*

É confuso acessar as informações.
## Fotos
![https://drive.google.com/open?id=1UJwBL1289bQPt7b5twSQLOdfJqwPyW8Y](./imgs/MAYARA_1UJwBL1289bQPt7b5twSQLOdfJqwPyW8Y.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: A instrução de uso não esta clara.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTR_MAYA_27]* Problema 27: Página não existe.
**Ocorre na página**: *Estrangeiro > Registro de Visto.*

O link redireciona para uma página que não existe.
## Fotos
![https://drive.google.com/open?id=1b00t55rntffMQL1wAaRqpzdDFzwzCmii](./imgs/MAYARA_1b00t55rntffMQL1wAaRqpzdDFzwzCmii.png)

![https://drive.google.com/open?id=1VkWNS6ZdpMajbS9TPHwl8bR-jomRe1Nv](./imgs/MAYARA_1VkWNS6ZdpMajbS9TPHwl8bR-jomRe1Nv.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde liberdade pois é redirecionado para uma página que não contém informações que o sistema diz ter.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[WEBM_MAYA_28]* Problema 28: Página "Ajuda" em inglês.
**Ocorre na página**: *Webmail > Entrar -> Ajuda.*

Ajuda está em inglês, sendo que toda a página está em português que é o idioma da maioria dos usuários.
## Fotos
![https://drive.google.com/open?id=1DiBDH1aa0MgsYjszv6s7dKqS6Tt3_Nd4](./imgs/MAYARA_1DiBDH1aa0MgsYjszv6s7dKqS6Tt3_Nd4.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: A página de ajuda em inglês é pouco útil já que o idioma da maioria dos usuários é português.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))




---------

# Problemas levantados por: *Pedro*




## *id:[SRVACAD_PEDR_1]* Problema 1: Problemas de Processamento.
**Ocorre na página**: *Serviços Acadêmicos > Login do usuário, ao clicar em "Acessar".*

Ao tentar logar utilizando caracteres do tipo emoji (não permitidos pelo sistema, entretanto, a informação não é explicitada) o sistema encaminha o usuário para um erro de processamento com uma mensagem contendo trechos de código SQL.
## Fotos
![https://drive.google.com/open?id=1O0c6hzbqEOSK4yfSvRpr6Bi_y5x6CH0x](./imgs/PEDRO_1O0c6hzbqEOSK4yfSvRpr6Bi_y5x6CH0x.png)

## Comentários
O grau de severidade é grave, pois o usuário não consegue ter acesso a uma parte fundamental do sistema, por esse motivo é de suma importância a rápida resolução.

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A heurística aplicada ao problema é a 9, pois em nenhum momento foi dito como o usuário poderia resolver o problema, apenas é solicitado que ele copie o código SQL e envie à DAC. O usuário não tem entendimento do tipo de problema cometido, e como ele poderia ser facilmente resolvido.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_PEDR_2]* Problema 2: Carregamento da página.
**Ocorre na página**: *Serviços Acadêmicos > Ao clicar em "Cursos Regulares" no tópico "Requerimento de Matrícula".*

A página que aparece está apenas em modo texto, a pagina não é carregada. Além disso, apresenta caracteres fora do padrão utf8.
## Fotos
![https://drive.google.com/open?id=1RZIfWJnIpO1YVtNeDsPPWGgJKrOoznt8](./imgs/PEDRO_1RZIfWJnIpO1YVtNeDsPPWGgJKrOoznt8.png)

## Comentários
Grau de severidade é 2, pois não é um problema grave, apesar de não condizer com a linguagem por meio da qual o usuário esta acostumado, ainda assim é possível extrair algumas informações da página.

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: A página apresenta conteúdo que não é coerente com o conhecimento do usuário leigo, não faz parte do que ele está habituado a encontrar. Não faz parte da "linguagem" do usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_PEDR_3]* Problema 3: Falta de verificação de campos.
**Ocorre na página**: *Serviços Acadêmicos > Ao tentar redirecionar o e-mail da DAC.*

O usuário pode digitar combinações de caracteres que não condizem com um endereço de e-mail válido. Não há verificação se o usuário realmente digitou um e-mail ou caracteres aleatórios, como o exemplo da imagem.
## Fotos
![https://drive.google.com/open?id=1knwfBLJO2jTwsIbFq5LoCxtHwZm6U6po](./imgs/PEDRO_1knwfBLJO2jTwsIbFq5LoCxtHwZm6U6po.png)

## Comentários
O grau de severidade é máximo, pois o usuário pode não receber mais e-mails da DAC, por conta de uma redirecionamento indevido.

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: A heurística correta é a 5, pois os desenvolvedores não pensaram em formas de circuncidar o sistema para que o usuário não pudesse inserir endereços de e-mail inválidos.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[PASSESCO_PEDR_4]* Problema 4: Link Inválido.
**Ocorre na página**: *Passe Escolar > Ao tentar acessar site da EMTU.*

O link redireciona para uma página dizendo que o recurso está indisponível.
## Fotos
![https://drive.google.com/open?id=1aH6To-aDckL93zr62tJUk8dxYn9NOl1u](./imgs/PEDRO_1aH6To-aDckL93zr62tJUk8dxYn9NOl1u.png)

![https://drive.google.com/open?id=1g4H_k9E3jTykGWNbM9x4VEwOUd9dbD2K](./imgs/PEDRO_1g4H_k9E3jTykGWNbM9x4VEwOUd9dbD2K.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde liberdade pois não consegue acessar um recurso que pensou estar disponível.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_PEDR_5]* Problema 5: Inconsistência no menu.
**Ocorre na página**: *Serviços Acadêmicos > Menu Principal de Serviços Acadêmicos.*

A opção CERTIFICADO PED é apresentada na parte de Graduação do Menu Principal, entretanto, um aluno de graduação não pode ser PED.
## Fotos
![https://drive.google.com/open?id=15cfCIlW8FVhSaHt8xB_K8B21BPPXjMWG](./imgs/PEDRO_15cfCIlW8FVhSaHt8xB_K8B21BPPXjMWG.png)

## Comentários
O grau de severidade é baixo, pois não afeta o desempenho do sistema, e possíveis ações erradas do usuário não levariam a erros complexos.

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A heurística correta é a 8, pois o sistema apresenta uma inconsistência de informações acadêmicas na parte de Estudantes (contida no Menu Principal), ou seja, houve uma falha conceitual na diferenciação de botões da graduação e da pós-graduação.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_PEDR_6]* Problema 6: Falta de botão na interface.
**Ocorre na página**: *Serviços Acadêmicos > Ocorre na "Desistência de Matrícula".*

O usuário não tem a opção de Voltar, já que o botão não existe. Ele pode apenas sair do sistema, não garantindo que a ação foi desfeita.
## Fotos
![https://drive.google.com/open?id=1O0G0a-oFC3-tcR_S8SAITlL_LxZBdUrt](./imgs/PEDRO_1O0G0a-oFC3-tcR_S8SAITlL_LxZBdUrt.png)

## Comentários
O grau de severidade é 3, ou seja, é necessário corrigir esse problema, pois caso o usuário não consiga retornar a um menu anterior, e seja obrigado a sair do sistema, o mesmo pode perder informações não-salvas.

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: A heurística correta é a 3, pois o usuário é impedido de voltar à página anterior, desfazendo uma ação, por conta da falta de um botão voltar.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_PEDR_7]* Problema 7: Inconsistência em "Requerimento de Matricula".
**Ocorre na página**: *Serviços Acadêmicos > Ao submeter login e senha na seção "Requerimento de Matrícula".*

O relatório de matricula não está no menu anterior, e sim no menu principal/inicial já que no menu anterior estão os campos de login e senha.
## Fotos
![https://drive.google.com/open?id=1Rij8I3KxQDLHvL0BchI7JNT6ruLv1aUv](./imgs/PEDRO_1Rij8I3KxQDLHvL0BchI7JNT6ruLv1aUv.png)

## Comentários
Grau de severidade baixo, pode causar certa confusão para o usuário, mas não implicará em erros de sistema.

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A heurística correta é a 8, pois há informação inútil e incorreta na tela, ao dizer que o relatório está em um menu, quando na realidade esta em outro.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[SRVACAD_PEDR_8]* Problema 8: Falta de botão na interface de "Serviços Acadêmicos".
**Ocorre na página**: *Serviços Acadêmicos > Ao tentar gerar o relatório de matrícula.*

O usuário não tem a opção de acessar o menu anterior, neste caso em que a busca retornou sem ocorrências. Ele acaba por ser obrigado a sair do sistema e logar novamente.
## Fotos
![https://drive.google.com/open?id=1HhWVkAV_M5b0UYCPUu6YvRC4xy3wiRwE](./imgs/PEDRO_1HhWVkAV_M5b0UYCPUu6YvRC4xy3wiRwE.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário não tem a liberdade de voltar ao menu anterior e refazer a ação. Não pode consultar novamente seu relatório final de matrícula, sem ter que sair do sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SENH_PEDR_9]* Problema 9: Menu de Cadastro de Senha com informação ambígua.
**Ocorre na página**: *Senha > Senha.*

Na opção cadastro de senha, diz que o usuário deve ter uma carta-senha para poder usar e cadastrar uma senha própria, entretanto, há uma confusão no trecho circulado dando a impressão que a senha cadastrada será a carta-senha.
## Fotos
![https://drive.google.com/open?id=1Ja-IqFBARPEmXGlgdFIpzqPu3Xs3O6FT](./imgs/PEDRO_1Ja-IqFBARPEmXGlgdFIpzqPu3Xs3O6FT.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A heuristica violada é a 2, pois há informação incoerente e ambígua na tela, que, além de desnecessária, atrapalha o entendimento do usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_PEDR_10]* Problema 10: Decodificação de caracteres.
**Ocorre na página**: *Serviços Acadêmicos > Integralização Curricular.*

Ao clicar em "Integralização Curricular", aparecem varias informações sobre o aluno, entretanto, há erros de codificação de Caracteres UTF-8. O conteúdo está com sentido comprometido.
## Fotos
![https://drive.google.com/open?id=1pzBGaZ37qE30lMISGowt86ICxLsfBm9_](./imgs/PEDRO_1pzBGaZ37qE30lMISGowt86ICxLsfBm9_.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: A informação não é apresentado na mesma linguagem que o usuário está habituado. Não é possível compreender o conteúdo da página.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SENH_PEDR_11]* Problema 11: Problemas de português.
**Ocorre na página**: *Senha > Regras de expiração de senha.*

Palavra escrita de maneira incorreta.
## Fotos
![https://drive.google.com/open?id=1h_R4Po-bqaO3dJtCKaDEVGTa4uCg_quH](./imgs/PEDRO_1h_R4Po-bqaO3dJtCKaDEVGTa4uCg_quH.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Há inconsistência textual na interface, manifestada pela presença de erros de português.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[SENH_PEDR_12]* Problema 12: Senha.
**Ocorre na página**: *Senha > Troca de senha por esquecimento.*

A página contem informação redundante, já que apresenta, em dois tópicos semelhantes, o mesmo conteúdo.
## Fotos
![https://drive.google.com/open?id=1Nbv0yg6E0kKX6TMJlWQbk1S6m-1B93lw](./imgs/PEDRO_1Nbv0yg6E0kKX6TMJlWQbk1S6m-1B93lw.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A heurística correta é a 8, pois há informação redundante (inútil) na página.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SENH_PEDR_13]* Problema 13: Ambiguidade em cancelamento de username e senha.
**Ocorre na página**: *Senha > Ao clicar em "Cancelamento de Username e Senha".*

Página contendo informação repetida e títulos incoerentes.
## Fotos
![https://drive.google.com/open?id=1CQlVQIj36WetyVqW3_q13P1RT78e4rbD](./imgs/PEDRO_1CQlVQIj36WetyVqW3_q13P1RT78e4rbD.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A heurística correta é a 8, pois existe informação excessiva e inútil na tela.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SENH_PEDR_14]* Problema 14: Falta de verificação de campos.
**Ocorre na página**: *Senha > Alterar Senha.*

Ao tentar alterar a senha, inserindo um username com caracteres emoji, não há verificação de teste para validação.
## Fotos
![https://drive.google.com/open?id=1ZXWrkMY9d27Q2krDYJKPCIZ4hFdnjDhK](./imgs/PEDRO_1ZXWrkMY9d27Q2krDYJKPCIZ4hFdnjDhK.png)

![https://drive.google.com/open?id=1HmTIB4a9zdkAt2iQBN4qSVNQZIvbnUuW](./imgs/PEDRO_1HmTIB4a9zdkAt2iQBN4qSVNQZIvbnUuW.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**:  A heuristica correta é a 5, pois não foram tomadas iniciativas por parte dos desenvolvedores para evitar que os usuários digitassem caracteres indesejados.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SENH_PEDR_15]* Problema 15: Erro de processamento ao tentar alterar senha.
**Ocorre na página**: *Senha > Alterar Senha.*

Ao tentar realizar a troca de senha, caso o usuário insira caracteres do tipo emoji no username, ocorre um erro de processamento do qual não se tem informações.
## Fotos
![https://drive.google.com/open?id=1wFLgggGlkSuAVbaF42eagL1FQ8vgq1y0](./imgs/PEDRO_1wFLgggGlkSuAVbaF42eagL1FQ8vgq1y0.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: O usuário cometeu um erro e não há indicação de como soluciona-lo de maneira rápida e efetiva.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ALTEMATR_PEDR_16]* Problema 16: Inconsistência em Menu.
**Ocorre na página**: *Alteração de Matrícula > Ao clicar em "Alteração de Matrícula".*

A página diz ser para a alteração de matrícula, entretanto, é possível fazer diversas consultas não relacionadas ao objetivo dito.
## Fotos
![https://drive.google.com/open?id=1TMZ6mDonk0vKUSjBuGM16j10NwwDrTAC](./imgs/PEDRO_1TMZ6mDonk0vKUSjBuGM16j10NwwDrTAC.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Informação inconsistente com o objetivo que o uso do botão propõe. Apenas opções de alteração de matrícula deveriam ser oferecidas, ao invés de consultas.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[ALTEMATR_PEDR_17]* Problema 17: Codificação de caracteres UTF-8 no menu "Ajuda".
**Ocorre na página**: *Alteração de Matrícula > Ao clicar em "Ajuda", no menu de "Alteração de Matrícula".*

A página apresenta problemas de codificação UTF-8, o que impede que o usuário visualize o conteúdo completamente, e tenha um bom entendimento da informação apresentada.
## Fotos
![https://drive.google.com/open?id=1C4w5PB4rKTSBQsEHtax-LmYhF9dXSdzV](./imgs/PEDRO_1C4w5PB4rKTSBQsEHtax-LmYhF9dXSdzV.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: A heurística violada é a 2, pois a página não esta sendo apresentada ao usuário na linguagem que ele possa compreender.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ALTEMATR_PEDR_18]* Problema 18: Codificação de caracteres.
**Ocorre na página**: *Alteração de Matrícula > Ao clicar em "Colsultar Relatório de Integralização".*

Nessa página, há problemas de codificação de caractere, o que atrapalha a compreensão do usuário a respeito do conteúdo que é apresentado.
## Fotos
![https://drive.google.com/open?id=1FGZXLuje8iV2-8-gGFkGaHMBLke1ciKd](./imgs/PEDRO_1FGZXLuje8iV2-8-gGFkGaHMBLke1ciKd.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: A heurística violada é a 2, pois parte do conteúdo é apresentado ao usuário em uma linguagem diferente da qual ele compreende e esta habituado.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ALTEMATR_PEDR_19]* Problema 19: Botão "Voltar" tem outro nome.
**Ocorre na página**: *Alteração de Matrícula > Ao consultar o "Relatório de Integralização".*

Nessa página, o botão "Voltar" é chamado de "Serviços Aluno",  não sendo nada intuitivo.
## Fotos
![https://drive.google.com/open?id=1VvdvhLlJUWsgBgB7FUA4ZvKjSgpmaSae](./imgs/PEDRO_1VvdvhLlJUWsgBgB7FUA4ZvKjSgpmaSae.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: A heurística violada é a 4, pois o padrão de design é diferente do que é conhecido pelos usuários. Não se espera que a opção de voltar tenha o nome de "Serviços do Aluno".

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_PEDR_20]* Problema 20: Botão não intuitivo e dificil de achar.
**Ocorre na página**: *Alteração de Matrícula > Ao consultar o "Relatório de Integralização".*

O botão "Serviços Aluno" que assume a função de voltar está numa parte da página dificil de ser localizada pelo usuário.
## Fotos
![https://drive.google.com/open?id=1BkBVE8PCuOelJ1b65_bVfpqHg3E7s5J1](./imgs/PEDRO_1BkBVE8PCuOelJ1b65_bVfpqHg3E7s5J1.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: O usuário precisa lembrar que o botão de voltar se chama "Serviços Aluno" e está localizada na parte superior da página, algo incomum.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_PEDR_21]* Problema 21: Falta de informação sobre vagas.
**Ocorre na página**: *Alteração de Matrícula > Na "Alteração de Matrícula, em "Situação de Vaga por Disciplina".*

A situação de vagas por disciplina não é exibida. Aparece em branco.
## Fotos
![https://drive.google.com/open?id=1IiAp9zLFv1WEfx7vtwcsSNYfilBCGlk5](./imgs/PEDRO_1IiAp9zLFv1WEfx7vtwcsSNYfilBCGlk5.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A heurística violada é a 8, pois faltam informações para o usuário. Ele é obrigado a intuir a situação da vaga. Não há uma explicação sobre as possíveis situações que uma vaga pode ter.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_PEDR_22]* Problema 22: "Ajuda" confusa.
**Ocorre na página**: *Alteração de Matrícula > Ao clicar em "Ajuda" na "Alteração de Matrícula".*

Há informações confusas e redundantes no menu de ajuda. Por exemplo: "Se existir apenas um periodo aberto, quando o usuário acessar o serviço já estará sendo considerado o periodo disponivel para consulta".
## Fotos
![https://drive.google.com/open?id=1lz5iJnQ9S-IJzUBSq1Yyg72I5w4FoSzf](./imgs/PEDRO_1lz5iJnQ9S-IJzUBSq1Yyg72I5w4FoSzf.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: A documentação da ajuda está em péssimas condições. Além de haver problemas de visualização, as informações são pouco úteis. .

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[PIF_PEDR_23]* Problema 23: Explicação confusa sobre o programa.
**Ocorre na página**: *PIF - Programa Integrado de Formação > Ao clicar em "PIF- Programa Integrado de Formação".*

O texto está confuso. Não diz onde encontrar as demais exigências, e nem as durações minima e máxima do curso.
## Fotos
![https://drive.google.com/open?id=1v-fRrfiaowN_hakHuXEf1gxRUSDnn7NG](./imgs/PEDRO_1v-fRrfiaowN_hakHuXEf1gxRUSDnn7NG.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Existe informação confusa para o usuário. Deveria estar mais detalhado quais são as exigências para participar do programa e as durações minima e máxima do curso.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[TESTPROF_PEDR_24]* Problema 24: Erro de Execução.
**Ocorre na página**: *Teste de Proficiência > Ao clicar em "Consultar Inscrição".*

Um erro de execução é exibido com diversos códigos Java, e o usuário não é informado de como resolvê-lo. Apenas pedem para consultar a DAC.
## Fotos
![https://drive.google.com/open?id=1l126XzpUH3UwM84J-aRoTsIXUjaB9pfX](./imgs/PEDRO_1l126XzpUH3UwM84J-aRoTsIXUjaB9pfX.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: O usuário cometeu uma ação errada ao consultar uma inscrição, sem estar inscrito no programa. Entretanto, o usuário não foi orientado sobre como corrigir o erro.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[TESTPROF_PEDR_25]* Problema 25: Erro na Execução.
**Ocorre na página**: *Teste de Proficiência > Ao clicar em "Consultar Resultado"*

Ao tentar realizar a consulta do resultado, inserindo um emoji no campo "Por disciplina/Nível", o usuário é redirecionado para um erro de execução, com trechos de código-fonte.
## Fotos
![https://drive.google.com/open?id=1dm8pSk8wQ_6egv5aae7GQlGADrqLbBCY](./imgs/PEDRO_1dm8pSk8wQ_6egv5aae7GQlGADrqLbBCY.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: O usuário não é orientado de como sair do erro, ou como resolvê-lo.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[PASSESCO_PEDR_26]* Problema 26: Texto confuso.
**Ocorre na página**: *Passe Escolar > Ao clicar em "Passe Escolar".*

O texto diz que a Universidade deverá cadastrar apenas o nome do estudante na EMTU, entretanto, pede para o estudante enviar nome, CPF, RG, CEP e RA.
## Fotos
![https://drive.google.com/open?id=1x-7cvOsSGcelyHlMAPP8M2QqoI3dRa80](./imgs/PEDRO_1x-7cvOsSGcelyHlMAPP8M2QqoI3dRa80.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Texto confuso apresentado para o usuário. Se é necessário vários documentos, é irrelevante e errado dizer que a Universidade cadastrará apenas o nome do estudante.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[TRANINTE_PEDR_27]* Problema 27: Texto confuso e ambíguo.
**Ocorre na página**: *Transferência Interna > Ao clicar em "Transferência Interna".*

Na página é dito que o estudante precisa ter 50% dos créditos aproveitáveis obtidos por um mesmo estudante do curso pelo qual se pretende ingressar, entretanto é dito que esses créditos não precisam ser correspondentes as mesmas disciplinas cursadas por um aluno do primeiro semestre do curso.
## Fotos
![https://drive.google.com/open?id=1qpr-zNiLSThq7d032Je5Lpo3Kgq_OWtf](./imgs/PEDRO_1qpr-zNiLSThq7d032Je5Lpo3Kgq_OWtf.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Existe informação inútil e ambigua na tela. Não está claro como se encaixam os 50% dos créditos aproveitáveis que o aluno deve ter.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[TRANINTE_PEDR_28]* Problema 28: Texto ambíguo.
**Ocorre na página**: *Transferência Interna > Ao clicar em "Transferência Interna".*

Não fica claro como a somatória de créditos do estudante será utilizada para o ingresso no curso ao qual se tem interesse em remanejar.
## Fotos
![https://drive.google.com/open?id=1Kxq0i728IrXUWwYIjmW1MfDY1QErSzXh](./imgs/PEDRO_1Kxq0i728IrXUWwYIjmW1MfDY1QErSzXh.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Há informação inútil e ambigua na tela. Não fica claro para o usuário como os créditos serão aproveitados, e nem como o cálculo é feito.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ESTR_PEDR_29]* Problema 29: Página inexistente.
**Ocorre na página**: *Estrangeiro > Ao clicar em "Registro de Visto".*

Página apresentada não existe.
## Fotos
![https://drive.google.com/open?id=1b00t55rntffMQL1wAaRqpzdDFzwzCmii](./imgs/PEDRO_1b00t55rntffMQL1wAaRqpzdDFzwzCmii.png)

![https://drive.google.com/open?id=1VkWNS6ZdpMajbS9TPHwl8bR-jomRe1Nv](./imgs/PEDRO_1VkWNS6ZdpMajbS9TPHwl8bR-jomRe1Nv.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde liberdade pois é direcionado a uma página que não esperava.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SIGA_PEDR_30]* Problema 30: Sigla desconhecida.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Após fazer login no SIGA.*

Uso da sigla SEESP, sem dizer o que significa.
## Fotos
![https://drive.google.com/open?id=1aCS-jJXky_LSrNi6eDVNPiTYZv4Vgr1v](./imgs/PEDRO_1aCS-jJXky_LSrNi6eDVNPiTYZv4Vgr1v.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O usuário pode não saber o significado dessa sigla. Pode não fazer parte da linguagem dele.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[SIGA_PEDR_31]* Problema 31: Informação desnecessária na tela.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Após fazer o login no SIGA.*

A lado da versão do sistema, uma série de números aparece na tela, entretanto, pouco se sabe sobre o significado deles.
## Fotos
![https://drive.google.com/open?id=1vT3UB5jz5rtdH4UQ-V5MjaHP5D_435zK](./imgs/PEDRO_1vT3UB5jz5rtdH4UQ-V5MjaHP5D_435zK.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Informação inútil e sem explicação apresentada ao usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[SIGA_PEDR_32]* Problema 32: Botão "Avançar" não funciona.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Ao clicar em Vida Acadêmica->Trabalho de Conclusão de Curso.*

O botão "Avançar" não funciona, mesmo havendo um radio button selecionado.
## Fotos
![https://drive.google.com/open?id=1JMA6uGx5aixK26CUyNpN4wbUWc7K8Ry1](./imgs/PEDRO_1JMA6uGx5aixK26CUyNpN4wbUWc7K8Ry1.png)

## Considerações

### Heurística ferida: 1ª
**Heurística ferida**: 1 - Visibilidade do estado do sistema

**Justificativa**: A heurística correta é a 1, pois o botão "Avançar", como não funciona, não atualiza  nem redireciona o usuário para alguma página. Ou seja, não dá um feedback a ele sobre a ação que foi tomada.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SIGA_PEDR_33]* Problema 33: Informação incorreta.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Ao clicar em "Desistência do Vestibular".*

Na página, diz que a funcionalidade não é permitida para um aluno que ingressou de uma forma diferente do Vestibular, entretanto, eu ingressei por vestibular.
## Fotos
![https://drive.google.com/open?id=1W32kt2qqca62Q3CXp6Qg-xed0vCEghja](./imgs/PEDRO_1W32kt2qqca62Q3CXp6Qg-xed0vCEghja.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A informação dita na tela, além de errada, é inútil.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SIGA_PEDR_34]* Problema 34: Data incoerente.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Ao clicar em "Anexar Diploma".*

É informado que o usuário não pode anexar o diploma, pois a data para upload se encerrou em 2011. Entretanto, o aluno só ingressou na Unicamp em 2016.
## Fotos
![https://drive.google.com/open?id=1BwBK7MY_6zog25-UV4aEvJBn1KqrPHSw](./imgs/PEDRO_1BwBK7MY_6zog25-UV4aEvJBn1KqrPHSw.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A informação apresentada na tela é inútil e está incorreta.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[SIGA_PEDR_35]* Problema 35: Informação sobre Pós-Graduação confusa.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Declaração de Matrícula.*

Na página de "Declaração de Matrícula", aparece a palavra Pós-Graduação, sendo que o aluno ainda está na graduação. Além disso, é dito que a declaração só é permitida para alunos de escola pública, o que não faz nenhum sentido, levando-se em conta que, qualquer aluno da Unicamp deve poder emitir uma declaração de sua matrícula.
## Fotos
![https://drive.google.com/open?id=1vkJM3iIprQio5ABEn0uP6ZR4DbkqbJb-](./imgs/PEDRO_1vkJM3iIprQio5ABEn0uP6ZR4DbkqbJb-.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A informação apresentada não condiz com a situação do aluno, já que o mesmo não é aluno de Pós-Graduação. Além disso, a informação de que um aluno deve ser de escola publica, está errada.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SIGA_PEDR_36]* Problema 36: Instituição de ensino do 2 grau não é mostrada.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Ao clicar em "Formação Acadêmica Anterior".*

A página não mostra a insituição em que fiz o ensino médio.
## Fotos
![https://drive.google.com/open?id=1hEOcw50MWxyW2y6tfb07RRv9lOrkFEao](./imgs/PEDRO_1hEOcw50MWxyW2y6tfb07RRv9lOrkFEao.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Informação está faltando, não é exibida.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[EDAC_PEDR_37]* Problema 37: Código de disciplina não referencia o nome.
**Ocorre na página**: *e-DAC > Ao clicar em "Notas/Conceitos".*

O código da disciplina é mostrado, mas não se sabe qual é a disciplina, qual o nome dela.
## Fotos
![https://drive.google.com/open?id=1hsti5Afl5m-1nEx9QbuBrasRCerZrthL](./imgs/PEDRO_1hsti5Afl5m-1nEx9QbuBrasRCerZrthL.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: É usada uma linguagem técnica. O aluno não pode ser obrigado a saber qual código corresponde a qual disciplina.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[EDAC_PEDR_38]* Problema 38: Janela com conteúdo repetido.
**Ocorre na página**: *e-DAC > Efetuar Solicitação->Entrega de Documentos.*

Uma janela de diálogo é aberta. Essa janela contém a mesma informação que está escrita na página.
## Fotos
![https://drive.google.com/open?id=1TzgTJNiy-YDeJBTZZXHh9PEk5SXjGaij](./imgs/PEDRO_1TzgTJNiy-YDeJBTZZXHh9PEk5SXjGaij.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Conteúdo redundante em janela de diálogo, quando na realidade já esta escrito na página.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[ESTU_PEDR_39]* Problema 39: Alteração de matrícula deveria estar em outro lugar.
**Ocorre na página**: *Estudantes > No menu de estudantes.*

A alteração de matrícula é um tipo de serviço acadêmico, ou seja, deveria estar em "Serviços Acadêmicos" ao invés de um menu exclusivo para isso.
## Fotos
![https://drive.google.com/open?id=1c8995WWNdruIljJADwsQYjVYNHLk_vrR](./imgs/PEDRO_1c8995WWNdruIljJADwsQYjVYNHLk_vrR.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Falta de planejamento ao criar esse Menu. Duas algo que faz parte de um seção está representado separadamente.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[ESTU_PEDR_40]* Problema 40: Falta de tópicos.
**Ocorre na página**: *Estudantes > No menu de Estudantes, em "Alteração de Matrícula".*

A lista de opções que são apresentadas no menu de estudantes, na parte de "Alteração de Matrícula", não condiz com as opções oferecidas pela alteração de matrícula.
## Fotos
![https://drive.google.com/open?id=1HyxUprFkxEK6nqZdIcvQ0tkZ42fFHHTT](./imgs/PEDRO_1HyxUprFkxEK6nqZdIcvQ0tkZ42fFHHTT.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Incoerência entre o que é dito em um menu, e o que a opção alteração de matrícula realmente representa.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[ESTU_PEDR_41]* Problema 41: Sigla sem explicação.
**Ocorre na página**: *Estudantes > No menu inicial, na página Estudantes.*

A sigla GDE não vem acompanhada do seu significado.
## Fotos
![https://drive.google.com/open?id=1UiQpS_gPXGiHEIm8EYyMTWFnEuyuM8dl](./imgs/PEDRO_1UiQpS_gPXGiHEIm8EYyMTWFnEuyuM8dl.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O usuário não pode ser obrigado a saber de antemão o significado da sigla.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[SRVACAD_PEDR_42]* Problema 42: Página em branco.
**Ocorre na página**: *Serviços Acadêmicos > Ao clicar no botão "Confirmar", em PED.*

O usuário é redirecionado para uma página em branco.
## Fotos
![https://drive.google.com/open?id=10xRVG11Wl6msHft6Q94BAKD1ydKP8aGZ](./imgs/PEDRO_10xRVG11Wl6msHft6Q94BAKD1ydKP8aGZ.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário é estudante de graduação, e tenta emitir um certificado não existente. Ele não tem a opção de voltar a ação.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_PEDR_43]* Problema 43: Página não encontrada.
**Ocorre na página**: *Serviços Acadêmicos > Ao clicar em "Caderno de Horarios da Graduação".*

O usuário é redirecionado para uma página não encontrada.
## Fotos
![https://drive.google.com/open?id=1AYqEyvbHo4eBrMyekl4FfC_eD70JSmLT](./imgs/PEDRO_1AYqEyvbHo4eBrMyekl4FfC_eD70JSmLT.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: O usuário não é levado a uma página válida.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SENH_PEDR_44]* Problema 44: Botão sair em lugar não intuitivo.
**Ocorre na página**: *Senha > Senha->Cadastre aqui.*

O botão sair está acima da tela, em um lugar não tão fácil de ser visto.
## Fotos
![https://drive.google.com/open?id=1zW3Tbh5VUN51zxoEhOsmm9agnjbLCi9F](./imgs/PEDRO_1zW3Tbh5VUN51zxoEhOsmm9agnjbLCi9F.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: O usuário é obrigado a lembrar onde fica o botão de sair, ao invés de ser algo intuitivo.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SENH_PEDR_45]* Problema 45: Página não encontrada
**Ocorre na página**: *Senha > Ao clicar em "Sobre a DAC".*

O usuário é redirecionado para uma página contendo a mensagem "Página Não Encontrada".
## Fotos
![https://drive.google.com/open?id=1xUNUCG3f0qeMHzRM9kDlnOVS0_sdiD_5](./imgs/PEDRO_1xUNUCG3f0qeMHzRM9kDlnOVS0_sdiD_5.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: A página não foi encontrada por algum erro relativo ao sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_PEDR_46]* Problema 46: Página não encontrada.
**Ocorre na página**: *Senha > Ao clicar em "Graduação".*

O usuário é redirecionado para uma página não encontrada.
## Fotos
![https://drive.google.com/open?id=1Pv8JkD3Xe-tzraQE0heRPA7Bfp9wP1y3](./imgs/PEDRO_1Pv8JkD3Xe-tzraQE0heRPA7Bfp9wP1y3.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: A página não foi encontrada por algum erro relativo ao sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_PEDR_47]* Problema 47: Página não encontrada.
**Ocorre na página**: *Senha > Ao clicar em "Pós-Graduação".*

O usuário é redirecionado para uma página contendo a mensagem "Página Não Encontrada".
## Fotos
![https://drive.google.com/open?id=1ruh0LLd-Qhr06xUn_Us-FyWH77AVA6Sp](./imgs/PEDRO_1ruh0LLd-Qhr06xUn_Us-FyWH77AVA6Sp.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: A página não foi encontrada por algum erro relativo ao sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_PEDR_48]* Problema 48: Página não encontrada.
**Ocorre na página**: *Senha > Ao clicar em "Extensão".*

O usuário é redirecionado para uma página não encontrada.
## Fotos
![https://drive.google.com/open?id=1gKE93knXsC_aMYd77cHtMFaoOp--TlBV](./imgs/PEDRO_1gKE93knXsC_aMYd77cHtMFaoOp--TlBV.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: A página não foi encontrada por algum erro relativo ao sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SENH_PEDR_49]* Problema 49: Falta de verificação de campos.
**Ocorre na página**: *Senha > Ao clicar em "Cadastre Senha->Clique aqui".*

Apenas a verificação de que os dados são numéricos é feita. Não é verificado se os dados são ou não válidos/possiveis. Por exemplo, o Mês 99.
## Fotos
![https://drive.google.com/open?id=1MjpfQ4fWFRJNv7-pmfF_XVHG5lWloHUY](./imgs/PEDRO_1MjpfQ4fWFRJNv7-pmfF_XVHG5lWloHUY.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: O sistema não impede que o usuário cometa determinados erros. Não há verificação de campos por parte do sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[WEBM_PEDR_50]* Problema 50: Erro fatal.
**Ocorre na página**: *Webmail > Ao fazer login.*

Quando o usuário tenta fazer o login inserindo caracteres do tipo emoji, um erro fatal ocorre, apresentando informações sobre código e em inglês.
## Fotos
![https://drive.google.com/open?id=1bWO1Mic3roWtgYU_zvt02-UE015_vyYh](./imgs/PEDRO_1bWO1Mic3roWtgYU_zvt02-UE015_vyYh.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: O usuário não é informado de como corrigir o erro. Apenas a informação confusa de que um Erro Fatal ocorreu é exibida.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[WEBM_PEDR_51]* Problema 51: Ajuda em inglês.
**Ocorre na página**: *Webmail > Ajuda.*

Ajuda está em inglês, usuário pode não saber o idioma e não compreender o conteúdo apresentado.
## Fotos
![https://drive.google.com/open?id=1Z_rCgTVTIygziSu0LC4Tuqs5hkBJWHmj](./imgs/PEDRO_1Z_rCgTVTIygziSu0LC4Tuqs5hkBJWHmj.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: A página não condiz com a lingua de grande parte dos usuários.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[WEBM_PEDR_52]* Problema 52: Página não encontrada.
**Ocorre na página**: *Webmail > Login -> Em caso de esquecimento de senha clique aqui.*

Ao clicar em "Esquecimento de Senha", o usuário é redirecionado para uma "página não encontrada".
## Fotos
![https://drive.google.com/open?id=12fJiFtgsPoc1Efgby154Yhk9ysHhJvmA](./imgs/PEDRO_12fJiFtgsPoc1Efgby154Yhk9ysHhJvmA.png)

![https://drive.google.com/open?id=1xFEhQcK2dwiv1H4QfjT_QfxnZDv8Bsrh](./imgs/PEDRO_1xFEhQcK2dwiv1H4QfjT_QfxnZDv8Bsrh.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde liberdade ao clicar em um link e não acessar a ferramenta que lhe foi prometida.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[WEBM_PEDR_53]* Problema 53: Falta de informação sobre "Dúvidas".
**Ocorre na página**: *Webmail > Ao clicar em Webmail.*

No link "Dúvidas? Acesse o Portal DAC", o usuário é redirecionado para página inicial da DAC e não é dito onde tirar dúvidas.
## Fotos
![https://drive.google.com/open?id=1-LXo216SWRJmW4Pv4YaeOkcBW361a0at](./imgs/PEDRO_1-LXo216SWRJmW4Pv4YaeOkcBW361a0at.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: Instruções não estão visíveis.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[CADEHORR_PEDR_54]* Problema 54: Tipos de Férias não explicados.
**Ocorre na página**: *Caderno de Horários > Ao clicar em Caderno de Horários.*

A diferença entre Férias, Férias de Verão e Férias de Inverno não é explicitada.
## Fotos
![https://drive.google.com/open?id=1JYGgnr3azwTWaJ_kwsS3htth7KGZq96d](./imgs/PEDRO_1JYGgnr3azwTWaJ_kwsS3htth7KGZq96d.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O usuário fica confuso ao ver tipos diferentes de férias referentes a graduação e pós graduação. Não é explicado em que condições os alunos tem aulas nas férias.

### Grau de Serveridade do problema
**Grau de Severidade**: 1 - Sem importância (Não afeta a operação da interface (não é um problema de usabilidade))





## *id:[ENSIABER_PEDR_55]* Problema 55: Falta de verificação de campos.
**Ocorre na página**: *Ensino Aberto > Esquecimento de Senha.*

Não há verificação dos dados do formulário.
## Fotos
![https://drive.google.com/open?id=1xopupa0pi-lWzoryiCBjlPiXMzDdklkG](./imgs/PEDRO_1xopupa0pi-lWzoryiCBjlPiXMzDdklkG.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: A falta de verificação faz com que o usuário consiga cometer erros no preenchimento do formulário.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ENSIABER_PEDR_56]* Problema 56: Erro de codificação de caracteres.
**Ocorre na página**: *Ensino Aberto > Relação das disciplinas ativas por unidade de ensino.*

Os caracteres da página estão fora do padrão UTF-8.
## Fotos
![https://drive.google.com/open?id=1J8UDhXa7yQjETYP_Tn7aWWgQub9-7L_6](./imgs/PEDRO_1J8UDhXa7yQjETYP_Tn7aWWgQub9-7L_6.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A forma como o texto foi codificado dificulta a leitura, texto que não pode ser lido não tem utilidade.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[ENSIABER_PEDR_57]* Problema 57: Página inexistente.
**Ocorre na página**: *Ensino Aberto > Página inicial.*

O link “orientações para o desenvolvimento de disciplinas no ambiente virtual” leva para uma página inexistente.
## Fotos
![https://drive.google.com/open?id=1Fqyv0UUZpU_xKwAjPAESCDAWOoRi3RNt](./imgs/PEDRO_1Fqyv0UUZpU_xKwAjPAESCDAWOoRi3RNt.png)

![https://drive.google.com/open?id=1LQneoTYd0IO6vr5x_Ce8F7QS7ZZFKJlw](./imgs/PEDRO_1LQneoTYd0IO6vr5x_Ce8F7QS7ZZFKJlw.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: Usuário perde liberdade,pois não consegue acessar um conteúdo que achava estar disponível.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ENSIABER_PEDR_58]* Problema 58: Erro interno.
**Ocorre na página**: *Ensino Aberto > Listas de disciplinas de Graduação e Tecnologia > Todos os links.*

O usuário é redirecionado para uma página com “erro interno do sistema”.
## Fotos
![https://drive.google.com/open?id=1aWTInUEVzMddwiJGwu3A3tdKX7ylGsU2](./imgs/PEDRO_1aWTInUEVzMddwiJGwu3A3tdKX7ylGsU2.png)

![https://drive.google.com/open?id=19SIJ8vag4L25zeSK9YIANvOD5Cku8ull](./imgs/PEDRO_19SIJ8vag4L25zeSK9YIANvOD5Cku8ull.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: Os erros mostrados não ajudam o usuário a entender o que ele fez de errado sendo que o erro está no sistema - páginas inexistentes.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[GDE_PEDR_59]* Problema 59: Página inexistente
**Ocorre na página**: *GDE > Ao clicar em GDE.*

O usuário é levado para uma página dizendo “Página não encontrada”.
## Fotos
![https://drive.google.com/open?id=1rWjGtpwZj6sMaEXIU4iqPkZJY0K54bYf](./imgs/PEDRO_1rWjGtpwZj6sMaEXIU4iqPkZJY0K54bYf.png)

![https://drive.google.com/open?id=1aYMjRhADfO9ypgb6fuJCFAmiRxeS8IyO](./imgs/PEDRO_1aYMjRhADfO9ypgb6fuJCFAmiRxeS8IyO.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário não pode acessar a página, perde a possibilidade de visualizar seu conteúdo.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[TESTPROF_PEDR_60]* Problema 60: Difícil encontrar informação.
**Ocorre na página**: *Teste de Proficiência > Proficiência.*

O acesso às informações não é simples.
## Fotos
![https://drive.google.com/open?id=1UJwBL1289bQPt7b5twSQLOdfJqwPyW8Y](./imgs/PEDRO_1UJwBL1289bQPt7b5twSQLOdfJqwPyW8Y.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: A instrução de uso não esta clara.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))




---------


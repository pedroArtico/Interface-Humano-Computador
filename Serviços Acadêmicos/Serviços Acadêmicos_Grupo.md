# Serviços Acadêmicos
 



## *id:[SRVACAD_GRUP_4]* Problema 4: Problemas de Processamento
**Ocorre na página**: *Serviços Acadêmicos > Login do usuário, ao clicar em "acessar"*

Ao tentar logar utilizando caracteres do tipo emoji (não permitidos pelo sistema, entretanto, a informação não é explicitada) o sistema encaminha o usuário para um erro de processamento com uma mensagem contendo trechos de código SQL.
## Fotos
![https://drive.google.com/open?id=1O0c6hzbqEOSK4yfSvRpr6Bi_y5x6CH0x](../../imgs/GRUPO_1O0c6hzbqEOSK4yfSvRpr6Bi_y5x6CH0x.png)

## Comentários
O grau de severidade é grave, pois o usuário não consegue ter acesso a uma parte fundamental do sistema, por esse motivo é de suma importância a rápida resolução.

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A heurística aplicada ao problema é a 9, pois em nenhum momento foi dito como o usuário poderia resolver o problema, apenas é solicitado que ele copie o código SQL e envie à DAC. O usuário não tem entendimento do tipo de problema cometido, e como ele poderia ser facilmente resolvido.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SRVACAD_GRUP_5]* Problema 5: Carregamento da página
**Ocorre na página**: *Serviços Acadêmicos > Ao clicar em "cursos regulares" no tópico REQUERIMENTO DE MATRÍCULA*

A página que aparece está apenas em modo texto, a pagina não é carregada. Além disso, apresenta caracteres fora do padrão utf8.
## Fotos
![https://drive.google.com/open?id=1RZIfWJnIpO1YVtNeDsPPWGgJKrOoznt8](../../imgs/GRUPO_1RZIfWJnIpO1YVtNeDsPPWGgJKrOoznt8.png)

## Comentários
Grau de severidade é 2, pois não é um problema grave, apesar de não condizer com a linguagem por meio da qual o usuário esta acostumado, ainda assim é possível extrair algumas informações da página.

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: A página apresenta conteúdo que não é coerente com o conhecimento do usuário leigo, não faz parte do que ele está habituado a encontrar. Não faz parte da "linguagem" do usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_GRUP_6]* Problema 6: Falta de verificação de campos
**Ocorre na página**: *Serviços Acadêmicos > Ao tentar redirecionar o e-mail da DAC*

O usuário pode digitar combinações de caracteres que não condizem com um endereço de e-mail válido. Não há verificação se o usuário realmente digitou um e-mail ou caracteres aleatórios, como o exemplo da imagem.
## Fotos
![https://drive.google.com/open?id=1knwfBLJO2jTwsIbFq5LoCxtHwZm6U6po](../../imgs/GRUPO_1knwfBLJO2jTwsIbFq5LoCxtHwZm6U6po.png)

## Comentários
O grau de severidade é máximo, pois o usuário pode não receber mais e-mails da DAC, por conta de uma redirecionamento indevido.

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: A heurística correta é a 5, pois os desenvolvedores não pensaram em formas de circuncidar o sistema para que o usuário não pudesse inserir endereços de e-mail inválidos.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SRVACAD_GRUP_7]* Problema 7: Falta de botão na interface
**Ocorre na página**: *Serviços Acadêmicos > Ocorre na Desistência de Matrícula*

O usuário não tem a opção de Voltar, já que o botão não existe. Ele pode apenas sair do sistema, não garantindo que a ação foi desfeita.
## Fotos
![https://drive.google.com/open?id=1O0G0a-oFC3-tcR_S8SAITlL_LxZBdUrt](../../imgs/GRUPO_1O0G0a-oFC3-tcR_S8SAITlL_LxZBdUrt.png)

## Comentários
O grau de severidade é 3, ou seja, é necessário corrigir esse problema, pois caso o usuário não consiga retornar a um menu anterior, e seja obrigado a sair do sistema, o mesmo pode perder informações não-salvas.

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: A heurística correta é a 3, pois o usuário é impedido de voltar à página anterior, desfazendo uma ação, por conta da falta de um botão voltar.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_GRUP_9]* Problema 9: Problema de Codificação de caracteres
**Ocorre na página**: *Serviços Acadêmicos > Integralização Curricular*

Problema com a codificação dos caracteres especiais.
## Fotos
![https://drive.google.com/open?id=1OE_BL1MHjrxycAOCTUWf5mpW69XO1GqC](../../imgs/GRUPO_1OE_BL1MHjrxycAOCTUWf5mpW69XO1GqC.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Usuário não é capaz de identificar que é um problema de codificação para caracteres especiais portanto não é capaz de entender a informação escrita.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_GRUP_28]* Problema 28: Falha de segurança ao usar navegador.
**Ocorre na página**: *Serviços Acadêmicos > Após o login.*

Ao fazer o login no sistema é mostrada uma mensagem dizendo que dependendo do navegador utilizado e de sua versão o usuário corre riscos relacionados com a segurança. 
O teste foi feito em um navegador fora da lista e a ferramenta funcionou normalmente, aparentemente é aceitável que os usuários do sistema corram riscos de segurança.
## Fotos
![https://drive.google.com/open?id=12aySqRu-gGf9jVow_c7lnUWr2rf-3jZ6](../../imgs/GRUPO_12aySqRu-gGf9jVow_c7lnUWr2rf-3jZ6.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: O sistema funciona normalmente em um navegador que não é recomendado, é dito que são problemas de segurança - mas a mensagem é mostrada após o usuário inserir seus dados em um navegador dito inseguro e fazer o login. 
Isso pode causar medo em alguns usuários ou dúvidas se precisam ou não utilizar os navegadores ditos já que o sistema funciona normalmente em um outro navegador.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_GRUP_29]* Problema 29: Funções estão em outro sistema.
**Ocorre na página**: *Serviços Acadêmicos > Após fazer o login na ferramenta.*

É exibida uma mensagem dizendo que para fazer certas alterações de dados existe um novo sistema. Não é esclarecido se tais funções continuam no sistema atual, além disso, essa mensagem poderia aparecer antes do usuário efetuar o login já que ele é obrigado a se autenticar para então descobrir que terá que sair do sistema para acessar outro.
## Fotos
![https://drive.google.com/open?id=1BG4NLRn1rOMCM_WPBJk8NODpo_7tjxb-](../../imgs/GRUPO_1BG4NLRn1rOMCM_WPBJk8NODpo_7tjxb-.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Não existe lógica nas ações ao requerer que um usuário já tenha feito o login para mostrar que as opções que quer podem não estar mais no portal que ele conhece.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_GRUP_30]* Problema 30: Opções de pós-graduação para aluno da graduação apenas.
**Ocorre na página**: *Serviços Acadêmicos > Pós-graduação.*

Mesmo logado como aluno que cursa apenas Graduação o sistema mostra botões clicáveis indicando que poderia acessar opções que não correspondem com o perfil do usuário. .
## Fotos
![https://drive.google.com/open?id=146lb6TTR3bVI6MXscRo-dalH5rqIRbhv](../../imgs/GRUPO_146lb6TTR3bVI6MXscRo-dalH5rqIRbhv.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: A heurística violada é a 2, pois um aluno de graduação não deve ter acesso à informações de pós-graduação. Não faz parte da "realidade" dele.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_GRUP_31]* Problema 31: Mensagem sem sentido no contexto.
**Ocorre na página**: *Serviços Acadêmicos > Relatório Final de Matrícula.*

O sistema mostra uma mensagem de  “campos obrigatórios” mesmo sem haver qualquer campo que possa ser preenchido.
## Fotos
![https://drive.google.com/open?id=1Jw9xGvEBQc5WsShRCgSlJqOtk52ck6uT](../../imgs/GRUPO_1Jw9xGvEBQc5WsShRCgSlJqOtk52ck6uT.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A informação não tem utilidade e só adiciona conteúdo inútil à carga visual do usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_GRUP_32]* Problema 32: Botões com design diferente.
**Ocorre na página**: *Serviços Acadêmicos > Integralização Curricular.*

Os botões imprimir e voltar tem tamanhos, cores, comportamentos, ... diferentes, diminuindo a consistência do sistema.
## Fotos
![https://drive.google.com/open?id=1j8_TBaJ3nVPgfgMrOeREnoL8ZMyr88kb](../../imgs/GRUPO_1j8_TBaJ3nVPgfgMrOeREnoL8ZMyr88kb.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema é inconsistente pois os botões deveriam seguir um mesmo padrão.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))


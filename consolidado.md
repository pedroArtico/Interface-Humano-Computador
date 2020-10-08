# Documento de avaliação segundo as Heurísticas de Nielsen
## Avaliação consolidada
**Página Avaliada**: [https://www.dac.unicamp.br/portal/acesso/estudantes](https://www.dac.unicamp.br/portal/acesso/estudantes)


![data/paginaavaliada.png](data/paginaavaliada.png)
O procedimento de avaliação das heurísticas foi feito em dois momentos distintos. Primeiro, cada um dos quatro integrantes do grupo avaliou individualmente o site da Diretoria Acadêmica. Foi criado um documento no GOOGLE FORMS contendo cada uma das questões referentes aos problemas, tais como: nome,  seção onde o problema aparece, descrição do problema, imagem, heurísticas, justificativa e grau de severidade. O documento foi preenchido para cada problema individualmente, gerando um documento do Google Sheets como resultado. Esse documento foi processado por um programa escrito em Python para colocar os dados da tabela em um documento de texto.

Após a avaliação ter sido feita individualmente (os alunos não trocaram informações sobre os problemas encontrados durante o período de análise), o grupo se uniu para definir quais problemas em comum foram encontrados. Os problemas que foram encontrados individualmente foram avaliados, e alguns erros na definição de heurísticas e graus de severidade foram corrigidos.


**Formulário utilizado**

![data/form.png](data/form.png)



* **Link para o formulário utilizado**: [Formulário](https://docs.google.com/forms/d/e/1FAIpQLScmZ_LzhXA_dx5XmhWrQjtcYFNG7xgcjER1TXufxEPOvflIjQ/viewform)
* **Link para o software desenvolvido**: [GitHub](https://github.com/ALREstevam/Gsheet-IHC/)

---------------


# Problemas levantados por: *Grupo*




## *id:[PASSESCO_GRUP_1]* Problema 1: Link Inválido
**Ocorre na página**: *Passe Escolar > Ao clicar em “O site da EMTU”*

O link redireciona para uma página dizendo que o recurso que seria acessado está indisponível.
## Fotos
![https://drive.google.com/open?id=1aH6To-aDckL93zr62tJUk8dxYn9NOl1u](./imgs/GRUPO_1aH6To-aDckL93zr62tJUk8dxYn9NOl1u.png)

![https://drive.google.com/open?id=1g4H_k9E3jTykGWNbM9x4VEwOUd9dbD2K](./imgs/GRUPO_1g4H_k9E3jTykGWNbM9x4VEwOUd9dbD2K.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: O usuário não tem acesso à página, além disso não tem como saber qual erro ocorreu, nem o motivo de a página estar indisponível. O usuário não é auxiliado à corrigr ou identificar as causas do erro.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[PIF_GRUP_2]* Problema 2: Explicação confusa
**Ocorre na página**: *PIF - Programa Integrado de Formação > PIF*

O texto está confuso. Não é explicado onde estão as demais exigências.
## Fotos
![https://drive.google.com/open?id=1v-fRrfiaowN_hakHuXEf1gxRUSDnn7NG](./imgs/GRUPO_1v-fRrfiaowN_hakHuXEf1gxRUSDnn7NG.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Existe informação confusa para o usuário. Deveria estar mais detalhado quais são as exigências para participar do programa e as durações minima e máxima do curso.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_GRUP_3]* Problema 3: Botão que não parece botão
**Ocorre na página**: *Alteração de Matrícula > Consultar Relatório de Integralização*

Na parte superior da página há um botão "serviços aluno", que não parece ser um botão, que volta para a página anterior. Não tem a aparência de um botão que o usuário já está familiarizado e não deixa claro qual a sua função.
## Fotos
![https://drive.google.com/open?id=1e2ddXftavr9RKS5KRRAjdj84upv6cV7P](./imgs/GRUPO_1e2ddXftavr9RKS5KRRAjdj84upv6cV7P.png)

## Considerações

### Heurística ferida: 6ª
**Heurística ferida**: 6 - Reconhecer ao invés de relembrar

**Justificativa**: Não segue o design já conhecido de um botão e não deixa claro qual sua função.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SRVACAD_GRUP_4]* Problema 4: Problemas de Processamento
**Ocorre na página**: *Serviços Acadêmicos > Login do usuário, ao clicar em "acessar"*

Ao tentar logar utilizando caracteres do tipo emoji (não permitidos pelo sistema, entretanto, a informação não é explicitada) o sistema encaminha o usuário para um erro de processamento com uma mensagem contendo trechos de código SQL.
## Fotos
![https://drive.google.com/open?id=1O0c6hzbqEOSK4yfSvRpr6Bi_y5x6CH0x](./imgs/GRUPO_1O0c6hzbqEOSK4yfSvRpr6Bi_y5x6CH0x.png)

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
![https://drive.google.com/open?id=1RZIfWJnIpO1YVtNeDsPPWGgJKrOoznt8](./imgs/GRUPO_1RZIfWJnIpO1YVtNeDsPPWGgJKrOoznt8.png)

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
![https://drive.google.com/open?id=1knwfBLJO2jTwsIbFq5LoCxtHwZm6U6po](./imgs/GRUPO_1knwfBLJO2jTwsIbFq5LoCxtHwZm6U6po.png)

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
![https://drive.google.com/open?id=1O0G0a-oFC3-tcR_S8SAITlL_LxZBdUrt](./imgs/GRUPO_1O0G0a-oFC3-tcR_S8SAITlL_LxZBdUrt.png)

## Comentários
O grau de severidade é 3, ou seja, é necessário corrigir esse problema, pois caso o usuário não consiga retornar a um menu anterior, e seja obrigado a sair do sistema, o mesmo pode perder informações não-salvas.

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: A heurística correta é a 3, pois o usuário é impedido de voltar à página anterior, desfazendo uma ação, por conta da falta de um botão voltar.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ENSIABER_GRUP_8]* Problema 8: Links levam a erro interno
**Ocorre na página**: *Ensino Aberto > Listas de disciplinas de Graduação e Tecnologia > Todos os links*

Links levam para uma página com “erro interno do sistema”.
## Fotos
![https://drive.google.com/open?id=1aWTInUEVzMddwiJGwu3A3tdKX7ylGsU2](./imgs/GRUPO_1aWTInUEVzMddwiJGwu3A3tdKX7ylGsU2.png)

![https://drive.google.com/open?id=19SIJ8vag4L25zeSK9YIANvOD5Cku8ull](./imgs/GRUPO_19SIJ8vag4L25zeSK9YIANvOD5Cku8ull.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: Os erros mostrados não ajudam o usuário a entender o que ele fez de errado sendo que o erro está no sistema - páginas inexistentes.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SRVACAD_GRUP_9]* Problema 9: Problema de Codificação de caracteres
**Ocorre na página**: *Serviços Acadêmicos > Integralização Curricular*

Problema com a codificação dos caracteres especiais.
## Fotos
![https://drive.google.com/open?id=1OE_BL1MHjrxycAOCTUWf5mpW69XO1GqC](./imgs/GRUPO_1OE_BL1MHjrxycAOCTUWf5mpW69XO1GqC.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Usuário não é capaz de identificar que é um problema de codificação para caracteres especiais portanto não é capaz de entender a informação escrita.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[TRANINTE_GRUP_10]* Problema 10: Sistema não fala como encontrar regimento
**Ocorre na página**: *Transferência Interna > No fim da página*

O site não diz como conseguir regimento, se é disponibilizado na web, na biblioteca ou na secretaria, por exemplo.
## Fotos
![https://drive.google.com/open?id=1kdNYcrBdYcxdguWWSrmlUVfCGP54goyK](./imgs/GRUPO_1kdNYcrBdYcxdguWWSrmlUVfCGP54goyK.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: O usuário não tem a opção de saber mais sobre o regimento.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ESTR_GRUP_11]* Problema 11: Página inexistente
**Ocorre na página**: *Estrangeiro > Registro de Visto*

O link redireciona para uma página inexistente.
## Fotos
![https://drive.google.com/open?id=1b00t55rntffMQL1wAaRqpzdDFzwzCmii](./imgs/GRUPO_1b00t55rntffMQL1wAaRqpzdDFzwzCmii.png)

![https://drive.google.com/open?id=1VkWNS6ZdpMajbS9TPHwl8bR-jomRe1Nv](./imgs/GRUPO_1VkWNS6ZdpMajbS9TPHwl8bR-jomRe1Nv.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: O usuário não tem acesso à página, além disso não tem como saber qual erro ocorreu, nem o motivo de a página estar indisponível. O usuário não é auxiliado à corrigr ou identificar as causas do erro.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[CADEHORR_GRUP_12]* Problema 12: Campos em inglês
**Ocorre na página**: *Caderno de Horários > Alunos de EL774: Lista de Projetos de Estágio em Licenciatura / Alunos de EL874: Lista de Projetos de Estágio em Licenciatura > Disciplinas > Estágio …*

Parte dos resultados estão em inglês.
## Fotos
![https://drive.google.com/open?id=1a3BwZkEO6I4n3TJHLDfALY6IUDnMAvmP](./imgs/GRUPO_1a3BwZkEO6I4n3TJHLDfALY6IUDnMAvmP.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: A página está inconsistente pois parte está em português e parte em inglês.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[CADEHORR_GRUP_13]* Problema 13: Falta de página de dúvidas
**Ocorre na página**: *Caderno de Horários > Alunos de EL774: Lista de Projetos de Estágio em Licenciatura / Alunos de EL874: Lista de Projetos de Estágio em Licenciatura*

Não existe página de dúvidas, caso o usuário tenha é dito que ligue em um telefone ou envie um e-mail.
## Fotos
![https://drive.google.com/open?id=1LSVQ92SNgNQuWOgVUvxirMH5xGwqixnq](./imgs/GRUPO_1LSVQ92SNgNQuWOgVUvxirMH5xGwqixnq.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: Não existe página de dúvidas.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[CADEHORR_GRUP_14]* Problema 14: Página confusa
**Ocorre na página**: *Caderno de Horários > Continência/Equivalência (Graduação)*

Faltam explicações, texto e notações são confusos.
A pesquisa é feita com letras de início do código da disciplina, isso dificulta o trabalho, poderia ter algo como um campo de pesquisa textual ou seleção da disciplina pelo nome ou código.
## Fotos
![https://drive.google.com/open?id=1NE6h0M7RfvebSOgStYvP6qbV1s8ZNJnN](./imgs/GRUPO_1NE6h0M7RfvebSOgStYvP6qbV1s8ZNJnN.png)

![https://drive.google.com/open?id=1eOPv93UxR_kgVdit2rmZBPsnMYMjgbpy](./imgs/GRUPO_1eOPv93UxR_kgVdit2rmZBPsnMYMjgbpy.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: As ações para encontrar as disciplinas não seguem uma lógica fácil de assimilar.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[CADEHORR_GRUP_15]* Problema 15: Falta de botão voltar
**Ocorre na página**: *Caderno de Horários > Continência/Equivalência (Graduação) > Alguma Letra*

Durante uma busca não é possível trocar de letra inicial do código da disciplina buscada, a página sugere voltar na página inicial, mas falta o botão para isso, se o usuário tiver clicado em vários dos links na página terá que passar por todos eles de novo se utilizar a opção voltar do navegador.
## Fotos
![https://drive.google.com/open?id=1dt_A6z6CPruVCMqeuBEZYKw5EpvySfZB](./imgs/GRUPO_1dt_A6z6CPruVCMqeuBEZYKw5EpvySfZB.png)

![https://drive.google.com/open?id=1zY3OdDiuctpZHVbqqdf0Kh1026CEKJw9](./imgs/GRUPO_1zY3OdDiuctpZHVbqqdf0Kh1026CEKJw9.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário perde liberdade no sistema ao não ter como voltar facilmente.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[WEBM_GRUP_16]* Problema 16: Página confusa
**Ocorre na página**: *Webmail > Preferências > Categorias e nomenclaturas*

A página não deixa claro o que são categorias e nomenclaturas. Além disso, apresenta códigos para representar cores. O usuário, caso não seja de T.I. , não saberá de antemão o significado desses códigos.
## Fotos
![https://drive.google.com/open?id=11R_QvadsAcQWuMBgKv9LmXwCM_f4Scev](./imgs/GRUPO_11R_QvadsAcQWuMBgKv9LmXwCM_f4Scev.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O sistema falha ao tentar estabelecer relação com o mundo real pois não explica o que são as cores, categorias e nomenclaturas naquele contexto.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[WEBM_GRUP_17]* Problema 17: Ajuda em inglês
**Ocorre na página**: *Webmail > Login > Entrar > Ajuda*

A página de ajuda do webmail está em inglês.
## Fotos
![https://drive.google.com/open?id=1DiBDH1aa0MgsYjszv6s7dKqS6Tt3_Nd4](./imgs/GRUPO_1DiBDH1aa0MgsYjszv6s7dKqS6Tt3_Nd4.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: A página em inglês é pouco útil para usuários com a primeira língua sendo o português.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[WEBM_GRUP_18]* Problema 18: Erro ao fazer login
**Ocorre na página**: *Webmail > após login*

Os campos são marcados como com erro, com mensagens em inglês.
## Fotos
![https://drive.google.com/open?id=1BhifwNqXiKKny--BQkTQQbHYIcMHzmYq](./imgs/GRUPO_1BhifwNqXiKKny--BQkTQQbHYIcMHzmYq.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: Os erros que aparecem não auxiliam o usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[WEBM_GRUP_19]* Problema 19: Página não encontrada
**Ocorre na página**: *Webmail > Login > Em caso de esquecimento de senha clique aqui*

Ao clicar no link de esquecimento de senha a página mostra uma mensagem de página não encontrada.
## Fotos
![https://drive.google.com/open?id=12fJiFtgsPoc1Efgby154Yhk9ysHhJvmA](./imgs/GRUPO_12fJiFtgsPoc1Efgby154Yhk9ysHhJvmA.png)

![https://drive.google.com/open?id=1xFEhQcK2dwiv1H4QfjT_QfxnZDv8Bsrh](./imgs/GRUPO_1xFEhQcK2dwiv1H4QfjT_QfxnZDv8Bsrh.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: O usuário não tem acesso à página, além disso não tem como saber qual erro ocorreu, nem o motivo de a página estar indisponível. O usuário não é auxiliado à corrigr ou identificar as causas do erro.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SENH_GRUP_20]* Problema 20: Página de ajuda não ajuda
**Ocorre na página**: *Senha > cadastre aqui > caso você não tenha recebido a senha inicial clique aqui > dúvidas*

A ajuda fala apenas sobre como preencher nomes, não explica demais campos ou o que o sistema faz.
## Fotos
![https://drive.google.com/open?id=1gk0KKlLL_Tc7LLIvJAUaa3zZhU8rKobN](./imgs/GRUPO_1gk0KKlLL_Tc7LLIvJAUaa3zZhU8rKobN.png)

![https://drive.google.com/open?id=1EoaEwsG7dVG9i3FEl3pIT9XyYutMdSyl](./imgs/GRUPO_1EoaEwsG7dVG9i3FEl3pIT9XyYutMdSyl.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: A página de ajuda é insuficiente.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SENH_GRUP_21]* Problema 21: Mensagem de erro incorreta
**Ocorre na página**: *Senha > cadastre aqui > caso você não tenha recebido a senha inicial clique aqui*

Ao tentar submeter um formulário vazio o erro mostrado é de conversão de campos numéricos, a mensagem não ajuda o usuário.
## Fotos
![https://drive.google.com/open?id=1kqUqhmA7Qexvwfpq167n7yq9OG0S7EDV](./imgs/GRUPO_1kqUqhmA7Qexvwfpq167n7yq9OG0S7EDV.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A mensagem de erro não reflete o que ocorreu realmente, confundindo o usuário.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SENH_GRUP_22]* Problema 22: Mensagem de erro pouco esclarecedora
**Ocorre na página**: *Senha > cadastre aqui > caso você não tenha recebido a senha inicial clique aqui*


A mensagem de erro não esclarece quais são os campos numéricos, ou se os campos de data são numéricos ou de data um usuário leigo não entenderia o que é um erro de conversão.
Outro exemplo é a possibilidade de colocar letras em campos numéricos.
## Fotos
![https://drive.google.com/open?id=1W6rGbaDI4d6wKv7cx122dq9pbdph0nyU](./imgs/GRUPO_1W6rGbaDI4d6wKv7cx122dq9pbdph0nyU.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: A mensagem de erro não é clara e não aponta para soluções de forma direta.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SENH_GRUP_23]* Problema 23: Falta de verificação de formulário
**Ocorre na página**: *Senha > cadastre aqui > caso você não tenha recebido a senha inicial clique aqui*

Falta de verificação do que foi digitado em todos os campos.
## Fotos
![https://drive.google.com/open?id=12v61bxr4LjJkJ0vz_9tFMvuHyAQZ4GOL](./imgs/GRUPO_12v61bxr4LjJkJ0vz_9tFMvuHyAQZ4GOL.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: Como os campos não são verificados antes da submissão o usuário não é impedido de causar erros no sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[ALTEMATR_GRUP_24]* Problema 24: Erro UTF-8
**Ocorre na página**: *Alteração de Matrícula > Relatório de Integralização*

O relatório contém erros de codificação UTF-8.
## Fotos
![https://drive.google.com/open?id=1X81fr_UcWbibV_YOCUz1L4bR7v3JQ5yz](./imgs/GRUPO_1X81fr_UcWbibV_YOCUz1L4bR7v3JQ5yz.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Problema com a codificação dos caracteres especiais. O texto está em linguagem diferente da linguagem do usuário, isso atrapalha sua compreensão do conteúdo.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[GDE_GRUP_25]* Problema 25: Página não encontrada
**Ocorre na página**: *GDE > Página inicial GDE*

Ao clicar na opção do GDE aparece a mensagem "Página não encontrada".
## Fotos
![https://drive.google.com/open?id=1jAgOgwkMG10qqyQdsufwGy_wmRoEM70W](./imgs/GRUPO_1jAgOgwkMG10qqyQdsufwGy_wmRoEM70W.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: O usuário não é orientado de como sair do erro, ou como resolvê-lo. Não há informações do motivo pelo qual a página não foi encontrada. Não fica claro para o usuário quem foi o responsável pelo erro (ele ou o sistema).

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SIGA_GRUP_26]* Problema 26: Mensagem de confirmação sem motivo
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Em atualizar (sem nenhuma alteração nos dados)*

A mensagem de confirmação de alteração nos dados cadastrais é exibida mesmo que nenhum dado tenha sido alterado.
## Fotos
![https://drive.google.com/open?id=1ucYpnMn_4eZkP1mcnbYDviwnGqC8hjyZ](./imgs/GRUPO_1ucYpnMn_4eZkP1mcnbYDviwnGqC8hjyZ.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: O sistema mostra uma tela que não tem necessidade de ser mostrada.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[SIGA_GRUP_27]* Problema 27: Validação de CEP incorreta
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Endereço > Localizar CEP*

Houve uma mudança nos números do CEP em minha cidade, o site da DAC não foi atualizado de acordo com essa mudança, dessa forma não é possível colocar o CEP atualizado. Pesquisando no site dos Correios é possível ver que o CEP em questão é válido.
## Fotos
![https://drive.google.com/open?id=1q3JMDuUlfS7TG7k7TvMhuIkgGm_9i1qx](./imgs/GRUPO_1q3JMDuUlfS7TG7k7TvMhuIkgGm_9i1qx.png)

![https://drive.google.com/open?id=1rQi8yDstnguP0kU0i3QT7fsZ45ZBHkgx](./imgs/GRUPO_1rQi8yDstnguP0kU0i3QT7fsZ45ZBHkgx.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: O sistema está desalinhado com o mundo real pois diz que um CEP que existe é inexistente .

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SRVACAD_GRUP_28]* Problema 28: Falha de segurança ao usar navegador.
**Ocorre na página**: *Serviços Acadêmicos > Após o login.*

Ao fazer o login no sistema é mostrada uma mensagem dizendo que dependendo do navegador utilizado e de sua versão o usuário corre riscos relacionados com a segurança. 
O teste foi feito em um navegador fora da lista e a ferramenta funcionou normalmente, aparentemente é aceitável que os usuários do sistema corram riscos de segurança.
## Fotos
![https://drive.google.com/open?id=12aySqRu-gGf9jVow_c7lnUWr2rf-3jZ6](./imgs/GRUPO_12aySqRu-gGf9jVow_c7lnUWr2rf-3jZ6.png)

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
![https://drive.google.com/open?id=1BG4NLRn1rOMCM_WPBJk8NODpo_7tjxb-](./imgs/GRUPO_1BG4NLRn1rOMCM_WPBJk8NODpo_7tjxb-.png)

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
![https://drive.google.com/open?id=146lb6TTR3bVI6MXscRo-dalH5rqIRbhv](./imgs/GRUPO_146lb6TTR3bVI6MXscRo-dalH5rqIRbhv.png)

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
![https://drive.google.com/open?id=1Jw9xGvEBQc5WsShRCgSlJqOtk52ck6uT](./imgs/GRUPO_1Jw9xGvEBQc5WsShRCgSlJqOtk52ck6uT.png)

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
![https://drive.google.com/open?id=1j8_TBaJ3nVPgfgMrOeREnoL8ZMyr88kb](./imgs/GRUPO_1j8_TBaJ3nVPgfgMrOeREnoL8ZMyr88kb.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema é inconsistente pois os botões deveriam seguir um mesmo padrão.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_GRUP_33]* Problema 33: Campos não verificados.
**Ocorre na página**: *Alteração de Matrícula > Alteração de Matrícula.*

Um erro ocorre ao digitar certos caracteres especiais, não é feita a verificação antes do envio dos dados.
## Fotos
![https://drive.google.com/open?id=1kLQGj0D5SdZHvjubxMO6VEWxv_0Ltzxa](./imgs/GRUPO_1kLQGj0D5SdZHvjubxMO6VEWxv_0Ltzxa.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: Como não há verificação o sistema não impede que o usuário deliberadamente cometa o erro.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SENH_GRUP_34]* Problema 34: Falta de verificação de campos.
**Ocorre na página**: *Senha > Alterar Senha.*

Ao tentar alterar a senha, inserindo um username com caracteres emoji, não há verificação de teste para validação.
## Fotos
![https://drive.google.com/open?id=1HmTIB4a9zdkAt2iQBN4qSVNQZIvbnUuW](./imgs/GRUPO_1HmTIB4a9zdkAt2iQBN4qSVNQZIvbnUuW.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**:  A heuristica correta é a 5, pois não foram tomadas iniciativas por parte dos desenvolvedores para evitar que os usuários digitassem caracteres indesejados.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[SENH_GRUP_35]* Problema 35: Erro de processamento ao tentar alterar senha.
**Ocorre na página**: *Senha > Alterar Senha.*

Ao tentar realizar a troca de senha, caso o usuário insira caracteres do tipo emoji no username, ocorre um erro de processamento do qual não se tem informações.
## Fotos
![https://drive.google.com/open?id=1wFLgggGlkSuAVbaF42eagL1FQ8vgq1y0](./imgs/GRUPO_1wFLgggGlkSuAVbaF42eagL1FQ8vgq1y0.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: O usuário cometeu um erro e não há indicação de como soluciona-lo de maneira rápida e efetiva.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[ALTEMATR_GRUP_36]* Problema 36: Problema com texto de ajuda.
**Ocorre na página**: *Alteração de Matrícula > Seção de ajuda.*

A página de ajuda está com problema na codificação dos caracteres.
## Fotos
![https://drive.google.com/open?id=1DRFt-T6yzmtMo7z3D60bLTZqMRoyIEIq](./imgs/GRUPO_1DRFt-T6yzmtMo7z3D60bLTZqMRoyIEIq.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: O problema de codificação leva o usuário a ter dificuldade na leitura, tornando a página de ajuda bem menos útil.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[ALTEMATR_GRUP_37]* Problema 37: Falta de informação sobre vagas.
**Ocorre na página**: *Alteração de Matrícula > Na "Alteração de Matrícula, em "Situação de Vaga por Disciplina".*

A situação de vagas por disciplina não é exibida. Aparece em branco.
## Fotos
![https://drive.google.com/open?id=1IiAp9zLFv1WEfx7vtwcsSNYfilBCGlk5](./imgs/GRUPO_1IiAp9zLFv1WEfx7vtwcsSNYfilBCGlk5.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: A heuristica violada é a 8, pois faltam informações para o usuário. Ele é obrigado a intuir a situação da vaga. Não há uma explicação sobre as possíveis situações que uma vaga pode ter.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ALTEMATR_GRUP_38]* Problema 38: "Ajuda" confusa.
**Ocorre na página**: *Alteração de Matrícula > Ao clicar em "Ajuda" na "Alteração de Matrícula".*

Há informações confusas e redundantes no menu de ajuda. Por exemplo: "Se existir apenas um periodo aberto, quando o usuário acessar o serviço já estará sendo considerado o periodo disponivel para consulta".
## Fotos
![https://drive.google.com/open?id=1lz5iJnQ9S-IJzUBSq1Yyg72I5w4FoSzf](./imgs/GRUPO_1lz5iJnQ9S-IJzUBSq1Yyg72I5w4FoSzf.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: A documentação da ajuda está em péssimas condições. Além de haver problemas de visualização, as informações são pouco úteis. .

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[TESTPROF_GRUP_39]* Problema 39: Erro de Execução.
**Ocorre na página**: *Teste de Proficiência > Ao clicar em "Consultar Inscrição"*

Um erro de execução é exibido com diversos códigos Java, e o usuário não é informado de como resolvê-lo. Apenas pedem para consultar a DAC.
## Fotos
![https://drive.google.com/open?id=1l126XzpUH3UwM84J-aRoTsIXUjaB9pfX](./imgs/GRUPO_1l126XzpUH3UwM84J-aRoTsIXUjaB9pfX.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: O usuário cometeu uma ação errada ao consultar uma inscrição, sem estar inscrito no programa. Entretanto, o usuário não foi orientado sobre como corrigir o erro.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[TESTPROF_GRUP_40]* Problema 40: Erro na Execução.
**Ocorre na página**: *Teste de Proficiência > Ao clicar em "Consultar Resultado"*

Ao tentar realizar a consulta do resultado, inserindo um emoji no campo "Por disciplina/Nível", o usuário é permitido, ouse ja, não há nenhum aviso de que a ação está errada.
## Fotos
![https://drive.google.com/open?id=1dm8pSk8wQ_6egv5aae7GQlGADrqLbBCY](./imgs/GRUPO_1dm8pSk8wQ_6egv5aae7GQlGADrqLbBCY.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: O usuário não é orientado de como sair do erro, ou como resolvê-lo.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[TRANINTE_GRUP_41]* Problema 41: Texto confuso e ambíguo.
**Ocorre na página**: *Transferência Interna > Ao clicar em "Transferência Interna".*

Na página é dito que o estudante precisa ter 50% dos créditos aproveitáveis obtidos por um mesmo estudante do curso pelo qual se pretende ingressar, entretanto é dito que esses créditos não precisam ser correspondentes as mesmas disciplinas cursadas por um aluno do primeiro semestre do curso.
## Fotos
![https://drive.google.com/open?id=1qpr-zNiLSThq7d032Je5Lpo3Kgq_OWtf](./imgs/GRUPO_1qpr-zNiLSThq7d032Je5Lpo3Kgq_OWtf.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Existe informação inútil e ambigua na tela. Não está claro como se encaixam os 50% dos créditos aproveitáveis que o aluno deve ter.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[TRANINTE_GRUP_42]* Problema 42: Texto ambíguo
**Ocorre na página**: *Transferência Interna > ao clicar em Transferência Interna*

Não fica claro como a somatória de créditos do estudante será utilizada para o ingresso no curso ao qual se tem interesse em remanejar.
## Fotos
![https://drive.google.com/open?id=1Kxq0i728IrXUWwYIjmW1MfDY1QErSzXh](./imgs/GRUPO_1Kxq0i728IrXUWwYIjmW1MfDY1QErSzXh.png)

## Considerações

### Heurística ferida: 8ª
**Heurística ferida**: 8 - Estética e design minimalista

**Justificativa**: Há informação inútil e ambigua na tela. Não fica claro para o usuário como os créditos serão aproveitados, e nem como o cálculo é feito.

### Grau de Serveridade do problema
**Grau de Severidade**: 3 - Simples (Problema de baixa prioridade (pode ser reparado))





## *id:[ENSIABER_GRUP_43]* Problema 43: Falta de verificação.
**Ocorre na página**: *Ensino Aberto > Contato.*

Nenhuma verificação de dados é feita, o usuário pode colocar um e-mail inválido inclusive.
## Fotos
![https://drive.google.com/open?id=1V5AQr1RQVmqsD8jjTSRP-EZScCxBpmsE](./imgs/GRUPO_1V5AQr1RQVmqsD8jjTSRP-EZScCxBpmsE.png)

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: A falta de verificação não impede que o usuário cometa erros no preenchimento do formulário.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[CADEHORR_GRUP_44]* Problema 44: Botão de informação não faz nada.
**Ocorre na página**: *Caderno de Horários > Caderno de Horários.*

Normalmente ícones com um “i” significam “informação” mas nada acontece ao passar o mouse ou clicar sobre eles.
## Fotos
![https://drive.google.com/open?id=1jMy3520pT-PTpij7t31843Iw53G4415x](./imgs/GRUPO_1jMy3520pT-PTpij7t31843Iw53G4415x.png)

## Considerações

### Heurística ferida: 4ª
**Heurística ferida**: 4 - Consistência e padrões

**Justificativa**: O sistema não segue o padrão de fornecer informações em botões com um "i".

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SIGA_GRUP_45]* Problema 45: Legendas em inglês.
**Ocorre na página**: *SIGA - Sistema de Gestão Acadêmica > Ao usar o menu “Legenda”.*

As legendas no sistema estão em inglês sendo que o sistema é voltado para usuários brasileiros e o restante dele está em português.
## Fotos
![https://drive.google.com/open?id=1Ew_LHJi2mYY0V1mRGx56gBJ_xsRHQMlU](./imgs/GRUPO_1Ew_LHJi2mYY0V1mRGx56gBJ_xsRHQMlU.png)

![https://drive.google.com/open?id=19uzfoVx8oHy6XBOjANAve7TyyU4pXDdY](./imgs/GRUPO_19uzfoVx8oHy6XBOjANAve7TyyU4pXDdY.png)

## Considerações

### Heurística ferida: 10ª
**Heurística ferida**: 10 - Ajuda e documentação

**Justificativa**: A ajuda em inglês é de pouca utilidade visto que a maioria dos usuários fala português.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[ENSIABER_GRUP_46]* Problema 46: Erro interno.
**Ocorre na página**: *Ensino Aberto > Listas de disciplinas de Graduação e Tecnologia > Todos os links.*

O usuário é redirecionado para uma página com “erro interno do sistema”.
## Fotos
![https://drive.google.com/open?id=1aWTInUEVzMddwiJGwu3A3tdKX7ylGsU2](./imgs/GRUPO_1aWTInUEVzMddwiJGwu3A3tdKX7ylGsU2.png)

![https://drive.google.com/open?id=19SIJ8vag4L25zeSK9YIANvOD5Cku8ull](./imgs/GRUPO_19SIJ8vag4L25zeSK9YIANvOD5Cku8ull.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: Os erros mostrados não ajudam o usuário a entender o que ele fez de errado sendo que o erro está no sistema - páginas inexistentes.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)





## *id:[ENSIABER_GRUP_47]* Problema 47: Erro de codificação de caracteres.
**Ocorre na página**: *Ensino Aberto > Relação das disciplinas ativas por unidade de ensino.*

Ao clicar no link de relação das disciplinas ativas por unidade de ensino a página que será aberta contém erros de codificação UTF-8.
## Fotos
![https://drive.google.com/open?id=1hGT_wOycTf7ESm7hkKnpyYKpy-nUQuxY](./imgs/GRUPO_1hGT_wOycTf7ESm7hkKnpyYKpy-nUQuxY.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: Problema com a codificação dos caracteres especiais. O texto está em linguagem diferente da linguagem do usuário, isso atrapalha sua compreensão do conteúdo.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[PASSESCO_GRUP_48]* Problema 48: Erro no link.
**Ocorre na página**: *Passe Escolar > Link EMTU.*

Quando o aluno clicar no link da EMTU aparece página com erro.
## Fotos
![https://drive.google.com/open?id=1Yqk4BSyIup9G01zEZbiXzJlAGreh6k2v](./imgs/GRUPO_1Yqk4BSyIup9G01zEZbiXzJlAGreh6k2v.png)

## Considerações

### Heurística ferida: 9ª
**Heurística ferida**: 9 - Auxiliar usuários a reconhecer, diagnosticar e recuperar ações erradas

**Justificativa**: Mensagem de erro em linguagem complexa.

### Grau de Serveridade do problema
**Grau de Severidade**: 5 - Catastrófico (Muito grave, deve ser reparado de qualquer forma -)




---------


# Serviços Acadêmicos
 



## *id:[SRVACAD_PEDR_1]* Problema 1: Problemas de Processamento.
**Ocorre na página**: *Serviços Acadêmicos > Login do usuário, ao clicar em "Acessar".*

Ao tentar logar utilizando caracteres do tipo emoji (não permitidos pelo sistema, entretanto, a informação não é explicitada) o sistema encaminha o usuário para um erro de processamento com uma mensagem contendo trechos de código SQL.
## Fotos
![https://drive.google.com/open?id=1O0c6hzbqEOSK4yfSvRpr6Bi_y5x6CH0x](../../imgs/PEDRO_1O0c6hzbqEOSK4yfSvRpr6Bi_y5x6CH0x.png)

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
![https://drive.google.com/open?id=1RZIfWJnIpO1YVtNeDsPPWGgJKrOoznt8](../../imgs/PEDRO_1RZIfWJnIpO1YVtNeDsPPWGgJKrOoznt8.png)

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
![https://drive.google.com/open?id=1knwfBLJO2jTwsIbFq5LoCxtHwZm6U6po](../../imgs/PEDRO_1knwfBLJO2jTwsIbFq5LoCxtHwZm6U6po.png)

## Comentários
O grau de severidade é máximo, pois o usuário pode não receber mais e-mails da DAC, por conta de uma redirecionamento indevido.

## Considerações

### Heurística ferida: 5ª
**Heurística ferida**: 5 - Prevenção de erro

**Justificativa**: A heurística correta é a 5, pois os desenvolvedores não pensaram em formas de circuncidar o sistema para que o usuário não pudesse inserir endereços de e-mail inválidos.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_PEDR_5]* Problema 5: Inconsistência no menu.
**Ocorre na página**: *Serviços Acadêmicos > Menu Principal de Serviços Acadêmicos.*

A opção CERTIFICADO PED é apresentada na parte de Graduação do Menu Principal, entretanto, um aluno de graduação não pode ser PED.
## Fotos
![https://drive.google.com/open?id=15cfCIlW8FVhSaHt8xB_K8B21BPPXjMWG](../../imgs/PEDRO_15cfCIlW8FVhSaHt8xB_K8B21BPPXjMWG.png)

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
![https://drive.google.com/open?id=1O0G0a-oFC3-tcR_S8SAITlL_LxZBdUrt](../../imgs/PEDRO_1O0G0a-oFC3-tcR_S8SAITlL_LxZBdUrt.png)

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
![https://drive.google.com/open?id=1Rij8I3KxQDLHvL0BchI7JNT6ruLv1aUv](../../imgs/PEDRO_1Rij8I3KxQDLHvL0BchI7JNT6ruLv1aUv.png)

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
![https://drive.google.com/open?id=1HhWVkAV_M5b0UYCPUu6YvRC4xy3wiRwE](../../imgs/PEDRO_1HhWVkAV_M5b0UYCPUu6YvRC4xy3wiRwE.png)

## Considerações

### Heurística ferida: 3ª
**Heurística ferida**: 3 - Liberdade e controle do usuário

**Justificativa**: O usuário não tem a liberdade de voltar ao menu anterior e refazer a ação. Não pode consultar novamente seu relatório final de matrícula, sem ter que sair do sistema.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)





## *id:[SRVACAD_PEDR_10]* Problema 10: Decodificação de caracteres.
**Ocorre na página**: *Serviços Acadêmicos > Integralização Curricular.*

Ao clicar em "Integralização Curricular", aparecem varias informações sobre o aluno, entretanto, há erros de codificação de Caracteres UTF-8. O conteúdo está com sentido comprometido.
## Fotos
![https://drive.google.com/open?id=1pzBGaZ37qE30lMISGowt86ICxLsfBm9_](../../imgs/PEDRO_1pzBGaZ37qE30lMISGowt86ICxLsfBm9_.png)

## Considerações

### Heurística ferida: 2ª
**Heurística ferida**: 2 - Equivalência entre o sistema e o mundo real

**Justificativa**: A informação não é apresentado na mesma linguagem que o usuário está habituado. Não é possível compreender o conteúdo da página.

### Grau de Serveridade do problema
**Grau de Severidade**: 4 - Grave (Problema de alta prioridade (deve ser reparado))





## *id:[SRVACAD_PEDR_42]* Problema 42: Página em branco.
**Ocorre na página**: *Serviços Acadêmicos > Ao clicar no botão "Confirmar", em PED.*

O usuário é redirecionado para uma página em branco.
## Fotos
![https://drive.google.com/open?id=10xRVG11Wl6msHft6Q94BAKD1ydKP8aGZ](../../imgs/PEDRO_10xRVG11Wl6msHft6Q94BAKD1ydKP8aGZ.png)

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
![https://drive.google.com/open?id=1AYqEyvbHo4eBrMyekl4FfC_eD70JSmLT](../../imgs/PEDRO_1AYqEyvbHo4eBrMyekl4FfC_eD70JSmLT.png)

## Considerações

### Heurística ferida: 0ª
**Heurística ferida**: 0 - A heurística não foi identificada: este tópico não se encaixa em nenhuma das heurísticas ou será discutido posteriormente para a definição de sua heurística

**Justificativa**: O usuário não é levado a uma página válida.

### Grau de Serveridade do problema
**Grau de Severidade**: 2 - Cosmético (Não há necessidade imediata de solução)


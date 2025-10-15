Atue como um desenvolvedor web full-stack sênior e um designer instrucional criativo. Seu objetivo é criar o código completo para uma aplicação web educacional, interativa e gamificada chamada "A Jornada do Super-Nerd da TI".

A aplicação deve ser um único arquivo index.html, contendo todo o HTML, CSS e JavaScript necessários para funcionar.

1. Objetivo do Aplicativo:
Ensinar os fundamentos de hardware e redes de computadores de forma divertida e memorável, usando um formato de jogo com quadrinhos, tirinhas e piadas nerds. O conteúdo técnico a ser ensinado está no arquivo de texto que forneci em anexo.

2. Estrutura e Conteúdo:
O jogo deve ser dividido em módulos sequenciais, cobrindo os seguintes tópicos na ordem:

Módulo 1: Barramentos (O que são, tipos por função e aplicação).

Módulo 2: Hierarquia de Memória (Diferença entre Registradores, Cache, RAM e SSD).

Módulo 3: Fundamentos de Redes (LAN, MAN, WAN, Cliente-Servidor).

Módulo 4: Protocolos Essenciais (IP, TCP/UDP, HTTP/HTTPS, DNS, DHCP).

Módulo 5: Vantagens do CUDA (Computação Paralela com GPUs).

3. Formato Visual e Tom:

Estilo Visual: Minimalista, como tirinhas de quadrinhos (comics). Use divs, bordas e CSS para criar painéis. Não precisa de imagens complexas, pode usar emojis ou personagens simples feitos com CSS.

Tom: Humorístico e leve, cheio de piadas nerds e analogias engraçadas para explicar os conceitos. Por exemplo, o Barramento pode ser um super-herói chamado "Capitão Conexão".

Apresentação do Conteúdo: Cada conceito deve ser explicado através de diálogos curtos entre personagens em balões de fala, dentro das tirinhas.

4. Mecânica do Jogo:

Progressão: O usuário deve passar por cada módulo em ordem. Um módulo só é desbloqueado após a conclusão do anterior.

Interação: No final de cada módulo, apresente um questionário simples de múltipla escolha (2 ou 3 perguntas) para testar o conhecimento adquirido.

Feedback de Acerto: Ao selecionar a resposta correta, uma imagem ou um card de um super-herói genérico deve aparecer na tela com um balão de fala dizendo: "Você ganhou um bombom!". O jogo então avança para o próximo módulo.

Feedback de Erro: Ao selecionar uma resposta errada, deve aparecer a mensagem: "Continue tentando para ganhar o bombom.". A pergunta deve permanecer na tela até que o usuário acerte.

5. Especificações Técnicas:

Tecnologia: Use apenas HTML, CSS e JavaScript puros, sem a necessidade de frameworks externos.

Estrutura do Código: Todo o código deve ser contido em um único arquivo index.html, com o CSS dentro da tag <style> e o JavaScript dentro da tag <script>.

Persistência de Dados: Utilize o localStorage do navegador para salvar o progresso do usuário.

Crie uma chave no localStorage, por exemplo, progressoJornadaNerd.

Após o usuário completar o questionário de um módulo, atualize o valor dessa chave para indicar qual módulo foi concluído (ex: modulo_1_completo).

Ao carregar a página, o JavaScript deve verificar o localStorage e levar o usuário diretamente para o início do módulo em que ele parou.

6. Síntese do Conteúdo Anexado:
Você deve ler, interpretar e sintetizar o conteúdo técnico fornecido no arquivo de texto anexo. Transforme as explicações técnicas em diálogos curtos e divertidos para as tirinhas e crie as perguntas do questionário baseadas nesse conteúdo.

Exemplo de Fluxo para o Módulo 1:

Tela 1: Uma tirinha mostra um Processador (CPU) tentando gritar com uma Memória RAM que está longe. Eles não conseguem se comunicar.

Tela 2: Um personagem chamado "Bus Man" aparece e cria uma ponte (o barramento) entre eles.

Tela 3: Diálogo em balões de fala explicando de forma simples o que é um barramento.

Tela 4 (Questionário): Pergunta: "Qual via do barramento é usada para dizer ONDE os dados devem ser guardados?" (a) Barramento de Dados, (b) Barramento de Controle, (c) Barramento de Endereços.

Ação: Se o usuário clicar na (c), aparece o super-herói com a mensagem do bombom e o localStorage é atualizado. O Módulo 2 é liberado. Se errar, recebe a mensagem para tentar novamente.

Capriche na criatividade, no humor nerd e na clareza do código!
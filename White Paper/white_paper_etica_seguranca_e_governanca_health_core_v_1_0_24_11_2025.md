# WHITE PAPER – ÉTICA, SEGURANÇA E GOVERNANÇA DOS DADOS NO HEALTH CORE

**Versão:** 1.0  
**Data:** 24 de novembro de 2025  
**Contato:** suporte@healthcore.app (provisório)

> **Resumo em uma frase:** O Health Core é um aplicativo que organiza seu histórico de saúde e usa IA para gerar alertas e sugestões de especialidades, com controle total do paciente sobre os próprios dados, sem diagnóstico, sem venda de dados e com proteção forte de privacidade.

---

## 1) Para quem é este documento
- Para usuários, familiares e profissionais de saúde que querem entender **como protegemos e usamos dados**.  
- Para parceiros e investidores que desejam conhecer nossos **princípios e práticas**.  
- Linguagem simples, **sem termos jurídicos**, para evitar dúvidas.

---

## 2) Nossos princípios básicos
1. **O dado é do paciente.** Você manda nos seus dados.  
2. **Transparência.** Explicamos o que fazemos e por que fazemos.  
3. **Mínimo necessário.** Coletamos e usamos só o que realmente precisa.  
4. **Segurança forte.** Criptografia, controle de acesso e auditoria.  
5. **IA responsável.** Sem diagnóstico, sem prescrição. Sempre com revisão humana e base científica.  
6. **Sem discriminação.** Nunca usamos dados para prejudicar pessoas (ex.: preço maior de convênio).  
7. **Consentimento claro.** Você escolhe participar do modo Comunidade e pode sair quando quiser.

---

## 3) O que coletamos e por quê
**Dados de cadastro**: nome, e-mail, telefone.  
— Para criar sua conta e falar com você.

**Dados de saúde**: exames, laudos, cirurgias, alergias, condições crônicas, medicamentos de uso contínuo (registro), datas.  
— Para organizar seu histórico, gerar alertas e sugerir especialidades.

**Uso do app**: cliques, tempo de uso, erros.  
— Para melhorar estabilidade e experiência.

> **Importante:** Não pedimos informação desnecessária. Você pode **revisar e excluir** o que quiser.

---

## 4) O que NÃO fazemos (proibições claras)
- **Não damos diagnóstico.**  
- **Não prescrevemos medicamentos.**  
- **Não vendemos dados.**  
- **Não compartilhamos dados com convênios/seguradoras para calcular preço, negar cobertura ou perfilar risco.**  
- **Não liberamos seus dados sem sua autorização**, exceto quando a lei exigir (casos raros e específicos).  
- **Não usamos linguagem alarmista.**

---

## 5) Como protegemos seus dados (em termos simples)
- **Criptografia o tempo todo:**  
  - Em trânsito (quando os dados circulam) e em repouso (quando guardados).  
  - Padrões fortes (TLS 1.3, AES-256).  
- **Separação de dados:**  
  - Dados pessoais (nome, e-mail) ficam separados dos dados clínicos (resultados, laudos).  
- **Acesso controlado:**  
  - Somente pessoas autorizadas, quando necessário, e com registro (log).  
- **Auditoria e trilhas:**  
  - Você pode ver **quem acessou** o quê e quando, sempre que for um acesso compartilhado.  
- **Backups e continuidade:**  
  - Cópias de segurança com proteção e testes de recuperação.  
- **Testes de segurança:**  
  - Avaliações periódicas (testes de invasão e correções).

---

## 6) IA no Health Core: o que faz e como funciona
### 6.1 O que a IA faz
- Lê exames (OCR) e organiza informações.  
- Detecta **padrões repetidos** fora do normal.  
- Compara com **valores de referência** do próprio exame.  
- **Sugere especialidades** médicas para você considerar.  
- **Resume** laudos para facilitar a consulta com seu médico.

### 6.2 O que a IA **não** faz
- Não diagnostica, não receita, não substitui consulta.  
- Não define urgência médica. Em caso de sintomas graves, busque atendimento.

### 6.3 Como treinamos a IA (com sua escolha)
Temos três níveis de participação. Você escolhe e pode mudar a qualquer momento:

- **Nível 1 – Privacidade Máxima (padrão):**  
  Seus dados **não** entram no treinamento. Usamos só para o seu app.  

- **Nível 2 – Comunidade Health Core (opt-in):**  
  Você autoriza usar **dados anonimizados** (sem nome, sem documento) para treinar a IA e melhorar o app.  
  **Benefícios:** selo no perfil, temas exclusivos, acesso antecipado a recursos e **insights extras**.  

- **Nível 3 – Super Participante (futuro):**  
  Você participa de estudos e testes avançados (sempre anônimo). Recebe benefícios adicionais.

### 6.4 Como anonimização funciona (em palavras simples)
- Removemos informações como **nome, e-mail, telefone, CPF, endereço**.  
- Agrupamos por faixas (ex.: idade 31–35) e reduzimos detalhes que identificam.  
- Misturamos seus dados com os de muitos usuários (quando você aceitar).  
- O objetivo é que ninguém consiga **voltar** do dado agregado para você.

### 6.5 Caminho do futuro (preservando privacidade)
- **Federated Learning:** parte do treino no seu próprio celular; enviamos só ajustes do modelo, **não** seus dados brutos.  
- **Differential Privacy:** técnicas que “adicionam ruído” matemático para evitar reidentificação, mantendo utilidade estatística.

### 6.6 Transparência da IA
- Publicamos “**cartas do modelo**” (o que o modelo faz, dados aproximados usados, limitações).  
- Indicamos **quando** um insight veio de IA.  
- Mantemos histórico de versões e melhoria.

---

## 7) Seus controles (o que você pode fazer)
- **Ver e baixar** seus dados.  
- **Corrigir** informações.  
- **Excluir** dados e **apagar a conta**.  
- **Revogar acessos** dados a médicos e parceiros.  
- **Mudar** seu nível de participação na Comunidade.  
- **Pedir explicação** de qualquer recomendação da IA, em linguagem clara.

---

## 8) Compartilhamento e parcerias (com muito controle)
**Com quem podemos compartilhar?**  
- **Provedores de tecnologia** (ex.: nuvem) para rodar o serviço.  
- **Laboratórios/hospitais** apenas quando **você autorizar** integração para puxar exames automaticamente.  
- **Profissionais de saúde** que **você** escolher e autorizar.  

**Com quem não compartilhamos?**  
- **Convênios e seguradoras para precificação, negativa de cobertura ou perfil de risco.**  

**Como garantimos controle?**  
- Contratos que exigem segurança e proíbem reuso.  
- Acesso sempre **limitado ao necessário**.  
- **Revogação** simples pelo app.  
- **Registros de acesso** visíveis ao usuário quando houver compartilhamento.

---

## 9) Como funciona o acesso de médicos
- Você escolhe **quem** pode ver o quê.  
- **Escopos** de acesso (ex.: só exames, ou histórico completo).  
- **Tempo limitado** (ex.: 30 dias, renovável).  
- **Revogação** a qualquer momento.  
- **Registro** de visualização para transparência.

---

## 10) Retenção e eliminação de dados
- Guardamos seus dados **enquanto você usa** o app.  
- Você pode pedir **exclusão**. Backups seguem um ciclo de limpeza seguro.  
- Dados usados para treinar IA na **Comunidade** viram dados **agregados/anônimos**; quando possível, removemos amostras ainda não agregadas se você pedir. Explicaremos o que é tecnicamente possível em cada caso.

---

## 11) Incidentes de segurança (e como avisamos)
**O que é um incidente?** Vazamento, acesso indevido, perda ou alteração injustificada de dados.  
**O que fazemos:**  
- Investigamos de imediato.  
- Contemos o problema.  
- Informamos você e as autoridades quando necessário.  
- Explicamos o que aconteceu e o que faremos para evitar repetição.

---

## 12) Crianças e adolescentes
- O uso por menores exige **responsável legal**.  
- Contas de dependentes ficam **vinculadas** ao responsável, com controles adequados.

---

## 13) Governança interna (quem cuida do quê)
- **Encarregado de Privacidade (DPO):** ponto de contato sobre dados.  
- **Comitê de Ética em IA:** revisa modelos, riscos e linguagem.  
- **Segurança da Informação:** cuida de criptografia, acessos, testes, alertas.  
- **Clínico responsável:** valida conteúdos de saúde e diretrizes usadas pela IA.

---

## 14) Consentimento: como pedimos e como você muda de ideia
- Tela clara explicando **benefícios e riscos**.  
- **Opt-in** para a Comunidade (não vem marcado por padrão).  
- **Opt-out** simples: um clique para sair e parar de enviar dados para treinamento.  
- Opção de pedir **remoção** dos dados ainda não agregados do treino, quando tecnicamente possível.

---

## 15) Cenários comuns (respostas diretas)
- **“Meu convênio pediu meus dados.”**  
  Não fornecemos. Seus dados são seus. Você pode baixar e escolher o que compartilhar por conta própria, se quiser.  

- **“Um laboratório quer integrar com o Health Core.”**  
  Só com sua autorização. Você pode ligar/desligar a qualquer momento.  

- **“Quero que meu médico veja meus exames.”**  
  Você concede acesso limitado e com prazo. Pode revogar a qualquer momento.  

- **“Quero sair da Comunidade.”**  
  Um clique nas configurações. Paramos de usar seus novos dados para treino. Sobre dados antigos, removemos o que **não** estiver agregado, quando possível.

- **“Perdi o celular.”**  
  Seus dados continuam criptografados. Troque a senha e encerre sessões pelo site/app.  

- **“Quero excluir minha conta.”**  
  Você pode excluir pelo app. Backups seguem uma fila de exclusão segura.

---

## 16) Atualizações deste White Paper
- Avisaremos pelo app e por e-mail quando houver mudanças importantes.  
- Manteremos um **histórico de versões** com o que mudou e por quê.

---

## 17) Fale com a gente
- E-mail: **suporte@healthcore.app** (provisório)  
- No app: Menu → Ajuda → Privacidade

---

### Anexo A – Glossário simples
- **Anonimização:** tirar informações que identificam você.  
- **Agregado:** dados misturados de muitas pessoas, vistos como grupo.  
- **Criptografia:** técnica para guardar dados de modo que só quem tem permissão consegue ler.  
- **OCR:** tecnologia que lê texto em imagens/PDFs.  
- **Modelo de IA:** programa que aprende padrões a partir de dados.

### Anexo B – Resumo rápido (1 página)
- Dado é do paciente.  
- Sem venda de dados.  
- Sem diagnóstico/prescrição.  
- IA com participação opcional (Comunidade).  
- Criptografia forte e auditoria.  
- Acesso a médicos **só com autorização**.  
- Você pode ver, baixar, corrigir e excluir seus dados.  
- Sem dados para precificação de convênios.

### Anexo C – Modelos úteis
**Pedir cópia dos meus dados:**  
“Olá, quero baixar uma cópia dos meus dados do Health Core.”

**Excluir minha conta:**  
“Olá, quero excluir minha conta e meus dados no Health Core.”

**Sair da Comunidade:**  
“Olá, quero sair da Comunidade Health Core e parar de compartilhar meus dados para treinamento de IA.”

### Anexo D – Selo Comunidade Health Core (critérios e benefícios)
- **Como ganhar:** optar por compartilhar dados anonimizados para treinar a IA.  
- **Benefícios:** tema exclusivo, selo no perfil, recursos antecipados e insights extras.  
- **Como sair:** configurações → Privacidade → “Sair da Comunidade”. Benefícios são removidos e param novos envios.

---

> **Compromisso final:** O Health Core existe para ajudar você a cuidar da sua saúde com clareza e respeito. Seus dados são seus. Nosso trabalho é protegê-los e gerar valor para você e para a comunidade, sempre com ética.


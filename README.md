# Health Care

**O seu histórico de saúde, organizado e inteligente.**  
O **Health Care** centraliza exames, laudos, cirurgias e alergias em um só lugar e usa IA para **identificar padrões** e **sugerir qual especialista você deve procurar** — **sem diagnóstico** e **sem prescrição**. Segurança e privacidade são o nosso alicerce.

<p align="center">
  <img src="image/ia_saude.png" alt="Health Care — IA na Saúde" width="520">
</p>

[![Status](https://img.shields.io/badge/status-pre--MVP-blue)](#)
[![Privacidade](https://img.shields.io/badge/privacidade-centrada_no_paciente-0a7)](#)
[![IA Responsável](https://img.shields.io/badge/IA-respons%C3%A1vel-success)](#)

---

## Sumário
- [Health Care](#health-care)
  - [Sumário](#sumário)
  - [Visão em 10 segundos](#visão-em-10-segundos)
  - [🔒 Estratégia de Segurança e Repositórios](#-estratégia-de-segurança-e-repositórios)
  - [Diferenciais](#diferenciais)
  - [O que entregaremos no MVP](#o-que-entregaremos-no-mvp)
    - [App — Versão Paciente](#app--versão-paciente)
    - [Painel — Versão Médico (MVP Light)](#painel--versão-médico-mvp-light)
  - [Privacidade, Ética e IA responsável](#privacidade-ética-e-ia-responsável)
  - [Comunidade Health Care (opt-in)](#comunidade-health-care-opt-in)
  - [Roadmap](#roadmap)
    - [Fase 0 — Organização do repositório (higiene + segurança)](#fase-0--organização-do-repositório-higiene--segurança)
    - [Fase 1 — Estrutura Base (Backend + Banco)](#fase-1--estrutura-base-backend--banco)
    - [Fase 2 — Segurança mínima (autenticação/autorização)](#fase-2--segurança-mínima-autenticaçãoautorização)
    - [Fase 3 — MVP do MVP (registro manual de saúde)](#fase-3--mvp-do-mvp-registro-manual-de-saúde)
    - [Fase 4 — Ingestão de dados (upload + OCR)](#fase-4--ingestão-de-dados-upload--ocr)
    - [Fase 5 — Estruturação (texto → JSON utilizável)](#fase-5--estruturação-texto--json-utilizável)
    - [Fase 6 — Linha do tempo e insights mínimos](#fase-6--linha-do-tempo-e-insights-mínimos)
    - [Fase 7 — Exportação e compartilhamento com consentimento](#fase-7--exportação-e-compartilhamento-com-consentimento)
    - [Fase 8 — Confiabilidade, custos e operação](#fase-8--confiabilidade-custos-e-operação)
    - [Próximas fases (pós-MVP)](#próximas-fases-pós-mvp)
  - [Mercado \& Tese](#mercado--tese)
  - [Pitch (1 frase)](#pitch-1-frase)
  - [Modelo de Capitalização (do MVP à Plataforma)](#modelo-de-capitalização-do-mvp-à-plataforma)
    - [Camada 1 — B2C (porta de entrada e recorrência)](#camada-1--b2c-porta-de-entrada-e-recorrência)
    - [Camada 2 — B2B2C (ticket maior via “pré-consulta”)](#camada-2--b2b2c-ticket-maior-via-pré-consulta)
    - [Camada 3 — Plataforma (infraestrutura e escala)](#camada-3--plataforma-infraestrutura-e-escala)
  - [Cenários de Evolução (Conservador, Base e Otimista)](#cenários-de-evolução-conservador-base-e-otimista)
    - [Cenário 1 — Conservador (B2C forte, crescimento orgânico)](#cenário-1--conservador-b2c-forte-crescimento-orgânico)
    - [Cenário 2 — Base (B2C + pilotos B2B2C em paralelo)](#cenário-2--base-b2c--pilotos-b2b2c-em-paralelo)
    - [Cenário 3 — Otimista (B2B2C escala + Plataforma/Integrações)](#cenário-3--otimista-b2b2c-escala--plataformaintegrações)
  - [O que buscamos agora](#o-que-buscamos-agora)
  - [Roadmap Comercial (para investidores)](#roadmap-comercial-para-investidores)
    - [Fase A — MVP de Valor (0 → 1)](#fase-a--mvp-de-valor-0--1)
    - [Fase B — Recomendação de Especialidade com Guardrails (1 → 10)](#fase-b--recomendação-de-especialidade-com-guardrails-1--10)
    - [Fase C — Go-to-Market e Monetização Inicial (10 → 100)](#fase-c--go-to-market-e-monetização-inicial-10--100)
    - [Fase D — Trust \& Compliance como vantagem competitiva (100 → 1000)](#fase-d--trust--compliance-como-vantagem-competitiva-100--1000)
    - [Fase E — Escala, Integrações e Eficiência (1000+)](#fase-e--escala-integrações-e-eficiência-1000)
  - [Estrutura do repositório](#estrutura-do-repositório)

---

## Visão em 10 segundos
> **“Health Care organiza seu histórico de saúde e usa IA para te alertar quando algo no seu exame merece atenção e qual especialista você deve procurar.”**  
Simples. Forte. Direto.

---

## 🔒 Estratégia de Segurança e Repositórios

Para reduzir risco e evitar exposição desnecessária de código e segredos, adotamos uma estratégia de dois repositórios:

- **Health-Care (este — público):** documentação, White Paper, roadmap, materiais e transparência.
- **Health-Care-Develop (privado):** desenvolvimento principal (backend, frontend e IA), com controles de acesso.

**Como contribuir:**  
- Sugestões, melhorias e bugs: use a aba **Issues** deste repositório público.  
- Contribuições de código: via PR no repositório privado (processo guiado pelos mantenedores).

> Observação: este repositório público pode conter arquivos de apoio/rascunhos e PoCs — mas **não é** o “código de produção”.

---

## Diferenciais
- **Histórico completo** do paciente, não só exames isolados.  
- **IA orientada para especialidades** (sem diagnóstico, sem prescrição).  
- **Privacidade por padrão** — dados pertencem 100% ao paciente.  
- **Acesso médico com consentimento** e escopos limitados.  
- **White Paper público** de ética, segurança e governança.

---

## O que entregaremos no MVP

### App — Versão Paciente
- **Central de Saúde Pessoal:** alergias, doenças crônicas, cirurgias, medicamentos de uso contínuo (registro).  
- **Upload inteligente de exames:** foto/PDF → OCR → extração de campos essenciais → organização automática.  
- **Linha do tempo médica:** visão cronológica + evolução simples.  
- **Insights seguros:** detecção de padrões e **sugestão de especialidades** (ex.: cardiologia, endocrino).  
- **Alertas preventivos:** lembretes de acompanhamento, nada alarmista.  
- **Exportação rápida para consulta:** PDF com últimos exames e resumo.

### Painel — Versão Médico (MVP Light)
- **Acesso concedido pelo paciente** (revogável, com prazo e escopo).  
- **Dashboard clínico resumido:** alergias, condições crônicas, cirurgias, últimos exames.  
- **Sumarização de laudos por IA** para facilitar a consulta (sem decidir conduta).

---

## Privacidade, Ética e IA responsável
- **Sem venda de dados.**  
- **Sem compartilhamento com convênios/seguradoras** para precificação, negação de cobertura ou perfil de risco.  
- **Criptografia forte** (em trânsito e em repouso).  
- **Separação de dados pessoais x dados clínicos.**  
- **Auditoria e transparência:** histórico de acessos quando houver compartilhamento.  
- **IA com limites claros:** sem diagnóstico, sem prescrição, linguagem clara e não alarmista.

> Detalhes completos no nosso **White Paper** abaixo.

---

## Comunidade Health Care (opt-in)
Ajude você e o próximo a ter mais saúde 💙  
Ao optar por compartilhar **dados anonimizados** para treinar/avaliar melhorias (modo Comunidade), você:

- Recebe o **selo “Comunidade Health Care”**  
- Ganha **tema visual exclusivo** e **acesso antecipado** a recursos  
- Obtém **insights extras** e relatórios mais ricos

**Importante:**  
- Você pode **entrar ou sair a qualquer momento**.  
- **Nunca** compartilhamos dados individuais com convênios/seguradoras para precificação.  
- Avaliamos **Federated Learning** e **Differential Privacy** no roadmap para proteger ainda mais sua privacidade.

---

## Roadmap

> Abaixo está um roadmap **mais completo**, com **novas etapas** e **subetapas menores**.  
> (Sem diagnóstico e sem prescrição: o produto sugere especialidade e organiza dados.)

### Fase 0 — Organização do repositório (higiene + segurança)
- **0.1** Remover/evitar versionar ambientes virtuais (`env*`, `.venv`) e cache (`__pycache__`)
- **0.2** Padronizar nomes (ex.: `README.md` em vez de `readme.md`, se você quiser)
- **0.3** Criar arquivos básicos de governança:
  - `LICENSE.txt`
  - `SECURITY.md` (como reportar vulnerabilidades)
  - `CHANGELOG.md` (mudanças relevantes)
- **0.4** Checklist LGPD (requisitos não-funcionais):
  - retenção/deleção
  - logs sem PII
  - consentimento auditável

### Fase 1 — Estrutura Base (Backend + Banco)
- **1.1** Estrutura do backend (FastAPI) e organização de módulos
- **1.2** Banco PostgreSQL + migrações (ex.: Alembic)
- **1.3** Modelos iniciais:
  - `User`
  - `HealthRecord`
- **1.4** Padrão de erros e validações (422/400/401/403/404)
- **1.5** Testes mínimos (smoke + integração simples)

### Fase 2 — Segurança mínima (autenticação/autorização)
- **2.1** Registro e login
- **2.2** JWT e proteção de rotas
- **2.3** Autorização por proprietário do dado (user só acessa o que é dele)
- **2.4** Rate limit (login/upload) e proteção anti-bruteforce
- **2.5** Auditoria mínima (eventos de login e acesso a registros)

### Fase 3 — MVP do MVP (registro manual de saúde)
- **3.1** CRUD de `HealthRecord` (manual)
  - criar / listar / detalhar / atualizar (opcional) / deletar
- **3.2** Paginação e filtros (por data/tipo/tag)
- **3.3** Linha de base de qualidade:
  - validação de datas
  - limites de texto
  - padronização de unidades (quando aplicável)
- **3.4** Exportação simples (JSON) para conferência do paciente

### Fase 4 — Ingestão de dados (upload + OCR)
- **4.1** Endpoint de upload (PDF/Imagem) com:
  - limite de tamanho
  - validação de MIME
- **4.2** Armazenamento seguro (estrutura de pastas/bucket futuro)
- **4.3** OCR básico (texto bruto)
- **4.4** Persistir artefatos e metadados:
  - hash do arquivo
  - data de envio
  - status do processamento
- **4.5** Tratamento de falhas e reprocessamento

### Fase 5 — Estruturação (texto → JSON utilizável)
- **5.1** Limpeza do texto (remoção de ruído)
- **5.2** Extração de campos mínimos (exame/valor/unidade/data)
- **5.3** Validação do JSON (schema + sanity checks)
- **5.4** Revisão pelo paciente (“confirmar/corrigir antes de salvar”)
- **5.5** Versionamento do parser (rastrear mudanças)

### Fase 6 — Linha do tempo e insights mínimos
- **6.1** Linha do tempo (ordenação + agrupamento)
- **6.2** Regras simples para **sugestão de especialidade**
- **6.3** Explicabilidade do insight (“por que sugeriu”)
- **6.4** Guardrails de linguagem (não alarmista; sem urgência clínica)

### Fase 7 — Exportação e compartilhamento com consentimento
- **7.1** Consentimento explícito (escopo + prazo + revogação)
- **7.2** Trilha de auditoria de acessos
- **7.3** Exportação para consulta (PDF/resumo)
- **7.4** Acesso “somente leitura” para médico (MVP Light)

### Fase 8 — Confiabilidade, custos e operação
- **8.1** Jobs assíncronos (fila) para OCR/estruturação (quando necessário)
- **8.2** Observabilidade (logs/métricas) sem dados sensíveis
- **8.3** Backups + restore testado
- **8.4** Política de retenção e deleção (LGPD-friendly)

### Próximas fases (pós-MVP)
- Integração com laboratórios (com consentimento)
- Importação automatizada de exames
- IA avançada e explicabilidade mais rica
- Expansão internacional (conformidades locais)

**Status atual:** foco em **Fase 1 — Estrutura Base**.

---

## Mercado & Tese

**O problema (hoje):**
- O histórico de saúde do paciente é **fragmentado** (PDFs, fotos, apps diferentes, pastas no WhatsApp/e-mail).
- Em consultas, tempo é perdido “reconstruindo contexto” (exames antigos, comorbidades, alergias, medicamentos).
- Mesmo pacientes organizados sofrem com **baixa continuidade** do cuidado (documentos dispersos, troca de médicos, mudança de cidade/convênio).

**A tese do Health Care:**
- A maior alavanca inicial não é “diagnosticar” — é **organizar, sumarizar e tornar acionável** o histórico do paciente.
- **Sugestão de especialidade** (com guardrails) reduz fricção: ajuda o usuário a escolher o próximo passo sem prometer conduta clínica.
- “Trust” (privacidade + transparência) deixa de ser custo e vira **diferencial competitivo**, especialmente em saúde.

**Por que agora:**
- Usuários estão mais acostumados a digitalizar documentos (PDF/foto) e esperar experiências “inteligentes”.
- Modelos e pipelines de extração/estruturação evoluíram, permitindo entregar valor sem invadir o domínio de diagnóstico.
- Reguladores e o mercado pressionam por **governança, auditoria e consentimento** — o que favorece soluções privacy-by-design.

**Hipóteses de monetização (em validação):**
- **B2C:** assinatura para organização + timeline + exportações + insights básicos.
- **B2B2C:** clínicas/telemed com “pré-consulta” (intake) e resumo estruturado para apoiar a consulta.
- Upsell por recursos premium: múltiplos perfis familiares, armazenamento ampliado, exportações avançadas, integrações.

---
## Pitch (1 frase)

**Uma plataforma de infraestrutura de dados de saúde centrada no paciente** — que organiza histórico (exames, laudos, alergias, cirurgias), gera uma timeline inteligente e sugere **qual especialidade procurar**, com privacidade por padrão (**sem diagnóstico** e **sem prescrição**).

---

## Modelo de Capitalização (do MVP à Plataforma)

A capitalização do Health Care é pensada em camadas — começamos com valor imediato no B2C e escalamos com B2B2C e plataforma, mantendo o princípio de **dados pertencem ao paciente** e **compartilhamento só com consentimento**.

### Camada 1 — B2C (porta de entrada e recorrência)
**O que é:** app para o público geral organizar o histórico de saúde e transformar documentos soltos em informação utilizável.  
**Como monetiza:**
- **Assinatura (mensal/anual)** com freemium (limites no plano gratuito)
- **Planos família** (múltiplos perfis)
- Upsell por conveniência: exportações avançadas, armazenamento, automações

**Por que funciona:** histórico acumulado cria **lock-in** (quanto mais o usuário usa, mais valioso fica).

### Camada 2 — B2B2C (ticket maior via “pré-consulta”)
**O que é:** módulo para clínicas/telemed/profissionais com **pré-consulta estruturada** e **resumo do histórico** para apoiar atendimento (sem conduta).  
**Como monetiza:**
- Licença por profissional/clínica, ou
- Cobrança por consulta/paciente ativo, ou
- Pacotes de pilotos (design partners) com contrato recorrente

**Por que funciona:** gera ROI operacional (tempo de consulta + qualidade do contexto clínico).

### Camada 3 — Plataforma (infraestrutura e escala)
**O que é:** infraestrutura de **ingestão + estruturação + governança/consentimento**, podendo evoluir para integrações e APIs.  
**Como monetiza:**
- Modelo **usage-based** (por volume de documentos/processamento)
- Contratos enterprise (SLA, auditoria, compliance)
- Integrações com parceiros (sempre com consentimento do paciente)

**Por que funciona:** transforma o Health Care em “camada de confiança” do histórico do paciente — com defensabilidade em privacidade e governança.

> Nota: esta seção descreve **possibilidades estratégicas** do produto completo. Não são projeções financeiras nem promessa de resultados.

---

## Cenários de Evolução (Conservador, Base e Otimista)

Abaixo estão cenários ilustrativos para mostrar **como o Health Care pode se capitalizar ao longo do roadmap**, do MVP ao produto completo.

### Cenário 1 — Conservador (B2C forte, crescimento orgânico)
**Tese:** crescimento sustentado no público geral, com monetização principalmente por assinatura.  
**Como capitaliza:**
- Freemium → Pro (assinatura)
- Planos família como principal alavanca de ARPU
- Crescimento via conteúdo, indicação e comunidades

**O que precisa provar (métricas de produto):**
- Ativação: usuário sobe documentos e volta para consultar/exportar
- Retenção (D30) crescente conforme a timeline fica “completa”
- Uso recorrente de exportação para consultas

**Riscos:** CAC pode subir; mitigação via orgânico + referral + parcerias leves.

### Cenário 2 — Base (B2C + pilotos B2B2C em paralelo)
**Tese:** B2C valida valor e gera volume; B2B2C começa a gerar ticket maior e previsibilidade.  
**Como capitaliza:**
- Assinatura B2C como base
- Pilotos pagos com clínicas/telemed (pré-consulta + resumo)
- Pacotes recorrentes por volume/assento em parceiros iniciais

**O que precisa provar:**
- B2C: retenção + adoção do “resumo pré-consulta”
- B2B2C: redução de tempo de intake / maior satisfação do profissional
- Repetição do uso em clínicas (recorrência real)

**Riscos:** ciclo de venda B2B2C; mitigação via pilotos curtos e proposta de ROI clara.

### Cenário 3 — Otimista (B2B2C escala + Plataforma/Integrações)
**Tese:** Health Care vira referência de **histórico estruturado + governança**, escalando via parceiros e integrações.  
**Como capitaliza:**
- B2B2C escalado (contratos recorrentes)
- Integrações e “plugs” (telemed, laboratórios, ecossistema)
- Plataforma/API com cobrança por uso (documentos/processamento)

**O que precisa provar:**
- Unit economics positivos (custo por documento controlado vs receita por volume)
- Segurança/privacidade como diferencial percebido (confiança e auditoria)
- Escalabilidade operacional (fila, reprocessamento, qualidade contínua)

**Riscos:** maior exigência de compliance e qualidade; mitigação com privacy-by-design desde o início.

---

## O que buscamos agora

Estamos construindo o Health Care com foco em **valor rápido para o paciente** e **confiança para o ecossistema**. No curto prazo, buscamos:

- **Design Partners (pilotos):** clínicas, telemed e profissionais que queiram testar o “pré-consulta + resumo” (MVP Light) com feedback estruturado.
- **Primeiros usuários (beta):** pessoas dispostas a usar o app, subir documentos e avaliar a utilidade da timeline e da sugestão de especialidade.
- **Parcerias estratégicas:** laboratórios, plataformas de telemed, healthtechs complementares (integrações futuras, sempre com consentimento).
- **Apoio de investidores (pré-seed/seed):** para acelerar produto, segurança e go-to-market.

**O que oferecemos em troca (nesta fase):**
- Acesso antecipado ao roadmap e demos
- Canal direto com o time para priorização (feedback com impacto real)
- Transparência: métricas do beta, aprendizados e evolução do produto

> Se você quer participar como **Design Partner**, abra uma Issue com o título: **[Design Partner] Nome / Tipo (clínica, telemed, etc.)**.

---

## Roadmap Comercial (para investidores)

Este roadmap traduz a evolução do Health Care em **marcos de valor, tração e monetização**, com métricas sugeridas para acompanhamento.

> Reforço: o Health Care **não faz diagnóstico**, **não prescreve** e **não decide conduta**. O foco é **organizar**, **sumarizar** e **sugerir especialidade** com linguagem segura e guardrails.

### Fase A — MVP de Valor (0 → 1)
**Objetivo:** provar que o usuário consegue centralizar documentos e obter uma timeline confiável.

**Entregáveis**
- Upload de PDF/imagem + OCR quando necessário  
- Timeline e busca/filtros (por tipo, data, tags)  
- Exportação de resumo para consulta (PDF/JSON)

**Métricas sugeridas**
- Ativação: % de usuários que sobem ≥ 3 documentos na 1ª semana  
- Tempo “documento → timeline” (p50/p95)  
- Qualidade: % de documentos com data + tipo + campos mínimos extraídos  
- Retenção D7/D30

### Fase B — Recomendação de Especialidade com Guardrails (1 → 10)
**Objetivo:** aumentar valor percebido com sugestão rastreável e segura.

**Entregáveis**
- Sugestão de especialidade (regras + IA)  
- Explicabilidade (“por que sugeriu?”) baseada nos documentos do usuário  
- Feedback loop (“foi útil?” / “qual especialidade você procurou?”)  
- Controles de linguagem: não alarmista, sem urgência clínica

**Métricas sugeridas**
- Adoção da recomendação (% de usuários que visualizam/confirmam)  
- Taxa de “útil” por recomendação  
- Taxa de contestação (“não faz sentido”)  
- Redução do tempo até “decidir o próximo passo” (auto-relato)

### Fase C — Go-to-Market e Monetização Inicial (10 → 100)
**Objetivo:** validar canal e disposição a pagar.

**Estratégia de packaging (exemplo)**
- **B2C (assinatura):** organização + timeline + exportação + insights básicos  
- **B2B2C (clínicas/telemed):** intake pré-consulta + resumo estruturado (sem conduta)

**Métricas sugeridas**
- Conversão waitlist → cadastro → upload  
- Conversão free → pago  
- CAC (teste) e payback (estimado)  
- NPS / satisfação

### Fase D — Trust & Compliance como vantagem competitiva (100 → 1000)
**Objetivo:** tornar privacidade/segurança uma alavanca para parcerias.

**Entregáveis**
- Trilhas de consentimento (escopo/prazo/revogação) + auditoria  
- Política de retenção/deleção (LGPD-friendly)  
- Hardening e observabilidade sem PII  
- Governança de IA (avaliação, logs de decisão, limites)

**Métricas sugeridas**
- Incidentes (meta: 0) + tempo de resposta (simulado)  
- % de logs sem PII (meta: 100%)  
- Taxa de consentimento para compartilhamento com médico  
- Sucesso em auditorias internas/checklists

### Fase E — Escala, Integrações e Eficiência (1000+)
**Objetivo:** reduzir fricção e otimizar unit economics por documento.

**Entregáveis**
- Integrações (laboratórios/telemed) **com consentimento**  
- Importação automatizada (drive/e-mail) com trilha auditável  
- Otimização de custos (OCR/IA), fila e reprocessamento  
- Qualidade contínua (datasets sintéticos/anonimizados, testes de regressão)

**Métricas sugeridas**
- Custo por documento processado (OCR/IA)  
- Falhas/reprocessamento (%)  
- Latência p95 do pipeline  
- Retenção e expansão (multi-perfil familiar, etc.)

---

## Estrutura do repositório

> A árvore abaixo reflete a estrutura do seu `tree.txt`, mas **omitindo a listagem interna do `env31210/`** para não poluir o README.

```text
C:.
├── .gitignore
├── readme.md
├── tree.txt
├── backend
│   ├── main.py
│   ├── main.txt
│   └── main.txt.ipynb
├── conhecimento
│   ├── conhecimento_bibliotecas.txt
│   └── primeiros_passos.txt
├── Data
│   ├── tree.txt
│   ├── Docs
│   │   ├── HealthCore_Escopo_MVP.pdf
│   │   └── White Paper — Ética, Segurança E Governança _ Health Core (v1.0 – 24_11_2025).pdf
│   └── Image
│       └── IA Saude.png
├── env31210
│   └── (omitido: ambiente virtual local)
└── White Paper
    └── white_paper_etica_seguranca_e_governanca_health_core_v_1_0_24_11_2025.md

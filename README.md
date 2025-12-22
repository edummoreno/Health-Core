# Health Care

**Seu histórico de saúde, organizado e inteligente — centrado no paciente.**  
O **Health Care** centraliza exames, laudos, cirurgias e alergias em um só lugar e usa IA para **organizar informações**, **destacar pontos relevantes** e **sugerir qual especialidade médica procurar** — **sem diagnóstico** e **sem prescrição**. Privacidade e segurança são parte do produto, não um “extra”.

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
  - [O que é o Health Care](#o-que-é-o-health-care)
  - [Health Core x Health Care (nomenclatura)](#health-core-x-health-care-nomenclatura)
  - [🔒 Estratégia de Segurança e Repositórios](#-estratégia-de-segurança-e-repositórios)
  - [Diferenciais](#diferenciais)
  - [O que entregaremos no MVP](#o-que-entregaremos-no-mvp)
    - [App — Versão Paciente](#app--versão-paciente)
    - [Painel — Versão Médico (MVP Light)](#painel--versão-médico-mvp-light)
  - [Privacidade, Ética e IA responsável](#privacidade-ética-e-ia-responsável)
  - [Comunidade Health Care (opt-in)](#comunidade-health-care-opt-in)
  - [Mercado \& Tese](#mercado--tese)
  - [Pitch (1 frase)](#pitch-1-frase)
  - [Modelo de Capitalização (do MVP à Plataforma)](#modelo-de-capitalização-do-mvp-à-plataforma)
    - [Camada 1 — B2C (porta de entrada e recorrência)](#camada-1--b2c-porta-de-entrada-e-recorrência)
    - [Camada 2 — B2B2C (ticket maior via pré-consulta)](#camada-2--b2b2c-ticket-maior-via-pré-consulta)
    - [Camada 3 — Plataforma (infraestrutura e escala)](#camada-3--plataforma-infraestrutura-e-escala)
  - [Cenários de Evolução (Conservador, Base e Otimista)](#cenários-de-evolução-conservador-base-e-otimista)
    - [Cenário 1 — Conservador (B2C forte, crescimento orgânico)](#cenário-1--conservador-b2c-forte-crescimento-orgânico)
    - [Cenário 2 — Base (B2C + pilotos B2B2C)](#cenário-2--base-b2c--pilotos-b2b2c)
    - [Cenário 3 — Otimista (B2B2C escala + Plataforma/Integrações)](#cenário-3--otimista-b2b2c-escala--plataformaintegrações)
  - [O que buscamos agora](#o-que-buscamos-agora)
  - [Por que o Health Care não compete com ERPs de Saúde ou Plataformas como Laboratórios](#por-que-o-health-care-não-compete-com-erps-de-saúde-ou-plataformas-como-laboratórios)
    - [Health Care ≠ ERP de Saúde (ex.: TOTVS)](#health-care--erp-de-saúde-ex-totvs)
    - [Health Care ≠ plataforma de laboratório (ex.: Dasa)](#health-care--plataforma-de-laboratório-ex-dasa)
    - [Neutralidade como diferencial](#neutralidade-como-diferencial)
  - [Roadmap (para investidores)](#roadmap-para-investidores)
  - [Roadmap Técnico](#roadmap-técnico)
    - [Fase 0 — Organização do repositório](#fase-0--organização-do-repositório)
    - [Fase 1 — Estrutura Base (Backend + Banco)](#fase-1--estrutura-base-backend--banco)
    - [Fase 2 — Segurança mínima (authn/authz)](#fase-2--segurança-mínima-authnauthz)
    - [Fase 3 — Registro manual (MVP do MVP)](#fase-3--registro-manual-mvp-do-mvp)
    - [Fase 4 — Upload + OCR](#fase-4--upload--ocr)
    - [Fase 5 — Estruturação (texto → JSON)](#fase-5--estruturação-texto--json)
    - [Fase 6 — Timeline + insights](#fase-6--timeline--insights)
    - [Fase 7 — Exportação + consentimento](#fase-7--exportação--consentimento)
    - [Fase 8 — Operação (confiabilidade e custos)](#fase-8--operação-confiabilidade-e-custos)
    - [Pós-MVP](#pós-mvp)
  - [Estrutura do repositório](#estrutura-do-repositório)

---

## Visão em 10 segundos
> **“O Health Care organiza seu histórico de saúde, transforma documentos em uma timeline clara e sugere qual especialidade procurar — com privacidade por padrão (sem diagnóstico e sem prescrição).”**

---

## O que é o Health Care
- Um lugar único para **juntar e organizar** documentos de saúde (PDF/foto).
- Uma **timeline** clara para acompanhar evolução ao longo do tempo.
- IA para **sumarizar e estruturar** informações e **sugerir especialidade** (sem diagnóstico/prescrição).
- Compartilhamento com médico **só com consentimento**, com escopo, prazo e revogação.

---

## Health Core x Health Care (nomenclatura)
Você pode ver “**Health Core**” em alguns arquivos (PDFs/white paper) porque foi um **nome anterior do projeto**.  
O produto e a marca atual são **Health Care**. Estamos padronizando isso aos poucos sem quebrar nomes de arquivos e links existentes.

---

## 🔒 Estratégia de Segurança e Repositórios
Para reduzir risco e evitar exposição de código sensível/segredos, adotamos dois repositórios:

- **Health-Care (este — público):** documentação, White Paper, roadmap e materiais de transparência.
- **Health-Care-Develop (privado):** desenvolvimento principal (backend, frontend e IA), com controles de acesso.

**Como contribuir**
- Sugestões, melhorias e bugs: use **Issues** neste repositório público.
- Contribuições de código: via PR no repositório privado (processo guiado pelos mantenedores).

---

## Diferenciais
- **Histórico longitudinal** (não só exames isolados).
- **IA orientada à ação segura**: organizar, sumarizar e sugerir especialidade — sem diagnóstico.
- **Privacidade por padrão**: dados pertencem ao paciente, com consentimento explícito.
- **Transparência**: White Paper público de ética, segurança e governança.

---

## O que entregaremos no MVP

### App — Versão Paciente
- Cadastro do histórico (alergias, crônicos, cirurgias, medicamentos).
- Upload de exame/laudo (PDF/foto) → OCR quando necessário → estruturação básica.
- Timeline + busca/filtros.
- Insights seguros (padrões simples) + sugestão de especialidade.
- Exportação rápida (resumo para consulta).

### Painel — Versão Médico (MVP Light)
- Acesso **concedido pelo paciente** (revogável, com prazo e escopo).
- Visão resumida: alergias, crônicos, cirurgias, últimos exames.
- Sumarização de laudos por IA para facilitar consulta (sem decidir conduta).

---

## Privacidade, Ética e IA responsável
- **Sem venda de dados.**
- **Sem uso por convênios/seguradoras** para precificação, negação de cobertura ou perfil de risco.
- Criptografia (em trânsito e em repouso), logs sem PII e trilha de auditoria quando houver compartilhamento.
- IA com limites claros: linguagem não alarmista, sem urgência clínica, sem diagnóstico/prescrição.

---

## Comunidade Health Care (opt-in)
Modo opcional para compartilhar **dados anonimizados** para avaliar melhorias e qualidade do produto.

- Você entra e sai quando quiser.
- Nunca compartilhamos dados individuais com convênios/seguradoras para precificação.
- Avaliamos técnicas como **Federated Learning** e **Differential Privacy** no roadmap.

---

## Mercado & Tese
**Problema:** o histórico de saúde do paciente é fragmentado (PDFs, fotos, e-mails, apps diferentes). Em consulta, tempo é perdido reconstruindo contexto.  
**Tese:** valor real começa em **organizar e tornar o histórico acionável**, com confiança, governança e consentimento — sem “invadir” diagnóstico.  
**Por que agora:** digitalização de documentos e maturidade de pipelines de extração/estruturação permitem entregar valor com limites claros.

---

## Pitch (1 frase)
**Uma plataforma de infraestrutura de dados de saúde centrada no paciente** — que organiza histórico, cria uma timeline inteligente e sugere qual especialidade procurar, com privacidade por padrão (**sem diagnóstico** e **sem prescrição**).

---

## Modelo de Capitalização (do MVP à Plataforma)
A monetização evolui em camadas: começamos com valor direto para o público geral e escalamos com parceiros e integrações.

### Camada 1 — B2C (porta de entrada e recorrência)
- Assinatura (mensal/anual) com freemium (limites no gratuito).
- Planos família (múltiplos perfis).
- Upsell: exportações avançadas, automações, armazenamento e reprocessamento.

### Camada 2 — B2B2C (ticket maior via pré-consulta)
- Módulo “pré-consulta + resumo do histórico” para clínicas/telemed.
- Cobrança por assento, por consulta ou por paciente ativo (pilotos → recorrência).

### Camada 3 — Plataforma (infraestrutura e escala)
- Integrações e APIs (ingestão, estruturação, consentimento, auditoria).
- Cobrança por uso (volume de documentos/processamento) e contratos enterprise.

> Nota: isto descreve possibilidades estratégicas do produto completo (não é promessa financeira).

---

## Cenários de Evolução (Conservador, Base e Otimista)

### Cenário 1 — Conservador (B2C forte, crescimento orgânico)
- Receita principalmente por assinatura + planos família.
- Foco em retenção e valor recorrente (timeline + exportação pré-consulta).

### Cenário 2 — Base (B2C + pilotos B2B2C)
- B2C valida e cria base.
- Pilotos pagos com clínicas/telemed provam ROI e abrem caminho para contratos.

### Cenário 3 — Otimista (B2B2C escala + Plataforma/Integrações)
- Contratos recorrentes com parceiros + integrações.
- Plataforma usage-based com governança/consentimento como diferencial.

---

## O que buscamos agora
- **Usuários beta (público geral):** para validar uso real de upload, timeline e exportação.
- **Design partners (pilotos):** clínicas/telemed interessadas no módulo de pré-consulta e resumo.
- **Parcerias estratégicas:** integrações futuras (sempre com consentimento).
- **Investimento (pré-seed/seed):** para acelerar produto, segurança e go-to-market.

---

## Por que o Health Care não compete com ERPs de Saúde ou Plataformas como Laboratórios
Atuamos em camadas diferentes da cadeia de valor: **institucional** vs **centrado no paciente**.

### Health Care ≠ ERP de Saúde (ex.: TOTVS)
**ERPs/prontuários** são sistemas internos de clínicas/hospitais (agenda, faturamento, convênios, operação e prontuário).  
**Health Care** organiza o histórico do paciente ao longo da vida, atravessando instituições e facilitando o compartilhamento consentido.

> Se o ERP é o sistema operacional da clínica, o Health Care é o sistema operacional do paciente.

### Health Care ≠ plataforma de laboratório (ex.: Dasa)
Plataformas laboratoriais organizam muito bem os exames feitos no próprio ecossistema.  
O Health Care organiza **toda a vida clínica do paciente**, inclusive dados de fora: PDFs antigos, fotos, laudos, cirurgias, alergias e medicamentos.

> Timeline de laboratório é timeline de fornecedor. O Health Care é a timeline da vida do paciente.

### Neutralidade como diferencial
Não somos laboratório, clínica ou operadora. Isso permite neutralidade, governança e confiança — com consentimento explícito e auditável.

---

## Roadmap (para investidores)
Marcos de produto e tração — do MVP ao produto completo.

- **Fase A — MVP de Valor (0 → 1):** upload + timeline + exportação pré-consulta.
- **Fase B — Especialidade com Guardrails (1 → 10):** sugestão rastreável + explicabilidade + feedback loop.
- **Fase C — Monetização Inicial (10 → 100):** assinatura B2C + pilotos B2B2C (pré-consulta/resumo).
- **Fase D — Trust & Compliance (100 → 1.000):** auditoria, consentimento, retenção/deleção (LGPD-friendly), governança de IA.
- **Fase E — Escala e Integrações (1.000+):** integrações e APIs, otimização de custo por documento, eficiência operacional.

---

## Roadmap Técnico

### Fase 0 — Organização do repositório
- Higiene: ignorar env/cache, padronizar nomes, e arquivos de governança (LICENSE/SECURITY/CHANGELOG).
- Checklist LGPD: retenção/deleção, logs sem PII, consentimento auditável.

### Fase 1 — Estrutura Base (Backend + Banco)
- FastAPI organizado por módulos + PostgreSQL + migrações.
- Modelos iniciais (`User`, `HealthRecord`) + validações + testes mínimos.

### Fase 2 — Segurança mínima (authn/authz)
- Registro/login + JWT.
- Autorização por proprietário do dado + rate limit e auditoria mínima.

### Fase 3 — Registro manual (MVP do MVP)
- CRUD de HealthRecord (manual) + paginação/filtros.
- Exportação simples (JSON) para conferência do paciente.

### Fase 4 — Upload + OCR
- Upload PDF/imagem com validações e limites.
- OCR básico + metadados (hash, status, data) + reprocessamento.

### Fase 5 — Estruturação (texto → JSON)
- Limpeza de texto + extração de campos mínimos + schema/sanity checks.
- Revisão pelo paciente antes de salvar + versionamento do parser.

### Fase 6 — Timeline + insights
- Timeline (ordenação/agrupamento).
- Regras simples de sugestão de especialidade + explicabilidade + guardrails.

### Fase 7 — Exportação + consentimento
- Consentimento explícito (escopo/prazo/revogação) + trilha de auditoria.
- Exportação para consulta + acesso read-only no painel médico.

### Fase 8 — Operação (confiabilidade e custos)
- Jobs/fila para OCR/estruturação.
- Observabilidade sem dados sensíveis + backups/restore testado.
- Política de retenção e deleção.

### Pós-MVP
- Importação automatizada, integrações (com consentimento), IA mais rica com explicabilidade e expansão por conformidade local.

**Status atual:** foco em **Fase 1 — Estrutura Base**.

---

## Estrutura do repositório
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

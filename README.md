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

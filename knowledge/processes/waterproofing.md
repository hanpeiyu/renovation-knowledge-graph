---
schema_version: "0.1.0"
id: PROC-WATERPROOF-0001
type: process
title: 涂膜防水施工工艺
status: draft
summary: 以选定涂膜材料按适用技术要求施工并形成防水层的技术过程。
scope: {domain: 室内装修, caveat: 不指定任何产品的加水量或遍数}
relations:
  - {kind: has_step, target: STEP-MIX-0001}
  - {kind: has_step, target: STEP-COAT-0001}
  - {kind: has_step, target: STEP-WAIT-0001}
---

# 涂膜防水施工工艺

流程仅为抽象示例；配制、重涂、养护、验收须按具体产品和适用标准决定。
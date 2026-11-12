---
schema_version: "0.1.0"
id: CFG-WATERPROOF-TWO-0001
type: process_configuration
title: 涂膜防水两遍涂刷配置（示例）
status: unverified
summary: 用于演示遍数参数与工序关系的抽象配置，非任何产品的施工要求。
scope: {domain: 涂膜防水, applicable_product: 未指定, instruction: 不得直接用于施工}
parameters: {coat_count: 2, total_consumption: null, target_dry_film_thickness: null, waiting_condition: 待由产品说明定义}
relations:
  - {kind: configures, target: PROC-WATERPROOF-0001}
  - {kind: requires_object, target: MAT-WATERPROOF-0001}
---

# 两遍涂刷参数示例

两遍并不自动代表用料双倍、达到合格膜厚或质量更好。需对总用量、每遍用量、型号和现场条件分别建模。
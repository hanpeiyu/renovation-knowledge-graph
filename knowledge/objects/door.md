---
schema_version: "0.1.0"
id: OBJ-DOOR-0001
type: physical_object
title: 室内门
status: draft
summary: 室内空间中用于分隔和通行控制的门类实物概念。
scope: {domain: 室内装修, specificity: 通用概念}
relations:
  - {kind: has_part, target: OBJ-LOCK-0001, note: 适用于采用门锁的配置}
  - {kind: has_part, target: OBJ-HINGE-0001, note: 适用于采用合页的平开门配置}
---

# 室内门

此卡只描述通用实物边界；并非所有门都配置同一种锁或合页。安装与交付参见对应独立卡。
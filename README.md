# 装修工程知识图谱 · Renovation Knowledge Graph

**状态：架构与样板 V0.1（草案） · 2026-11-12**

以住宅装修为起点，建立可追溯、可复用、可扩展的工程知识体系，支持日后拓展到其他室内装修领域。

这里不是“把问答写成一堆文章”的百科。底层将产品、部件、材料、工艺、工序、配置、性能、证据、成本、工作与交付成果作为独立知识对象，通过有类型、可追溯、带适用条件的关系组合回答问题。

## 入口

- [今日讨论的完整决策与待办](docs/discussion-summary-2026-11-12.md)
- [架构原则](ARCHITECTURE.md)
- [知识对象与关系模型](docs/domain-model.md)
- [证据与推理规范](docs/evidence-and-reasoning.md)
- [工艺、工序、配置、执行与交付](docs/process-delivery.md)
- [成本、激励和选购决策](docs/cost-and-decisions.md)
- [客户、设计师与研究者的展示](docs/presentation.md)
- [AI 撰写、质量检查和 PR 审核](docs/authoring-workflow.md)
- [授权、署名与引用](docs/licensing-and-attribution.md)
- [知识类型词表](ontology/types.yaml) / [关系词表](ontology/relations.yaml)
- [知识卡片模板](templates/node.md) / [论点模板](templates/claim.md)
- [“门的供货安装”样板](examples/door-supply-install.md)
- [“防水工序与推理”样板](examples/waterproofing.md)
- [架构决策 ADR-0001](docs/adr/0001-github-first.md)
- [AI 协作指引](AGENTS.md)

## 设计底线

1. **知识与问题分离**：用户问“为什么只刷一遍防水”，不意味着要创造一个名为“为什么只刷一遍”的永久节点。
2. **对象与角色分离**：门锁是对象，单卖是产品、装在门上是部件；这取决于关系和场景。
3. **定义与执行分离**：防水工艺、工序、施工参数、工艺配置和现场执行记录不能混为一谈。
4. **产品与交付分离**：门、安装门、安装合格的门、供货安装合同项不是同一个对象。
5. **结论有边界**：成本、性能、风险与因果必须注明适用条件和证据，不允许把可能性写成已证实的事实。
6. **证据可复用**：一份原始报告可支持多个论点，但转述同一报告的多个网站不能当作多份独立证据。

## 当前状态

此提交是架构草案、词表、最小可运行结构校验和**示例知识节点**；示例不构成施工建议、真实报价或已验证的工程性能声明。正式知识需逐条经过证据审核。现场施工始终以现行适用标准和具体产品技术文件为准。

## 贡献与许可

原创知识文档与原创图文拟采用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)；引用时应给予适当署名并提供来源、许可和修改说明。代码另按 [MIT 许可](LICENSE-CODE) 使用。第三方原文、图片、标准全文与受限制材料不因被引用而自动获得本仓库许可。详见 [授权与署名规范](docs/licensing-and-attribution.md) 和 [许可证说明](LICENSE)。

项目署名：**hanpeiyu**（GitHub 账号）。
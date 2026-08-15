---
status: working
version: 0.1
baseline_date: 2026-08-15
owner: research
---

# Standards Baseline

## 纳入规则

每项来源至少记录唯一 ID、准确版本、发布者、层级、适用范围、官方定位和条款级精读状态。正式规范结论必须能够追溯到合法取得的原文；官方公开摘要只用于版本和范围确认。

| ID | Standard | Layer | Baseline status | Official metadata | Full-text review |
|---|---|---|---|---|---|
| STD-ISO15288-2023 | ISO/IEC/IEEE 15288:2023, *Systems and software engineering — System life cycle processes* | 通用系统生命周期 | active | ISO，Edition 2，2023-05，Published | pending |
| STD-ARP4754B | SAE ARP4754B, *Guidelines for Development of Civil Aircraft and Systems* | Aircraft/System Development Assurance | active | SAE，Revised 2023-12-20，DOI 10.4271/ARP4754B | pending |
| STD-ARP4761A | SAE ARP4761A / EUROCAE ED-135 | System Safety | queued | 待官方元数据复核 | pending |
| STD-DO178C | RTCA DO-178C / EUROCAE ED-12C | Software Item Assurance | queued | 待官方元数据复核 | pending |
| STD-DO254 | RTCA DO-254 / EUROCAE ED-80 | Electronic Hardware Assurance | queued | 待官方元数据复核 | pending |
| STD-DO297 | RTCA DO-297 / EUROCAE ED-124 | IMA Assurance | queued | 待官方元数据复核 | pending |

## 官方入口

- ISO/IEC/IEEE 15288:2023: https://www.iso.org/standard/81702.html
- SAE ARP4754B: https://saemobilus.sae.org/standards/arp4754b-guidelines-development-civil-aircraft-systems
- SAE ARP4754B DOI: https://doi.org/10.4271/ARP4754B

## 分层解释

- ISO 15288 提供跨领域的系统生命周期过程框架，不规定特定开发方法、建模方法或验证技术。
- ARP4754B 面向民用航空 aircraft/system development，公开范围明确包含 requirements validation 与 design implementation verification，并把软件、电子硬件、IMA 和安全评估的详细过程分别指向相应文件。
- 后续标准加入时必须保留适用层级，尤其不得把 DO-178C 的软件结构覆盖概念无条件上移到系统层。

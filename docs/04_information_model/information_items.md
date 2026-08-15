---
status: working
version: 0.1
baseline_date: 2026-08-15
owner: research
---

# Verification Information Items V0.1

## 核心对象

Requirement、Verification Obligation、Assurance Objective、Verification Strategy、Verification Activity、Method、Technique、Case、Procedure、Environment、Configuration、Stimulus、System State、Expected Result、Observed Result、Oracle、Coverage Obligation、Coverage Result、Evidence、Anomaly、Change、Regression Activity、Compliance Claim。

## 核心关系

```text
Requirement → creates → Verification Obligation
Verification Obligation → satisfiedBy → Verification Strategy
Verification Strategy → selects → Level / Method / Technique
Verification Strategy → defines → Coverage Obligation / Required Evidence
Verification Case → realizes → Verification Strategy
Procedure → implements → Verification Case
Execution → produces → Evidence
Evidence → supports → Compliance Claim
```

## 稳定 ID 前缀

| Object | Prefix | Example |
|---|---|---|
| Standard source | STD | STD-ARP4754B |
| Activity | ACT | ACT-V03-001 |
| Verification obligation | VOB | VOB-0001 |
| Verification strategy record | VSR | VSR-0001 |
| Pattern | PAT | PAT-BVA-01 |
| Coverage obligation | COV | COV-REQ-01 |
| Claim | CLAIM | CLAIM-0001 |
| Evidence | EVD | EVD-0001 |

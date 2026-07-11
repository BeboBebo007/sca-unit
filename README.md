# SCA-Unit

**SCA-Unit** is a structural assessment prototype designed to compare
two system representations as structures rather than as isolated values.

It accepts two structural descriptions in JSON format and produces a
deterministic assessment report containing:

- Node similarity
- Edge similarity
- Structural compatibility
- Shared-domain conflict
- A structural verdict

The current public prototype intentionally excludes proprietary
structural consolidation, optimization, self-evolution, and protected
decision mechanisms.

---

## Current Version

```text
0.3.0
` 

## Local Demo Package

Run the local browser demo with:

```powershell
.\run_demo.ps1
```

The demo opens http://127.0.0.1:8765 and uses SCA_UNIT_API_KEY from .env.local.



## Demo Examples

Use these files for a quick browser demo:

- demo_examples/baseline_user.json
- demo_examples/changed_user.json

Paste baseline_user.json into the first JSON box and changed_user.json into the second JSON box, then click Compare structures.




## First-time setup after extraction

Before running the demo, create a local environment file named `.env.local` in the project root:

```text
SCA_UNIT_API_KEY=sca-unit-demo-key-2026-secure-local-001
```

This file is intentionally excluded from the public ZIP package.


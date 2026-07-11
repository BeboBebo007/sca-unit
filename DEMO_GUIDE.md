# SCA-Unit Demo Guide

## Goal

This demo shows how SCA-Unit detects structural changes between two JSON documents.

## Start the demo

```powershell
.\run_demo.ps1
```

Open the browser page at:

```text
http://127.0.0.1:8765
```

## Demo input files

Use:

- demo_examples/baseline_user.json
- demo_examples/changed_user.json

Paste baseline_user.json into the first JSON box.
Paste changed_user.json into the second JSON box.

Click:

```text
Compare structures
```

## Expected result

The report should show a partial structural change because the second document adds:

```text
user.roles
```

You can then download the report as JSON or HTML.

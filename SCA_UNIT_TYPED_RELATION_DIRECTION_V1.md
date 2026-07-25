# SCA-Unit Typed Relation Direction v1.0

## Purpose
Define the first technical direction for moving SCA-Unit beyond raw set similarity.

## Direction status
Typed relation direction selected.

## Problem with current edge comparison
Current edge comparison mainly checks whether relationships are present or absent. This is useful but shallow.

## Selected improvement
Typed Relation Conflict Engine.

## Core idea
A relation should be treated as a structured entity, not only as a pair of nodes.

## Relation fields to support later
- source
- target
- relation type
- direction
- required status
- weight
- constraint
- version
- evidence reference

## Conflict types to support later
- missing relation
- added relation
- changed relation type
- reversed direction
- required relation removed
- optional relation changed
- constraint mismatch
- weight change
- version conflict

## Why this matters
Two systems may have the same raw Jaccard score while one remains structurally compatible and the other contains a serious typed-relation conflict.

## First implementation target
Detect changed relation type and reversed direction inside the shared node domain.

## Expected user value
The report should explain not only that structures differ, but why a relationship-level change may matter.

## SCA-Audit Lite connection
This typed relation engine will later support project audit reports by identifying meaningful architecture, dependency, or configuration relationship conflicts.

## Boundary
This file defines direction only. It does not yet implement the engine.

## Final direction result
Typed relations are selected as the first technical upgrade path beyond basic Jaccard-style comparison.

## Next milestone
Typed Relation Conflict Engine Specification v1.

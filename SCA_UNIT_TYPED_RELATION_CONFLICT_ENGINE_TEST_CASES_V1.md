# SCA-Unit Typed Relation Conflict Engine Test Cases v1.0

## Purpose
Define deterministic test cases for the future Typed Relation Conflict Engine.

## Test case status
Specification-level test cases only.

## Background
These cases prepare the first implementation step for typed relation conflict detection without adding runtime code yet.

## Minimal typed relation format
A typed relation should include:
- source
- target
- type
- required

## Case 1: relation_type_changed

### First structure relation
{
  "source": "api",
  "target": "database",
  "type": "depends_on",
  "required": true
}

### Second structure relation
{
  "source": "api",
  "target": "database",
  "type": "writes_to",
  "required": true
}

### Expected conflict
relation_type_changed

### Expected explanation
The relation between api and database exists in both structures, but its type changed from depends_on to writes_to.

## Case 2: relation_direction_reversed

### First structure relation
{
  "source": "api",
  "target": "database",
  "type": "depends_on",
  "required": true
}

### Second structure relation
{
  "source": "database",
  "target": "api",
  "type": "depends_on",
  "required": true
}

### Expected conflict
relation_direction_reversed

### Expected explanation
The relation direction changed from api -> database to database -> api inside the shared node domain.

## Case 3: required_relation_removed

### First structure relation
{
  "source": "auth",
  "target": "user_store",
  "type": "requires",
  "required": true
}

### Second structure relation
No matching relation exists.

### Expected conflict
required_relation_removed

### Expected explanation
A required relation from auth to user_store exists in the first structure but is missing from the second structure.

## Case 4: required_status_changed

### First structure relation
{
  "source": "payment",
  "target": "ledger",
  "type": "writes_to",
  "required": true
}

### Second structure relation
{
  "source": "payment",
  "target": "ledger",
  "type": "writes_to",
  "required": false
}

### Expected conflict
required_status_changed

### Expected explanation
The relation between payment and ledger kept the same source, target, and type, but changed required status from true to false.

## Case 5: no_conflict_same_relation

### First structure relation
{
  "source": "frontend",
  "target": "api",
  "type": "calls",
  "required": true
}

### Second structure relation
{
  "source": "frontend",
  "target": "api",
  "type": "calls",
  "required": true
}

### Expected conflict
none

### Expected explanation
The typed relation is unchanged.

## First implementation expectation
The first implementation should detect the four conflict types deterministically and preserve no-conflict behavior for unchanged typed relations.

## Compatibility expectation
Existing simple edge-based examples should continue to work after typed relation support is added.

## Boundary
This file defines test cases only. It does not implement the engine.

## Final test case result
The Typed Relation Conflict Engine now has clear deterministic cases for the first implementation.

## Next milestone
Typed Relation Conflict Engine Minimal Implementation v1.
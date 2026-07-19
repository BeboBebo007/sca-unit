# SCA-Unit Structural Assessment Engine Public Overview v1.0

## Purpose
Provide a public overview of SCA-Unit as a JSON-first Structural Assessment Engine.

## Public overview status
Structural Assessment Engine public overview.

## Core definition
SCA-Unit is a Structural Assessment Engine that compares two structured states and produces a deterministic structural compatibility assessment.

## Current implementation
The current public implementation is JSON-first. It accepts two JSON structural state files and produces a structured report with similarity, compatibility, conflict, and verdict signals.

## Why this is not a generic diff tool
A generic diff tool compares text lines or file changes. SCA-Unit compares structural representations and focuses on relationships, compatibility, and structural change.

## Current input model
The current input model is a JSON structural state containing:
- identity
- nodes
- edges

## Current output model
The current output model may include:
- node similarity
- edge similarity
- structural compatibility
- shared-domain conflict
- structural verdict

## Primary use cases
SCA-Unit can support:
- software migration review
- integration review
- structured system comparison
- configuration evolution review
- architecture change assessment
- manual Structural Report generation

## Evidence direction
SCA-Unit output should help users understand why two structured states appear compatible, partially compatible, or incompatible.

## JSON-first boundary
JSON is the current public execution format. Additional formats such as YAML, OpenAPI, graphs, and data schemas are future extension directions, not current public execution promises.

## Service boundary
SCA-Unit provides a structural comparison report. It is not intended to replace legal, financial, medical, cybersecurity, compliance, or full audit advice.

## Public language rule
Public documentation should focus on documented functionality, current implementation scope, and clear user value.

## Final overview result
SCA-Unit is externally described as a JSON-first Structural Assessment Engine with a clear current scope and future extension direction.

## Next milestone
SCA-Unit README Structural Engine Positioning Update v1.

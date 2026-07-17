# SCA-Unit v0.4.0 Public Release Note

## Release summary
SCA-Unit v0.4.0 is a public Python package for structural compatibility assessment between two structured software or logical states.

## What is new in this public/product phase
- Published package on PyPI
- Clear CLI usage
- Public examples directory
- README product positioning
- Sample structural report
- Automated paid report generator
- Service-like paid report workflow

## Public value
SCA-Unit helps users compare structural states and understand whether two versions, systems, or logical structures remain compatible.

## Install
pip install sca-unit==0.4.0

## Quick example
sca-unit examples/example_system_v1.json examples/example_system_v2.json --output examples/example_raw_report.json

## Paid report foundation
The public tool can support generated structural compatibility reports without exposing protected internal architecture.

## Safety boundary
This release does not expose AMNE internals or protected structural architecture.

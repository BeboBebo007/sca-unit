# SCA-Unit Move Service Records from Root v1.0

## Purpose
Record the controlled movement of service, customer, paid-report, intake, delivery, correction, rejection, feedback, and first-revenue Markdown files into docs/service_records/.

## Movement status
Service records moved from repository root.

## Destination
docs/service_records/

## Movement method
git mv

## Scope
Only service-operation and customer-workflow records were moved.

## Boundary
This milestone does not delete files.

## README link handling
README links were reviewed and updated where matching moved file names were found.

## Public surface value
This significantly reduces the number of commercial and operational Markdown files visible at the repository root.

## Safety rule
No project history was deleted.

## Not included
- archive record movement
- code change
- package build
- PyPI upload
- real customer data

## Final movement result
Service records are organized under docs/service_records/.

## Next milestone
Move Archive Records from Root v1.
# SCA-Unit MVP Specification



## Product Name



SCA-Unit Structural Compatibility Assessment



## Product Objective



Provide a controlled service that compares two structural descriptions and returns a clear compatibility assessment without exposing protected algorithms or internal intellectual property.



## Target Users



- Software developers

- Systems engineers

- Technical research teams

- Data and architecture analysts

- Organizations comparing system structures



## MVP Inputs



The first commercial version accepts two JSON files containing:



- Structure identity

- Node definitions

- Edge definitions

- Structural metadata



## MVP Outputs



The service returns:



- Node similarity

- Edge similarity

- Overall compatibility score

- Conflict score

- Compatibility verdict

- Engine version

- Report schema version



## MVP Workflow



1\. The user uploads two structural JSON files.

2\. The public interface validates the file format.

3\. The files are sent securely to the private server.

4\. The server performs the permitted assessment.

5\. A structured report is returned.

6\. The user views or downloads the report.



## Public Components



The public product may contain only:



- Input validation

- Authentication

- Secure request submission

- Report presentation

- Export functions

- Non-proprietary examples



## Private Components



The private server contains:



- Protected assessment engine

- Proprietary formulas

- Internal decision logic

- Optimization mechanisms

- Adaptive mechanisms

- Audit and usage controls



## Initial Commercial Model



- Private demonstrations

- Limited pilot accounts

- Subscription-based access

- Usage-based plans

- No offline protected engine distribution



## MVP Success Criteria



The MVP is considered ready when:



- Valid JSON files are accepted

- Invalid inputs are rejected clearly

- Assessments are reproducible

- Reports are generated successfully

- Protected source code remains server-side

- Every request is logged

- Tests pass in a clean environment



## Current Status



The local prototype and release candidate are validated.



The hosted commercial separation has not yet been implemented.


# SCA-Unit Commercial Architecture



## Objective



Provide SCA-Unit as a commercial service without distributing the protected engine source code.



## Architecture



### Private Server



The private server contains:



- Protected structural assessment engine

- Proprietary algorithms and formulations

- Authentication and authorization

- Usage limits and subscription controls

- Audit logging

- Version control for the protected engine



This component must never be distributed to customers.



### Public Client



The customer-facing client may contain only:



- Input validation

- Secure request submission

- Authentication token handling

- Result retrieval

- Result presentation

- Non-proprietary examples



The public client must not contain protected decision logic.



## Execution Flow



1\. The customer submits structural input.

2\. The public client validates the input format.

3\. The request is transmitted securely to the private server.

4\. The protected engine performs the assessment.

5\. The server returns only the permitted result.

6\. The client displays or exports the result.



## Security Boundary



The private server must not return:



- Internal formulas

- Intermediate protected states

- Candidate generation data

- Optimization parameters

- Adaptive weighting values

- Internal decision traces

- AMNE mechanisms

- Unpublished patent material



## Commercial Delivery



The preferred delivery model is:



- Hosted software service

- Account-based access

- Subscription or usage-based billing

- Private demonstrations for selected customers



Offline distribution requires a separate protection review.



## Release Rule



No commercial release is authorized until the public client and private engine are technically separated and independently tested.


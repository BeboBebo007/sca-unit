# SCA-Unit Server Readiness

This document describes the minimum requirements for running SCA-Unit on a private server.

## Current status

- Public demo package is ready
- Local demo is verified
- Independent install is verified
- Independent demo run is verified

## Before production

- Use a strong private API key
- Do not expose .env.local
- Run behind a reverse proxy if exposed online
- Use HTTPS for public access
- Keep this prototype as a controlled private service first

## Recommended next deployment mode

Private VPS test deployment before public production.

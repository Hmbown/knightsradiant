# Security Policy

## Reporting

If you find a security issue in this repo, especially involving:
- installer behavior
- unsafe profile mutation
- supply-chain risks in installation guidance
- misleading or dangerous Hermes configuration advice

please report it privately to the maintainer before public disclosure.

Until a dedicated security mailbox exists, open a private GitHub security advisory if available for the repository.

## Scope

This project is mostly documentation, prompts, and shell/Python install helpers. Relevant security issues still include:
- path handling bugs
- dangerous shell behavior
- accidental secret exposure in docs or profile templates
- unsafe recommendations that could cause destructive Hermes behavior

## Expectations

- do not publish working exploit details before the maintainer has a reasonable chance to patch
- include reproduction steps, affected files, and expected impact
- prefer minimal proof of concept over noisy demonstration

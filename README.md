# Supraj.dev Banner Generator

A reusable editorial banner-generation skill for Supraj.dev.

Provide a technical topic — or, even better, the article itself — and the skill turns it into a technically meaningful visual concept plus production-ready prompts for:

- blog thumbnails
- article hero banners
- OG/social cards

The generator is designed for AI Engineering, AI Agents, Cloud, Kubernetes, DevOps, MLOps, Security, Architecture, and GPU/AI Infrastructure content.

## Repository layout

```text
banner-generator/
├── README.md
├── SKILL.md
├── references/
│   ├── visual-language.md
│   ├── category-rules.md
│   └── examples.md
└── scripts/
    └── validate-banner-spec.py
```

Because this repository itself is the skill package, there is intentionally no extra nested `supraj-banner-generator/` directory.

## Minimal usage

A topic alone is sufficient:

```text
Topic: Kubernetes TLS Certificates
```

or:

```text
Topic: CUDA Explained
Asset: all
```

The skill must understand the subject, propose three meaningful visual directions, select the strongest one, and produce related-but-distinct prompts for thumbnail, article hero, and OG/social assets.

## Best-quality usage

When available, give the skill the article Markdown or a detailed article summary as well as the topic. The generator should then visualize the **specific angle of the article**, rather than creating generic artwork for the broad technology.

Example:

```text
Topic: Kubernetes TLS Certificates
Asset: all

Article:
<article markdown here>
```

## Design principle

One article should have **one strong visual concept expressed in multiple compositions**, rather than one generic image cropped everywhere or three unrelated images.

The target quality bar is a serious engineering publication — not generic AI-generated blog art.

## Output validation

Save a generated text specification and run:

```bash
python scripts/validate-banner-spec.py banner-output.txt
```

The validator checks that the skill returned all required sections, asset prompts, avoid lists, and final PASS/FAIL quality checks.

## Important boundary

This repository defines the **creative reasoning and prompt-generation layer**. Image generation can be connected later as a separate execution step, allowing us to swap image models/tools without rewriting the editorial art-direction system.

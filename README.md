# Supraj.dev Banner Generator

A reusable editorial banner-generation skill for Supraj.dev.

The goal is simple: provide a technical topic (or optionally an article), and the skill turns it into a meaningful visual concept plus production-ready prompts for:

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

## Intended usage

Minimal input is enough:

```text
Topic: Kubernetes TLS Certificates
```

or:

```text
Topic: CUDA Explained
Asset: all
```

The skill is expected to understand the technical subject, propose three meaningful visual directions, choose the strongest one, and produce related-but-distinct prompts for thumbnail, article hero, and OG/social assets.

## Design principle

One article should have **one strong visual concept expressed in multiple compositions**, rather than one generic image cropped everywhere or three unrelated images.

The target quality bar is a serious engineering publication — not generic AI-generated blog art.

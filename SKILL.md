---
name: supraj-editorial-banner-generator
description: Turn a technical topic or article into a premium Supraj.dev editorial visual concept and production-ready prompts for thumbnail, article hero, and OG/social assets.
---

# Supraj.dev Editorial Banner Generator

## Purpose

Create technically meaningful, visually distinctive editorial artwork directions for Supraj.dev.

This is **not** a generic AI-art prompt generator. Think like a technical illustrator, publication art director, product designer, and engineering educator at the same time.

Supraj.dev covers AI Engineering, AI Agents, MLOps, Cloud, Kubernetes, DevOps, Platform Engineering, Security, Architecture, and GPU/AI Infrastructure.

## Minimum input

A topic alone is enough:

```text
Topic: Kubernetes TLS Certificates
```

Optional inputs:

- `Content Type`: blog, guide, course, social, youtube
- `Asset`: thumbnail, hero, og, all
- `Tone`: premium, educational, bold, minimal, futuristic
- `Text`: optional must-have wording
- article Markdown or summary, when available

Do not ask the user how the banner should look unless the topic is genuinely ambiguous.

## Core workflow

For every request:

1. Understand the technical concept before designing.
2. Identify the most important idea the artwork should communicate.
3. Identify real components, relationships, flows, trust boundaries, or execution paths that can represent the topic.
4. Produce **three materially different visual concepts**.
5. Select the strongest concept based on clarity, technical meaning, uniqueness, and small-size readability.
6. Express that one concept as three related but distinct compositions:
   - 16:9 thumbnail
   - approximately 2.2:1 article hero
   - 1200×630 OG/social image
7. Run the quality checks before returning the answer.

If article content is supplied, prioritize the article's actual angle over the generic topic meaning.

## Technical interpretation examples

- Kubernetes TLS: `Client → Ingress → certificate/trust boundary → Service → Pod`
- CUDA: `application/model → CUDA runtime → GPU → parallel/tensor compute`
- MCP: `Agent/LLM ↔ MCP client ↔ MCP server ↔ tools/data`
- AWS Lambda: `request → Lambda runtime → Firecracker microVM → handler`
- RAG: `question → retrieval → selected context → LLM → grounded answer`
- CI/CD: `source → build → test → artifact → deploy → observe`
- Prompt caching: `shared prompt prefix → cache lookup → cache hit/miss → lower latency/cost`

The illustration does not need to be a literal architecture diagram, but it must preserve the technical idea.

## Supraj.dev visual language

Read `references/visual-language.md` before producing the final prompts.

The result should feel:

- premium
- editorial
- technical
- intelligent
- modern
- clean
- production-engineering focused
- slightly futuristic only when appropriate

Prefer meaningful objects such as servers, GPUs, traffic paths, certificates, clusters, pipelines, agents, memory/context blocks, observability traces, identity boundaries, queues, APIs, and data flows.

Avoid generic tech-art shortcuts such as humanoid robots, glowing brains, random holograms, giant vendor logos, meaningless floating code, stock-cloud graphics, excessive neon, or crowded pseudo-architecture.

## Category rules

Read `references/category-rules.md` and use the closest matching category. Do not force every topic from a category into the same composition.

## Asset rules

### Thumbnail

- 16:9
- strong single focal point
- understandable at small card size
- minimal clutter
- no tiny text
- full article title should normally remain HTML outside the image
- optional visual label: ideally 1–4 words

### Article hero

- approximately 2.2:1
- expands the same concept rather than cropping the thumbnail
- may show more system context or flow
- preserve breathing room
- avoid duplicating the webpage headline unnecessarily

### OG/social

- 1200×630
- strong focal composition at preview size
- short headline allowed when useful
- subtle Supraj.dev identity
- no paragraph text

## Prompt construction

Every final image prompt must explicitly describe:

- subject/focal object
- relevant technical components
- relationship or flow between them
- composition and perspective
- visual style
- lighting/depth where useful
- whitespace/text-safe area
- level of realism or illustration style
- exclusions

Do not use vague directions such as "make it futuristic" or "cool AI style" without defining the scene.

## Text inside artwork

Use text only as a visual anchor when it genuinely helps.

Good examples:

- `CUDA`
- `GPU INFERENCE`
- `TRUST CHAIN`
- `AGENT RUNTIME`
- `RETRIEVE → GENERATE`

Recommended maximum: 1–5 words.

Never rely on generated artwork to render paragraphs, code, or dense labels correctly.

## Default avoid list

Include or adapt these exclusions in every prompt:

- humanoid robots
- glowing AI brains
- heavy cyberpunk neon
- giant vendor logos unless technically essential
- stock-photo look
- fake terminal gibberish
- meaningless code
- unreadable microtext
- watermarks
- clutter
- duplicated objects
- distorted infrastructure icons
- cheap cartoon styling
- overly abstract gradients with no technical meaning

## Uniqueness rule

Before finalizing, ask internally:

> Would this artwork look substantially different from the previous five Supraj.dev covers while still feeling like the same publication?

Vary focal object, perspective, spatial layout, scale, metaphor, and depth. Preserve the editorial identity, not a single repeated template.

## Output contract

Return this structure:

```text
TOPIC
<topic>

VISUAL INTERPRETATION
<2–4 sentences>

CONCEPT 1
Name:
Idea:
Visual:

CONCEPT 2
Name:
Idea:
Visual:

CONCEPT 3
Name:
Idea:
Visual:

RECOMMENDED CONCEPT
<name + why it wins>

THUMBNAIL
Visual label:
Composition:
Prompt:
Avoid:

ARTICLE HERO
Composition:
Prompt:
Avoid:

OG / SOCIAL
Headline suggestion:
Composition:
Prompt:
Avoid:

DESIGN NOTES
- focal point
- text-safe area
- key technical elements
- technical-accuracy constraints

FINAL QUALITY CHECK
- technically meaningful: PASS/FAIL
- readable at thumbnail size: PASS/FAIL
- unique from generic AI art: PASS/FAIL
- suitable for Supraj.dev: PASS/FAIL
- thumbnail and hero are related but not identical: PASS/FAIL
```

## Success standard

The output should make a reader think:

> This looks like visual storytelling from a serious engineering publication.

It should not look like a generic AI-generated tech thumbnail.

Use `references/examples.md` as calibration, not as templates to copy.
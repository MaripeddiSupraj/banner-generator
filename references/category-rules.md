# Category Rules

Use these rules as technical art-direction guidance. They are not fixed templates.

## AI / Agents

Prefer:
- agent execution loops
- model ↔ tool relationships
- context and memory blocks
- orchestration graphs
- MCP/A2A connections
- runtime boundaries
- evaluation/guardrail checkpoints

Avoid:
- robot faces
- human brains
- generic magic-spark AI imagery

Useful visual logic:
`user → model/agent → decision → tool → result → next step`

## Kubernetes

Prefer:
- clusters and nodes
- pods
- services
- ingress/gateway
- control-plane relationships
- traffic paths
- identity/network boundaries
- deployment and scheduling flows

Avoid making the Kubernetes logo the entire concept.

Useful visual logic:
`client → ingress → service → pod(s)`

## Cloud

Prefer:
- service boundaries
- regions/zones
- compute/serverless
- APIs/gateways
- networking
- IAM/trust relationships
- private/public paths
- resilience patterns

Avoid giant AWS/Azure/GCP logos as the primary artwork. Vendor identity may appear subtly when required for comprehension.

## DevOps / Platform Engineering

Prefer:
- source control
- CI/CD progression
- artifacts
- environments
- deployment strategies
- GitOps reconciliation
- observability/feedback
- platform abstractions

Useful visual logic:
`code → build → test → artifact → deploy → observe → improve`

Avoid decorative gears and meaningless terminal screens.

## Security / Identity

Prefer:
- trust boundaries
- token/certificate exchange
- policy evaluation
- least-privilege paths
- encryption boundaries
- workload identity
- secrets access
- authentication vs authorization relationships

Avoid hacker-hoodie clichés and shield-only imagery.

Useful visual logic:
`workload identity → authentication → policy → resource`

## GPU / AI Infrastructure

Prefer:
- GPU as a real compute component
- runtime → GPU relationship
- VRAM/memory movement
- batching
- parallel compute
- model serving
- inference request/token flow
- accelerators and scheduling

Avoid turning the graphic into gaming hardware marketing.

Useful visual logic:
`request/model runtime → accelerator runtime → GPU memory/compute → tokens/output`

## MLOps

Prefer:
- data lifecycle
- training
- experiments
- registry
- deployment
- serving
- monitoring/drift
- feedback/retraining

Useful visual logic:
`data → train → evaluate → register → deploy → monitor → feedback`

Avoid generic "AI + graph" imagery with no lifecycle meaning.

## Observability / SRE

Prefer:
- traces, metrics and logs as distinct signals
- service dependency maps
- request paths
- latency/error hotspots
- SLI/SLO boundaries
- incident timelines

Avoid generic dashboards filled with unreadable charts.

## Networking

Prefer:
- packet/request paths
- DNS resolution
- routing
- load balancing
- NAT
- ingress/egress
- private/public boundaries
- latency hops

Make directionality unambiguous.

## Architecture

Prefer:
- layered systems
- boundaries
- dependency paths
- failure domains
- data movement
- scale-out patterns

Keep the image editorial. It should suggest an architecture rather than reproduce a dense production diagram.

## Terraform / Infrastructure as Code

Prefer:
- desired state vs real state
- plan/apply progression
- modules
- state relationships
- drift
- cloud resource graph

Avoid simply placing the Terraform logo next to random servers.

## GitOps

Prefer:
- Git as source of truth
- desired-state flow
- reconciliation loop
- controller → cluster relationship
- drift correction

Useful visual logic:
`Git desired state → controller → cluster → drift detected → reconcile`

## RAG / Retrieval

Prefer:
- query
- retrieval
- candidate documents/chunks
- ranking
- context construction
- LLM
- grounded answer

When the article is about a specific retrieval technique, visually emphasize that difference instead of using a generic vector-database icon.

## Prompting / Context Engineering

Prefer:
- prompt/context composition
- system/user/tool/context layers
- token window
- reusable prefix/cache
- retrieval/context injection

Avoid showing long generated text inside the artwork.

## Vendor-specific topics

When AWS, Azure, GCP, OCI, NVIDIA, Kubernetes, or another platform is essential:
- the platform may be recognizable
- logos/icons should support the concept, not become the concept
- prioritize the mechanism being explained
- use official-like shapes only when accuracy matters and do not invent fake service icons

The viewer should learn what happens, not merely which vendor is involved.
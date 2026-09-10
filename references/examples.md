# Calibrated Examples

These examples establish quality and reasoning depth. Do not copy their layouts mechanically.

## Example 1 — CUDA Explained

### Visual interpretation
CUDA should be shown as the software/runtime bridge that lets applications and AI workloads execute massively parallel work on GPU hardware. The image should communicate software → CUDA → GPU compute, not merely show a glowing GPU.

### Concept 1
**Name:** GPU Execution Path  
**Idea:** Follow an AI workload into GPU execution.  
**Visual:** A model/application layer on one side, a distinct CUDA/runtime bridge in the middle, and a GPU with highlighted parallel compute lanes on the other side.

### Concept 2
**Name:** CUDA as the Bridge  
**Idea:** Explain the abstraction layer.  
**Visual:** A clean layered stack: application/model → CUDA runtime → GPU memory/compute.

### Concept 3
**Name:** Parallel Compute Engine  
**Idea:** Emphasize why CUDA matters.  
**Visual:** One workload splitting into many synchronized compute paths inside a GPU.

### Recommended concept
**GPU Execution Path** — strongest balance of technical meaning, immediate recognition, and adaptability to thumbnail and hero layouts.

### Thumbnail
**Visual label:** CUDA  
**Composition:** Strong GPU focal object on the right; compact software/runtime flow entering from the left; very little background detail.  
**Prompt:** Create a premium 16:9 technical editorial illustration for a serious engineering publication explaining CUDA. Show an application or AI-model workload entering a clearly distinct CUDA runtime/software layer and flowing into a modern GPU where the workload fans into parallel compute lanes. The GPU is the focal object, but the relationship between software, CUDA, and hardware must remain visually obvious. Clean architectural storytelling, restrained cobalt/indigo accents, neutral dark and light materials, subtle depth, crisp edges, generous negative space, no dense labels, optional small readable label “CUDA”. Avoid gaming-ad aesthetics, giant vendor logos, humanoid robots, glowing brains, random code, hologram clutter, illegible microtext, and watermarks.

### Article hero
**Composition:** Wide left-to-right execution story with more room for runtime, memory, and compute relationships.  
**Prompt:** Create a wide approximately 2.2:1 editorial hero illustration explaining the CUDA execution path. Show a software/application or model workload on the left, a clear CUDA runtime/driver abstraction in the center, and a GPU subsystem on the right with visible memory and parallel compute structure. Use a clean systems-engineering visual language, elegant spacing, restrained dimensionality, and enough negative space for a webpage headline outside the artwork. Preserve technical directionality without turning the image into a dense architecture diagram. Avoid stock-tech styling, giant logos, fake terminal code, excessive neon, and unreadable labels.

### OG/social
**Headline suggestion:** CUDA Explained  
**Composition:** Software-to-GPU bridge centered, with a bolder focal GPU and shorter visual path.  
**Prompt:** Create a 1200×630 social card for an engineering article about CUDA. Show the relationship application/model → CUDA runtime → GPU compute as one strong, clean visual story. Premium editorial presentation, high small-preview readability, restrained cobalt/indigo accent, minimal copy, subtle Supraj.dev publication feel. Avoid generic AI imagery, robots, gaming hardware advertising, fake code, excessive glow, and watermarks.

---

## Example 2 — Kubernetes TLS Certificates

### Visual interpretation
The core story is trust and encrypted traffic entering a Kubernetes workload. The viewer should see that a client reaches an ingress/gateway, where certificate/TLS handling protects the path before traffic moves to services and pods.

### Concept 1
**Name:** Trust Chain  
**Idea:** Visualize the encrypted request path.  
**Visual:** Client → certificate/trust checkpoint → ingress → service → pod.

### Concept 2
**Name:** Secure Cluster Entry  
**Idea:** Make ingress the secure boundary.  
**Visual:** A cluster boundary with one clearly protected entry point and internal routing beyond it.

### Concept 3
**Name:** Certificate Chain  
**Idea:** Focus on why a full certificate chain matters.  
**Visual:** Root/intermediate/server trust elements resolving into the TLS connection terminating at ingress.

### Recommended concept
**Trust Chain** — readable at small size and accurately communicates both security and Kubernetes traffic flow.

### Thumbnail
**Visual label:** TLS / TRUST CHAIN  
**Composition:** Browser/client on left, certificate checkpoint and ingress in center, compact cluster/pods on right.  
**Prompt:** Create a premium 16:9 technical editorial thumbnail explaining TLS certificates in Kubernetes. Show a client request traveling through a visible encrypted/trust path into a Kubernetes ingress or gateway, then routing to a service and pod inside the cluster. Represent the certificate as a meaningful trust checkpoint rather than a decorative padlock. Keep the architecture simple enough for card-size readability, with one clear directional path and restrained cobalt/indigo accents. Avoid giant Kubernetes logos, generic shield art, hacker imagery, fake code, excessive neon, tiny labels, and clutter.

---

## Example 3 — Prompt Caching

### Visual interpretation
The important idea is reuse: repeated prompt-prefix work does not need to be recomputed every time. The banner should contrast a first request that establishes reusable context with later requests that hit the cache and reach model generation faster.

### Concept 1
**Name:** Reused Context Lane  
**Idea:** Show first-run vs repeated-run behavior.  
**Visual:** Shared prompt prefix enters cache once; later requests branch through a shorter cache-hit path.

### Concept 2
**Name:** The Fast Lane  
**Idea:** Use cache hit as a systems-performance metaphor.  
**Visual:** Two execution paths, one longer cold path and one shorter cached path.

### Concept 3
**Name:** Prefix Memory  
**Idea:** Focus on reusable prompt blocks.  
**Visual:** Stable system/context blocks grouped into a cache, while changing user input continues to the model.

### Recommended concept
**Reused Context Lane** — it teaches the mechanism and naturally communicates why latency/cost can improve.

### Thumbnail
**Visual label:** CACHE HIT  
**Composition:** Reusable prompt block → cache node → short model path, with a subtle faded cold path behind it.  
**Prompt:** Create a clean 16:9 engineering-publication illustration explaining prompt caching for LLM applications. Show a stable reusable prompt/context prefix being stored in a cache and subsequent requests taking a visibly shorter cache-hit path toward the model, while a subtle longer cold-processing path provides contrast. Use simple blocks and directional motion, high clarity at thumbnail size, restrained cobalt/indigo accents, premium editorial styling, and generous negative space. Avoid brains, robots, random database cylinders, meaningless code, speedometer clichés, excessive labels, and neon cyberpunk styling.

---

## Example 4 — MCP Server Architecture

### Visual interpretation
MCP should be represented as a protocol boundary connecting an agent/model to external capabilities. The essential relationship is Agent/LLM ↔ MCP client ↔ MCP server ↔ tools/data/services.

### Recommended visual direction
Use a clean protocol bridge with the agent on one side and multiple external capabilities on the other. The MCP server should be a distinct boundary, not just another generic API box.

**Visual label:** MCP  
**Thumbnail prompt:** Create a premium 16:9 technical editorial illustration for Model Context Protocol architecture. Show an AI agent or LLM runtime on the left communicating through a clearly defined MCP client/server protocol bridge in the center to several concrete external capabilities on the right, such as a file source, API/service, database, or engineering tool. Keep the flow bidirectional and technically legible without becoming a dense architecture diagram. Elegant publication style, strong focal bridge, restrained cobalt/indigo accents, ample negative space. Avoid humanoid robots, generic glowing brains, fake code, giant brand logos, excessive arrows, tiny text, and clutter.

---

## Calibration rule

Good outputs should match the examples in **reasoning quality**, not visual sameness. Every topic should earn its own visual metaphor or system composition.
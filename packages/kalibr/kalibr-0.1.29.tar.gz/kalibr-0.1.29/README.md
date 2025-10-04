# Kalibr SDK

Expose your SaaS API once — run it everywhere.

Kalibr makes any SaaS instantly **agent-ready** by generating the connectors required for AI platforms like **ChatGPT (OpenAI Actions)**, **Claude (MCP)**, and more.  

Instead of writing and maintaining separate integrations for every agent framework, you integrate once with Kalibr, and Kalibr handles the rest.

---

## Features

- **One-line deployment** – Define your API actions once.
- **Multi-agent support** – Exposes your API to:
  - OpenAI ChatGPT (`/.well-known/ai-plugin.json`)
  - Claude MCP (`/mcp.json`)
  - Future: Gemini, Copilot, Perplexity, etc.
- **Proxy & ngrok integration** – Run your API locally and test instantly.
- **Schema normalization** – Consistent parameters, auth, and error handling across models.

---

## Quick Start

### 1. Install
```bash
pip install kalibr

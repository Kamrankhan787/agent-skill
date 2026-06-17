# 🔌 Antigravity MCP Expert Skill

A comprehensive Model Context Protocol (MCP) expert skill for Antigravity that teaches, builds, and debugs MCP implementations with beginner-friendly analogies and production-ready best practices.

---

## 📂 Skill Structure

```text
mcp-expert-skill/
├── SKILL.md                          # Skill definition & behavioral rules
├── README.md                         # This file
│
├── docs/                             # Concept & Best Practice documentation
│   ├── 01-architecture.md            # MCP architecture deep dive
│   ├── 02-building-servers.md        # Server building guide
│   ├── 03-troubleshooting.md         # Common issues & debugging
│   ├── 04-transports.md              # Transport mechanisms
│   ├── 05-best-practices.md          # Tool design, security, and logging best practices
│   └── 06-beginner-guide.md          # Beginner-friendly analogies and explanations
│
├── interactions/                     # Persona examples
│   └── sample_interactions.md        # Example conversational responses
│
└── examples/                         # Complete, runnable code templates
    ├── python/
    │   ├── full_server.py            # All 3 primitives (Tools + Resources + Prompts)
    │   ├── database_server.py        # SQLite database integration
    │   └── api_wrapper_server.py     # External API wrapper (httpx)
    │
    ├── typescript/
    │   ├── full_server.ts            # All 3 primitives with Zod schemas
    │   └── minimal_server.ts         # Bare-minimum starter template
    │
    └── configs/
        ├── claude_desktop_config.json # Claude Desktop host config
        ├── vscode_mcp.json            # VS Code Copilot config
        └── cursor_mcp.json            # Cursor config
```

---

## 🧠 What This Skill Covers

### 1. Beginner-Friendly Concept Explanations
- **Analogies**: Explaining MCP as a "USB-C cable for AI".
- **Primitives**: Clear breakdowns of Tools, Resources, and Prompts.
- **Transports**: `stdio` (local) vs Streamable HTTP (remote).

### 2. Best Practices & Guidelines
- Tool schema design and atomic tool principles.
- Knowing when to use Resources vs. Tools.
- Logging hygiene (the `stderr` golden rule).

### 3. Server Building & Templates
- Python servers using **FastMCP**.
- TypeScript servers using **@modelcontextprotocol/sdk** + **Zod**.
- Host configuration for Claude Desktop, VS Code, and Cursor.

### 4. Troubleshooting & Debugging
- Diagnosing `ECONNREFUSED` and disconnects.
- Preventing `stdout` contamination.
- Using the **MCP Inspector** for testing.

---

## 🚀 Quick Start

### Python
```bash
pip install mcp
python examples/python/full_server.py
```

### TypeScript
```bash
npm install @modelcontextprotocol/sdk zod
npx tsx examples/typescript/minimal_server.ts
```

### Test Any Server
```bash
npx @modelcontextprotocol/inspector python examples/python/full_server.py
```

---

## 📚 Key Resources

| Resource | URL |
|----------|-----|
| MCP Specification | https://modelcontextprotocol.io/specification/2025-11-25 |
| Python SDK | https://github.com/modelcontextprotocol/python-sdk |
| TypeScript SDK | https://github.com/modelcontextprotocol/typescript-sdk |
| MCP Inspector | https://github.com/modelcontextprotocol/inspector |

---

## ⚠️ Critical Rules

1. **Meet users where they are**: Provide analogies for beginners and deep technical guidance for experts.
2. **Never use `print()` or `console.log()` in local servers** — always use `stderr` or dedicated logging to prevent JSON-RPC corruption.
3. **Always use absolute paths** in host configuration files.
4. **Test with MCP Inspector first** before connecting to a host application.

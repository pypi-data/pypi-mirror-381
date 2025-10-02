# **FlockParse - Document RAG Intelligence with Distributed Processing**

[![CI Status](https://img.shields.io/github/actions/workflow/status/BenevolentJoker-JohnL/FlockParser/ci.yml?branch=main&label=tests)](https://github.com/BenevolentJoker-JohnL/FlockParser/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Free Forever](https://img.shields.io/badge/Free-Forever-green.svg)](https://github.com/BenevolentJoker-JohnL/FlockParser)
[![Privacy First](https://img.shields.io/badge/Privacy-First-brightgreen.svg)](https://github.com/BenevolentJoker-JohnL/FlockParser)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Demo Video](https://img.shields.io/badge/Demo-YouTube-red.svg)](https://youtu.be/M-HjXkWYRLM)
[![GitHub Stars](https://img.shields.io/github/stars/BenevolentJoker-JohnL/FlockParser?style=social)](https://github.com/BenevolentJoker-JohnL/FlockParser)

> **Distributed document RAG system that turns mismatched hardware into a coordinated inference cluster.** Auto-discovers Ollama nodes, intelligently routes workloads across heterogeneous GPUs/CPUs, and achieves 60x+ speedups through adaptive load balancing. Privacy-first with local/network/cloud interfaces.

**What makes this different:** Real distributed systems engineering—not just API wrappers. Handles heterogeneous hardware (RTX 4090 + GTX 1050Ti + CPU laptops working together), network failures, and privacy requirements that rule out cloud APIs.

---

## **📹 Demo Video (76 seconds)**

Watch FlockParser in action: **372 seconds → 6 seconds (61.7x speedup)** through automatic GPU routing.

[![FlockParser Demo - 61.7x Speedup](https://img.youtube.com/vi/M-HjXkWYRLM/maxresdefault.jpg)](https://youtu.be/M-HjXkWYRLM)

**What you'll see:**
- Single CPU node (372.76s) → Parallel processing (159.79s) → GPU routing (6.04s)
- Real-time document processing with visible timing on screen
- Distributed chat functionality and MCP integration with Claude Desktop
- No editing tricks - all timing shown in real-time

---

## **🔒 Privacy Model**

| Interface | Privacy Level | External Calls | Best For |
|-----------|---------------|----------------|----------|
| **CLI** (`flockparsecli.py`) | 🟢 **100% Local** | None | Personal use, air-gapped systems |
| **Web UI** (`flock_webui.py`) | 🟢 **100% Local** | None | GUI users, visual monitoring |
| **REST API** (`flock_ai_api.py`) | 🟡 **Local Network** | None | Multi-user, app integration |
| **MCP Server** (`flock_mcp_server.py`) | 🔴 **Cloud** | ⚠️ Claude Desktop (Anthropic) | AI assistant integration |

**⚠️ MCP Privacy Warning:** The MCP server integrates with Claude Desktop, which sends queries and document snippets to Anthropic's cloud API. Use CLI/Web UI for 100% offline processing.

---

## **Table of Contents**

- [Key Features](#-key-features)
- [Architecture](#-architecture) | **[📖 Deep Dive: Architecture & Design Decisions](docs/architecture.md)**
- [Quickstart](#-quickstart-3-steps)
- [Benchmarks](#-benchmarks)
- [Usage Examples](#-usage)
- [Security & Production](#-security--production-notes)
- [Troubleshooting](#-troubleshooting-guide)
- [Contributing](#-contributing)

## **⚡ Key Features**

- **🌐 Intelligent Load Balancing** - Auto-discovers Ollama nodes, detects GPU vs CPU, monitors VRAM, and routes work adaptively (10x speedup on heterogeneous clusters)
- **🔌 Multi-Protocol Support** - CLI (100% local), REST API (network), MCP (Claude Desktop), Web UI (Streamlit) - choose your privacy level
- **🎯 Adaptive Routing** - Sequential vs parallel decisions based on cluster characteristics (prevents slow nodes from bottlenecking)
- **📊 Production Observability** - Real-time health scores, performance tracking, VRAM monitoring, automatic failover
- **🔒 Privacy-First Architecture** - No external API calls required (CLI mode), all processing on-premise
- **📄 Complete Pipeline** - PDF extraction → OCR fallback → Multi-format conversion → Vector embeddings → RAG with source citations

## **🏗️ Architecture**

```
┌─────────────────────────────────────────────────────────────┐
│             Interfaces (Choose Your Privacy Level)           │
│  CLI (Local) | REST API (Network) | MCP (Claude) | Web UI   │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                  FlockParse Core Engine                      │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────┐       │
│  │   PDF       │  │  Semantic    │  │     RAG      │       │
│  │ Processing  │→ │   Search     │→ │   Engine     │       │
│  └─────────────┘  └──────────────┘  └──────────────┘       │
│         │                │                    │              │
│         ▼                ▼                    ▼              │
│  ┌───────────────────────────────────────────────────┐      │
│  │        ChromaDB Vector Store (Persistent)         │      │
│  └───────────────────────────────────────────────────┘      │
└──────────────────────┬──────────────────────────────────────┘
                       │ Intelligent Load Balancer
                       │ • Health scoring (GPU/VRAM detection)
                       │ • Adaptive routing (sequential vs parallel)
                       │ • Automatic failover & caching
                       ▼
    ┌──────────────────────────────────────────────┐
    │       Distributed Ollama Cluster              │
    │  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
    │  │ Node 1   │  │ Node 2   │  │ Node 3   │   │
    │  │ GPU A    │  │ GPU B    │  │ CPU      │   │
    │  │16GB VRAM │  │ 8GB VRAM │  │ 16GB RAM │   │
    │  │Health:367│  │Health:210│  │Health:50 │   │
    │  └──────────┘  └──────────┘  └──────────┘   │
    └──────────────────────────────────────────────┘
         ▲ Auto-discovery | Performance tracking
```

**Want to understand how this works?** Read the **[📖 Architecture Deep Dive](docs/architecture.md)** for detailed explanations of:
- Why distributed AI inference solves real-world problems
- How adaptive routing decisions are made (sequential vs parallel)
- MCP integration details and privacy implications
- Technical trade-offs and design decisions

## **🚀 Quickstart (3 Steps)**

**Requirements:**
- Python 3.10 or later
- Ollama 0.1.20+ (install from [ollama.com](https://ollama.com))
- 4GB+ RAM (8GB+ recommended for GPU nodes)

```bash
# 1. Clone and install
git clone https://github.com/BenevolentJoker-JohnL/FlockParser.git
cd FlockParser

# Option A: Install dependencies only
pip install -r requirements.txt

# Option B: Install as package (recommended - adds console commands)
pip install -e .
# This adds commands: flockparse, flockparse-webui, flockparse-api, flockparse-mcp

# 2. Start Ollama and pull models
ollama serve  # In a separate terminal
ollama pull mxbai-embed-large    # Required for embeddings
ollama pull llama3.1:latest       # Required for chat

# 3. Run your preferred interface
streamlit run flock_webui.py         # Web UI - easiest (recommended) ⭐
python flockparsecli.py              # CLI - 100% local
python flock_ai_api.py               # REST API - multi-user
python flock_mcp_server.py           # MCP - Claude Desktop integration

# Or if you installed with pip (Option B above):
flockparse-webui                     # Web UI
flockparse                           # CLI
flockparse-api                       # REST API
flockparse-mcp                       # MCP Server
```

**💡 Pro tip:** Start with the Web UI to see distributed processing with real-time VRAM monitoring and node health dashboards.

### **Quick Test (30 seconds)**

```bash
# Start the CLI
python flockparsecli.py

# Process the sample PDF
> open_pdf testpdfs/sample.pdf

# Chat with it
> chat
🙋 You: Summarize this document
```

**First time?** Start with the Web UI (`streamlit run flock_webui.py`) - it's the easiest way to see distributed processing in action with a visual dashboard.

---

## **🌐 Setting Up Distributed Nodes**

**Want the 60x speedup?** Set up multiple Ollama nodes across your network.

### Quick Multi-Node Setup

**On each additional machine:**

```bash
# 1. Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 2. Configure for network access
export OLLAMA_HOST=0.0.0.0:11434
ollama serve

# 3. Pull models
ollama pull mxbai-embed-large
ollama pull llama3.1:latest

# 4. Allow firewall (if needed)
sudo ufw allow 11434/tcp  # Linux
```

**FlockParser will automatically discover these nodes!**

Check with:
```bash
python flockparsecli.py
> lb_stats  # Shows all discovered nodes and their capabilities
```

**📖 Complete Guide:** See **[DISTRIBUTED_SETUP.md](DISTRIBUTED_SETUP.md)** for:
- Step-by-step multi-machine setup
- Network configuration and firewall rules
- Troubleshooting node discovery
- Example setups (budget home lab to professional clusters)
- GPU router configuration for automatic optimization

---

### **🔒 Privacy Levels by Interface:**
- **Web UI (`flock_webui.py`)**: 🟢 100% local, runs in your browser
- **CLI (`flockparsecli.py`)**: 🟢 100% local, zero external calls
- **REST API (`flock_ai_api.py`)**: 🟡 Local network only
- **MCP Server (`flock_mcp_server.py`)**: 🔴 Integrates with Claude Desktop (Anthropic cloud service)

**Choose the interface that matches your privacy requirements!**

## **🏆 Why FlockParse? Comparison to Competitors**

| Feature | **FlockParse** | LangChain | LlamaIndex | Haystack |
|---------|---------------|-----------|------------|----------|
| **100% Local/Offline** | ✅ Yes (CLI/JSON) | ⚠️ Partial | ⚠️ Partial | ⚠️ Partial |
| **Zero External API Calls** | ✅ Yes (CLI/JSON) | ❌ No | ❌ No | ❌ No |
| **Built-in GPU Load Balancing** | ✅ Yes (auto) | ❌ No | ❌ No | ❌ No |
| **VRAM Monitoring** | ✅ Yes (dynamic) | ❌ No | ❌ No | ❌ No |
| **Multi-Node Auto-Discovery** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **CPU Fallback Detection** | ✅ Yes | ❌ No | ❌ No | ❌ No |
| **Document Format Export** | ✅ 4 formats | ❌ Limited | ❌ Limited | ⚠️ Basic |
| **Setup Complexity** | 🟢 Simple | 🔴 Complex | 🔴 Complex | 🟡 Medium |
| **Dependencies** | 🟢 Minimal | 🔴 Heavy | 🔴 Heavy | 🟡 Medium |
| **Learning Curve** | 🟢 Low | 🔴 Steep | 🔴 Steep | 🟡 Medium |
| **Privacy Control** | 🟢 High (CLI/JSON) | 🔴 Limited | 🔴 Limited | 🟡 Medium |
| **Out-of-Box Functionality** | ✅ Complete | ⚠️ Requires config | ⚠️ Requires config | ⚠️ Requires config |
| **MCP Integration** | ✅ Native | ❌ No | ❌ No | ❌ No |
| **Embedding Cache** | ✅ MD5-based | ⚠️ Basic | ⚠️ Basic | ⚠️ Basic |
| **Batch Processing** | ✅ Parallel | ⚠️ Sequential | ⚠️ Sequential | ⚠️ Basic |
| **Performance** | 🚀 60x+ faster with GPU auto-routing | ⚠️ Varies by config | ⚠️ Varies by config | ⚠️ Varies by config |
| **Cost** | 💰 Free | 💰💰 Free + Paid | 💰💰 Free + Paid | 💰💰 Free + Paid |

### **Key Differentiators:**

1. **Privacy by Design**: CLI and JSON interfaces are 100% local with zero external calls (MCP interface uses Claude Desktop for chat)
2. **Intelligent GPU Management**: Automatically finds, tests, and prioritizes GPU nodes
3. **Production-Ready**: Works immediately with sensible defaults
4. **Resource-Aware**: Detects VRAM exhaustion and prevents performance degradation
5. **Complete Solution**: CLI, REST API, MCP, and batch interfaces - choose your privacy level

## **📊 Performance**

### **📹 [76-Second Demo Video](https://youtu.be/M-HjXkWYRLM)** - Watch 6 minutes become 6 seconds

**Real-Time Demo Results** (unedited timing shown on screen):

| Processing Mode | Time | Speedup | What It Shows |
|----------------|------|---------|---------------|
| Single CPU node | 372.76s (~6 min) | 1x baseline | Sequential CPU processing |
| Parallel (multi-node) | 159.79s (~2.5 min) | **2.3x faster** | Distributed across cluster |
| GPU node routing | 6.04s (~6 sec) | **61.7x faster** | Automatic GPU detection & routing |

**Why the Massive Speedup?**
- GPU processes embeddings in milliseconds vs seconds on CPU
- Adaptive routing detected GPU was 60x+ faster and sent all work there
- Avoided bottleneck of waiting for slower CPU nodes to finish
- No network overhead (local cluster, no cloud APIs)

**Demo Contents:**
- `0:00` - Single node baseline (372.76s)
- `0:30` - Auto-discover cluster nodes on network
- `0:45` - Parallel processing across nodes (159.79s)
- `1:00` - GPU routing with adaptive decision (6.04s)
- `1:10` - Document chat with RAG + source citations
- `1:15` - MCP integration with Claude Desktop

**Key Insight:** The system **automatically** detected performance differences and made routing decisions - no manual GPU configuration needed.

**Hardware (Demo Cluster):**
- **Node 1 (10.9.66.90):** Intel i9-12900K, 32GB DDR5-6000, 6TB NVMe Gen4, RTX A4000 16GB - routed here
- **Node 2 (10.9.66.159):** AMD Ryzen 7 5700X, 32GB DDR4-3600, GTX 1050Ti (CPU-mode)
- **Node 3:** Intel i7-12th gen (laptop), 16GB DDR5, CPU-only
- **Software:** Python 3.10, Ollama, Ubuntu 22.04

**Reproducibility:**
- Timing shown on-screen in real-time (not edited)
- Commands visible in terminal output
- Full source code available in this repo
- Test with your own hardware - results will vary based on GPU

The project offers four main interfaces:
1. **flock_webui.py** - 🎨 Beautiful Streamlit web interface (NEW!)
2. **flockparsecli.py** - Command-line interface for personal document processing
3. **flock_ai_api.py** - REST API server for multi-user or application integration
4. **flock_mcp_server.py** - Model Context Protocol server for AI assistants like Claude Desktop

## **🔧 Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/yourusername/flockparse.git
cd flockparse
```

### **2. Install System Dependencies (Required for OCR)**

**⚠️ IMPORTANT: Install these BEFORE pip install, as pytesseract and pdf2image require system packages**

#### For Better PDF Text Extraction:
- **Linux**:
  ```bash
  sudo apt-get update
  sudo apt-get install poppler-utils
  ```
- **macOS**:
  ```bash
  brew install poppler
  ```
- **Windows**: Download from [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)

#### For OCR Support (Scanned Documents):
FlockParse automatically detects scanned PDFs and uses OCR!

- **Linux (Ubuntu/Debian)**:
  ```bash
  sudo apt-get update
  sudo apt-get install tesseract-ocr tesseract-ocr-eng poppler-utils
  ```
- **Linux (Fedora/RHEL)**:
  ```bash
  sudo dnf install tesseract poppler-utils
  ```
- **macOS**:
  ```bash
  brew install tesseract poppler
  ```
- **Windows**:
  1. Install [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki) - Download the installer
  2. Install [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)
  3. Add both to your system PATH

**Verify installation:**
```bash
tesseract --version
pdftotext -v
```

### **3. Install Python Dependencies**
```bash
pip install -r requirements.txt
```

**Key Python dependencies** (installed automatically):
- fastapi, uvicorn - Web server
- pdfplumber, PyPDF2, pypdf - PDF processing
- **pytesseract** - Python wrapper for Tesseract OCR (requires system Tesseract)
- **pdf2image** - PDF to image conversion (requires system Poppler)
- Pillow - Image processing for OCR
- chromadb - Vector database
- python-docx - DOCX generation
- ollama - AI model integration
- numpy - Numerical operations
- markdown - Markdown generation

**How OCR fallback works:**
1. Tries PyPDF2 text extraction
2. Falls back to pdftotext if no text
3. **Falls back to OCR** if still no text (<100 chars) - **Requires Tesseract + Poppler**
4. Automatically processes scanned documents without manual intervention

### **4. Install and Configure Ollama**  

1. Install Ollama from [ollama.com](https://ollama.com)
2. Start the Ollama service:
   ```bash
   ollama serve
   ```
3. Pull the required models:
   ```bash
   ollama pull mxbai-embed-large
   ollama pull llama3.1:latest
   ```

## **📜 Usage**

### **🎨 Web UI (flock_webui.py) - Easiest Way to Get Started!**

Launch the beautiful Streamlit web interface:
```bash
streamlit run flock_webui.py
```

The web UI will open in your browser at `http://localhost:8501`

**Features:**
- 📤 **Upload & Process**: Drag-and-drop PDF files for processing
- 💬 **Chat Interface**: Interactive chat with your documents
- 📊 **Load Balancer Dashboard**: Real-time monitoring of GPU nodes
- 🔍 **Semantic Search**: Search across all documents
- 🌐 **Node Management**: Add/remove Ollama nodes, auto-discovery
- 🎯 **Routing Control**: Switch between routing strategies

**Perfect for:**
- Users who prefer graphical interfaces
- Quick document processing and exploration
- Monitoring distributed processing
- Managing multiple Ollama nodes visually

---

### **CLI Interface (flockparsecli.py)**

Run the script:
```bash
python flockparsecli.py
```

Available commands:
```
📖 open_pdf <file>   → Process a single PDF file
📂 open_dir <dir>    → Process all PDFs in a directory
💬 chat              → Chat with processed PDFs
📊 list_docs         → List all processed documents
🔍 check_deps        → Check for required dependencies
🌐 discover_nodes    → Auto-discover Ollama nodes on local network
➕ add_node <url>    → Manually add an Ollama node
➖ remove_node <url> → Remove an Ollama node from the pool
📋 list_nodes        → List all configured Ollama nodes
⚖️  lb_stats          → Show load balancer statistics
❌ exit              → Quit the program
```

### **Web Server API (flock_ai_api.py)**

Start the API server:
```bash
# Set your API key (or use default for testing)
export FLOCKPARSE_API_KEY="your-secret-key-here"

# Start server
python flock_ai_api.py
```

The server will run on `http://0.0.0.0:8000` by default.

#### **🔒 Authentication (NEW!)**

All endpoints except `/` require an API key in the `X-API-Key` header:

```bash
# Default API key (change in production!)
X-API-Key: your-secret-api-key-change-this

# Or set via environment variable
export FLOCKPARSE_API_KEY="my-super-secret-key"
```

#### **Available Endpoints:**

| Endpoint | Method | Auth Required | Description |
|----------|--------|---------------|-------------|
| `/` | GET | ❌ No | API status and version info |
| `/upload/` | POST | ✅ Yes | Upload and process a PDF file |
| `/summarize/{file_name}` | GET | ✅ Yes | Get an AI-generated summary |
| `/search/?query=...` | GET | ✅ Yes | Search for relevant documents |

#### **Example API Usage:**

**Check API status (no auth required):**
```bash
curl http://localhost:8000/
```

**Upload a document (with authentication):**
```bash
curl -X POST \
  -H "X-API-Key: your-secret-api-key-change-this" \
  -F "file=@your_document.pdf" \
  http://localhost:8000/upload/
```

**Get a document summary:**
```bash
curl -H "X-API-Key: your-secret-api-key-change-this" \
  http://localhost:8000/summarize/your_document.pdf
```

**Search across documents:**
```bash
curl -H "X-API-Key: your-secret-api-key-change-this" \
  "http://localhost:8000/search/?query=your%20search%20query"
```

**⚠️ Production Security:**
- Always change the default API key
- Use environment variables, never hardcode keys
- Use HTTPS in production (nginx/apache reverse proxy)
- Consider rate limiting for public deployments

### **MCP Server (flock_mcp_server.py)**

The MCP server allows FlockParse to be used as a tool by AI assistants like Claude Desktop.

#### **Setting up with Claude Desktop**

1. **Start the MCP server:**
   ```bash
   python flock_mcp_server.py
   ```

2. **Configure Claude Desktop:**
   Add to your Claude Desktop config file (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS, or `%APPDATA%\Claude\claude_desktop_config.json` on Windows):

   ```json
   {
     "mcpServers": {
       "flockparse": {
         "command": "python",
         "args": ["/absolute/path/to/FlockParser/flock_mcp_server.py"]
       }
     }
   }
   ```

3. **Restart Claude Desktop** and you'll see FlockParse tools available!

#### **Available MCP Tools:**

- `process_pdf` - Process and add PDFs to the knowledge base
- `query_documents` - Search documents using semantic search
- `chat_with_documents` - Ask questions about your documents
- `list_documents` - List all processed documents
- `get_load_balancer_stats` - View node performance metrics
- `discover_ollama_nodes` - Auto-discover Ollama nodes
- `add_ollama_node` - Add an Ollama node manually
- `remove_ollama_node` - Remove an Ollama node

#### **Example MCP Usage:**

In Claude Desktop, you can now ask:
- "Process the PDF at /path/to/document.pdf"
- "What documents do I have in my knowledge base?"
- "Search my documents for information about quantum computing"
- "What does my research say about black holes?"

## **💡 Practical Use Cases**

### **Knowledge Management**
- Create searchable archives of research papers, legal documents, and technical manuals
- Generate summaries of lengthy documents for quick review
- Chat with your document collection to find specific information without manual searching

### **Legal & Compliance**
- Process contract repositories for semantic search capabilities
- Extract key terms and clauses from legal documents
- Analyze regulatory documents for compliance requirements

### **Research & Academia**
- Process and convert academic papers for easier reference
- Create a personal research assistant that can reference your document library
- Generate summaries of complex research for presentations or reviews

### **Business Intelligence**
- Convert business reports into searchable formats
- Extract insights from PDF-based market research
- Make proprietary documents more accessible throughout an organization

## **🌐 Distributed Processing with Load Balancer**

FlockParse includes a sophisticated load balancer that can distribute embedding generation across multiple Ollama instances on your local network.

### **Setting Up Distributed Processing**

#### **Option 1: Auto-Discovery (Easiest)**
```bash
# Start FlockParse
python flockparsecli.py

# Auto-discover Ollama nodes on your network
⚡ Enter command: discover_nodes
```

The system will automatically scan your local network (/24 subnet) and detect any running Ollama instances.

#### **Option 2: Manual Node Management**
```bash
# Add a specific node
⚡ Enter command: add_node http://192.168.1.100:11434

# List all configured nodes
⚡ Enter command: list_nodes

# Remove a node
⚡ Enter command: remove_node http://192.168.1.100:11434

# View load balancer statistics
⚡ Enter command: lb_stats
```

### **Benefits of Distributed Processing**

- **Speed**: Process documents 2-10x faster with multiple nodes
- **GPU Awareness**: Automatically detects and prioritizes GPU nodes over CPU nodes
- **VRAM Monitoring**: Detects when GPU nodes fall back to CPU due to insufficient VRAM
- **Fault Tolerance**: Automatic failover if a node becomes unavailable
- **Load Distribution**: Smart routing based on node performance, GPU availability, and VRAM capacity
- **Easy Scaling**: Just add more machines with Ollama installed

### **Setting Up Additional Ollama Nodes**

On each additional machine:
```bash
# Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# Pull the embedding model
ollama pull mxbai-embed-large

# Start Ollama (accessible from network)
OLLAMA_HOST=0.0.0.0:11434 ollama serve
```

Then use `discover_nodes` or `add_node` to add them to FlockParse.

### **GPU and VRAM Optimization**

FlockParse automatically detects GPU availability and VRAM usage using Ollama's `/api/ps` endpoint:

- **🚀 GPU nodes** with models loaded in VRAM get +200 health score bonus
- **⚠️ VRAM-limited nodes** that fall back to CPU get only +50 bonus
- **🐢 CPU-only nodes** get -50 penalty

**To ensure your GPU is being used:**

1. **Check GPU detection**: Run `lb_stats` command to see node status
2. **Preload model into GPU**: Run a small inference to load model into VRAM
   ```bash
   ollama run mxbai-embed-large "test"
   ```
3. **Verify VRAM usage**: Check that `size_vram > 0` in `/api/ps`:
   ```bash
   curl http://localhost:11434/api/ps
   ```
4. **Increase VRAM allocation**: If model won't load into VRAM, free up GPU memory or use a smaller model

**Dynamic VRAM monitoring**: FlockParse continuously monitors embedding performance and automatically detects when a GPU node falls back to CPU due to VRAM exhaustion during heavy load.

## **🔄 Example Workflows**

### **CLI Workflow: Research Paper Processing**

1. **Check Dependencies**:
   ```
   ⚡ Enter command: check_deps
   ```

2. **Process a Directory of Research Papers**:
   ```
   ⚡ Enter command: open_dir ~/research_papers
   ```

3. **Chat with Your Research Collection**:
   ```
   ⚡ Enter command: chat
   🙋 You: What are the key methods used in the Smith 2023 paper?
   ```

### **API Workflow: Document Processing Service**

1. **Start the API Server**:
   ```bash
   python flock_ai_api.py
   ```

2. **Upload Documents via API**:
   ```bash
   curl -X POST -F "file=@quarterly_report.pdf" http://localhost:8000/upload/
   ```

3. **Generate a Summary**:
   ```bash
   curl http://localhost:8000/summarize/quarterly_report.pdf
   ```

4. **Search Across Documents**:
   ```bash
   curl http://localhost:8000/search/?query=revenue%20growth%20Q3
   ```

## **🔧 Troubleshooting Guide**

### **Ollama Connection Issues**

**Problem**: Error messages about Ollama not being available or connection failures.

**Solution**:
1. Verify Ollama is running: `ps aux | grep ollama`
2. Restart the Ollama service: 
   ```bash
   killall ollama
   ollama serve
   ```
3. Check that you've pulled the required models:
   ```bash
   ollama list
   ```
4. If models are missing:
   ```bash
   ollama pull mxbai-embed-large
   ollama pull llama3.1:latest
   ```

### **PDF Text Extraction Failures**

**Problem**: No text extracted from certain PDFs.

**Solution**:
1. Check if the PDF is scanned/image-based:
   - Install OCR tools: `sudo apt-get install tesseract-ocr` (Linux)
   - For better scanned PDF handling: `pip install ocrmypdf`
   - Process with OCR: `ocrmypdf input.pdf output.pdf`

2. If the PDF has unusual fonts or formatting:
   - Install poppler-utils for better extraction
   - Try using the `-layout` option with pdftotext manually:
     ```bash
     pdftotext -layout problem_document.pdf output.txt
     ```

### **Memory Issues with Large Documents**

**Problem**: Application crashes with large PDFs or many documents.

**Solution**:
1. Process one document at a time for very large PDFs
2. Reduce the chunk size in the code (default is 512 characters)
3. Increase your system's available memory or use a swap file
4. For server deployments, consider using a machine with more RAM

### **API Server Not Starting**

**Problem**: Error when trying to start the API server.

**Solution**:
1. Check for port conflicts: `lsof -i :8000`
2. If another process is using port 8000, kill it or change the port
3. Verify FastAPI is installed: `pip install fastapi uvicorn`
4. Check for Python version compatibility (requires Python 3.7+)

---

## **🔐 Security & Production Notes**

### **REST API Security**

**⚠️ The default API key is NOT secure - change it immediately!**

```bash
# Set a strong API key via environment variable
export FLOCKPARSE_API_KEY="your-super-secret-key-change-this-now"

# Or generate a random one
export FLOCKPARSE_API_KEY=$(openssl rand -hex 32)

# Start the API server
python flock_ai_api.py
```

**Production Checklist:**
- ✅ **Change default API key** - Never use `your-secret-api-key-change-this`
- ✅ **Use environment variables** - Never hardcode secrets in code
- ✅ **Enable HTTPS** - Use nginx or Apache as reverse proxy with SSL/TLS
- ✅ **Add rate limiting** - Use nginx `limit_req` or FastAPI middleware
- ✅ **Network isolation** - Don't expose API to public internet unless necessary
- ✅ **Monitor logs** - Watch for authentication failures and abuse

**Example nginx config with TLS:**
```nginx
server {
    listen 443 ssl;
    server_name your-domain.com;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

### **MCP Privacy & Security**

**What data leaves your machine:**
- 🔴 **Document queries** - Sent to Claude Desktop → Anthropic API
- 🔴 **Document snippets** - Retrieved context chunks sent as part of prompts
- 🔴 **Chat messages** - All RAG conversations processed by Claude
- 🟢 **Document files** - Never uploaded (processed locally, only embeddings stored)

**To disable MCP and stay 100% local:**
1. Remove FlockParse from Claude Desktop config
2. Use CLI (`flockparsecli.py`) or Web UI (`flock_webui.py`) instead
3. Both provide full RAG functionality without external API calls

**MCP is safe for:**
- ✅ Public documents (research papers, manuals, non-sensitive data)
- ✅ Testing and development
- ✅ Personal use where you trust Anthropic's privacy policy

**MCP is NOT recommended for:**
- ❌ Confidential business documents
- ❌ Personal identifiable information (PII)
- ❌ Regulated data (HIPAA, GDPR sensitive content)
- ❌ Air-gapped or classified environments

### **Database Security**

**SQLite limitations (ChromaDB backend):**
- ⚠️ No concurrent writes from multiple processes
- ⚠️ File permissions determine access (not true auth)
- ⚠️ No encryption at rest by default

**For production with multiple users:**
```bash
# Option 1: Separate databases per interface
CLI:     chroma_db_cli/
API:     chroma_db_api/
MCP:     chroma_db_mcp/

# Option 2: Use PostgreSQL backend (ChromaDB supports it)
# See ChromaDB docs: https://docs.trychroma.com/
```

### **VRAM Detection Method**

FlockParse detects GPU usage via Ollama's `/api/ps` endpoint:

```bash
# Check what Ollama reports
curl http://localhost:11434/api/ps

# Response shows VRAM usage:
{
  "models": [{
    "name": "mxbai-embed-large:latest",
    "size": 705530880,
    "size_vram": 705530880,  # <-- If >0, model is in GPU
    ...
  }]
}
```

**Health score calculation:**
- `size_vram > 0` → +200 points (GPU in use)
- `size_vram == 0` but GPU present → +50 points (GPU available, not used)
- CPU-only → -50 points

This is **presence-based detection**, not utilization monitoring. It detects *if* the model loaded into VRAM, not *how efficiently* it's being used.

---

## **💡 Features**

| Feature | Description |
|---------|-------------|
| **Multi-method PDF Extraction** | Uses both PyPDF2 and pdftotext for best results |
| **Format Conversion** | Converts PDFs to TXT, Markdown, DOCX, and JSON |
| **Semantic Search** | Uses vector embeddings to find relevant information |
| **Interactive Chat** | Discuss your documents with AI assistance |
| **Privacy Options** | Web UI/CLI: 100% offline; REST API: local network; MCP: Claude Desktop (cloud) |
| **Distributed Processing** | Load balancer with auto-discovery for multiple Ollama nodes |
| **Accurate VRAM Monitoring** | Real GPU memory tracking with nvidia-smi/rocm-smi + Ollama API (NEW!) |
| **GPU & VRAM Awareness** | Automatically detects GPU nodes and prevents CPU fallback |
| **Intelligent Routing** | 4 strategies (adaptive, round_robin, least_loaded, lowest_latency) with GPU priority |
| **Flexible Model Matching** | Supports model name variants (llama3.1, llama3.1:latest, llama3.1:8b, etc.) |
| **ChromaDB Vector Store** | Production-ready persistent vector database with cosine similarity |
| **Embedding Cache** | MD5-based caching prevents reprocessing same content |
| **Model Weight Caching** | Keep models in VRAM for faster repeated inference |
| **Parallel Batch Processing** | Process multiple embeddings simultaneously |
| **Database Management** | Clear cache and clear DB commands for easy maintenance (NEW!) |
| **Filename Preservation** | Maintains original document names in converted files |
| **REST API** | Web server for multi-user/application integration |
| **Document Summarization** | AI-generated summaries of uploaded documents |
| **OCR Processing** | Extract text from scanned documents using image recognition |

## **Comparing FlockParse Interfaces**

| Feature | **flock_webui.py** | flockparsecli.py | flock_ai_api.py | flock_mcp_server.py |
|---------|-------------------|----------------|-----------|---------------------|
| **Interface** | 🎨 Web Browser (Streamlit) | Command line | REST API over HTTP | Model Context Protocol |
| **Ease of Use** | ⭐⭐⭐⭐⭐ Easiest | ⭐⭐⭐⭐ Easy | ⭐⭐⭐ Moderate | ⭐⭐⭐ Moderate |
| **Use case** | Interactive GUI usage | Personal CLI processing | Service integration | AI Assistant integration |
| **Document formats** | Creates TXT, MD, DOCX, JSON | Creates TXT, MD, DOCX, JSON | Stores extracted text only | Creates TXT, MD, DOCX, JSON |
| **Interaction** | Point-and-click + chat | Interactive chat mode | Query/response via API | Tool calls from AI assistants |
| **Multi-user** | Single user (local) | Single user | Multiple users/applications | Single user (via AI assistant) |
| **Storage** | Local file-based | Local file-based | ChromaDB vector database | Local file-based |
| **Load Balancing** | ✅ Yes (visual dashboard) | ✅ Yes | ❌ No | ✅ Yes |
| **Node Discovery** | ✅ Yes (one-click) | ✅ Yes | ❌ No | ✅ Yes |
| **GPU Monitoring** | ✅ Yes (real-time charts) | ✅ Yes | ❌ No | ✅ Yes |
| **Batch Operations** | ⚠️ Multiple upload | ❌ No | ❌ No | ❌ No |
| **Privacy Level** | 🟢 100% Local | 🟢 100% Local | 🟡 Local Network | 🔴 Cloud (Claude) |
| **Best for** | **🌟 General users, GUI lovers** | Direct CLI usage | Integration with apps | Claude Desktop, AI workflows |

## **📁 Project Structure**

- `/converted_files` - Stores the converted document formats (flockparsecli.py)
- `/knowledge_base` - Legacy JSON storage (backwards compatibility only)
- `/chroma_db_cli` - **ChromaDB vector database for CLI** (flockparsecli.py) - **Production storage**
- `/uploads` - Temporary storage for uploaded documents (flock_ai_api.py)
- `/chroma_db` - ChromaDB vector database (flock_ai_api.py)

## **🚀 Recent Additions**
- ✅ **GPU Auto-Optimization** - Background process ensures models use GPU automatically (NEW!)
- ✅ **Programmatic GPU Control** - Force models to GPU/CPU across distributed nodes (NEW!)
- ✅ **Accurate VRAM Monitoring** - Real GPU memory tracking across distributed nodes
- ✅ **ChromaDB Production Integration** - Professional vector database for 100x faster search
- ✅ **Clear Cache & Clear DB Commands** - Manage embeddings and database efficiently
- ✅ **Model Weight Caching** - Keep models in VRAM for 5-10x faster inference
- ✅ **Web UI** - Beautiful Streamlit interface for easy document management
- ✅ **Advanced OCR Support** - Automatic fallback to OCR for scanned documents
- ✅ **API Authentication** - Secure API key authentication for REST API endpoints
- ⬜ **Document versioning** - Track changes over time (Coming soon)

## **📚 Complete Documentation**

### Core Documentation
- **[📖 Architecture Deep Dive](docs/architecture.md)** - System design, routing algorithms, technical decisions
- **[🌐 Distributed Setup Guide](DISTRIBUTED_SETUP.md)** - ⭐ **Set up your own multi-node cluster**
- **[🐛 Error Handling Guide](ERROR_HANDLING.md)** - Troubleshooting common issues
- **[🤝 Contributing Guide](CONTRIBUTING.md)** - How to contribute to the project
- **[📋 Code of Conduct](CODE_OF_CONDUCT.md)** - Community guidelines
- **[📝 Changelog](CHANGELOG.md)** - Version history

### Technical Guides
- **[⚡ Performance Optimization](PERFORMANCE_OPTIMIZATION.md)** - Tuning for maximum speed
- **[🔧 GPU Router Setup](GPU_ROUTER_SETUP.md)** - Distributed cluster configuration
- **[🤖 GPU Auto-Optimization](GPU_AUTO_OPTIMIZATION.md)** - Automatic GPU management
- **[📊 VRAM Monitoring](VRAM_MONITORING.md)** - GPU memory tracking
- **[🎯 Adaptive Parallelism](ADAPTIVE_PARALLELISM.md)** - Smart workload distribution
- **[🗄️ ChromaDB Production](CHROMADB_PRODUCTION.md)** - Vector database scaling
- **[💾 Model Caching](MODEL_CACHING.md)** - Performance through caching
- **[🖥️ Node Management](NODE_MANAGEMENT.md)** - Managing distributed nodes
- **[⚡ Quick Setup](QUICK_SETUP.md)** - Fast track to getting started

### Additional Resources
- **[📹 Demo Video (76 seconds)](https://youtu.be/M-HjXkWYRLM)** - Watch FlockParser in action
- **[📦 Docker Setup](docker-compose.yml)** - Containerized deployment
- **[⚙️ Environment Config](.env.example)** - Configuration template
- **[🧪 Tests](tests/)** - Test suite and CI/CD

## **📝 Development Process**

This project was developed iteratively using Claude and Claude Code as coding assistants. All design decisions, architecture choices, and integration strategy were directed and reviewed by me.

## **🤝 Contributing**
Contributions are welcome! Please feel free to submit a Pull Request.

## **📄 License**
This project is licensed under the MIT License - see the LICENSE file for details.

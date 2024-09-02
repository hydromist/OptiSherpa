# OptiSherpa

[OptiSherpa](https://www.tasking.ai) is a BaaS (Backend as a Service) platform for **LLM-based Agent Development and Deployment**. It unified the integration of hundreds of LLM models, and provides an intuitive user interface for managing your LLM application's functional modules, including tools, RAG systems, assistants, conversation history, and more.

### Key Features

1. **All-In-One LLM Platform**: Access hundreds of AI models with unified APIs.
2. **Abundant enhancement**: Enhance LLM agent performance with hundreds of customizable built-in **tools** and advanced **Retrieval-Augmented Generation** (RAG) system
3. **BaaS-Inspired Workflow**: Separate AI logic (server-side) from product development (client-side), offering a clear pathway from console-based prototyping to scalable solutions using RESTful APIs and client SDKs.
4. **One-Click to Production**: Deploy your AI agents with a single click to production stage, and scale them with ease. Let OptiSherpa handle the rest.
5. **Asynchronous Efficiency**: Harness Python FastAPI's asynchronous features for high-performance, concurrent computation, enhancing the responsiveness and scalability of the applications.
6. **Intuitive UI Console**: Simplifies project management and allows in-console workflow testing.

### Integrations

**Models**: OptiSherpa connects with hundreds of LLMs from various providers, including OpenAI, Anthropic, and more. We also allow users to integrate local host models through Ollama, LM Studio and Local AI.

<p>
<img src="./static/img/model_providers.png" alt="">
</p>

**Plugins**: OptiSherpa supports a wide range of built-in plugins to empower your AI agents, including Google search, website reader, stock market retrieval, and more. Users can also create custom tools to meet their specific needs.
---

## Why OptiSherpa?

### Problems with existing solutions 🙁

**LangChain** is a tool framework for LLM application development, but it faces practical limitations:

- **Statelessness**: Relies on client-side or external services for data management.
- **Scalability Challenges**: Statelessness impacts consistent data handling across sessions.
- **External Dependencies**: Depends on outside resources like model SDKs and vector storage.

**OpenAI's Assistant API** excels in delivering GPTs-like functionalities but comes with its own constraints:

- **Tied Functionalities**: Integrations like tools and retrievals are tied to each assistant, not suitable for multi-tenant applications.
- **Proprietary Limitations**: Restricted to OpenAI models, unsuitable for diverse needs.
- **Customization Limits**: Users cannot customize agent configuration such as memory and retrieval system.

### How OptiSherpa solves the problem 😃

- **Supports both stateful and stateless usages**: Whether to keep track of and manage the message histories and agent conversation sessions, or just make stateless chat completion requests, OptiSherpa has them both covered.
- **Decoupled modular management**: Decoupled the management of tools, RAGs systems, language models from the agent. And allows free combination of these modules to build a powerful AI agent.
- **Multi-tenant support**: OptiSherpa supports fast deployment after development, and can be used in multi-tenant scenarios. No need to worry about the cloud services, just focus on the AI agent development.
- **Unified API**: OptiSherpa provides unified APIs for all the modules, including tools, RAGs systems, language models, and more. Super easy to manage and change the AI agent's configurations.

## What Can You Build with OptiSherpa?

- [x] **Interactive Application Demos**
- [x] **AI Agents for Enterprise Productivity**
- [x] **Multi-Tenant AI-Native Applications for Business**

## Quickstart with Docker

### Prerequisites

- Docker and Docker Compose installed on your machine.
- Git installed for cloning the repository.
- Python environment (above Python 3.8) for running the client SDK.

### Installation

First, clone the OptiSherpa (community edition) repository from GitHub.


Inside the cloned repository, go to the docker directory.

```bash
cd docker
```

1. **Copy `.env.example` to `.env`**:

   ```sh
   cp .env.example .env
   ```

2. **Edit the `.env` file**:
   Open the `.env` file in your favorite text editor and update the necessary configurations. Ensure all required environment variables are set correctly.

3. **Start Docker Compose**:
   Run the following command to start all services:
   ```sh
   docker-compose -p taskingai --env-file .env up -d
   ```

Once the service is up, access the OptiSherpa console through your browser with the URL http://localhost:8080. The default username and password are `admin` and `TaskingAI321`.

### Upgrade

If you have already installed OptiSherpa with a previous version and want to upgrade to the latest version, first update the repository.

```bash
git pull origin master
```

Then stop the current docker service, upgrade to the latest version by pulling the latest image, and finally restart the service.

```bash
cd docker
docker-compose -p taskingai down
docker-compose -p taskingai pull
docker-compose -p taskingai --env-file .env up -d
```

Don't worry about data loss; your data will be automatically migrated to the latest version schema if needed.


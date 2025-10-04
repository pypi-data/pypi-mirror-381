# Examples

**Working examples for django-ipc**

---

## 📁 Structure

```
examples/
├── README.md              # This file
├── basic/                 # 🚀 Basic examples (start here!)
│   ├── simple_server.py           # Minimal WebSocket server
│   └── config_example.py          # Environment configuration
├── codegen/              # 🤖 Code generation examples
│   ├── generate_client_with_config.py  # Generate with env config
│   └── generate_client.py              # Basic generation
├── tests/                # 🧪 Example tests
│   ├── test_server.py             # Server testing
│   └── test_client_config.py      # Client config testing
└── clients/              # 📦 Generated clients (output)
    ├── python/                     # Generated Python client
    └── typescript/                 # Generated TypeScript client
```

---

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd examples
poetry install
# or
pip install -r ../requirements.txt
```

### 2. Run Basic Examples

**Simple Server**:
```bash
poetry run python basic/simple_server.py
```

**Environment Config**:
```bash
poetry run python basic/config_example.py
```

### 3. Generate Clients

**With environment config** (recommended):
```bash
poetry run python codegen/generate_client_with_config.py
```

**Basic generation**:
```bash
poetry run python codegen/generate_client.py
```

### 4. Run Tests

```bash
poetry run pytest tests/ -v
```

---

## 📚 Example Descriptions

### Basic Examples

#### 🔹 basic/simple_server.py
Minimal WebSocket RPC server in ~30 lines.

**What it shows**:
- WebSocket server setup
- Connection manager
- Message router
- Basic RPC handler

**Run**:
```bash
poetry run python basic/simple_server.py
```

#### 🔹 basic/config_example.py
Environment-aware configuration demo.

**What it shows**:
- RPCServerConfig usage
- Multi-environment setup
- Environment detection
- Config validation

**Run**:
```bash
poetry run python basic/config_example.py
```

---

### Code Generation Examples

#### 🔹 codegen/generate_client_with_config.py
**Main example** - Generate clients with environment config.

**What it generates**:
- TypeScript client (10 files)
- Python client (9 files)
- All configs (tsconfig.json, package.json, etc.)
- Complete tooling (ESLint, Prettier)

**Run**:
```bash
poetry run python codegen/generate_client_with_config.py
```

**Output**: `clients/typescript/` and `clients/python/`

#### 🔹 codegen/generate_client.py
Basic client generation without environment config.

**What it shows**:
- Minimal generation
- Router setup
- RPC method definitions

**Run**:
```bash
poetry run python codegen/generate_client.py
```

---

### Test Examples

#### 🔹 tests/test_server.py
WebSocket server testing example.

**What it shows**:
- Server testing
- Connection testing
- Message routing tests
- Handler testing

**Run**:
```bash
poetry run pytest tests/test_server.py -v
```

#### 🔹 tests/test_client_config.py
Client configuration testing.

**What it shows**:
- Environment detection tests
- Config validation
- URL generation
- Factory methods

**Run**:
```bash
poetry run pytest tests/test_client_config.py -v
```

---

## 📦 Generated Clients

After running code generation, you'll have:

### TypeScript Client (10 files)

```
clients/typescript/
├── client.ts           # RPC client
├── types.ts            # TypeScript types
├── index.ts            # Exports
├── tsconfig.json       # TypeScript config
├── package.json        # npm config (8 scripts!)
├── .eslintrc.json      # ESLint config
├── .prettierrc         # Prettier config
├── .gitignore          # Git exclusions
├── .editorconfig       # Editor config
└── README.md           # Documentation
```

**Ready to use**:
```bash
cd clients/typescript
npm install
npm run build
npm run lint
npm run format
```

### Python Client (9 files)

```
clients/python/
├── client.py           # RPC client
├── models.py           # Pydantic models
├── __init__.py         # Package exports
├── requirements.txt    # Dependencies
├── setup.py            # setuptools
├── pyproject.toml      # Modern packaging
├── .gitignore          # Git exclusions
├── .editorconfig       # Editor config
└── README.md           # Documentation
```

**Ready to use**:
```bash
cd clients/python
pip install -e .
```

---

## 🎯 Learning Path

### Beginner
1. Run `basic/simple_server.py` - See minimal server
2. Run `basic/config_example.py` - Understand environment config
3. Read generated `clients/*/README.md` - See what you get

### Intermediate
1. Run `codegen/generate_client_with_config.py` - Generate clients
2. Explore `clients/typescript/` - TypeScript project structure
3. Explore `clients/python/` - Python package structure

### Advanced
1. Modify `codegen/generate_client_with_config.py` - Customize generation
2. Add custom RPC methods - Extend functionality
3. Study `tests/` - See how to test

---

## 🧪 Testing

### Run All Example Tests

```bash
poetry run pytest tests/ -v
```

### Run Specific Test

```bash
poetry run pytest tests/test_server.py -v
poetry run pytest tests/test_client_config.py -v
```

### Run with Coverage

```bash
poetry run pytest tests/ --cov=. --cov-report=html
```

---

## 📋 Requirements

All examples use:
- Python 3.10+
- Redis (for server examples)
- Node.js 16+ (optional, for TypeScript clients)

**Install**:
```bash
# Python dependencies
poetry install

# Redis (macOS)
brew install redis
brew services start redis

# Redis (Docker)
docker run -d -p 6379:6379 redis:7-alpine
```

---

## 🔗 Links

- **Main README**: [../README.md](../README.md)
- **Documentation**: [../docs/INDEX.md](../docs/INDEX.md)
- **Code Generation Guide**: [../docs/guides/code-generation.md](../docs/guides/code-generation.md)
- **Environment-Aware Guide**: [../docs/guides/environment-aware-rpc.md](../docs/guides/environment-aware-rpc.md)

---

## 💡 Tips

### Modify Examples

All examples are **fully editable**. Feel free to:
- Add new RPC methods
- Change environment configs
- Customize generated code
- Experiment with handlers

### Regenerate Clients

After modifying, regenerate:
```bash
poetry run python codegen/generate_client_with_config.py
```

### Check Generated Code Quality

**TypeScript**:
```bash
cd clients/typescript
npm install
npm run lint      # ESLint
npm run format    # Prettier
npm run build     # TypeScript
```

**Python**:
```bash
cd clients/python
python -m py_compile *.py
```

---

## 🐛 Troubleshooting

### Example won't run?

**Check dependencies**:
```bash
poetry install
```

### Redis connection error?

**Start Redis**:
```bash
# macOS
brew services start redis

# Docker
docker run -d -p 6379:6379 redis:7-alpine

# Verify
redis-cli ping  # Should return PONG
```

### Generated clients not working?

**Regenerate**:
```bash
poetry run python codegen/generate_client_with_config.py
```

---

**Happy coding! 🚀**

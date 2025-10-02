       # Commit-Gen - AI-Powered Git Commit Message Generator

[![PyPI version](https://badge.fury.io/py/commit-gen.svg)](https://badge.fury.io/py/commit-gen)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**Generate intelligent commit messages using AI with support for multiple providers including OpenRouter, Ollama, Google Gemini, Mistral AI, and Z.AI.**

## 🚀 Quick Start

### Installation

```bash
pip install commit-gen
```

### First Time Setup

```bash
# Interactive setup wizard (recommended)
commit-gen --setup

# Or manual setup
commit-gen --set-provider openrouter
commit-gen --set-api-key YOUR_API_KEY
```

### Basic Usage

```bash
# Interactive file selection and commit
commit-gen

# Commit specific files
commit-gen --files src/main.py tests/test_main.py

# Commit all files
commit-gen --all

# Commit and push
commit-gen --push
```

## 🔑 API Key Setup

### OpenRouter

**Step 1: Create Account**
1. Visit [OpenRouter](https://openrouter.ai/)
2. Click "Sign Up" and create an account
3. Verify your email address

**Step 2: Get API Key**
1. Go to [OpenRouter API Keys](https://openrouter.ai/keys)
2. Click "Create Key"
3. Give your key a name (e.g., "commit-gen")
4. Copy the generated API key

**Step 3: Configure**
```bash
commit-gen --set-provider openrouter
commit-gen --set-api-key YOUR_OPENROUTER_API_KEY
```

**💡 Tips:**
- OpenRouter provides access to multiple AI models
- Free tier available with limited usage
- Supports models like GPT-4, Claude, and others

### Google Gemini

**Step 1: Create Google Cloud Project**
1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the Gemini API

**Step 2: Enable Gemini API**
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Get API key"
3. Create a new API key
4. Copy the generated key

**Step 3: Configure**
```bash
commit-gen --set-provider gemini
commit-gen --set-api-key YOUR_GEMINI_API_KEY
```

**💡 Tips:**
- Free tier: 15 requests per minute
- Supports models: gemini-2.5-flash, gemini-2.5-pro
- Requires Google Cloud account

### Mistral AI

**Step 1: Create Account**
1. Visit [Mistral AI](https://console.mistral.ai/)
2. Click "Sign Up" and create an account
3. Verify your email address

**Step 2: Get API Key**
1. Go to [Mistral AI Console](https://console.mistral.ai/api-keys/)
2. Click "Create new API key"
3. Give your key a name (e.g., "commit-gen")
4. Copy the generated API key

**Step 3: Configure**
```bash
commit-gen --set-provider mistral
commit-gen --set-api-key YOUR_MISTRAL_API_KEY
```

**💡 Tips:**
- Free tier: 20 requests per minute
- Supports models: mistral-large-latest, mistral-medium-latest
- High-quality reasoning capabilities

### Z.AI

**Step 1: Create Account**
1. Visit the Z.AI Open Platform Quick Start: [Z.AI Quick Start](https://docs.z.ai/guides/overview/quick-start)
2. Register or log in
3. Create an API key in the API Keys page

**Step 2: Configure**
```bash
commit-gen --set-provider zai
commit-gen --set-api-key YOUR_ZAI_API_KEY
# Optional: set model (default: glm-4.6)
commit-gen --set-model glm-4.6
```

**Notes:**
- Endpoint: `https://api.z.ai/api/paas/v4/chat/completions`
- OpenAI-compatible request/response (non-stream)
- See docs: [Z.AI Quick Start](https://docs.z.ai/guides/overview/quick-start)

### Ollama (Local - No API Key Required)

**Step 1: Install Ollama**
```bash
# macOS/Linux
curl -fsSL https://ollama.ai/install.sh | sh

# Windows
# Download from https://ollama.ai/download
```

**Step 2: Start Ollama**
```bash
ollama serve
```

**Step 3: Pull Model**
```bash
ollama pull qwen2.5-coder:7b
```

**Step 4: Configure**
```bash
commit-gen --set-provider ollama
# No API key needed for local Ollama
```

**💡 Tips:**
- Runs locally on your machine
- No internet required after model download
- Free to use
- Supports many open-source models

### Custom Provider

**Step 1: Get API Key**
1. Obtain API key from your custom provider
2. Note the base URL for the provider

**Step 2: Configure**
```bash
commit-gen --set-provider custom
commit-gen --set-api-key YOUR_CUSTOM_API_KEY
commit-gen --set-base-url https://your-provider.com/api/v1
```

## ✨ Key Features

- **🤖 AI-Powered**: Generate commit messages using advanced AI models
- **📁 Interactive File Selection**: Choose which files to commit with arrow key navigation
- **🔧 Multiple AI Providers**: Support for OpenRouter, Ollama, Google Gemini, Mistral AI
- **⚙️ Easy Configuration**: Interactive setup wizard and simple CLI commands
- **📝 Smart Review**: Edit and confirm commit messages before committing
- **🚀 Auto Push**: Optional automatic push to remote repository

## 🛠️ Supported AI Providers

| Provider | Type | Default Model | API Key Required | Free Tier |
|----------|------|---------------|------------------|-----------|
| **OpenRouter** | Cloud | moonshotai/kimi-k2:free | ✅ | ✅ |
| **Ollama** | Local | qwen2.5-coder:7b | ❌ | ✅ |
| **Google Gemini** | Cloud | gemini-2.5-flash | ✅ | ✅ |
| **Mistral AI** | Cloud | mistral-large-2411 | ✅ | ✅ |
| **Z.AI** | Cloud | glm-4.6 | ✅ | Varies |
| **Custom** | Any | Configurable | ✅ | Varies |

## 📖 Usage Examples

### Interactive File Selection

```bash
commit-gen
```

Shows an interactive interface where you can:
- Navigate files with ↑/↓ arrow keys
- Toggle selection with SPACE
- See file status (modified, added, untracked)

### File Selection Interface

When you run `commit-gen` without arguments, you'll see an interactive interface with arrow key navigation:

```
📁 Files to commit:
============================================================
Use ↑/↓ to navigate, SPACE to toggle, ENTER to confirm
a=select all, n=select none, s=skip (stage all), q=quit

📂 CODE:
→ [ ] commit_gen/cli.py (modified, 18KB)
  [x] demo_file2.py (added, 13B) ✅
  [ ] README.md (modified, 9KB)
  [ ] arrow_config.json (untracked, 12B)

Selected: 1/4 files
```

**Navigation Controls:**
- **↑/↓ Arrow Keys**: Navigate through files
- **SPACE**: Toggle file selection (check/uncheck)
- **ENTER**: Confirm selection and proceed
- **a**: Select all files
- **n**: Select none (use only already staged files)
- **s**: Skip selection (stage all files)
- **q**: Quit without committing

**Visual Indicators:**
- **→**: Current cursor position
- **[x]**: Selected file
- **[ ]**: Unselected file
- **✅**: Already staged file
- **Selected: X/Y files**: Shows selection count

**Features:**
- **Status indicators**: Shows if files are modified, added, or untracked
- **Size information**: Displays file sizes
- **Staged markers**: Shows which files are already staged
- **Real-time selection**: See selection count update as you navigate
- **Keyboard navigation**: Intuitive arrow key and spacebar controls

### Commit Confirmation

After selecting files, commit-gen will:

1. **Generate AI commit message**
2. **Show commit message for review**
3. **Allow editing** (with external editor or simple input)
4. **Confirm before committing**

**Commit Review Interface:**
```
🤖 Generating commit message...

📝 Edit commit message:
============================================================
Current commit message:
------------------------------
feat: add interactive file selection with arrow keys

- Implement arrow key navigation for file selection
- Add spacebar toggle for file selection
- Improve UX with visual indicators and real-time feedback
------------------------------

Options:
1. Edit message
2. Use as-is
3. Cancel
```

**Commit Confirmation:**
```
🔍 Commit Review:
============================================================
Commit message:
------------------------------
feat: add interactive file selection with arrow keys

- Implement arrow key navigation for file selection
- Add spacebar toggle for file selection
- Improve UX with visual indicators and real-time feedback
------------------------------

Options:
1. ✅ Yes, commit
2. 🚀 Yes, commit and push
3. ❌ No, go back to editing
4. 🚪 Cancel
```

**Confirmation Options:**
- **Yes, commit**: Commit only
- **Yes, commit and push**: Commit and push to remote
- **No, go back to editing**: Return to edit commit message
- **Cancel**: Exit without committing

**Editing Options:**
- **External Editor**: Uses `$EDITOR` (default: nano)
- **Simple Input**: Fallback if editor not available
- **Validation**: Ensures commit message is not empty

### Quick Commits

```bash
# Commit specific files
commit-gen --files src/main.py tests/test_main.py

# Commit all modified files
commit-gen --all

# Commit and push automatically
commit-gen --push
```

### Provider Configuration

```bash
# Set provider
commit-gen --set-provider gemini

# Set API key
commit-gen --set-api-key YOUR_API_KEY

# Set custom model
commit-gen --set-model gemini-2.5-pro

# View current config
commit-gen --config
```

## 🔧 Configuration

### Interactive Setup (Recommended)

```bash
commit-gen --setup
```

Guides you through:
- Provider selection
- API key configuration
- Model selection
- Connection testing

### Manual Configuration

```bash
# Show available providers
commit-gen --providers

# Configure OpenRouter
commit-gen --set-provider openrouter
commit-gen --set-api-key YOUR_OPENROUTER_KEY

# Configure Ollama (local)
commit-gen --set-provider ollama
# No API key needed for Ollama

# Configure Google Gemini
commit-gen --set-provider gemini
commit-gen --set-api-key YOUR_GEMINI_KEY

# Configure Mistral AI
commit-gen --set-provider mistral
commit-gen --set-api-key YOUR_MISTRAL_KEY

# Configure Z.AI
commit-gen --set-provider zai
commit-gen --set-api-key YOUR_ZAI_KEY
# Optional: set model (default is glm-4.6)
commit-gen --set-model glm-4.6
```

## 🎯 Advanced Features

### Custom Prompts

```bash
# Inline prompt
commit-gen --prompt "Generate a conventional commit message: {changes}"

# Load prompt from file
commit-gen --prompt-file my_prompt.txt

# Save current prompt to file
commit-gen --save-prompt-file my_prompt.txt
```

**Example prompt file (`my_prompt.txt`):**
```
You are an expert developer. Generate a clear, concise commit message based on the following changes:

{changes}

Requirements:
- Use conventional commit format (type: description)
- Keep it under 50 characters for the first line
- Add detailed description if needed
- Focus on what changed and why
- Use present tense ("add" not "added")
- Be specific but concise

Examples:
- feat: add user authentication system
- fix: resolve memory leak in data processing
- docs: update API documentation
- refactor: simplify database query logic
```

### Changelog Generation

```bash
commit-gen --changelog
commit-gen --changelog --compare-branch develop
```

### Debug Mode

```bash
commit-gen --debug
```

### Troubleshooting

### Issue: Command not found after installation

If `commit-gen` command is not found after installation:

1. **Check if symlink exists:**
   ```bash
   ls -la /usr/local/bin/commit-gen
   ```

2. **If symlink is broken, recreate it:**
   ```bash
   sudo ln -s /path/to/your/project/commit-gen.py /usr/local/bin/commit-gen
   ```

3. **For pip installation, check PATH:**
   ```bash
   which commit-gen
   echo $PATH
   ```

### Issue: Configuration files not cleaned up

If configuration files remain after uninstallation:

```bash
rm -rf ~/.config/git-commit-ai/
```

### Issue: API Key Authentication Failed

**Common Solutions:**

1. **Check API Key Format:**
   - Ensure no extra spaces or characters
   - Copy the entire key from provider dashboard

2. **Verify Provider Configuration:**
   ```bash
   commit-gen --config
   ```

3. **Test with Different Model:**
   ```bash
   commit-gen --set-model gpt-4o-mini  # For OpenRouter
   commit-gen --set-model gemini-2.5-flash  # For Gemini
   ```

4. **Check API Key Permissions:**
   - Ensure key has proper permissions
   - Check if key is active in provider dashboard

### Issue: Rate Limiting

**Solutions:**
- **OpenRouter**: Upgrade to paid plan for higher limits
- **Gemini**: Wait for rate limit reset (usually 1 minute)
- **Mistral**: Check usage in Mistral console
- **Ollama**: No rate limits (local usage)

## 📋 Requirements

- **Python**: 3.8 or higher
- **Git**: Working git repository
- **AI Provider**: At least one AI provider configured

## 🙏 Acknowledgments
- Powered by various AI providers
- Inspired by the need for better commit messages

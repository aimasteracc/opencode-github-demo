# OpenCode GitHub Demo

A demonstration repository for OpenCode GitHub agent feature with AI-powered issue handling and code generation.

## 🚀 Features

### OpenCode Integration
- ✅ **Automatic Issue Handling** - AI agents respond to GitHub issues automatically
- ✅ **PR Review** - Automated pull request review and suggestions
- ✅ **Code Generation** - Generate code from issue descriptions
- ✅ **AI-Powered** - Uses Google Gemini Flash model for intelligent responses

### Project Features
- ✅ **Comprehensive Calculator** - Mathematical operations and functions
- ✅ **Extended Functions** - Advanced mathematical capabilities
- ✅ **Full Test Coverage** - 73 test cases with pytest
- ✅ **CI/CD Pipeline** - GitHub Actions workflow for automated testing

## 📊 Calculator Functions

### Core Functions (calculator.py)
| Function | Description | Example |
|----------|-------------|----------|
| `add(a, b)` | Add two numbers | `add(10, 5)` → 15 |
| `subtract(a, b)` | Subtract b from a | `subtract(10, 5)` → 5 |
| `multiply(a, b)` | Multiply two numbers | `multiply(10, 5)` → 50 |
| `divide(a, b)` | Divide a by b | `divide(10, 5)` → 2.0 |
| `power(base, exp)` | Calculate power | `power(2, 8)` → 256 |
| `sqrt(number)` | Square root | `sqrt(16)` → 4.0 |
| `modulo(a, b)` | Calculate remainder | `modulo(10, 3)` → 1 |

### Extended Functions (calculator_extended.py)
| Function | Description | Example |
|----------|-------------|----------|
| `percentage(part, whole)` | Calculate percentage | `percentage(25, 100)` → 25.0% |
| `absolute(value)` | Absolute value | `absolute(-5)` → 5 |
| `maximum(*values)` | Find maximum | `maximum(1, 5, 3)` → 5 |
| `minimum(*values)` | Find minimum | `minimum(1, 5, 3)` → 1 |
| `average(*values)` | Calculate mean | `average(1, 2, 3)` → 2.0 |
| `median(*values)` | Calculate median | `median(1, 5, 3)` → 3.0 |
| `round_number(value, dec)` | Round to decimals | `round_number(3.14159, 2)` → 3.14 |
| `logarithm(value, base)` | Calculate logarithm | `logarithm(100)` → 2.0 |
| `factorial(n)` | Calculate factorial | `factorial(5)` → 120 |
| `is_prime(n)` | Check if prime | `is_prime(7)` → True |

## 🧪 Usage

### Installation

```bash
# Clone the repository
git clone https://github.com/aimasteracc/opencode-github-demo.git

# Navigate to project
cd opencode-github-demo

# Install dependencies
uv run --with pytest pytest

# Run tests
uv run --with pytest pytest -v
```

### Running the Calculator

```bash
# Basic calculator
python calculator.py

# Extended calculator
python calculator_extended.py
```

### OpenCode Integration

1. Create a GitHub issue describing what you want
2. Include `/oc` in your issue or PR comment
3. OpenCode GitHub agent will automatically respond
4. The agent can create PRs to implement features

Example issue:
```markdown
Add a function to calculate Fibonacci sequence
```

The AI agent will automatically generate code and create a pull request.

## 🧪 Testing

### Run All Tests

```bash
# Run original calculator tests
uv run --with pytest pytest test_calculator.py -v

# Run extended calculator tests
uv run --with pytest pytest test_calculator_extended.py -v

# Run all tests
uv run --with pytest pytest -v
```

### Test Coverage

- **Original Calculator**: 30 test cases (100% pass)
- **Extended Calculator**: 43 test cases (100% pass)
- **Total Coverage**: 73 test cases (100% pass)

## 📁 Project Structure

```
opencode-github-demo/
├── calculator.py              # Basic calculator module
├── calculator_extended.py     # Extended calculator with advanced functions
├── test_calculator.py         # Tests for basic calculator
├── test_calculator_extended.py # Tests for extended calculator
├── opencode.json            # AI configuration
├── .github/
│   └── workflows/
│       └── opencode.yml   # GitHub Actions workflow
└── README.md               # This file
```

## 🤖 AI Configuration

The project uses Google Gemini Flash for AI-powered features:

**Model**: `google/gemini-3-flash-preview`
- Context: 1,000,000 tokens
- Output: 65,536 tokens

To use the OpenCode agent feature, set up your API keys in GitHub repository secrets:
- `GOOGLE_GENERATIVE_AI_API_KEY`
- `GEMINI_API_KEY`

## 🎯 How to Use OpenCode Agent

### Triggering the Agent

To trigger the OpenCode agent in your issues or PR comments:

```markdown
/oc Add a function to calculate the greatest common divisor (GCD)
```

The `/oc` prefix signals the OpenCode agent to process your request.

### Example Use Cases

1. **Feature Requests**: Describe a new feature you want
   ```
   /oc Add support for complex number operations
   ```

2. **Bug Reports**: Describe a bug and ask for a fix
   ```
   /oc Fix the division by zero handling to return infinity
   ```

3. **Code Review**: Ask the agent to review your PR
   ```
   /oc Please review this PR and suggest improvements
   ```

4. **Code Generation**: Request specific code snippets
   ```
   /oc Generate a function to parse JSON safely
   ```

## 📈 Continuous Integration

The project uses GitHub Actions for automated testing:

```yaml
name: opencode
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
```

Trigger: Issue or PR comments containing `/oc`

## 🤝 Contributing

Contributions are welcome! Please feel free to:

1. Fork the repository
2. Create a feature branch
3. Add your changes
4. Submit a pull request

### Adding New Functions

1. Add function to `calculator_extended.py`
2. Add tests to `test_calculator_extended.py`
3. Update this README
4. Create a PR with `/oc Add [function name]`

## 📝 License

This project is open source and available for use under the same license as the OpenCode project.

## 🔗 Resources

- [OpenCode Documentation](https://opencode.ai)
- [GitHub Actions Documentation](https://docs.github.com/actions)
- [Google Gemini Documentation](https://ai.google.dev/gemini-api/docs)
- [Pytest Documentation](https://docs.pytest.org/)

---

**Status**: ✅ All tests passing (73/73)
**Last Updated**: 2026-01-27
**Version**: 2.0.0 - Extended Edition

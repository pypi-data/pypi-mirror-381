# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-10-01

### Added
- Initial release of LangGraph A2A Client
- `A2AClientToolProvider` class for managing A2A agent connections
- Three core tools:
  - `a2a_discover_agent`: Discover A2A agents by URL
  - `a2a_list_discovered_agents`: List all discovered agents
  - `a2a_send_message`: Send messages to A2A agents
- Support for push notifications via webhook configuration
- LangChain StructuredTool integration
- Async context manager support
- Comprehensive test suite
- Example usage code
- Full documentation

### Features
- Agent discovery and caching
- Non-streaming message support
- Error handling and logging
- HTTP client connection pooling
- Configurable timeouts
- Push notification configuration

[0.1.0]: https://github.com/yourusername/langgraph-a2a-client-as-tool/releases/tag/v0.1.0

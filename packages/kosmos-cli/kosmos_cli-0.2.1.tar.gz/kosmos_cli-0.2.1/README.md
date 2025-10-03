# Kosmos CLI

A powerful command-line interface for interacting with the Kosmos knowledge base system.

## Installation

```bash
pip install kosmos-cli
```

## Usage

After installation, you can use the `kosmos` command:

```bash
kosmos --help
```

### Available Commands

- `login` - Authenticate with the Kosmos server
- `search` - Search for documents and content
- `read` - Read document content
- `document` - Manage documents
- `asset` - Manage assets
- `job` - Manage background jobs
- `logs` - View system logs

## Configuration

Set environment variables for authentication:

```bash
export KOSMOS_USERNAME=your_username
export KOSMOS_PASSWORD=your_password
export KOSMOS_BASE_URL=https://your-kosmos-server.com
```

## Development

To install from source:

```bash
git clone https://github.com/IndenScale/Kosmos.git
cd Kosmos
pip install -e .
```

## License

MIT License
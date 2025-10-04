[![MseeP.ai Security Assessment Badge](https://mseep.net/pr/nolleh-mcp-vertica-badge.png)](https://mseep.ai/app/nolleh-mcp-vertica)

# MCP Vertica

[![smithery badge](https://smithery.ai/badge/@nolleh/mcp-vertica)](https://smithery.ai/server/@nolleh/mcp-vertica)

A Vertica MCP(model-context-protocol) Server

> [!IMPORTANT]
> If you have troubles to connect this mcp server, try to run `uv cache clean`, and then retry.

### Example: MCP Server Setting

Create or edit the file your mcp client config file with the following content:

#### UVX

```json
{
  "mcpServers": {
    "vertica": {
      "command": "uvx",
      "args": ["mcp-vertica"],
      "env": {
        "VERTICA_HOST": "localhost",
        "VERTICA_PORT": 5433,
        "VERTICA_DATABASE": "VMart",
        "VERTICA_USER": "dbadmin",
        "VERTICA_PASSWORD": "test_password",
        "VERTICA_CONNECTION_LIMIT": 10,
        "VERTICA_SSL": false,
        "VERTICA_SSL_REJECT_UNAUTHORIZED": true
      }
    }
  }
}
```

Or with args

```json
{
  "mcpServers": {
    "vertica": {
      "command": "uvx",
      "args": [
        "mcp-vertica",
        "--host=localhost",
        "--db-port=5433",
        "--database=VMart",
        "--user=dbadmin",
        "--password=test_password",
        "--connection-limit=10"
      ]
    }
  }
}
```


#### Docker
```json
{
  "mcpServers": {
    "vertica": {
      "command": "docker",
      "args": ["run", "-i", "--rm", "nolleh/mcp-vertica"],
      "env": {
        "VERTICA_HOST": "localhost",
        "VERTICA_PORT": 5433,
        "VERTICA_DATABASE": "VMart",
        "VERTICA_USER": "dbadmin",
        "VERTICA_PASSWORD": "test_password",
        "VERTICA_CONNECTION_LIMIT": 10,
        "VERTICA_SSL": false,
        "VERTICA_SSL_REJECT_UNAUTHORIZED": true
      }
    }
  }
}
```


> [!Note]
>
> - For boolean flags like `--ssl` or `--ssl-reject-unauthorized`, simply add the flag (e.g., `"--ssl"`) to enable it, or omit it to disable.
> - For an empty password, use an empty string as shown above.

## Features

### Database Connection Management

- Connection pooling with configurable limits
- SSL/TLS support
- Automatic connection cleanup
- Connection timeout handling

### Query Operations

- Execute SQL queries
- Stream large query results in batches
- Copy data operations
- Transaction management

### Schema Management

- Table structure inspection
- Index management
- View management
- Constraint information
- Column details

### Security Features

- Operation-level permissions (INSERT, UPDATE, DELETE, DDL)
- Schema-specific permissions
- SSL/TLS support
- Password masking in logs

## Tools

### Database Operations

1. `execute_query`

   - Execute SQL queries
   - Support for all SQL operations

2. `stream_query`

   - Stream large query results in batches
   - Configurable batch size

3. `copy_data`
   - Bulk data loading using COPY command
   - Efficient for large datasets

### Schema Management

1. `get_table_structure`

   - Get detailed table structure
   - Column information
   - Constraints

2. `list_indexes`

   - List all indexes for a table
   - Index type and uniqueness
   - Column information

3. `list_views`
   - List all views in a schema
   - View definitions

## Configuration

### Environment Variables

```env
VERTICA_HOST=localhost
VERTICA_PORT=5433
VERTICA_DATABASE=VMart
VERTICA_USER=newdbadmin
VERTICA_PASSWORD=vertica
VERTICA_CONNECTION_LIMIT=10
VERTICA_SSL=false
VERTICA_SSL_REJECT_UNAUTHORIZED=true
```

### Operation Permissions

```env
ALLOW_INSERT_OPERATION=false
ALLOW_UPDATE_OPERATION=false
ALLOW_DELETE_OPERATION=false
ALLOW_DDL_OPERATION=false
```

### Schema Permissions

```env
SCHEMA_INSERT_PERMISSIONS=schema1:true,schema2:false
SCHEMA_UPDATE_PERMISSIONS=schema1:true,schema2:false
SCHEMA_DELETE_PERMISSIONS=schema1:true,schema2:false
SCHEMA_DDL_PERMISSIONS=schema1:true,schema2:false
```

## Installation

### Installing via Smithery

To install Vertica Database Connector for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@nolleh/mcp-vertica):

```bash
npx -y @smithery/cli install @nolleh/mcp-vertica --client claude
```

### Installing Manually

Open your favorite mcp client's config file, then configure with `uvx mcp-vertica`

[Example: Mcp Server Setting](#example%3A-mcp-server-setting)

## Development

#### Appendix: For Testing, VerticaDB Docker Compose Example

```yaml
version: "3.8"

services:
  vertica:
    # image: vertica/vertica-ce:11.1.0-0
    image: vertica/vertica-ce:latest
    platform: linux/amd64
    container_name: vertica-ce
    environment:
      VERTICA_MEMDEBUG: 2
    ports:
      - "5433:5433"
      - "5444:5444"
    volumes:
      - vertica_data:/home/dbadmin/VMart
    healthcheck:
      test:
        [
          "CMD",
          "/opt/vertica/bin/vsql",
          "-h",
          "localhost",
          "-d",
          "VMart",
          "-U",
          "dbadmin",
          "-c",
          "SELECT 1",
        ]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    restart: unless-stopped

volumes:
  vertica_data:
    driver: local
```

Then run server by following instruction [Example: Mcp Server Setting](#example%3A-mcp-server-setting),
Then see everything works as fine

## License

This project is licensed under the MIT License - see the LICENSE file for details.

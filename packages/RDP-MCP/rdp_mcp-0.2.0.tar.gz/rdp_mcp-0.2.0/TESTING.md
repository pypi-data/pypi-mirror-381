# Testing the RiboSeq MCP Server

## Quick Test with Claude Desktop

The easiest way to test is to configure it in Claude Desktop directly.

### Step 1: Configure Claude Desktop

Add to your `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "riboseq": {
      "command": "uvx",
      "args": [
        "--from",
        "/Users/jackt/RiboSeqOrg-DataPortal/rdp-mcp-server",
        "rdp-mcp"
      ]
    }
  }
}
```

### Step 2: Restart Claude Desktop

Completely quit and restart Claude Desktop.

### Step 3: Test in Claude

Look for the 🔌 icon in Claude Desktop that shows connected MCP servers. You should see "riboseq" listed.

Try asking Claude:

- "What tools are available from the riboseq MCP server?"
- "Find some human liver samples in the RiboSeq database"
- "Show me what metadata fields are available"

## Manual Testing (Advanced)

If you want to test the API client without Claude Desktop:

### Create a virtual environment

```bash
cd rdp-mcp-server
python3 -m venv venv
source venv/bin/activate
pip install httpx
```

### Run the test script

```bash
python test_api.py
```

This will test:
1. Getting available fields
2. Querying samples
3. Searching by organism
4. Getting sample details
5. Getting file links

## Testing with MCP Inspector

You can also use the official MCP inspector tool:

```bash
npx @modelcontextprotocol/inspector uvx --from /Users/jackt/RiboSeqOrg-DataPortal/rdp-mcp-server rdp-mcp
```

This will open a web interface where you can manually test each MCP tool.

## Expected Behavior

The MCP server should:
- Connect to https://rdp.ucc.ie without errors
- Return sample data in JSON format
- Provide 5 tools: `query_samples`, `get_sample_details`, `get_file_links`, `search_by_organism`, `list_available_fields`
- Handle errors gracefully if the API is unavailable

## Troubleshooting

### "No such module: httpx"
You need to install dependencies. Either:
- Use uvx (handles this automatically)
- Or create a venv and install: `pip install httpx mcp`

### "Connection refused" or timeout errors
The RiboSeq Data Portal API at https://rdp.ucc.ie may be down or unreachable. Check if the website loads in a browser.

### MCP server doesn't show up in Claude Desktop
- Check JSON syntax in claude_desktop_config.json
- Verify the file path is correct
- Look at Claude Desktop logs for error messages
- Restart Claude Desktop completely

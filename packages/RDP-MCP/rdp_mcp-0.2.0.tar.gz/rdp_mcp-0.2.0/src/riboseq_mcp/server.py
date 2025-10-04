"""MCP Server for RiboSeq Data Portal."""

import asyncio
import json
from typing import Any, Optional

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from .api_client import RiboSeqAPIClient


# Initialize the MCP server
app = Server("RiboSeq Data Portal MCP")

# Global API client
api_client: Optional[RiboSeqAPIClient] = None


@app.list_tools()
async def list_tools() -> list[Tool]:
    """List available MCP tools for querying RiboSeq data."""
    return [
        Tool(
            name="count_samples",
            description=(
                "Count how many samples match the given filters WITHOUT fetching all the data. "
                "This is much more efficient than query_samples when you just need the total count. "
                "Use this for questions like 'how many samples are there for organism X' or "
                "'how many human liver samples exist'. Supports all the same filters as query_samples."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "ScientificName": {
                        "type": "string",
                        "description": "Organism scientific name (e.g., 'Homo sapiens', 'Mus musculus')"
                    },
                    "TISSUE": {
                        "type": "string",
                        "description": "Tissue type (e.g., 'liver', 'brain', 'heart')"
                    },
                    "CELL_LINE": {
                        "type": "string",
                        "description": "Cell line name (e.g., 'HEK293', 'HeLa')"
                    },
                    "INHIBITOR": {
                        "type": "string",
                        "description": "Translation inhibitor used (e.g., 'CHX', 'harringtonine')"
                    },
                    "LIBRARYTYPE": {
                        "type": "string",
                        "description": "Library type (e.g., 'RPF', 'RNA', 'polysome')"
                    },
                    "CONDITION": {
                        "type": "string",
                        "description": "Experimental condition"
                    }
                },
            }
        ),
        Tool(
            name="query_samples",
            description=(
                "Search for ribosome profiling samples in the RiboSeq Data Portal. "
                "You can filter by any metadata field such as organism (ScientificName), "
                "tissue (TISSUE), cell line (CELL_LINE), inhibitor (INHIBITOR), "
                "library type (LIBRARYTYPE), condition (CONDITION), etc. "
                "Returns sample metadata including Run IDs and BioProject accessions. "
                "Supports pagination via offset parameter. Use count_samples first if you need the total count."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "ScientificName": {
                        "type": "string",
                        "description": "Organism scientific name (e.g., 'Homo sapiens', 'Mus musculus')"
                    },
                    "TISSUE": {
                        "type": "string",
                        "description": "Tissue type (e.g., 'liver', 'brain', 'heart')"
                    },
                    "CELL_LINE": {
                        "type": "string",
                        "description": "Cell line name (e.g., 'HEK293', 'HeLa')"
                    },
                    "INHIBITOR": {
                        "type": "string",
                        "description": "Translation inhibitor used (e.g., 'CHX', 'harringtonine')"
                    },
                    "LIBRARYTYPE": {
                        "type": "string",
                        "description": "Library type (e.g., 'RPF', 'RNA', 'polysome')"
                    },
                    "CONDITION": {
                        "type": "string",
                        "description": "Experimental condition"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Maximum number of results to return (default: 100)",
                        "default": 100
                    },
                    "offset": {
                        "type": "number",
                        "description": "Number of results to skip for pagination (default: 0)",
                        "default": 0
                    },
                    "fields": {
                        "type": "string",
                        "description": "Comma-separated list of fields to return (e.g., 'Run,BioProject,TISSUE')"
                    },
                    "paginated": {
                        "type": "boolean",
                        "description": "Return pagination metadata (total, has_more, etc.) Default: false",
                        "default": False
                    }
                },
            }
        ),
        Tool(
            name="get_sample_details",
            description=(
                "Get detailed metadata for a specific sample by its Run accession number "
                "(e.g., 'SRR123456'). Returns all available metadata fields for that sample."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "run_id": {
                        "type": "string",
                        "description": "The Run accession number (e.g., 'SRR123456')"
                    }
                },
                "required": ["run_id"]
            }
        ),
        Tool(
            name="get_file_links",
            description=(
                "Get download links for all data files associated with a sample. "
                "Returns URLs for FASTA reads, BAM files, BigWig files, and QC reports "
                "(FastQC, fastp, RiboMetric, adapter reports)."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "run_id": {
                        "type": "string",
                        "description": "The Run accession number (e.g., 'SRR123456')"
                    }
                },
                "required": ["run_id"]
            }
        ),
        Tool(
            name="list_available_fields",
            description=(
                "Get a list of all metadata fields that can be queried or retrieved. "
                "Useful for discovering what information is available about samples."
            ),
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        Tool(
            name="search_by_organism",
            description=(
                "Search for all ribosome profiling samples from a specific organism. "
                "You can also add additional filters like tissue type, cell line, etc. "
                "Supports pagination via offset parameter."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "organism": {
                        "type": "string",
                        "description": "Scientific name of organism (e.g., 'Homo sapiens', 'Saccharomyces cerevisiae')"
                    },
                    "TISSUE": {
                        "type": "string",
                        "description": "Optional: filter by tissue type"
                    },
                    "CELL_LINE": {
                        "type": "string",
                        "description": "Optional: filter by cell line"
                    },
                    "INHIBITOR": {
                        "type": "string",
                        "description": "Optional: filter by inhibitor"
                    },
                    "limit": {
                        "type": "number",
                        "description": "Maximum number of results (default: 100)",
                        "default": 100
                    },
                    "offset": {
                        "type": "number",
                        "description": "Number of results to skip for pagination (default: 0)",
                        "default": 0
                    },
                    "paginated": {
                        "type": "boolean",
                        "description": "Return pagination metadata (total, has_more, etc.) Default: false",
                        "default": False
                    }
                },
                "required": ["organism"]
            }
        )
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> list[TextContent]:
    """Handle tool calls from the MCP client."""
    global api_client

    if api_client is None:
        api_client = RiboSeqAPIClient()

    try:
        if name == "count_samples":
            # Extract filters only (no limit, offset, fields for counting)
            filters = {k: v for k, v in arguments.items() if v}

            count = await api_client.count_samples(
                filters=filters if filters else None
            )

            return [TextContent(
                type="text",
                text=json.dumps({"count": count}, indent=2)
            )]

        elif name == "query_samples":
            # Extract known parameters
            limit = arguments.pop("limit", 100)
            offset = arguments.pop("offset", 0)
            paginated = arguments.pop("paginated", False)
            fields_str = arguments.pop("fields", None)
            fields = fields_str.split(",") if fields_str else None

            # Remaining arguments are filters
            filters = {k: v for k, v in arguments.items() if v}

            if paginated:
                results = await api_client.query_samples_paginated(
                    filters=filters if filters else None,
                    fields=fields,
                    limit=limit,
                    offset=offset
                )
            else:
                results = await api_client.query_samples(
                    filters=filters if filters else None,
                    fields=fields,
                    limit=limit,
                    offset=offset
                )

            return [TextContent(
                type="text",
                text=json.dumps(results, indent=2)
            )]

        elif name == "get_sample_details":
            run_id = arguments["run_id"]
            result = await api_client.get_sample_by_run(run_id)

            if result is None:
                return [TextContent(
                    type="text",
                    text=f"No sample found with Run ID: {run_id}"
                )]

            return [TextContent(
                type="text",
                text=json.dumps(result, indent=2)
            )]

        elif name == "get_file_links":
            run_id = arguments["run_id"]
            links = await api_client.get_sample_file_links(run_id)

            if not links:
                return [TextContent(
                    type="text",
                    text=f"No sample found with Run ID: {run_id}"
                )]

            # Filter out empty links
            available_links = {k: v for k, v in links.items() if v}

            return [TextContent(
                type="text",
                text=json.dumps(available_links, indent=2)
            )]

        elif name == "list_available_fields":
            fields = await api_client.get_available_fields()

            return [TextContent(
                type="text",
                text=json.dumps(fields, indent=2)
            )]

        elif name == "search_by_organism":
            organism = arguments["organism"]
            limit = arguments.get("limit", 100)
            offset = arguments.get("offset", 0)
            paginated = arguments.get("paginated", False)

            # Extract additional filters
            additional_filters = {
                k: v for k, v in arguments.items()
                if k not in ["organism", "limit", "offset", "paginated"] and v
            }

            if paginated:
                results = await api_client.search_by_organism_paginated(
                    organism=organism,
                    limit=limit,
                    offset=offset,
                    additional_filters=additional_filters if additional_filters else None
                )
            else:
                results = await api_client.search_by_organism(
                    organism=organism,
                    limit=limit,
                    offset=offset,
                    additional_filters=additional_filters if additional_filters else None
                )

            return [TextContent(
                type="text",
                text=json.dumps(results, indent=2)
            )]

        else:
            return [TextContent(
                type="text",
                text=f"Unknown tool: {name}"
            )]

    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error executing tool {name}: {str(e)}"
        )]


async def main():
    """Run the MCP server."""
    global api_client

    async with stdio_server() as (read_stream, write_stream):
        try:
            await app.run(
                read_stream,
                write_stream,
                app.create_initialization_options()
            )
        finally:
            if api_client:
                await api_client.close()


def run():
    """Entry point for the MCP server."""
    asyncio.run(main())


if __name__ == "__main__":
    run()

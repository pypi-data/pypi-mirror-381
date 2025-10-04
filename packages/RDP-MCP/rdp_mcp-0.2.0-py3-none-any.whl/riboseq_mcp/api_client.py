"""API client for the RiboSeq Data Portal."""

import httpx
from typing import Dict, List, Optional, Any, TypedDict


class PaginatedResponse(TypedDict):
    """Paginated response structure."""
    data: List[Dict[str, Any]]
    total: int
    offset: int
    limit: int
    has_more: bool


class RiboSeqAPIClient:
    """Client for interacting with the RiboSeq Data Portal API."""

    def __init__(self, base_url: str = "https://rdp.ucc.ie"):
        """Initialize the API client.

        Args:
            base_url: Base URL of the RiboSeq Data Portal (default: https://rdp.ucc.ie)
        """
        self.base_url = base_url.rstrip('/')
        self.client = httpx.AsyncClient(timeout=30.0)

    async def close(self):
        """Close the HTTP client."""
        await self.client.aclose()

    async def count_samples(
        self,
        filters: Optional[Dict[str, Any]] = None
    ) -> int:
        """Count samples matching filters without fetching data.

        This is much more efficient than fetching all samples just to count them.
        We fetch with limit=1 and then query with a very high limit to get the actual count.

        Args:
            filters: Dictionary of field filters

        Returns:
            Total count of matching samples
        """
        # Fetch with a very high limit to get all results, but only request Run field
        params = {"limit": 999999, "fields": "Run"}

        if filters:
            params.update(filters)

        response = await self.client.get(
            f"{self.base_url}/api/samples/",
            params=params
        )
        response.raise_for_status()
        results = response.json()
        return len(results)

    async def query_samples(
        self,
        filters: Optional[Dict[str, Any]] = None,
        fields: Optional[List[str]] = None,
        limit: int = 100,
        offset: int = 0
    ) -> List[Dict[str, Any]]:
        """Query samples with optional filters.

        Args:
            filters: Dictionary of field filters (e.g., {"ScientificName": "Homo sapiens", "TISSUE": "liver"})
            fields: List of fields to return (if None, returns default fields)
            limit: Maximum number of results to return
            offset: Number of results to skip (for pagination)

        Returns:
            List of sample dictionaries matching the query
        """
        # Since the API doesn't support offset, we fetch more and slice
        fetch_limit = limit + offset
        params = {"limit": fetch_limit}

        if filters:
            params.update(filters)

        if fields:
            params["fields"] = ",".join(fields)

        response = await self.client.get(
            f"{self.base_url}/api/samples/",
            params=params
        )
        response.raise_for_status()
        all_results = response.json()

        # Apply offset by slicing
        return all_results[offset:offset + limit]

    async def query_samples_paginated(
        self,
        filters: Optional[Dict[str, Any]] = None,
        fields: Optional[List[str]] = None,
        limit: int = 100,
        offset: int = 0
    ) -> PaginatedResponse:
        """Query samples with pagination metadata.

        Args:
            filters: Dictionary of field filters
            fields: List of fields to return (if None, returns default fields)
            limit: Maximum number of results to return
            offset: Number of results to skip

        Returns:
            PaginatedResponse with data and metadata
        """
        # Get the actual data
        data = await self.query_samples(filters=filters, fields=fields, limit=limit, offset=offset)

        # Get total count (only if needed - this is expensive)
        # We'll fetch one extra result to determine if there are more
        check_limit = limit + offset + 1
        params = {"limit": check_limit}
        if filters:
            params.update(filters)
        if fields:
            params["fields"] = ",".join(fields)

        response = await self.client.get(
            f"{self.base_url}/api/samples/",
            params=params
        )
        response.raise_for_status()
        all_results = response.json()

        total = len(all_results)
        has_more = len(all_results) > (offset + limit)

        return {
            "data": data,
            "total": min(total, offset + limit + (1 if has_more else 0)),  # Approximate total
            "offset": offset,
            "limit": limit,
            "has_more": has_more
        }

    async def get_available_fields(self) -> List[str]:
        """Get list of all available fields that can be queried.

        Returns:
            List of field names
        """
        response = await self.client.get(f"{self.base_url}/api/samples/fields/")
        response.raise_for_status()
        return response.json()

    async def get_sample_by_run(self, run_id: str) -> Optional[Dict[str, Any]]:
        """Get detailed information for a specific sample by Run ID.

        Args:
            run_id: The Run accession number (e.g., "SRR123456")

        Returns:
            Sample data dictionary or None if not found
        """
        results = await self.query_samples(filters={"Run": run_id}, limit=1)
        return results[0] if results else None

    async def get_sample_file_links(self, run_id: str) -> Dict[str, str]:
        """Get file download links for a specific sample.

        Args:
            run_id: The Run accession number

        Returns:
            Dictionary with file types as keys and URLs as values
        """
        fields = [
            "Run",
            "fastqc_link",
            "fastp_link",
            "adapter_report_link",
            "ribometric_link",
            "reads_link",
            "counts_link",
            "bam_link",
            "bigwig_forward_link",
            "bigwig_reverse_link"
        ]

        sample = await self.query_samples(
            filters={"Run": run_id},
            fields=fields,
            limit=1
        )

        if not sample:
            return {}

        data = sample[0]
        return {
            "run": data.get("Run", ""),
            "fastqc_report": data.get("fastqc_link", ""),
            "fastp_report": data.get("fastp_link", ""),
            "adapter_report": data.get("adapter_report_link", ""),
            "ribometric_report": data.get("ribometric_link", ""),
            "reads_fasta": data.get("reads_link", ""),
            "counts_file": data.get("counts_link", ""),
            "bam_file": data.get("bam_link", ""),
            "bigwig_forward": data.get("bigwig_forward_link", ""),
            "bigwig_reverse": data.get("bigwig_reverse_link", "")
        }

    async def search_by_organism(
        self,
        organism: str,
        limit: int = 100,
        offset: int = 0,
        additional_filters: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """Search samples by organism/species name.

        Args:
            organism: Scientific name of organism (e.g., "Homo sapiens")
            limit: Maximum number of results
            offset: Number of results to skip
            additional_filters: Additional filters to apply

        Returns:
            List of matching samples
        """
        filters = {"ScientificName": organism}
        if additional_filters:
            filters.update(additional_filters)

        return await self.query_samples(filters=filters, limit=limit, offset=offset)

    async def search_by_organism_paginated(
        self,
        organism: str,
        limit: int = 100,
        offset: int = 0,
        additional_filters: Optional[Dict[str, Any]] = None
    ) -> PaginatedResponse:
        """Search samples by organism with pagination metadata.

        Args:
            organism: Scientific name of organism (e.g., "Homo sapiens")
            limit: Maximum number of results
            offset: Number of results to skip
            additional_filters: Additional filters to apply

        Returns:
            PaginatedResponse with data and metadata
        """
        filters = {"ScientificName": organism}
        if additional_filters:
            filters.update(additional_filters)

        return await self.query_samples_paginated(filters=filters, limit=limit, offset=offset)

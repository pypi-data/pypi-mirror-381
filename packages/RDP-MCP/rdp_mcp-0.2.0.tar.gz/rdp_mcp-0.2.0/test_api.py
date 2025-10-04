#!/usr/bin/env python3
"""Quick test of the API client to verify it works."""

import asyncio
import sys
import os

# Add src to path so we can import without installing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from riboseq_mcp.api_client import RiboSeqAPIClient


async def test_api():
    """Test the API client."""
    client = RiboSeqAPIClient()

    try:
        print("Testing API client...")
        print("\n1. Getting available fields...")
        fields = await client.get_available_fields()
        print(f"   Found {len(fields)} fields")
        print(f"   Sample fields: {fields[:10]}")

        print("\n2. Querying samples (limit 3)...")
        samples = await client.query_samples(limit=3)
        print(f"   Found {len(samples)} samples")
        if samples:
            print(f"   First sample Run: {samples[0].get('Run')}")

        print("\n3. Searching for Homo sapiens samples (limit 2)...")
        human_samples = await client.search_by_organism("Homo sapiens", limit=2)
        print(f"   Found {len(human_samples)} samples")
        if human_samples:
            print(f"   First sample: {human_samples[0].get('Run')}")

        print("\n4. Getting sample details...")
        if samples:
            run_id = samples[0].get('Run')
            sample = await client.get_sample_by_run(run_id)
            if sample:
                print(f"   Sample {run_id} - BioProject: {sample.get('BioProject')}")

        print("\n5. Getting file links...")
        if samples:
            run_id = samples[0].get('Run')
            links = await client.get_sample_file_links(run_id)
            available = {k: v for k, v in links.items() if v}
            print(f"   Found {len(available)} file links for {run_id}")
            for link_type, url in list(available.items())[:3]:
                print(f"   - {link_type}: {url[:60]}...")

        print("\n✅ All tests passed!")

    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        await client.close()


if __name__ == "__main__":
    asyncio.run(test_api())

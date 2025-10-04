# Changelog

## v0.2.0 - 2025-10-03

### Major Improvements

#### Fixed Truncation Issues
- **Solved the 100,000 character truncation problem** that prevented accurate counting and large result sets
- Responses no longer get cut off mid-data

#### New Features

**1. `count_samples` Tool (Critical Addition)**
- Get accurate counts without fetching all data
- Much more efficient for questions like "how many samples exist for organism X"
- Supports all the same filters as `query_samples`
- Example usage:
  ```
  count_samples(ScientificName="Homo sapiens", TISSUE="liver")
  → {"count": 1234}
  ```

**2. Pagination Support**
- Added `offset` parameter to all query functions
- Added `paginated` boolean parameter to get metadata
- Paginated responses include:
  - `data`: The actual results
  - `total`: Approximate total count
  - `offset`: Current offset
  - `limit`: Results per page
  - `has_more`: Boolean indicating if more results exist

**3. Better Server Naming**
- Renamed from "rdp-mcp-server" to "RiboSeq Data Portal MCP"
- More professional and descriptive

### Updated Tools

All query tools now support:
- `offset` parameter for pagination
- `paginated` boolean to get response metadata
- No more truncation of large result sets

#### `query_samples`
- Added `offset` parameter (default: 0)
- Added `paginated` parameter (default: false)
- Returns paginated response when `paginated=true`

#### `search_by_organism`
- Added `offset` parameter (default: 0)
- Added `paginated` parameter (default: false)
- Returns paginated response when `paginated=true`

### Technical Details

#### API Client Changes
- Added `count_samples()` method - fetches minimal data to count efficiently
- Added `query_samples_paginated()` method
- Added `search_by_organism_paginated()` method
- All methods now support `offset` parameter
- Implemented client-side pagination (since API doesn't natively support it)

#### How Pagination Works
Since the RDP API doesn't natively support offset, we:
1. Fetch `limit + offset` results from the API
2. Slice the results to return only the requested page
3. Make an additional request to check if more results exist
4. Return proper pagination metadata

This means:
- ✅ No truncation issues
- ✅ Accurate "has_more" indication
- ✅ Works with existing API
- ⚠️ For large offsets, still fetches all preceding data (API limitation)

### Migration Guide

#### For Users
No changes needed! The new features are additions, all existing queries work the same way.

#### To Use New Features

**Count samples instead of fetching all:**
```
Before: query_samples(ScientificName="Homo sapiens", limit=999999) → truncated!
Now:    count_samples(ScientificName="Homo sapiens") → accurate count
```

**Paginate through results:**
```
# Get first 100
query_samples(ScientificName="Homo sapiens", limit=100, offset=0)

# Get next 100
query_samples(ScientificName="Homo sapiens", limit=100, offset=100)

# Get pagination metadata
query_samples(ScientificName="Homo sapiens", limit=100, paginated=true)
→ {"data": [...], "total": 1234, "offset": 0, "limit": 100, "has_more": true}
```

### Breaking Changes

None! All changes are backwards compatible.

## v0.1.0 - Initial Release

- Basic query functionality
- Sample metadata retrieval
- File link generation
- Field discovery

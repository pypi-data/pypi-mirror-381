#!/usr/bin/env python3
"""Foreman MCP Server - Provides Foreman API access through MCP protocol."""

import os
import requests
from requests.auth import HTTPBasicAuth
from mcp.server.fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("Foreman Server")

def get_foreman_config():
    """Get Foreman configuration from environment variables"""
    base_url = os.getenv('FOREMAN_URL')
    username = os.getenv('FOREMAN_USERNAME')
    password = os.getenv('FOREMAN_PASSWORD')
    verify_ssl = os.getenv('FOREMAN_VERIFY_SSL', 'true').lower() == 'true'

    if not base_url:
        raise ValueError("FOREMAN_URL environment variable is required")
    if not username or not password:
        raise ValueError("FOREMAN_USERNAME and FOREMAN_PASSWORD environment variables are required")

    return {
        'base_url': base_url.rstrip('/'),
        'auth': HTTPBasicAuth(username, password),
        'verify_ssl': verify_ssl
    }

def filter_fields(data, include_fields=None, exclude_fields=None):
    """Filter fields from API response data to reduce context window usage.

    Args:
        data: API response data (dict or list of dicts)
        include_fields: List of fields to keep (if specified, only these are kept)
        exclude_fields: List of fields to remove (ignored if include_fields is specified)
    """
    if not isinstance(data, (dict, list)):
        return data

    def filter_single_item(item):
        if not isinstance(item, dict):
            return item

        if include_fields:
            return {k: v for k, v in item.items() if k in include_fields}
        if exclude_fields:
            return {k: v for k, v in item.items() if k not in exclude_fields}
        return item

    if isinstance(data, list):
        return [filter_single_item(item) for item in data]
    return filter_single_item(data)

@mcp.tool()
def list_hosts(search: str = "", per_page: int = 10, page: int = 1,
               include_fields: str = "") -> dict:
    """List hosts from Foreman with optional search filter and field filtering.

    CONTEXT OPTIMIZATION: Default per_page=10 to prevent overflow.
    Use search filters like 'location ~ SYD03' or 'os ~ Windows' to narrow results.
    Total hosts available: ~1000+. Always use search parameter for large inventories.

    Field filtering: By default returns essential fields only (id, name, ip, os, location, status).
    Use include_fields="all" for complete data, or specify comma-separated fields
    like "id,name,ip,mac".
    """
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/v2/hosts"

        params = {
            'per_page': per_page,
            'page': page
        }

        if search:
            params['search'] = search

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        result = response.json()

        # Apply field filtering to reduce context window usage
        if include_fields == "all":
            # Return all fields
            pass
        elif include_fields:
            # Return specified fields
            fields = [f.strip() for f in include_fields.split(',')]
            result['results'] = filter_fields(result['results'], include_fields=fields)
        else:
            # Default essential fields for hosts
            essential_fields = [
                'id', 'name', 'ip', 'operatingsystem_name', 'location_name',
                'global_status_label', 'hostgroup_name', 'environment_name',
                'last_report', 'build_status_label'
            ]
            result['results'] = filter_fields(result['results'], include_fields=essential_fields)

        return result

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list hosts: {str(e)}"}

@mcp.tool()
def get_host(host_id: str) -> dict:
    """Get detailed information about a specific host"""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/v2/hosts/{host_id}"

        response = requests.get(url, auth=config['auth'], verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to get host {host_id}: {str(e)}"}

@mcp.tool()
def search_hosts_by_location(location: str, per_page: int = 10) -> dict:
    """Search hosts by location (e.g., 'SYD03', 'MEL03').

    CONTEXT OPTIMIZATION: Returns max 10 results by default.
    Use specific location codes for best results."""
    search_query = f"location ~ {location}"
    return list_hosts(search=search_query, per_page=per_page)

@mcp.tool()
def search_hosts_by_os(os_name: str, per_page: int = 10) -> dict:
    """Search hosts by operating system (e.g., 'Windows', 'Oracle Linux').

    CONTEXT OPTIMIZATION: Returns max 10 results by default.
    Use specific OS names like 'Windows Server 2022' for targeted results."""
    search_query = f"os ~ {os_name}"
    return list_hosts(search=search_query, per_page=per_page)

@mcp.tool()
def search_hosts_by_environment(environment: str, per_page: int = 10) -> dict:
    """Search hosts by environment (e.g., 'production', 'development').

    CONTEXT OPTIMIZATION: Returns max 10 results by default."""
    search_query = f"environment = {environment}"
    return list_hosts(search=search_query, per_page=per_page)


@mcp.tool()
def list_organizations(per_page: int = 15) -> dict:
    """List all organizations in Foreman.

    CONTEXT OPTIMIZATION: Typically <20 organizations. Safe for context window."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/katello/api/organizations"

        params = {'per_page': per_page}

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list organizations: {str(e)}"}


@mcp.tool()
def list_locations(per_page: int = 15) -> dict:
    """List all locations in Foreman.

    CONTEXT OPTIMIZATION: Typically <30 locations. Safe for context window."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/locations"

        params = {'per_page': per_page}

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list locations: {str(e)}"}


@mcp.tool()
def list_hostgroups(per_page: int = 15) -> dict:
    """List all hostgroups in Foreman.

    CONTEXT OPTIMIZATION: Can be 50+ hostgroups. Consider using search if available."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/hostgroups"

        params = {'per_page': per_page}

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list hostgroups: {str(e)}"}


@mcp.tool()
def search_hosts_by_hostgroup(hostgroup: str, per_page: int = 10) -> dict:
    """Search hosts by hostgroup name or title.

    CONTEXT OPTIMIZATION: Returns max 10 results by default."""
    search_query = f"hostgroup ~ {hostgroup}"
    return list_hosts(search=search_query, per_page=per_page)


@mcp.tool()
def get_host_status(host_id: str) -> dict:
    """Get status information for a specific host."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/hosts/{host_id}/status"

        response = requests.get(url, auth=config['auth'], verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to get host status for {host_id}: {str(e)}"}


@mcp.tool()
def search_hosts_by_fact(fact_name: str, fact_value: str, per_page: int = 10) -> dict:
    """Search hosts by a specific fact name and value.

    CONTEXT OPTIMIZATION: Returns max 10 results by default."""
    search_query = f"facts.{fact_name} = {fact_value}"
    return list_hosts(search=search_query, per_page=per_page)


@mcp.tool()
def list_subnets(per_page: int = 15) -> dict:
    """List all subnets in Foreman.

    CONTEXT OPTIMIZATION: Network subnets typically <50. Safe for context window."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/subnets"

        params = {'per_page': per_page}

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list subnets: {str(e)}"}


@mcp.tool()
def get_subnet(subnet_id: str) -> dict:
    """Get detailed information about a specific subnet."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/subnets/{subnet_id}"

        response = requests.get(url, auth=config['auth'], verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to get subnet {subnet_id}: {str(e)}"}


@mcp.tool()
def list_domains(per_page: int = 15) -> dict:
    """List all domains in Foreman.

    CONTEXT OPTIMIZATION: DNS domains typically <30. Safe for context window."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/domains"

        params = {'per_page': per_page}

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list domains: {str(e)}"}


@mcp.tool()
def get_domain(domain_id: str) -> dict:
    """Get detailed information about a specific domain."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/domains/{domain_id}"

        response = requests.get(url, auth=config['auth'], verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to get domain {domain_id}: {str(e)}"}


@mcp.tool()
def list_smart_proxies(per_page: int = 15) -> dict:
    """List all smart proxies in Foreman.

    CONTEXT OPTIMIZATION: Smart proxies typically <20. Safe for context window."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/smart_proxies"

        params = {'per_page': per_page}

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list smart proxies: {str(e)}"}


@mcp.tool()
def get_smart_proxy(proxy_id: str) -> dict:
    """Get detailed information about a specific smart proxy."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/smart_proxies/{proxy_id}"

        response = requests.get(url, auth=config['auth'], verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to get smart proxy {proxy_id}: {str(e)}"}


@mcp.tool()
def list_operatingsystems(per_page: int = 15) -> dict:
    """List all operating systems in Foreman.

    CONTEXT OPTIMIZATION: 67 total OS entries. Use per_page=5-10 for quick overview."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/v2/operatingsystems"

        params = {'per_page': per_page}

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list operating systems: {str(e)}"}


@mcp.tool()
def get_operatingsystem(os_id: str) -> dict:
    """Get detailed information about a specific operating system."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/v2/operatingsystems/{os_id}"

        response = requests.get(url, auth=config['auth'], verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to get operating system {os_id}: {str(e)}"}


@mcp.tool()
def list_architectures(per_page: int = 10) -> dict:
    """List all architectures in Foreman.

    CONTEXT OPTIMIZATION: Only 6 architectures total. Safe for context window."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/v2/architectures"

        params = {'per_page': per_page}

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list architectures: {str(e)}"}


@mcp.tool()
def get_architecture(arch_id: str) -> dict:
    """Get detailed information about a specific architecture."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/v2/architectures/{arch_id}"

        response = requests.get(url, auth=config['auth'], verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to get architecture {arch_id}: {str(e)}"}


@mcp.tool()
def list_media(per_page: int = 15) -> dict:
    """List all installation media in Foreman.

    CONTEXT OPTIMIZATION: 22 total media entries. Safe for context window."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/v2/media"

        params = {'per_page': per_page}

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list media: {str(e)}"}


@mcp.tool()
def get_media(media_id: str) -> dict:
    """Get detailed information about a specific installation media."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/api/v2/media/{media_id}"

        response = requests.get(url, auth=config['auth'], verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to get media {media_id}: {str(e)}"}


@mcp.tool()
def list_content_views(per_page: int = 10, include_fields: str = "") -> dict:
    """List all content views in Foreman/Katello with field filtering.

    CONTEXT OPTIMIZATION: 102 total content views! Use per_page=5-10 max.
    Each content view has extensive metadata. Consider getting specific CV by ID.

    Field filtering: By default returns essential fields only
    (id, name, version_count, latest_version).
    Use include_fields="all" for complete data, or specify comma-separated fields."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/katello/api/content_views"

        params = {'per_page': per_page}

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        result = response.json()

        # Apply field filtering to reduce context window usage
        if include_fields == "all":
            # Return all fields
            pass
        elif include_fields:
            # Return specified fields
            fields = [f.strip() for f in include_fields.split(',')]
            result['results'] = filter_fields(result['results'], include_fields=fields)
        else:
            # Default essential fields for content views
            essential_fields = [
                'id', 'name', 'version_count', 'latest_version', 'composite',
                'default', 'organization'
            ]
            result['results'] = filter_fields(result['results'], include_fields=essential_fields)

        return result

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list content views: {str(e)}"}


@mcp.tool()
def get_content_view(cv_id: str) -> dict:
    """Get detailed information about a specific content view."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/katello/api/content_views/{cv_id}"

        response = requests.get(url, auth=config['auth'], verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to get content view {cv_id}: {str(e)}"}


@mcp.tool()
def list_repositories(per_page: int = 5, include_fields: str = "") -> dict:
    """List all repositories in Foreman/Katello with field filtering.

    ⚠️  CONTEXT WARNING: 258 total repositories with extensive metadata!
    Use per_page=5 max or context will overflow. Consider specific repo searches.

    Field filtering: By default returns essential fields only
    (id, name, content_type, url, product).
    Use include_fields="all" for complete data, or specify comma-separated fields."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/katello/api/repositories"

        params = {'per_page': per_page}

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        result = response.json()

        # Apply field filtering to reduce context window usage
        if include_fields == "all":
            # Return all fields
            pass
        elif include_fields:
            # Return specified fields
            fields = [f.strip() for f in include_fields.split(',')]
            result['results'] = filter_fields(result['results'], include_fields=fields)
        else:
            # Default essential fields for repositories
            essential_fields = [
                'id', 'name', 'content_type', 'url', 'product', 'content_view',
                'last_sync', 'content_counts'
            ]
            result['results'] = filter_fields(result['results'], include_fields=essential_fields)

        return result

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list repositories: {str(e)}"}


@mcp.tool()
def get_repository(repo_id: str) -> dict:
    """Get detailed information about a specific repository."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/katello/api/repositories/{repo_id}"

        response = requests.get(url, auth=config['auth'], verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to get repository {repo_id}: {str(e)}"}


@mcp.tool()
def list_lifecycle_environments(organization_id: str, per_page: int = 15,
                               include_fields: str = "") -> dict:
    """List all lifecycle environments for a specific organization in Foreman/Katello.

    CONTEXT OPTIMIZATION: 16 total environments. Safe for context window.

    Args:
        organization_id: Required numeric organization ID (e.g., "1", "4").
                        Organization names are not supported by this endpoint.
        per_page: Number of results per page.
        include_fields: Field filtering options.

    Field filtering: By default returns essential fields only (id, name, description, library).
    Use include_fields="all" for complete data, or specify comma-separated fields."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/katello/api/organizations/{organization_id}/environments"

        params = {'per_page': per_page}

        response = requests.get(url, auth=config['auth'], params=params,
                              verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        result = response.json()

        # Apply field filtering to reduce context window usage
        if include_fields == "all":
            # Return all fields
            pass
        elif include_fields:
            # Return specified fields
            fields = [f.strip() for f in include_fields.split(',')]
            result['results'] = filter_fields(result['results'], include_fields=fields)
        else:
            # Default essential fields for lifecycle environments
            essential_fields = [
                'id', 'name', 'label', 'description', 'library',
                'organization', 'prior', 'successor'
            ]
            result['results'] = filter_fields(result['results'], include_fields=essential_fields)

        return result

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to list lifecycle environments for org "
                         f"{organization_id}: {str(e)}"}


@mcp.tool()
def get_lifecycle_environment(env_id: str) -> dict:
    """Get detailed information about a specific lifecycle environment."""
    try:
        config = get_foreman_config()
        url = f"{config['base_url']}/katello/api/environments/{env_id}"

        response = requests.get(url, auth=config['auth'], verify=config['verify_ssl'], timeout=30)
        response.raise_for_status()

        return response.json()

    except (requests.RequestException, ValueError) as e:
        return {"error": f"Failed to get lifecycle environment {env_id}: {str(e)}"}

def main() -> None:
    """Main entry point for the server."""
    mcp.run()


if __name__ == "__main__":
    main()

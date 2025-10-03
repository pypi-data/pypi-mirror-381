"""Shared MCP tools for both local and remote servers."""

from typing import List, Optional

from mcp.server.fastmcp import Context
from mcp.server.session import ServerSession
from point_topic_mcp.core.context_assembly import list_datasets, assemble_context  
from point_topic_mcp.core.utils import dynamic_docstring



def register_tools(mcp):
    """Register all MCP tools on the provided FastMCP instance."""
    
    @mcp.tool()
    @dynamic_docstring([("{DATASETS}", list_datasets)])
    def assemble_dataset_context(
        dataset_names: List[str], 
        ctx: Optional[Context[ServerSession, None]] = None
    ) -> str:
        """
        Assemble full context (instructions, schema, examples) for one or more datasets.

        This is essential before executing a query, for the agent to understand how to query the datasets.
        
        Args:
            dataset_names: List of dataset names to include (e.g., ['upc', 'upc_take_up'])
        
        {DATASETS}
        
        Returns the complete context needed for querying these datasets.
        """
        # Check if user is authenticated and apply dataset restrictions

        return assemble_context(dataset_names)

    @mcp.tool()
    def execute_query(
        sql_query: str, 
        ctx: Optional[Context[ServerSession, None]] = None
    ) -> str:
        """
        Execute safe SQL queries against the Snowflake database.
        Only read-only queries allowed (SELECT, WITH, SHOW, DESCRIBE, EXPLAIN).
        
        Multiple queries can be executed in one call by separating them with semicolons (;).
        Each query will be validated and executed separately, with clearly labeled results.
        
        Args:
            sql_query: The SQL query or queries to execute (separated by semicolons for multiple queries)
            
        Returns:
            Query results in CSV format or error message.
            For multiple queries, results are clearly separated with query labels.
            
        Examples:
            Single query: "SELECT COUNT(*) FROM table1"
            Multiple queries: "SELECT COUNT(*) FROM table1; SELECT AVG(price) FROM table2; SHOW TABLES"
        """
        from point_topic_mcp.connectors.snowflake import SnowflakeDB

        sf = SnowflakeDB()
        sf.connect()
        
        # Use the new multi-query method that handles both single and multiple queries
        result = sf.execute_safe_queries(sql_query)
        
        sf.close_connection()
        return result

    @mcp.tool()
    def describe_table(table_name: str,ctx: Optional[Context[ServerSession, None]] = None) -> str:
        """
        Describe a table in the Snowflake database.

        Note the schema is already included in the assemble context function

        Args:
            table_name: The name of the table to describe. 
            Use the full database and schema name.
            e.g. "upc_core.reports.upc_output"

        Returns:
            The schema as CSV string
        """
        from point_topic_mcp.connectors.snowflake import SnowflakeDB
        sf = SnowflakeDB()
        sf.connect()
        result = sf.describe_table(table_name)
        sf.close_connection()
        return result

    @mcp.tool()
    def get_la_code(la_name: str,ctx: Optional[Context[ServerSession, None]] = None) -> str:
        """
        Get the LA code for a given LA name.

        Args:
            la_name: The name of the LA to get the code for

        Returns:
            The LA code for the given LA name

        Example:
            get_la_code("Westminster") -> "E09000033"
        """
        from point_topic_mcp.connectors.snowflake import SnowflakeDB

        sql_query = f"select distinct la_code from upc_core.reports.upc_output where lower(la_name) like lower('{la_name}')"
        sf = SnowflakeDB()
        sf.connect()
        result = sf.execute_safe_query(sql_query)
        sf.close_connection()
        return result

    @mcp.tool()
    def get_la_list_full(la_name: str,ctx: Optional[Context[ServerSession, None]] = None) -> str:
        """
        Get the full list of LA codes and names.

        Can be used if the get_la_code tool doesn't match the LA name.

        Returns the full list of LA codes and names in CSV format.
        """
        from point_topic_mcp.connectors.snowflake import SnowflakeDB

        sql_query = f"select distinct la_code, la_name from upc_core.reports.upc_output"
        sf = SnowflakeDB()
        sf.connect()
        result = sf.execute_safe_query(sql_query)
        sf.close_connection()
        return result

    @mcp.tool()
    def get_point_topic_public_chart_catalog(ctx: Optional[Context[ServerSession, None]] = None) -> str:
        """Get all available public charts from the Point Topic Charts API.
        
        Fetches the public chart catalog from https://charts.point-topic.com/public
        which includes chart metadata, available parameters, and example URLs for
        embedding visualizations.
        
        Returns:
            JSON string containing chart catalog with structure including project names,
            chart titles, tags, required parameters, and example URLs for HTML/PNG/CSV formats.
        """
        import requests
        import json
        response = requests.get("https://charts.point-topic.com/public")
        return json.dumps(response.json())
    
    @mcp.tool()
    def get_point_topic_public_chart_csv(url: str,ctx: Optional[Context[ServerSession, None]] = None) -> str:
        """Get a specific chart from Point Topic Charts API for context.
        
        When displaying charts to the user in an iframe, use this tool to see
        the chart contents and provide context. The user can only see charts if
        you embed them as iframes without the format parameter.
        
        Strategy: Embed the iframe first, then give some context about the chart
        with the info returned by this tool.
        
        Args:
            url: Chart URL WITHOUT the format parameter (e.g., no &format=png/csv).
        
        Returns: csv string
        """
        import urllib.parse
        import requests

        # strip any existing format param and add format=csv
        parsed = urllib.parse.urlparse(url)
        query = urllib.parse.parse_qs(parsed.query)
        query.pop('format', None)
        query['format'] = 'csv'
        csv_url = urllib.parse.urlunparse(parsed._replace(query=urllib.parse.urlencode(query, doseq=True)))

        resp = requests.get(csv_url)
        if resp.status_code != 200:
            return f"Error: {resp.status_code} {resp.text}"
        
        return resp.text
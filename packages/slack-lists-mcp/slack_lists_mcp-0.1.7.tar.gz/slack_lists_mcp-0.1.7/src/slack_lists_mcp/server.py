"""FastMCP server for Slack Lists API operations."""

import logging
from typing import Any

from fastmcp import Context, FastMCP

from slack_lists_mcp.config import get_settings
from slack_lists_mcp.slack_client import SlackListsClient

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize settings
settings = get_settings()

# Configure logging level from settings
logging.getLogger().setLevel(getattr(logging, settings.log_level.upper()))

# Initialize FastMCP server
mcp = FastMCP(
    name=settings.mcp_server_name,
    version=settings.mcp_server_version,
)

# Initialize Slack client
slack_client = SlackListsClient()


@mcp.tool
async def add_list_item(
    initial_fields: list[dict[str, Any]],
    list_id: str | None = None,
    ctx: Context = None,
) -> dict[str, Any]:
    """Add a new item to a Slack list.

    Args:
        initial_fields: List of field dictionaries. Each field needs:
                       - column_id: The column ID
                       - Value in appropriate format (rich_text, user, date, select, checkbox, etc.)
        list_id: The ID of the list (optional, uses DEFAULT_LIST_ID env var if not provided)
                 When DEFAULT_LIST_ID is set, you can omit this parameter entirely
        ctx: FastMCP context (automatically injected)

    Returns:
        The created item or error information

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            await ctx.info(
                f"Adding item to list {list_id} with {len(initial_fields)} fields",
            )

        result = await slack_client.add_item(
            list_id=list_id,
            initial_fields=initial_fields,
        )

        if ctx:
            await ctx.info(f"Successfully added item to list {list_id}")

        return {
            "success": True,
            "item": result,
        }

    except Exception as e:
        logger.error(f"Error adding item: {e}")
        if ctx:
            await ctx.error(f"Failed to add item: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


@mcp.tool
async def update_list_item(
    cells: list[dict[str, Any]],
    list_id: str | None = None,
    ctx: Context = None,
) -> dict[str, Any]:
    """Update items in a Slack list.

    Use get_list_structure first to understand the column IDs and types.

    Args:
        cells: List of cell dictionaries. Each cell needs:
               - row_id: The item ID to update
               - column_id: The column ID
               - Value in appropriate format (rich_text, user, date, select, checkbox, etc.)
        list_id: The ID of the list (optional, uses DEFAULT_LIST_ID env var if not provided)
                 When DEFAULT_LIST_ID is set, you can omit this parameter entirely
        ctx: FastMCP context (automatically injected)

    Returns:
        Success status or error information


    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            await ctx.info(f"Updating items in list {list_id} with {len(cells)} cells")

        result = await slack_client.update_item(
            list_id=list_id,
            cells=cells,
        )

        if ctx:
            await ctx.info(f"Successfully updated items in list {list_id}")

        return result

    except Exception as e:
        logger.error(f"Error updating items: {e}")
        if ctx:
            await ctx.error(f"Failed to update items: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


@mcp.tool
async def delete_list_item(
    item_id: str,
    list_id: str | None = None,
    ctx: Context = None,
) -> dict[str, Any]:
    """Delete an item from a Slack list.

    Args:
        item_id: The ID of the item to delete
        list_id: The ID of the list containing the item (optional, uses DEFAULT_LIST_ID env var if not provided)
        ctx: FastMCP context (automatically injected)

    Returns:
        Deletion confirmation or error information

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            await ctx.info(f"Deleting item {item_id} from list {list_id}")

        await slack_client.delete_item(
            list_id=list_id,
            item_id=item_id,
        )

        if ctx:
            await ctx.info(f"Successfully deleted item {item_id}")

        return {
            "success": True,
            "deleted": True,
            "item_id": item_id,
            "list_id": list_id,
        }

    except Exception as e:
        logger.error(f"Error deleting list item: {e}")
        if ctx:
            await ctx.error(f"Failed to delete item: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


@mcp.tool
async def get_list_item(
    item_id: str,
    list_id: str | None = None,
    ctx: Context = None,
    include_is_subscribed: bool = False,
) -> dict[str, Any]:
    """Get a specific item from a Slack list.

    Args:
        item_id: The ID of the item to retrieve
        list_id: The ID of the list containing the item (optional, uses DEFAULT_LIST_ID env var if not provided)
        include_is_subscribed: Whether to include subscription status
        ctx: FastMCP context (automatically injected)

    Returns:
        The item data including list metadata and subtasks or error information

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            await ctx.info(f"Retrieving item {item_id} from list {list_id}")

        result = await slack_client.get_item(
            list_id=list_id,
            item_id=item_id,
            include_is_subscribed=include_is_subscribed,
        )

        if ctx:
            await ctx.info(f"Successfully retrieved item {item_id}")

        return {
            "success": True,
            "item": result.get("item", {}),
            "list_metadata": result.get("list", {}).get("list_metadata", {}),
            "subtasks": result.get("subtasks", []),
        }

    except Exception as e:
        logger.error(f"Error getting list item: {e}")
        if ctx:
            await ctx.error(f"Failed to get item: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


@mcp.tool
async def list_items(
    list_id: str | None = None,
    limit: int | None = 100,
    cursor: str | None = None,
    archived: bool | None = None,
    filters: dict[str, dict[str, Any]] | None = None,
    ctx: Context = None,
) -> dict[str, Any]:
    """List all items in a Slack list with optional filtering.

    Args:
        list_id: The ID of the list to retrieve items from (optional, uses DEFAULT_LIST_ID env var if not provided)
        limit: Maximum number of items to return (default: 100)
        cursor: Pagination cursor for next page
        archived: Whether to return archived items (True) or normal items (False/None)
        filters: Column filters. Keys are column IDs or keys, values are filter conditions.
                Supported operators: equals, not_equals, contains, not_contains, in, not_in
        ctx: FastMCP context (automatically injected)

    Returns:
        List of items with pagination info or error information

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            filter_desc = f" with {len(filters)} filters" if filters else ""
            await ctx.info(f"Listing items from list {list_id}{filter_desc}")

        response = await slack_client.list_items(
            list_id=list_id,
            limit=limit or 100,
            cursor=cursor,
            archived=archived,
            filters=filters,
        )

        if ctx:
            await ctx.info(
                f"Retrieved {len(response.get('items', []))} items from list {list_id}",
            )

        return {
            "success": True,
            "items": response.get("items", []),
            "has_more": response.get("has_more", False),
            "next_cursor": response.get("next_cursor"),
            "total": response.get("total"),
        }

    except Exception as e:
        logger.error(f"Error listing items: {e}")
        if ctx:
            await ctx.error(f"Failed to list items: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


@mcp.tool
async def get_list_info(
    list_id: str | None = None,
    ctx: Context = None,
) -> dict[str, Any]:
    """Get information about a Slack list.

    Args:
        list_id: The ID of the list (optional, uses DEFAULT_LIST_ID env var if not provided)
        ctx: FastMCP context (automatically injected)

    Returns:
        The list information or error information

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            await ctx.info(f"Retrieving information for list {list_id}")

        result = await slack_client.get_list(list_id=list_id)

        if ctx:
            await ctx.info("Successfully retrieved list information")

        return {
            "success": True,
            "list": result,
        }

    except Exception as e:
        logger.error(f"Error getting list info: {e}")
        if ctx:
            await ctx.error(f"Failed to get list info: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


@mcp.tool
async def get_list_structure(
    list_id: str | None = None,
    ctx: Context = None,
) -> dict[str, Any]:
    """Get the structure and column information of a Slack list.

    Args:
        list_id: The ID of the list (optional, uses DEFAULT_LIST_ID env var if not provided)
        ctx: FastMCP context (automatically injected)

    Returns:
        The list structure including columns and their configurations

    """
    try:
        # Use default list ID from environment if not provided
        if list_id is None:
            list_id = settings.default_list_id
            if list_id is None:
                return {
                    "success": False,
                    "error": "list_id is required. Either provide it as parameter or set DEFAULT_LIST_ID environment variable.",
                }

        if ctx:
            await ctx.info(f"Analyzing structure for list {list_id}")

        # Get list items to find any item ID, then use items.info to get schema
        items_response = await slack_client.list_items(
            list_id=list_id,
            limit=1,  # We just need one item to get the schema
        )

        # If we have any item, use items.info to get the full schema
        if items_response.get("items") and len(items_response["items"]) > 0:
            first_item = items_response["items"][0]
            item_id = first_item.get("id")

            # Get item info which includes list metadata with schema
            item_info_response = await slack_client.get_item(
                list_id=list_id,
                item_id=item_id,
            )

            # Extract schema from list metadata
            list_data = item_info_response.get("list", {})
            list_metadata = list_data.get("list_metadata", {})
            schema = list_metadata.get("schema", [])

            # Build column mapping from schema
            columns = {}
            for column in schema:
                col_id = column.get("id")
                if col_id:
                    columns[col_id] = {
                        "id": col_id,
                        "name": column.get("name"),
                        "key": column.get("key"),
                        "type": column.get("type"),
                        "is_primary": column.get("is_primary_column", False),
                        "options": column.get("options", {}),
                    }

            # Find the name/title column
            name_column = None
            for col_id, col_info in columns.items():
                if col_info.get("is_primary") or col_info.get("key") in [
                    "name",
                    "title",
                    "todo_name",
                ]:
                    name_column = col_id
                    break

            if ctx:
                await ctx.info(f"Found {len(columns)} columns in list schema")

            return {
                "success": True,
                "structure": {
                    "list_id": list_id,
                    "metadata": {
                        "name": list_data.get("name", "Unknown"),
                        "title": list_data.get("title", "Unknown"),
                        "description": list_metadata.get("description", ""),
                    },
                    "schema": schema,
                    "columns": columns,
                    "name_column": name_column,
                    "views": list_metadata.get("views", []),
                    "todo_mode": list_metadata.get("todo_mode", False),
                },
            }
        # No items in the list, try to get basic info
        if ctx:
            await ctx.info("List has no items, returning basic structure")

        return {
            "success": True,
            "structure": {
                "list_id": list_id,
                "message": "List is empty. Add items to see full structure.",
                "columns": {},
            },
        }

    except Exception as e:
        logger.error(f"Error getting list structure: {e}")
        if ctx:
            await ctx.error(f"Failed to get list structure: {e!s}")
        return {
            "success": False,
            "error": str(e),
        }


# Add a resource to show server information
@mcp.resource("resource://server/info")
def get_server_info() -> dict[str, Any]:
    """Provide server configuration and status information."""
    return {
        "name": settings.mcp_server_name,
        "version": settings.mcp_server_version,
        "debug_mode": settings.debug_mode,
        "log_level": settings.log_level,
        "slack_api_timeout": settings.slack_api_timeout,
        "slack_retry_count": settings.slack_retry_count,
        "status": "running",
        "tools": [
            "add_list_item",
            "update_list_item",
            "delete_list_item",
            "get_list_item",
            "list_items",
            "get_list_info",
            "get_list_structure",
        ],
    }


# Add a prompt template for Slack API documentation
@mcp.prompt("slack-api-documentation")
def slack_api_documentation() -> str:
    """Provide formatted Slack API documentation for system prompt usage."""
    return """
# slackLists.items.create method

## 概要
This method is used to create a new item, also known as a record, in an existing List.

## Usage info
This method is used to create a new item, also known as a record, in an existing List.
The item will be created with the field values specified in the initial_fields parameter. Each field corresponds to a column in the List and must reference a valid column_id.

## Sample requests data

### Creating items

#### Basic item creation
Provide field values using the initial_fields parameter:
```json
{
  "list_id": "F1234ABCD",
  "initial_fields": [
    {
      "column_id": "Col10000000",
      "rich_text": [
        {
          "type": "rich_text",
          "elements": [
            {
              "type": "rich_text_section",
              "elements": [
                {
                  "type": "text",
                  "text": "Complete project documentation"
                }
              ]
            }
          ]
        }
      ]
    }
  ]
}
```

#### Duplicating items
Create a copy of an existing item by specifying the duplicated_item_id:
```json
{
  "list_id": "F1234ABCD",
  "duplicated_item_id": "Rec12345678"
}
```

#### Creating subtasks
Create a subtask by specifying the parent_item_id:
```json
{
  "list_id": "F1234ABCD",
  "parent_item_id": "Rec12345678",
  "initial_fields": [
    {
      "column_id": "Col10000000",
      "select": ["OptHIGH123"]
    }
  ]
}
```

### Field types
The initial_fields parameter supports all column types available in Lists. The supported field formats are as follows:

#### Text field (rich_text)
```json
{
  "column_id": "Col123",
  "rich_text": [
    {
      "type": "rich_text",
      "elements": [
        {
          "type": "rich_text_section",
          "elements": [
            {
              "type": "text",
              "text": "Your text content"
            }
          ]
        }
      ]
    }
  ]
}
```

#### User field
```json
{
  "column_id": "Col123",
  "user": ["U1234567", "U2345678"]
}
```

#### Date field
```json
{
  "column_id": "Col123",
  "date": ["2024-12-31"]
}
```

#### Select field
```json
{
  "column_id": "Col123",
  "select": ["OptionId123"]
}
```

#### Checkbox field
```json
{
  "column_id": "Col123",
  "checkbox": true
}
```

#### Number field
```json
{
  "column_id": "Col123",
  "number": [5000]
}
```

#### Email Field
```json
{
  "column_id": "Col123",
  "email": ["contact@example.com"]
}
```

#### Phone field
```json
{
  "column_id": "Col123",
  "phone": ["+1-555-123-4567"]
}
```

#### Attachment field
```json
{
  "column_id": "Col123",
  "attachment": ["F1234567890"]
}
```

#### Link field
```json
{
  "column_id": "Col123",
  "link": [
    {
      "original_url": "https://example.com",
      "display_as_url": false,
      "display_name": "Example Website"
    }
  ]
}
```

#### Message field
```json
{
  "column_id": "Col123",
  "message": ["https://yourteam.slack.com/archives/C1234567890/p1234567890123456"]
}
```

#### Rating field
```json
{
  "column_id": "Col123",
  "rating": [4]
}
```

#### Timestamp Field
```json
{
  "column_id": "Col123",
  "timestamp": [1704067200]
}
```

---

## 重要な注意事項

1. **リスト構造の理解**: アイテムを追加または更新する前に、`get_list_structure`を使用してリストの列構造を理解してください。

2. **DEFAULT_LIST_IDの活用**: 環境変数`DEFAULT_LIST_ID`が設定されている場合、すべてのツール呼び出しで`list_id`パラメータを省略できます。

## フィルター演算子

リストアイテムを検索する際に使用できる演算子：

- `equals`: 完全一致
- `not_equals`: 値が等しくない
- `contains`: 部分文字列を含む（大文字小文字を区別しない）
- `not_contains`: 部分文字列を含まない
- `in`: 指定されたリストに値が含まれる
- `not_in`: 指定されたリストに値が含まれない

## ドキュメント出典

このドキュメントは、Slack公式ドキュメント (https://docs.slack.dev/reference/methods/slackLists.items.create) に基づいて作成されています。
最新の情報については、公式ドキュメントを参照してください。
"""

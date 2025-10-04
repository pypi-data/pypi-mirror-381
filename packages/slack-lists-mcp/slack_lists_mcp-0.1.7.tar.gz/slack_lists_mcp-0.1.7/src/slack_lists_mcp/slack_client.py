"""Slack Lists API client implementation."""

import logging
from typing import Any

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

from slack_lists_mcp.config import get_settings
from slack_lists_mcp.models import ErrorResponse

logger = logging.getLogger(__name__)


class SlackListsClient:
    """Client for interacting with Slack Lists API."""

    def __init__(self, token: str | None = None):
        """Initialize the Slack Lists client.

        Args:
            token: Slack bot token. If not provided, will use from settings.

        """
        settings = get_settings()
        self.token = token or settings.slack_bot_token_value
        self.client = WebClient(
            token=self.token,
            timeout=settings.slack_api_timeout,
        )
        self.retry_count = settings.slack_retry_count

    def _handle_api_error(self, e: SlackApiError) -> ErrorResponse:
        """Handle Slack API errors consistently.

        Args:
            e: The SlackApiError exception

        Returns:
            ErrorResponse model with error details

        """
        error_msg = e.response.get("error", "Unknown error")
        error_details = {
            "response": e.response,
            "status_code": e.response.status_code
            if hasattr(e.response, "status_code")
            else None,
            "headers": dict(e.response.headers)
            if hasattr(e.response, "headers")
            else None,
        }
        logger.error(f"Slack API error: {error_msg} - Details: {error_details}")
        return ErrorResponse(
            error=error_msg,
            error_code=str(e.response.get("error_code", "")),
            details=error_details,
        )

    def _normalize_fields(self, fields: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Normalize field formats for better API usability.

        Handles common format issues:
        - Wraps select field values in arrays if not already
        - Wraps user field values in arrays if not already
        - Ensures rich_text fields have proper structure

        Args:
            fields: List of field dictionaries to normalize

        Returns:
            Normalized field list

        """
        normalized = []
        for field in fields:
            # Create a copy to avoid mutating the original
            normalized_field = field.copy()

            # Handle select fields - wrap single values in array
            if "select" in normalized_field and not isinstance(
                normalized_field["select"],
                list,
            ):
                normalized_field["select"] = [normalized_field["select"]]

            # Handle user fields - wrap single values in array
            if "user" in normalized_field and not isinstance(
                normalized_field["user"],
                list,
            ):
                normalized_field["user"] = [normalized_field["user"]]

            # Handle text fields by converting to rich_text if needed
            if "text" in normalized_field and "rich_text" not in normalized_field:
                # Convert plain text to rich_text format
                text_value = normalized_field.pop("text")
                normalized_field["rich_text"] = [
                    {
                        "type": "rich_text",
                        "elements": [
                            {
                                "type": "rich_text_section",
                                "elements": [{"type": "text", "text": str(text_value)}],
                            },
                        ],
                    },
                ]

            normalized.append(normalized_field)

        return normalized

    async def add_item(
        self,
        list_id: str,
        initial_fields: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Add a new item to a list.

        Use get_list_structure first to understand the column IDs and types.

        Args:
            list_id: The ID of the list
            initial_fields: List of field dictionaries with column_id and appropriate value format.
                           Each field should have:
                           - column_id: The column ID
                           - One of: rich_text, user, date, select, checkbox, number, email, phone, etc.

        Returns:
            The created item data

        Example:
            initial_fields = [
                {
                    "column_id": "Col123",
                    "rich_text": [{
                        "type": "rich_text",
                        "elements": [{
                            "type": "rich_text_section",
                            "elements": [{"type": "text", "text": "My Task"}]
                        }]
                    }]
                },
                {
                    "column_id": "Col456",
                    "user": ["U123456"]  # user fields expect an array
                },
                {
                    "column_id": "Col789",
                    "select": ["OptABC123"]  # select fields also expect an array
                },
                {
                    "column_id": "Col012",
                    "checkbox": False  # checkbox is a boolean
                }
            ]

        """
        try:
            if not initial_fields:
                raise ValueError("At least one field must be provided")

            # Normalize field formats for better usability
            normalized_fields = self._normalize_fields(initial_fields)

            logger.debug(
                f"Creating item with {len(normalized_fields)} fields in list {list_id}",
            )
            response = self.client.api_call(
                api_method="slackLists.items.create",
                json={
                    "list_id": list_id,
                    "initial_fields": normalized_fields,
                },
            )

            if response.get("ok"):
                return response.get("item", {})
            raise SlackApiError(
                message="Failed to add item",
                response=response,
            )

        except SlackApiError as e:
            error_response = self._handle_api_error(e)
            raise Exception(f"Failed to add item: {error_response.error}")
        except Exception as e:
            logger.error(f"Unexpected error adding item: {e}")
            raise

    async def update_item(
        self,
        list_id: str,
        cells: list[dict[str, Any]],
    ) -> dict[str, Any]:
        """Update items in a list.

        Use get_list_structure first to understand the column IDs and types.

        Args:
            list_id: The ID of the list
            cells: List of cell dictionaries with row_id, column_id and appropriate value format.
                   Each cell must have:
                   - row_id: The item/row ID to update
                   - column_id: The column ID
                   - One of: rich_text, user, date, select, checkbox, number, email, phone, etc.

        Returns:
            Success indicator

        Example:
            cells = [
                {
                    "row_id": "Rec123",
                    "column_id": "Col123",
                    "rich_text": [{
                        "type": "rich_text",
                        "elements": [{
                            "type": "rich_text_section",
                            "elements": [{"type": "text", "text": "Updated Task"}]
                        }]
                    }]
                },
                {
                    "row_id": "Rec123",
                    "column_id": "Col456",
                    "checkbox": True
                },
                {
                    "row_id": "Rec123",
                    "column_id": "Col789",
                    "select": ["OptABC123"]  # select fields expect an array
                },
                {
                    "row_id": "Rec123",
                    "column_id": "Col012",
                    "user": ["U123456"]  # user fields expect an array
                }
            ]

        """
        try:
            if not cells:
                raise ValueError("At least one cell must be provided")

            # Normalize field formats for better usability
            normalized_cells = self._normalize_fields(cells)

            logger.info(
                f"Updating {len(normalized_cells)} cells in list {list_id}",
            )
            response = self.client.api_call(
                api_method="slackLists.items.update",
                json={
                    "list_id": list_id,
                    "cells": normalized_cells,
                },
            )

            if response.get("ok"):
                return {"success": True}
            raise SlackApiError(
                message="Failed to update items",
                response=response,
            )

        except SlackApiError as e:
            error_response = self._handle_api_error(e)
            raise Exception(f"Failed to update items: {error_response.error}")
        except Exception as e:
            logger.error(f"Unexpected error updating items: {e}")
            raise

    async def delete_item(
        self,
        list_id: str,
        item_id: str,
    ) -> dict[str, Any]:
        """Delete an item from a list.

        Args:
            list_id: The ID of the list
            item_id: The ID of the item to delete

        Returns:
            Confirmation of deletion

        """
        try:
            response = self.client.api_call(
                api_method="slackLists.items.delete",
                json={
                    "list_id": list_id,
                    "id": item_id,  # API expects 'id' not 'item_id'
                },
            )

            if response.get("ok"):
                return {"deleted": True, "item_id": item_id}
            raise SlackApiError(
                message="Failed to delete item",
                response=response,
            )

        except SlackApiError as e:
            error_response = self._handle_api_error(e)
            raise Exception(f"Failed to delete item: {error_response.error}")
        except Exception as e:
            logger.error(f"Unexpected error deleting item: {e}")
            raise

    async def get_item(
        self,
        list_id: str,
        item_id: str,
        include_is_subscribed: bool = False,
    ) -> dict[str, Any]:
        """Get a specific item from a list.

        Args:
            list_id: The ID of the list
            item_id: The ID of the item
            include_is_subscribed: Whether to include subscription status

        Returns:
            The item data including list metadata and subtasks if present

        """
        try:
            params = {
                "list_id": list_id,
                "id": item_id,  # API expects 'id' not 'item_id'
            }

            if include_is_subscribed:
                params["include_is_subscribed"] = include_is_subscribed

            response = self.client.api_call(
                api_method="slackLists.items.info",
                json=params,
            )

            if response.get("ok"):
                # API returns 'record' not 'item'
                return {
                    "item": response.get("record", {}),
                    "list": response.get("list", {}),
                    "subtasks": response.get("subtasks", []),
                }
            raise SlackApiError(
                message="Failed to get item",
                response=response,
            )

        except SlackApiError as e:
            error_response = self._handle_api_error(e)
            raise Exception(f"Failed to get item: {error_response.error}")
        except Exception as e:
            logger.error(f"Unexpected error getting item: {e}")
            raise

    async def list_items(
        self,
        list_id: str,
        limit: int = 100,
        cursor: str | None = None,
        archived: bool | None = None,
        filters: dict[str, dict[str, Any]] | None = None,
    ) -> dict[str, Any]:
        """List items in a list with optional filtering.

        Args:
            list_id: The ID of the list
            limit: Maximum number of items to return (default: 100)
            cursor: Pagination cursor for next page
            archived: Whether to return archived items (True) or normal items (False/None)
            filters: Dictionary of column filters. Keys are column IDs or keys, values are filter conditions.
                    Example: {
                        "name": {"contains": "タスク"},
                        "Col09HEURLL6A": {"equals": "OptRCQF2AM6"},  # ステータス
                        "todo_completed": {"equals": True},
                        "Col09H0PTP23Z": {"in": ["U123", "U456"]},  # 担当者リスト
                    }
                    Supported operators: equals, not_equals, contains, not_contains, in, not_in

        Returns:
            Dictionary with items and pagination info

        """
        try:
            # API parameters (only supported ones)
            params = {
                "list_id": list_id,
                "limit": limit * 3 if filters else limit,  # Get more items if filtering
            }

            if cursor:
                params["cursor"] = cursor
            if archived is not None:
                params["archived"] = archived

            response = self.client.api_call(
                api_method="slackLists.items.list",
                json=params,
            )

            if response.get("ok"):
                items = response.get("items", [])

                # Apply client-side filters if provided
                if filters:
                    filtered_items = []
                    for item in items:
                        if self._matches_filters(item, filters):
                            filtered_items.append(item)
                            if len(filtered_items) >= limit:
                                break
                    items = filtered_items

                return {
                    "items": items,
                    "has_more": response.get("has_more", False),
                    "next_cursor": response.get("next_cursor"),
                    "total": len(items),
                }

            raise SlackApiError(
                message="Failed to list items",
                response=response,
            )

        except SlackApiError as e:
            error_response = self._handle_api_error(e)
            raise Exception(f"Failed to list items: {error_response.error}")
        except Exception as e:
            logger.error(f"Unexpected error listing items: {e}")
            raise

    def _matches_filters(
        self,
        item: dict[str, Any],
        filters: dict[str, dict[str, Any]],
    ) -> bool:
        """Check if an item matches all filter conditions.

        Args:
            item: The item to check
            filters: Filter conditions

        Returns:
            True if item matches all filters, False otherwise

        """
        fields = item.get("fields", [])

        for filter_key, filter_condition in filters.items():
            matched = False

            # Find matching field
            for field in fields:
                # Match by column_id or key
                if (
                    field.get("column_id") == filter_key
                    or field.get("key") == filter_key
                ):
                    field_value = self._extract_field_value(field)

                    # Apply filter condition
                    if self._apply_filter_condition(field_value, filter_condition):
                        matched = True
                        break

            # If no field matched this filter, item doesn't match
            if not matched:
                return False

        return True

    def _extract_field_value(self, field: dict[str, Any]) -> Any:
        """Extract the actual value from a field.

        Args:
            field: Field dictionary

        Returns:
            The extracted value

        """
        # Priority order for value extraction
        if "checkbox" in field:
            return field["checkbox"]
        if "select" in field:
            return field["select"]
        if "user" in field:
            return field["user"]
        if "date" in field:
            return field["date"]
        if "text" in field:
            return field["text"]
        if "number" in field:
            return field["number"]
        if "email" in field:
            return field["email"]
        if "phone" in field:
            return field["phone"]
        if "value" in field:
            return field["value"]
        return None

    def _apply_filter_condition(self, value: Any, condition: dict[str, Any]) -> bool:
        """Apply a filter condition to a value.

        Args:
            value: The value to check
            condition: Filter condition with operator and expected value

        Returns:
            True if value matches condition

        """
        for operator, expected in condition.items():
            if operator == "equals":
                if not self._values_equal(value, expected):
                    return False
            elif operator == "not_equals":
                if self._values_equal(value, expected):
                    return False
            elif operator == "contains":
                if not self._value_contains(value, expected):
                    return False
            elif operator == "not_contains":
                if self._value_contains(value, expected):
                    return False
            elif operator == "in":
                if not self._value_in_list(value, expected):
                    return False
            elif operator == "not_in":
                if self._value_in_list(value, expected):
                    return False

        return True

    def _values_equal(self, value: Any, expected: Any) -> bool:
        """Check if values are equal."""
        if isinstance(value, list) and len(value) == 1:
            return value[0] == expected
        return value == expected

    def _value_contains(self, value: Any, search: str) -> bool:
        """Check if value contains search string."""
        if value is None:
            return False
        if isinstance(value, str):
            return search.lower() in value.lower()
        if isinstance(value, list):
            return any(search.lower() in str(v).lower() for v in value)
        return search.lower() in str(value).lower()

    def _value_in_list(self, value: Any, expected_list: list) -> bool:
        """Check if value is in expected list."""
        if isinstance(value, list):
            return any(v in expected_list for v in value)
        return value in expected_list

    async def get_list(self, list_id: str) -> dict[str, Any]:
        """Get information about a list.

        Note: There's no direct slackLists.info API, so we use items.list with limit=1
        to get list metadata from the first item's response.

        Args:
            list_id: The ID of the list

        Returns:
            The list information

        """
        try:
            # Use list_items to get basic list info
            response = self.client.api_call(
                api_method="slackLists.items.list",
                json={"list_id": list_id, "limit": 1},
            )

            if response.get("ok"):
                # If we have items, try to get more detailed info
                items = response.get("items", [])
                if items:
                    # Get first item info which includes list metadata
                    item_response = self.client.api_call(
                        api_method="slackLists.items.info",
                        json={
                            "list_id": list_id,
                            "id": items[0]["id"],
                        },
                    )
                    if item_response.get("ok"):
                        return item_response.get("list", {})

                # No items or couldn't get item info, return basic info
                return {
                    "id": list_id,
                    "item_count": len(items),
                    "message": "List metadata not available. List may be empty.",
                }

            raise SlackApiError(
                message="Failed to get list",
                response=response,
            )

        except SlackApiError as e:
            error_response = self._handle_api_error(e)
            raise Exception(f"Failed to get list: {error_response.error}")
        except Exception as e:
            logger.error(f"Unexpected error getting list: {e}")
            raise

    async def create_list(
        self,
        name: str,
        channel_id: str,
        description: str | None = None,
        is_private: bool = False,
    ) -> dict[str, Any]:
        """Create a new list.

        Args:
            name: Name of the list
            channel_id: Channel ID where the list will be created
            description: Optional description
            is_private: Whether the list should be private

        Returns:
            The created list data

        """
        try:
            list_data = {
                "name": name,
                "channel_id": channel_id,
            }

            if description:
                list_data["description"] = description
            if is_private:
                list_data["is_private"] = is_private

            response = self.client.api_call(
                api_method="slackLists.create",
                json=list_data,
            )

            if response.get("ok"):
                return response.get("list", {})
            raise SlackApiError(
                message="Failed to create list",
                response=response,
            )

        except SlackApiError as e:
            error_response = self._handle_api_error(e)
            raise Exception(f"Failed to create list: {error_response.error}")
        except Exception as e:
            logger.error(f"Unexpected error creating list: {e}")
            raise


# Create a singleton instance
slack_client = SlackListsClient()

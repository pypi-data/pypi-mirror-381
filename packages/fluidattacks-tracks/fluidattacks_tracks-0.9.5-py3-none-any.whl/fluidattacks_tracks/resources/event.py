"""Tracks event resource."""

from collections.abc import AsyncGenerator, Mapping
from datetime import datetime
from typing import Literal, NotRequired, TypedDict

from pydantic import BaseModel

from fluidattacks_tracks.client import TracksClient
from fluidattacks_tracks.utils import fire_and_forget


class TracksEvent(BaseModel):
    """Tracks event."""

    action: str
    author: str
    date: datetime
    id: str
    mechanism: str
    metadata: Mapping[str, object]
    object_id: str


class PageInfo(BaseModel):
    """Tracks page info."""

    end_cursor: str
    has_next_page: bool


class TracksResponse(BaseModel):
    """Tracks response."""

    events: tuple[TracksEvent, ...]
    page_info: PageInfo


ActionType = Literal["CREATE", "READ", "UPDATE", "DELETE"]


MechanismType = Literal[
    "API",
    "DESKTOP",
    "EMAIL",
    "FIXES",
    "FORCES",
    "JIRA",
    "MCP",
    "MELTS",
    "MESSAGING",
    "MIGRATION",
    "RETRIEVES",
    "SCHEDULER",
    "SMELLS",
    "TASK",
    "WEB",
]


class Event(TypedDict):
    """Tracks event."""

    action: ActionType
    author_anonymous: NotRequired[bool]
    author_ip: NotRequired[str]
    author_role: NotRequired[str]
    author_user_agent: NotRequired[str]
    author: str
    date: datetime
    mechanism: MechanismType
    metadata: Mapping[str, object]
    object_id: str
    object: str
    session_id: NotRequired[str]


class EventResource:
    """Tracks event resource."""

    def __init__(self, client: TracksClient) -> None:
        """Initialize the event resource."""
        self.client = client

    @fire_and_forget
    def create(self, event: Event) -> None:
        """Create an event."""
        self.client.post("/event", json=event)

    async def create_batch_async(self, events: list[Event]) -> None:
        """Create a batch of events."""
        await self.client.post_async("/events/batch", authenticated=True, json=events)

    async def read_pages(  # noqa: PLR0913
        self,
        *,
        after: str | None = None,
        end_date: datetime | None = None,
        group_name: str,
        limit: int = 100,
        object_: str,
        object_id: str | None = None,
        start_date: datetime | None = None,
        state_type: str | None = None,
    ) -> AsyncGenerator[TracksResponse]:
        """Read pages of events matching the given filters."""
        end_cursor = datetime.fromisoformat(after) if after else start_date
        has_next_page = True
        limit_with_offset = limit + 1  # Needed to check if there is a next page

        while has_next_page:
            response = await self.client.get_async(
                f"/groups/{group_name}/events",
                authenticated=True,
                params={
                    "limit": limit_with_offset,
                    "object": object_,
                    **({"end_date": end_date.isoformat()} if end_date else {}),
                    **({"object_id": object_id} if object_id else {}),
                    **({"start_date": end_cursor.isoformat()} if end_cursor else {}),
                    **({"state_type": state_type} if state_type else {}),
                },
            )
            response.raise_for_status()
            response_json: list[dict[str, object]] = await response.json()  # type: ignore[misc]
            has_next_page = len(response_json) == limit_with_offset
            trimmed_response = response_json[:-1] if has_next_page else response_json
            events = tuple(TracksEvent.model_validate(event) for event in trimmed_response)
            end_cursor = events[-1].date if events else None

            yield TracksResponse(
                events=events,
                page_info=PageInfo(
                    has_next_page=has_next_page,
                    end_cursor=end_cursor.isoformat() if end_cursor else "",
                ),
            )

    async def read(  # noqa: PLR0913
        self,
        *,
        after: str | None = None,
        end_date: datetime | None = None,
        group_name: str,
        limit: int = 100,
        object_: str,
        object_id: str | None = None,
        start_date: datetime | None = None,
        state_type: str | None = None,
    ) -> TracksResponse:
        """Read all events matching the given filters."""
        pages = [
            page
            async for page in self.read_pages(
                after=after,
                end_date=end_date,
                group_name=group_name,
                limit=limit,
                object_=object_,
                object_id=object_id,
                start_date=start_date,
                state_type=state_type,
            )
        ]

        return TracksResponse(
            events=tuple(event for page in pages for event in page.events),
            page_info=pages[-1].page_info,
        )

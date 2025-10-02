from typing import Any, Dict, List, Optional, Set

from pydantic import BaseModel


class OWAFile(BaseModel):
    """Represents an OWA file (MCAP+MKV pair)"""

    basename: str
    original_basename: Optional[str] = None
    size: int
    local: bool
    url: str
    url_mcap: str
    url_mkv: str


class DatasetInfo(BaseModel):
    """Dataset information for the viewer"""

    repo_id: str
    files: int
    size: str


class McapMetadata(BaseModel):
    """Metadata for an MCAP file"""

    start_time: int  # Timestamp in nanoseconds
    end_time: int  # Timestamp in nanoseconds
    topics: Set[str]  # Set of topic names

    def duration_seconds(self) -> float:
        """Get the duration in seconds"""
        return (self.end_time - self.start_time) / 1_000_000_000


class McapDataRequest(BaseModel):
    """Request parameters for MCAP data retrieval"""

    mcap_filename: str
    local: bool = True
    start_time: Optional[int] = None
    end_time: Optional[int] = None
    window_size: int = 10_000_000_000  # Default 10-second window in nanoseconds


class McapTopicData(BaseModel):
    """Data for a single MCAP topic"""

    topic: str
    messages: List[Dict[str, Any]]

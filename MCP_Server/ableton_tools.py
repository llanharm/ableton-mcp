"""Ableton Live MCP tool definitions for the MCP server.

This module defines the MCP tools that expose Ableton Live functionality
through the Model Context Protocol, allowing AI assistants to control
Ableton Live via the remote script connection.

Personal fork notes:
- Valid tempo range extended to 20-999 BPM to match Ableton's actual limits
  (the original 60-200 range was overly restrictive for experimental use)
- create_midi_track now defaults index to -1 (append) since that's almost
  always what you want when adding a new track interactively
"""

from typing import Any
import mcp.types as types


def get_tool_definitions() -> list[types.Tool]:
    """Return all tool definitions for the Ableton MCP server."""
    return [
        types.Tool(
            name="get_session_info",
            description="Get information about the current Ableton Live session, including BPM, time signature, tracks, and playback state.",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
        types.Tool(
            name="get_track_info",
            description="Get detailed information about a specific track including its clips, devices, and mixer settings.",
            inputSchema={
                "type": "object",
                "properties": {
                    "track_index": {
                        "type": "integer",
                        "description": "Zero-based index of the track to inspect.",
                    }
                },
                "required": ["track_index"],
            },
        ),
        types.Tool(
            name="set_tempo",
            description="Set the BPM (tempo) of the Ableton Live session.",
            inputSchema={
                "type": "object",
                "properties": {
                    "tempo": {
                        "type": "number",
                        # Ableton's actual supported range is 20–999 BPM;
                        # the original 60–200 was unnecessarily restrictive.
                        "description": "Tempo in BPM (beats per minute). Valid range: 20–999.",
                    }
                },
                "required": ["tempo"],
            },
        ),
        types.Tool(
            name="create_midi_track",
            description="Create a new MIDI track in the Ableton Live session.",
            inputSchema={
                "type": "object",
                "properties": {
                    "index": {
                        "type": "integer",
                        # Default to -1 (append) — inserting at a specific position
                        # is rarely needed and easy to forget to set correctly.
                        "description": "Position at which to insert the track. Defaults to -1 to append at the end.",
                        "default": -1,
                    }
                },
                "required": [],
            },
        ),
        types.Tool(
            name="create_audio_track",
            description="Create a new audio track in the Ableton Live session.",
            inputSchema={
                "type": "object",
                "properties": {
                    "index": {
                        "type": "integer",
                        "description": "Position at which to insert the track. Use -1 to append at the end.",
                    }
                },
                "required": [],
            },
        ),
    ]

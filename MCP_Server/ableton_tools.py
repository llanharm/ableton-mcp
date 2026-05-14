"""Ableton Live MCP tool definitions for the MCP server.

This module defines the MCP tools that expose Ableton Live functionality
through the Model Context Protocol, allowing AI assistants to control
Ableton Live via the remote script connection.
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
                        "description": "Tempo in BPM (beats per minute). Valid range: 60–200.",
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
                        "description": "Position at which to insert the track. Use -1 to append at the end.",
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
        types.Tool(
            name="create_clip",
            description="Create a new MIDI clip in a track's clip slot.",
            inputSchema={
                "type": "object",
                "properties": {
                    "track_index": {
                        "type": "integer",
                        "description": "Zero-based index of the target track.",
                    },
                    "clip_index": {
                        "type": "integer",
                        "description": "Zero-based index of the clip slot.",
                    },
                    "length": {
                        "type": "number",
                        "description": "Length of the clip in bars.",
                    },
                },
                "required": ["track_index", "clip_index", "length"],
            },
        ),
        types.Tool(
            name="add_notes_to_clip",
            description="Add MIDI notes to an existing clip.",
            inputSchema={
                "type": "object",
                "properties": {
                    "track_index": {
                        "type": "integer",
                        "description": "Zero-based index of the target track.",
                    },
                    "clip_index": {
                        "type": "integer",
                        "description": "Zero-based index of the clip slot.",
                    },
                    "notes": {
                        "type": "array",
                        "description": "List of note objects to add.",
                        "items": {
                            "type": "object",
                            "properties": {
                                "pitch": {"type": "integer", "description": "MIDI pitch (0–127)."},
                                "start_time": {"type": "number", "description": "Start time in beats."},
                                "duration": {"type": "number", "description": "Duration in beats."},
                                "velocity": {"type": "integer", "description": "Velocity (0–127)."},
                                "muted": {"type": "boolean", "description": "Whether the note is muted."},
                            },
                            "required": ["pitch", "start_time", "duration", "velocity"],
                        },
                    },
                },
                "required": ["track_index", "clip_index", "notes"],
            },
        ),
        types.Tool(
            name="start_playback",
            description="Start playback in Ableton Live.",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
        types.Tool(
            name="stop_playback",
            description="Stop playback in Ableton Live.",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
        types.Tool(
            name="load_instrument_or_effect",
            description="Load an instrument or effect plugin onto a track by its URI from the Ableton browser.",
            inputSchema={
                "type": "object",
                "properties": {
                    "track_index": {
                        "type": "integer",
                        "description": "Zero-based index of the target track.",
                    },
                    "uri": {
                        "type": "string",
                        "description": "The browser URI of the instrument or effect to load.",
                    },
                },
                "required": ["track_index", "uri"],
            },
        ),
        types.Tool(
            name="set_track_volume",
            description="Set the volume of a track.",
            inputSchema={
                "type": "object",
                "properties": {
                    "track_index": {
                        "type": "integer",
                        "description": "Zero-based index of the target track.",
                    },
                    "volume": {
                        "type": "number",
                        "description": "Volume level (0.0 to 1.0, where 0.85 ≈ 0 dB).",
                    },
                },
                "required": ["track_index", "volume"],
            },
        ),
        types.Tool(
            name="set_track_pan",
            description="Set the panning of a track.",
            inputSchema={
                "type": "object",
                "properties": {
                    "track_index": {
                        "type": "integer",
                        "description": "Zero-based index of the target track.",
                    },
                    "pan": {
                        "type": "number",
                        "description": "Pan value from -1.0 (full left) to 1.0 (full right). 0.0 is center.",
                    },
                },
                "required": ["track_index", "pan"],
            },
        ),
        types.Tool(
            name="fire_clip",
            description="Launch/fire a clip slot in Ableton Live.",
            inputSchema={
                "type": "object",
                "properties": {
                    "track_index": {
                        "type": "integer",
                        "description": "Zero-based index of the target track.",
                    },
                    "clip_index": {
                        "type": "integer",
                        "description": "Zero-based index of the clip slot to fire.",
                    },
                },
                "required": ["track_index", "clip_index"],
            },
        ),
        types.Tool(
            name="stop_clip",
            description="Stop a playing clip in a specific track slot.",
            inputSchema={
                "type": "object",
                "properties": {
                    "track_index": {
                        "type": "integer",
                        "description": "Zero-based index of the target track.",
                    },
                    "clip_index": {
                        "type": "integer",
                        "description": "Zero-based index of the clip slot to stop.",
                    },
                },
                "required": ["track_index", "clip_index"],
            },
        ),
    ]

"""Command builders for Ableton Live MCP server.

This module provides helper functions to construct well-formed command
dictionaries that are sent to the Ableton Remote Script over the socket
connection. Keeping command construction separate from the server logic
makes it easier to add, test, and document individual commands.
"""

from typing import Any, Dict, Optional


def _cmd(command: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Return a base command dict, optionally merging in params."""
    payload: Dict[str, Any] = {"command": command}
    if params:
        payload.update(params)
    return payload


# ---------------------------------------------------------------------------
# Transport
# ---------------------------------------------------------------------------

def play() -> Dict[str, Any]:
    """Start playback from the current position."""
    return _cmd("play")


def stop() -> Dict[str, Any]:
    """Stop playback."""
    return _cmd("stop")


def get_tempo() -> Dict[str, Any]:
    """Request the current session tempo in BPM."""
    return _cmd("get_tempo")


def set_tempo(bpm: float) -> Dict[str, Any]:
    """Set the session tempo.

    Args:
        bpm: Target tempo in beats per minute (20–999).
    """
    if not (20.0 <= bpm <= 999.0):
        raise ValueError(f"Tempo must be between 20 and 999 BPM, got {bpm}")
    return _cmd("set_tempo", {"tempo": bpm})


# ---------------------------------------------------------------------------
# Tracks
# ---------------------------------------------------------------------------

def get_track_info(track_index: int) -> Dict[str, Any]:
    """Request detailed info for a single track.

    Args:
        track_index: Zero-based index of the track.
    """
    return _cmd("get_track_info", {"track_index": track_index})


def get_tracks() -> Dict[str, Any]:
    """Request a summary list of all tracks in the session."""
    return _cmd("get_tracks")


def set_track_volume(track_index: int, volume: float) -> Dict[str, Any]:
    """Set the volume of a track.

    Args:
        track_index: Zero-based index of the track.
        volume: Volume as a linear gain value (0.0 – 1.0).
    """
    if not (0.0 <= volume <= 1.0):
        raise ValueError(f"Volume must be between 0.0 and 1.0, got {volume}")
    return _cmd("set_track_volume", {"track_index": track_index, "volume": volume})


def set_track_pan(track_index: int, pan: float) -> Dict[str, Any]:
    """Set the panning of a track.

    Args:
        track_index: Zero-based index of the track.
        pan: Pan position from -1.0 (full left) to 1.0 (full right).
    """
    if not (-1.0 <= pan <= 1.0):
        raise ValueError(f"Pan must be between -1.0 and 1.0, got {pan}")
    return _cmd("set_track_pan", {"track_index": track_index, "pan": pan})


def set_track_mute(track_index: int, muted: bool) -> Dict[str, Any]:
    """Mute or un-mute a track."""
    return _cmd("set_track_mute", {"track_index": track_index, "muted": muted})


def set_track_solo(track_index: int, soloed: bool) -> Dict[str, Any]:
    """Solo or un-solo a track."""
    return _cmd("set_track_solo", {"track_index": track_index, "soloed": soloed})


# ---------------------------------------------------------------------------
# Clips
# ---------------------------------------------------------------------------

def get_clip_info(track_index: int, clip_index: int) -> Dict[str, Any]:
    """Request info for a specific clip slot.

    Args:
        track_index: Zero-based track index.
        clip_index: Zero-based clip slot index.
    """
    return _cmd("get_clip_info", {"track_index": track_index, "clip_index": clip_index})


def fire_clip(track_index: int, clip_index: int) -> Dict[str, Any]:
    """Launch a clip."""
    return _cmd("fire_clip", {"track_index": track_index, "clip_index": clip_index})


def stop_clip(track_index: int, clip_index: int) -> Dict[str, Any]:
    """Stop a playing clip."""
    return _cmd("stop_clip", {"track_index": track_index, "clip_index": clip_index})


# ---------------------------------------------------------------------------
# Devices / Parameters
# ---------------------------------------------------------------------------

def get_device_parameters(track_index: int, device_index: int) -> Dict[str, Any]:
    """Request all parameters for a device on a track.

    Args:
        track_index: Zero-based track index.
        device_index: Zero-based device index on that track.
    """
    return _cmd(
        "get_device_parameters",
        {"track_index": track_index, "device_index": device_index},
    )


def set_device_parameter(
    track_index: int, device_index: int, parameter_index: int, value: float
) -> Dict[str, Any]:
    """Set a single device parameter value.

    Args:
        track_index: Zero-based track index.
        device_index: Zero-based device index.
        parameter_index: Zero-based parameter index within the device.
        value: Normalised parameter value (0.0 – 1.0).
    """
    return _cmd(
        "set_device_parameter",
        {
            "track_index": track_index,
            "device_index": device_index,
            "parameter_index": parameter_index,
            "value": value,
        },
    )

"""Navigation turn timing levels and their persistent parameter values."""

LIMIT = 3
# Keep the original saved values so existing timing preferences survive updates.
SAVED_LEVELS = {str(level * 25).encode(): level for level in range(-LIMIT, LIMIT + 1)}


def saved_level(raw: bytes | None) -> int | None:
  return 0 if raw is None else SAVED_LEVELS.get(raw)

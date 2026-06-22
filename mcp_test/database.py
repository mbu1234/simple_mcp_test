"""Mock database for the MCP test server."""

MOCK_DATABASE: dict[str, dict] = {
    "1": {
        "id": 1,
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "role": "admin",
    },
    "2": {
        "id": 2,
        "name": "Bob Smith",
        "email": "bob@example.com",
        "role": "user",
    },
    "3": {
        "id": 3,
        "name": "Carol Davis",
        "email": "carol@example.com",
        "role": "user",
    },
}


def get_user_by_id(user_id: int) -> dict:
    """Return a user record from the mock database as a dictionary."""
    record = MOCK_DATABASE.get(str(user_id))
    if record is None:
        return {"error": "not_found", "user_id": user_id}
    return dict(record)

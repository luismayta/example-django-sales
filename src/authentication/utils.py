import uuid


def generate_token():
    """Genera un token unico de 32 caracteres."""
    return str(uuid.uuid4()).replace('-', '')

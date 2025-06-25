import sqlalchemy as sa
from alembic import op


def created_at_type():
    """Return TIMESTAMP for MySQL, otherwise DateTime."""
    bind = op.get_bind()
    if bind is not None and bind.dialect.name == "mysql":
        return sa.TIMESTAMP()
    return sa.DateTime()

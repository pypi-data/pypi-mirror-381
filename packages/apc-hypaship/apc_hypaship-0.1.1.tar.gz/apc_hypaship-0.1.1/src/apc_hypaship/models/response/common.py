from apc_hypaship.config import APCBaseModel


class Messages(APCBaseModel):
    code: str | None = None
    description: str | None = None

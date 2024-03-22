from skyvern.exceptions import SkyvernException


class BaseWorkflowException(SkyvernException):
    pass


class WorkflowDefinitionHasDuplicateBlockLabels(BaseWorkflowException):
    def __init__(self, duplicate_labels: set[str]) -> None:
        super().__init__(
            f"WorkflowDefinition has blocks with duplicate labels. Each block needs to have a unique "
            f"label. Duplicate label(s): {','.join(duplicate_labels)}"
        )


class OutputParameterKeyCollisionError(BaseWorkflowException):
    def __init__(self, key: str, retry_count: int | None = None) -> None:
        message = f"Output parameter key {key} already exists in the context manager."
        if retry_count is not None:
            message += f" Retrying {retry_count} more times."
        elif retry_count == 0:
            message += " Max duplicate retries reached, aborting."
        super().__init__(message)

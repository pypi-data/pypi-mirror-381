from typing import Literal, Optional

from candela_kit.dtos import ObjectId


class App:
    def __init__(
        self,
        type: Literal["Agent", "Pipeline"],
        circuit_id: ObjectId,
        directive_id: ObjectId,
    ):
        self.type = type
        self.circuit_id = circuit_id
        self.directive_id = directive_id

    @staticmethod
    def _make(
        type: Literal["Agent", "Pipeline"],
        circuit_code: str,
        directive_code: str,
        scope: str,
        circuit_version: Optional[str],
        directive_version: Optional[str],
    ):
        return App(
            type=type,
            circuit_id=ObjectId(
                scope=scope,
                code=circuit_code,
                version=circuit_version,
            ),
            directive_id=ObjectId(
                scope=scope,
                code=directive_code,
                version=directive_version,
            ),
        )

    @staticmethod
    def make_agent(
        circuit_code: str,
        directive_code: str,
        scope: str = "default",
        circuit_version: Optional[str] = None,
        directive_version: Optional[str] = None,
    ):
        return App._make(
            type="Agent",
            circuit_code=circuit_code,
            directive_code=directive_code,
            scope=scope,
            circuit_version=circuit_version,
            directive_version=directive_version,
        )

    @staticmethod
    def make_pipeline(
        circuit_code: str,
        directive_code: str,
        scope: str = "default",
        circuit_version: Optional[str] = None,
        directive_version: Optional[str] = None,
    ):
        return App._make(
            type="Pipeline",
            circuit_code=circuit_code,
            directive_code=directive_code,
            scope=scope,
            circuit_version=circuit_version,
            directive_version=directive_version,
        )

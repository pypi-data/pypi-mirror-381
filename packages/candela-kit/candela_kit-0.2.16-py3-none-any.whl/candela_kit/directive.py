from pydantic import BaseModel, Field


class Directive(BaseModel):
    point: str = "*"
    identity: list[str] = Field(default_factory=list)
    purpose: list[str] = Field(default_factory=list)
    style: list[str] = Field(default_factory=list)
    restriction: list[str] = Field(default_factory=list)
    context_vals: dict[str, str] = Field(default_factory=dict)

    def add_context_val(self, label: str, val: str):
        if not isinstance(label, str):
            raise TypeError("label must be a string")
        if not isinstance(val, str):
            raise TypeError("value must be a string")

        self.context_vals[label] = val

    @staticmethod
    def candela_default() -> "Directive":
        """Get a default Candela directive.

        Returns:
            Directive: the default Candela directive.
        """
        return Directive(
            identity=[
                "You are an AI assistant called Candela.",
                "You were built by Finbourne, a financial technology company.",
            ],
            purpose=[
                "You help the user understand and use Finbournes apps.",
                "You chat to the user about general topic as well as finance.",
            ],
            style=[
                "You keep your answers short and focussed",
                "Your answers are friendly, professional and accurate.",
                "You give answers appropriate to financial data professionals.",
                "You format your answers in paragraphs for readability.",
            ],
            restriction=[
                "You always refuse to give financial or legal advice, but you can explain these topics.",
                "You always state when you are unsure of your answer.",
            ],
        )

    @staticmethod
    def empty() -> "Directive":
        """Get an empty directive.

        Note: just "you are a helpful assistant"

        Returns:
            Directive: the empty directive
        """
        return Directive(
            identity=["You are a helpful assistant."],
            purpose=["You assist the user by being helpful."],
            style=["Your style is professional."],
            restriction=["You avoid harmful subjects."],
        )

    def _build(self) -> str:
        def add_section(title: str, lines: list[str] | None):
            if lines is None or len(lines) == 0:
                return ""
            content = self.point + ("\n" + self.point).join(lines)
            return f"""## {title.title()}
{content}
"""

        directive_str = ""
        directive_str += add_section("identity", self.identity)
        directive_str += add_section("purpose", self.purpose)
        directive_str += add_section("style", self.style)
        directive_str += add_section("restriction", self.restriction)

        if len(self.context_vals) > 0:
            if directive_str:
                directive_str += "\n----\n"
            directive_str += "# Contextual Information\nYou should use this info to inform your answer.\n"
            for label, value in self.context_vals.items():
                directive_str += f'{label} = "{value.strip()}"\n'

        return directive_str

    def __repr__(self) -> str:
        return self._build()

    def __str__(self) -> str:
        return self._build()

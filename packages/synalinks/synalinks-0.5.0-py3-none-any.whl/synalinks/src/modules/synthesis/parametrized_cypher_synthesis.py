from synalinks.src.backend import Trainable


class QueryParameter(DataModel):
    name: str = Field(
        description="The name of the parameter (in snake_case)",
    )
    description: str = Field(
        description="The natural language description of the parameter",
    )
    type: Literal["string", "int", "float"] = Field(
        description="The type of the parameter",
    )

class ParametrizedCypherQuery(Trainable):
    parameters: List[QueryParameter] = Field(
        description="The parameters for the Cypher query",
    )
    cypher_query: str = Field(
        description="The parametrized Cypher query",
    )
    

class ParametrizedCypherSynthesis(Module):
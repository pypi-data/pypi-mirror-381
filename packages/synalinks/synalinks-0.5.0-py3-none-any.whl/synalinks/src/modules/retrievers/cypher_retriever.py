

class GraphSchema(DataModel):
    entity_schemas: List[Dict[str, Any]] = Field(
        description="The entity schemas"
    )
    relation_schemas: List[Dict[str, Any]] = Field(
        description="The relation schemas"
    )


class CypherQuery(DataModel):
    cypher_query: str = Field(
        description="The cypher query",
    )


class CypherRetriever(Module):
    def __init__(
        self,
        knowledge_base=None,
        language_model=None,
        entity_models=None,
        relation_models=None,
        prompt_template=None,
        examples=None,
        instructions=None,
        seed_instructions=None,
    ):
        self.knowledge_base = knowledge_base
        self.language_model = language_model
        self.entity_models = entity_models
        self.relation_models = relation_models
        
        self.query_generator = ChainOfThought(
            data_model=CypherQuery,
            language_model=language_model,
        )
        
    def call(self, inputs, training=False):
        
        
        
    def get_config(self):
        config = {
            "k": self.question,
            "threshold": self.labels,
            "prompt_template": self.prompt_template,
            "examples": self.examples,
            "instructions": self.instructions,
            "temperature": self.temperature,
            "use_inputs_schema": self.use_inputs_schema,
            "use_outputs_schema": self.use_outputs_schema,
            "return_inputs": self.return_inputs,
            "return_query": self.return_query,
            "name": self.name,
            "description": self.description,
            "trainable": self.trainable,
        }
        knowledge_base_config = {
            "knowledge_base": serialization_lib.serialize_synalinks_object(
                self.knowledge_base,
            )
        }
        language_model_config = {
            "language_model": serialization_lib.serialize_synalinks_object(
                self.language_model,
            )
        }
        entity_models_config = {
            "entity_models": [
                (
                    serialization_lib.serialize_synalinks_object(
                        entity_model.to_symbolic_data_model(
                            name=self.name + "_entity_model" + ("_{i}" if i > 0 else "")
                        )
                    )
                    if not is_symbolic_data_model(entity_model)
                    else serialization_lib.serialize_synalinks_object(entity_model)
                )
                for i, entity_model in enumerate(self.entity_models)
            ]
        }
        relation_models_config = {
            "relation_models": [
                (
                    serialization_lib.serialize_synalinks_object(
                        relation_model.to_symbolic_data_model(
                            name=self.name + "_relation_model" + ("_{i}" if i > 0 else "")
                        )
                    )
                    if not is_symbolic_data_model(relation_model)
                    else serialization_lib.serialize_synalinks_object(relation_model)
                )
                for i, relation_model in enumerate(self.relation_models)
            ]
        }
        return {
            **config,
            **knowledge_base_config,
            **language_model_config,
            **entity_models_config,
            **relation_models_config,
        }

    @classmethod
    def from_config(cls, config):
        knowledge_base = serialization_lib.deserialize_synalinks_object(
            config.pop("knowledge_base"),
        )
        language_model = serialization_lib.deserialize_synalinks_object(
            config.pop("language_model"),
        )
        entity_models_config = config.pop("entity_models")
        entity_models = [
            serialization_lib.deserialize_synalinks_object(entity_model)
            for entity_model in entity_models_config
        ]
        relation_models_config = config.pop("relation_models")
        relation_models = [
            serialization_lib.deserialize_synalinks_object(relation_model)
            for relation_model in relation_models_config
        ]
        return cls(
            knowledge_base=knowledge_base,
            entity_models=entity_models,
            relation_models=relation_models,
            language_model=teacher_language_model,
            **config,
        )
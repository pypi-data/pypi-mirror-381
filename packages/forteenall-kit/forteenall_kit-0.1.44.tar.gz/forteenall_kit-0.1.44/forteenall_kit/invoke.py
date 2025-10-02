from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any
from forteenall_kit.models import FeatureData, FieldBase
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.manager import FeatureManager

# class FeatureManager:
#     def __init__(self):
#         self._features: dict[str, Invoker] = {}
#         self.appendedFeatures = {}
#         self.executed = set()
#         self.jsonData = {}
#         self.projectName = ""

#     def success(self, message: str):
#         pass

#     def warning(self, message: str):
#         pass

#     def error(self, message: str):
#         pass

#     def print(self, message: str):
#         pass

#     def shell(self, command: str, message: None | str = None):
#         pass


class Invoker(ABC):
    model: FeatureData = None

    def __init__(
        self,
        feature_id: int,
        name: str,
        manager,
        options: dict[str, Any],
        invokerType: str,
    ):
        # set main data from manager
        self.id = feature_id
        self.name = name
        self.manager: FeatureManager = manager
        self.options = options
        self.feature_type = invokerType

        if self.model is None:
            raise SyntaxError(f"model `{self.feature_type}:{self.name}` is None")

        self.objects: FeatureData = self.model(options)

        # set field and another data
        for option, value in self.options.items():
            feature_model_field_instance: FieldBase = self.model.__dict__[option]
            feature_model_field_instance.setValue(value)
            self.objects._addField(option, feature_model_field_instance)

            self.__setattr__(option, value)

    def init(self):
        pass

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    def log(self, message):
        print(f"[{self.name}:{self.id}] {message}")

    def _generate(self):
        """
        this function generate YAML standard
        this yaml use in forteenall kit
        for another packages
        """

    def invoke(self, feature_name, obj, safeCheck=False):
        """
        this function invoke the Forteenall Object
        """

        self.manager.execute(feature_name, **obj)

    def ask(self, quest: str, options: list[str]) -> str:
        """this function select an option from question

        Args:
            quest (_type_): text that option is similiar that
            options (_type_): list of options
        """

        return options[0]

import typing as t

from ellar.pydantic import as_pydantic_validator
from ellar.utils.importer import import_from_string
from jinja2 import TemplateNotFound
from jinja2.loaders import BaseLoader

if t.TYPE_CHECKING:  # pragma: no cover
    from ellar.app.main import App

    from .environment import Environment


class JinjaLoader(BaseLoader):
    """A loader that looks for templates in the application.
    An idea from flask
    """

    def __init__(self, app: "App") -> None:
        self.app = app

    def get_source(  # type: ignore
        self, environment: "Environment", template: str
    ) -> t.Tuple[str, t.Optional[str], t.Optional[t.Callable]]:
        return self._get_source_fast(environment, template)

    def _get_source_fast(
        self, environment: "Environment", template: str
    ) -> t.Tuple[str, t.Optional[str], t.Optional[t.Callable]]:
        for loader in self._iter_loaders(template):
            try:
                return loader.get_source(environment, template)
            except TemplateNotFound:
                continue
        raise TemplateNotFound(template)

    def _iter_loaders(self, template: str) -> t.Generator[BaseLoader, None, None]:
        for module in self.app.get_module_loaders():
            loader = module.jinja_loader
            if loader is not None:
                yield loader

    def list_templates(self) -> t.List[str]:  # pragma: no cover
        # TODO: add test for this
        result = set()

        for module_loader in self.app.get_module_loaders():
            loader = module_loader.jinja_loader
            if loader is not None:
                for template in loader.list_templates():
                    result.add(template)

        return list(result)


@as_pydantic_validator("__validate_input__", schema={"type": "object"})
class JinjaLoaderType(BaseLoader):
    @classmethod
    def __validate_input__(cls, v: t.Any, _: t.Any) -> t.Any:
        if isinstance(v, str):
            v = import_from_string(v)

        if not isinstance(v, BaseLoader):
            raise ValueError(f"Expected {BaseLoader} object, received: {type(v)}")
        return v

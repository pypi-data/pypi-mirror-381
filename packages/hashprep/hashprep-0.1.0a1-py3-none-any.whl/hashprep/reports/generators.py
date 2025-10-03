from abc import ABC, abstractmethod


class ReportGenerator(ABC):
    @abstractmethod
    def generate(self, summary, full=False, output_file=None):
        pass


# Lazy loading report classes
def _load_generators():
    from .markdown import MarkdownReport
    from .json import JsonReport
    from .html import HtmlReport
    from .pdf import PdfReport

    return {
        "md": MarkdownReport(),
        "json": JsonReport(),
        "html": HtmlReport(),
        "pdf": PdfReport(),
    }

# get generators dictionary
def get_generators():
    if not hasattr(get_generators, 'cache'):
        get_generators.cache = _load_generators()
        return get_generators.cache

def generate_report(summary, format="md", full=False, output_file=None, include_plots=False):
    generators = get_generators()
    if format not in generators:
        raise ValueError(f"Unsupported format: {format}")
    return generators[format].generate(summary, full, output_file=output_file, include_plots=include_plots)

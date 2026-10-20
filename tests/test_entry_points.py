"""The conda recipe entry point must match the console script the package installs.

`[project.scripts]` in the scikit-package pyproject template installs
`diffpy-cmipdf` (dots replaced by dashes), so the generated recipe must
declare the same name. These tests render the `entry_points` line of the
meta.yaml template directly with Jinja2, which keeps them runnable in an
environment without the `cookiecutter` package.
"""
from pathlib import Path

from jinja2 import Environment

TEMPLATE_DIR = Path(__file__).resolve().parents[1] / "{{ cookiecutter.package_import_name }}"


def _render_entry_points_line(package_import_name: str) -> str:
    """Render the entry_points line of meta.yaml as cookiecutter would."""
    template_text = (TEMPLATE_DIR / "meta.yaml").read_text()
    entry_points_line = next(
        line for line in template_text.splitlines() if line.lstrip().startswith("-  {{ cookiecutter")
    )
    rendered = (
        Environment()
        .from_string(entry_points_line)
        .render(cookiecutter={"package_import_name": package_import_name})
    )
    # drop the YAML list marker (`-  `) so only the entry point remains
    return rendered.strip().lstrip("-").strip()


def test_namespace_package_entry_point_name_uses_dashes() -> None:
    rendered = _render_entry_points_line("diffpy.cmipdf")

    assert rendered == "diffpy-cmipdf = diffpy.cmipdf.diffpy_cmipdf_app:main"


def test_single_module_package_entry_point_name_unchanged() -> None:
    rendered = _render_entry_points_line("mypackage")

    assert rendered == "mypackage = mypackage.mypackage_app:main"


def test_reference_file_uses_the_dashed_name() -> None:
    """The committed reference meta.yaml the cookiecutter test compares against."""
    reference = Path(__file__).parent / "diffpy.example" / "meta.yaml"
    entry_points_line = next(
        line.strip().lstrip("-").strip()
        for line in reference.read_text().splitlines()
        if "= diffpy.pdfgui." in line
    )

    assert entry_points_line == "diffpy-pdfgui = diffpy.pdfgui.diffpy_pdfgui_app:main"

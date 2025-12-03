from __future__ import annotations

import csv
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple



data_dir = Path(__file__).resolve().parent.parent / "data"
results_path = Path(__file__).resolve().parent.parent / "results" / "data_summary.md"
figures_dir = Path(__file__).resolve().parent.parent / "results" / "figures"


@dataclass
class SubsystemSummary:
    name: str
    total_tests: int
    fault_types: Counter
    components: Counter
    classes: Counter
    functions: Counter

    @property
    def unique_components(self) -> int:
        return len(self.components)

    @property
    def unique_classes(self) -> int:
        return len(self.classes)

    @property
    def unique_functions(self) -> int:
        return len(self.functions)


def load_rows(path: Path) -> List[Dict[str, str]]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter=";")
        return list(reader)


def summarize_subsystem(name: str) -> SubsystemSummary:
    path = data_dir / f"{name}.csv"
    rows = load_rows(path)
    fault_types = Counter(row["Fault_Type"] for row in rows)
    components = Counter(row["Target_Component"] for row in rows)
    classes = Counter(row["Target_Class"] for row in rows)
    functions = Counter(row["Target_Function"] for row in rows)

    return SubsystemSummary(
        name=name,
        total_tests=len(rows),
        fault_types=fault_types,
        components=components,
        classes=classes,
        functions=functions,
    )


def format_counter_table(counter: Counter, limit: int | None = None) -> str:
    items = counter.most_common(limit)
    lines = ["| Item | Count |", "| --- | ---: |"]
    lines.extend(f"| {item} | {count} |" for item, count in items)
    return "\n".join(lines)


def plot_bar_chart(
    items: Sequence[Tuple[str, int]],
    title: str,
    xlabel: str,
    ylabel: str,
    filename: str,
    rotation: int = 45,
) -> Path:
    path = figures_dir / filename

    if not items:
        path.write_text("<svg xmlns=\"http://www.w3.org/2000/svg\"></svg>")
        return path

    labels, values = zip(*items)
    width, height = 1000, 600
    margin = 80
    bar_area_width = width - 2 * margin
    bar_area_height = height - 2 * margin
    bar_width = bar_area_width / len(values)
    max_value = max(values)
    scale = bar_area_height / max_value if max_value else 0

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}">',
        f'<text x="{width / 2}" y="30" text-anchor="middle" font-size="18" font-family="Arial" fill="#111">{title}</text>',
        f'<text x="{width / 2}" y="{height - 20}" text-anchor="middle" font-size="14" font-family="Arial" fill="#111">{xlabel}</text>',
        f'<text x="20" y="{height / 2}" text-anchor="middle" font-size="14" font-family="Arial" fill="#111" transform="rotate(-90 20,{height / 2})">{ylabel}</text>',
        f'<line x1="{margin}" y1="{height - margin}" x2="{width - margin}" y2="{height - margin}" stroke="#444"/>',
        f'<line x1="{margin}" y1="{margin}" x2="{margin}" y2="{height - margin}" stroke="#444"/>',
    ]

    for idx, (label, value) in enumerate(items):
        bar_height = value * scale
        x = margin + idx * bar_width
        y = height - margin - bar_height
        svg_parts.append(
            f'<rect x="{x + bar_width * 0.1}" y="{y}" width="{bar_width * 0.8}" height="{bar_height}" fill="#4C72B0"/>'
        )
        svg_parts.append(
            f'<text x="{x + bar_width / 2}" y="{height - margin + 15}" transform="rotate({-rotation} {x + bar_width / 2},{height - margin + 15})" font-size="10" text-anchor="end" font-family="Arial">{label}</text>'
        )
        svg_parts.append(
            f'<text x="{x + bar_width / 2}" y="{y - 5}" text-anchor="middle" font-size="10" font-family="Arial" fill="#111">{value}</text>'
        )

    svg_parts.append("</svg>")
    path.write_text("\n".join(svg_parts))
    return path


def generate_visualizations(summaries: Sequence[SubsystemSummary]) -> List[Tuple[str, Path]]:
    figures_dir.mkdir(parents=True, exist_ok=True)
    figures: List[Tuple[str, Path]] = []

    totals = [(summary.name, summary.total_tests) for summary in summaries]
    figures.append(
        (
            "Total tests per subsystem",
            plot_bar_chart(
                totals,
                title="Total fault-injection tests per subsystem",
                xlabel="Subsystem",
                ylabel="Number of tests",
                filename="subsystem_totals.svg",
                rotation=0,
            ),
        )
    )

    overall_faults = Counter()
    for summary in summaries:
        overall_faults.update(summary.fault_types)

    figures.append(
        (
            "Overall fault-type distribution (top 15)",
            plot_bar_chart(
                overall_faults.most_common(15),
                title="Top 15 fault types across all subsystems",
                xlabel="Fault type",
                ylabel="Count",
                filename="overall_fault_types.svg",
            ),
        )
    )

    for summary in summaries:
        figures.append(
            (
                f"{summary.name} fault-type distribution",
                plot_bar_chart(
                    summary.fault_types.most_common(),
                    title=f"{summary.name} fault-type distribution",
                    xlabel="Fault type",
                    ylabel="Count",
                    filename=f"{summary.name.lower()}_fault_types.svg",
                ),
            )
        )

        figures.append(
            (
                f"{summary.name} top 10 target components",
                plot_bar_chart(
                    summary.components.most_common(10),
                    title=f"{summary.name} top 10 target components",
                    xlabel="Component",
                    ylabel="Count",
                    filename=f"{summary.name.lower()}_components.svg",
                ),
            )
        )

    return figures


def write_summary(
    summaries: Iterable[SubsystemSummary],
    figures: Sequence[Tuple[str, Path]] | None = None,
) -> None:
    summaries = list(summaries)
    overall_total = sum(summary.total_tests for summary in summaries)
    content = [
        "# Fault Injection Dataset Summary",
        "",
        "This report provides quick statistics for the OpenStack fault injection data in the `data/` directory.",
        "",
        f"Total tests across all subsystems: **{overall_total}**.",
        "",
    ]

    if figures:
        content.extend(["## Visual summaries", ""])
        for description, path in figures:
            relative_path = path.relative_to(results_path.parent)
            content.append(f"* {description}: `{relative_path.as_posix()}`")
        content.extend(["", "---", ""])

    for summary in summaries:
        content.extend(
            [
                f"## {summary.name}",
                "",
                f"* Total tests: **{summary.total_tests}**",
                f"* Unique target components: **{summary.unique_components}**",
                f"* Unique target classes: **{summary.unique_classes}**",
                f"* Unique target functions: **{summary.unique_functions}**",
                "",
                "### Fault types",
                format_counter_table(summary.fault_types),
                "",
                "### Top 5 target components",
                format_counter_table(summary.components, limit=5),
                "",
                "### Top 5 target classes",
                format_counter_table(summary.classes, limit=5),
                "",
                "### Top 5 target functions",
                format_counter_table(summary.functions, limit=5),
                "",
            ]
        )

    results_path.parent.mkdir(parents=True, exist_ok=True)
    results_path.write_text("\n".join(content))


if __name__ == "__main__":
    subsystems = [summarize_subsystem(name) for name in ("Cinder", "Neutron", "Nova")]
    figure_paths = generate_visualizations(subsystems)
    write_summary(subsystems, figures=figure_paths)

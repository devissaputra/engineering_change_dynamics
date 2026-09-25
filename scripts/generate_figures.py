#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import html
import math
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

COLORS = {
    "perfective": "#2563eb",
    "corrective": "#f97316",
    "other": "#16a34a",
}
PURPLE = "#7c3aed"
GRAY = "#64748b"
INK = "#172033"
SOFT = "#475569"
GRID = "#e2e8f0"


def esc(value):
    return html.escape(str(value))


def open_svg(width, height):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}"><rect width="100%" height="100%" fill="#ffffff"/>'
    )


def text(x, y, value, size=16, weight="400", anchor="start", fill=INK):
    return (
        f'<text x="{x}" y="{y}" font-family="Arial, Helvetica, sans-serif" '
        f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" fill="{fill}">'
        f'{esc(value)}</text>'
    )


def line(x1, y1, x2, y2, stroke=GRID, width=1, dash=None):
    extra = f' stroke-dasharray="{dash}"' if dash else ""
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{stroke}" stroke-width="{width}"{extra}/>'
    )


def box(x, y, width, height, title, lines, fill, stroke, title_fill=INK):
    output = [
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="15" '
        f'fill="{fill}" stroke="{stroke}" stroke-width="1.5"/>',
        text(x + 18, y + 31, title, 16, "700", "start", title_fill),
    ]
    for index, item in enumerate(lines):
        output.append(
            text(x + 18, y + 57 + index * 21, item, 12.5, "400", "start", SOFT)
        )
    return "".join(output)


def arrow(x1, y1, x2, y2, color=GRAY):
    return (
        line(x1, y1, x2 - 12, y2, color, 2)
        + f'<polygon points="{x2-12},{y2-6} {x2},{y2} {x2-12},{y2+6}" fill="{color}"/>'
    )


def read_csv(name):
    with (ROOT / "data/derived" / name).open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def architecture():
    projects = read_csv("project_composition.csv")

    perfective_vertex = (110, 600)
    corrective_vertex = (790, 600)
    other_vertex = (450, 120)

    def ternary(perfective, corrective, other):
        return (
            perfective * perfective_vertex[0]
            + corrective * corrective_vertex[0]
            + other * other_vertex[0],
            perfective * perfective_vertex[1]
            + corrective * corrective_vertex[1]
            + other * other_vertex[1],
        )

    output = [
        open_svg(1200, 740),
        text(55, 50, "Cross-project maintenance-intent composition", 30, "700"),
        text(
            55,
            80,
            "Each point is one Apache project; position encodes perfective, corrective, and other shares; point size reflects labeled sample size.",
            15,
            "400",
            "start",
            SOFT,
        ),
        (
            f'<polygon points="{perfective_vertex[0]},{perfective_vertex[1]} '
            f'{corrective_vertex[0]},{corrective_vertex[1]} '
            f'{other_vertex[0]},{other_vertex[1]}" fill="#f8fafc" '
            'stroke="#334155" stroke-width="2"/>'
        ),
    ]

    for fraction in (0.2, 0.4, 0.6, 0.8):
        p1 = ternary(fraction, 0, 1 - fraction)
        p2 = ternary(fraction, 1 - fraction, 0)
        c1 = ternary(0, fraction, 1 - fraction)
        c2 = ternary(1 - fraction, fraction, 0)
        o1 = ternary(0, 1 - fraction, fraction)
        o2 = ternary(1 - fraction, 0, fraction)
        output.extend(
            [
                line(*p1, *p2),
                line(*c1, *c2),
                line(*o1, *o2),
            ]
        )

    output.extend(
        [
            text(100, 635, "Perfective", 14, "700", "start", COLORS["perfective"]),
            text(800, 635, "Corrective", 14, "700", "end", COLORS["corrective"]),
            text(450, 102, "Other", 14, "700", "middle", COLORS["other"]),
        ]
    )

    labels = {"phoenix", "pdfbox", "commons-math", "commons-lang", "tez", "nifi"}

    for row in projects:
        p = float(row["perfective_share"])
        c = float(row["corrective_share"])
        o = float(row["other_share"])
        x, y = ternary(p, c, o)
        dominant = max(
            (("perfective", p), ("corrective", c), ("other", o)),
            key=lambda item: item[1],
        )[0]
        radius = 4 + math.sqrt(int(row["n"])) * 0.35

        output.append(
            f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius:.1f}" '
            f'fill="{COLORS[dominant]}" fill-opacity="0.62" stroke="#ffffff" stroke-width="1.2"/>'
        )
        if row["project"] in labels:
            output.append(
                text(x + 8, y - 10, row["project"], 11.5, "700", "start", "#334155")
            )

    pooled_x, pooled_y = ternary(0.403474, 0.27043, 0.326096)
    output.extend(
        [
            f'<circle cx="{pooled_x}" cy="{pooled_y}" r="11" fill="#111827" stroke="#fbbf24" stroke-width="4"/>',
            text(pooled_x + 18, pooled_y + 5, "Pooled composition", 12.5, "700"),
            '<rect x="850" y="118" width="300" height="255" rx="16" fill="#f8fafc" stroke="#cbd5e1"/>',
            text(875, 150, "Released evidence", 17, "700"),
            text(875, 182, "2,533 manually classified commits", 12.5, "600"),
            text(875, 207, "54 Java Apache projects", 12.5, "600"),
            text(875, 232, "Perfective 40.3%", 12.5, "700", "start", COLORS["perfective"]),
            text(875, 257, "Corrective 27.0%", 12.5, "700", "start", COLORS["corrective"]),
            text(875, 282, "Other 32.6%", 12.5, "700", "start", COLORS["other"]),
            text(875, 322, "Primary n ≥ 20 analysis", 13, "700", "start", "#334155"),
            text(875, 347, "Cramér's V = 0.302", 13, "700", "start", PURPLE),
            '<rect x="850" y="400" width="300" height="200" rx="16" fill="#fff7ed" stroke="#fdba74"/>',
            text(875, 432, "Interpretation", 15, "700", "start", "#9a3412"),
            text(875, 463, "Projects occupy visibly different", 12.5, "400", "start", "#7c2d12"),
            text(875, 485, "regions of the composition space.", 12.5, "400", "start", "#7c2d12"),
            text(875, 517, "The pooled marker is a portfolio", 12.5, "400", "start", "#7c2d12"),
            text(875, 539, "average, not a project template.", 12.5, "400", "start", "#7c2d12"),
            text(55, 712, "Color marks the dominant observed category. Point size represents the manually labeled sample size.", 12, "400", "start", GRAY),
            "</svg>",
        ]
    )
    return "".join(output)


def method():
    output = [
        open_svg(1200, 720),
        text(55, 50, "Reproducible cross-project heterogeneity pipeline", 30, "700"),
        text(
            55,
            80,
            "The pipeline preserves the source taxonomy, separates description from inference, and exposes the projects driving the omnibus pattern.",
            15,
            "400",
            "start",
            SOFT,
        ),
        box(45, 135, 205, 125, "1 • Zenodo source", ["manual_labels.csv", "2,533 commits", "54 projects"], "#eff6ff", "#3b82f6", "#1d4ed8"),
        box(290, 135, 205, 125, "2 • Taxonomy check", ["Perfective", "Corrective", "Other only"], "#f5f3ff", "#8b5cf6", "#6d28d9"),
        box(535, 135, 205, 125, "3 • Project profiles", ["Counts + shares", "Wilson intervals"], "#f0fdf4", "#22c55e", "#15803d"),
        box(780, 135, 205, 125, "4 • Primary inference", ["Projects n ≥ 20", "χ² + Cramér's V"], "#fff7ed", "#f59e0b", "#92400e"),
        arrow(250, 198, 290, 198),
        arrow(495, 198, 535, 198),
        arrow(740, 198, 780, 198),
        box(780, 335, 205, 135, "5 • Sensitivity", ["n ≥ 10 / 20 / 30", "40 / 50", "Track V stability"], "#eef2ff", "#6366f1", "#4338ca"),
        arrow(882, 260, 882, 335, "#6366f1"),
        box(505, 335, 225, 135, "6 • Cell diagnostics", ["Primary residuals", "Observed vs expected", "No separate p claims"], "#fef2f2", "#ef4444", "#991b1b"),
        arrow(780, 402, 730, 402, "#ef4444"),
        box(230, 335, 225, 135, "7 • Project contribution", ["Sum cell χ² terms", "Explain omnibus result", "No quality ranking"], "#ecfeff", "#06b6d4", "#0e7490"),
        arrow(505, 402, 455, 402, "#06b6d4"),
        box(230, 540, 755, 105, "8 • Bounded interpretation", ["Portfolio average can hide local maintenance profiles", "No causal, temporal, cost, schedule, or quality ranking claim"], "#f8fafc", "#94a3b8", "#334155"),
        arrow(342, 470, 342, 540, "#06b6d4"),
        arrow(618, 470, 618, 540, "#ef4444"),
        arrow(882, 470, 882, 540, "#6366f1"),
        text(55, 700, "Scientific safeguard: the n ≥ 20 primary restriction is explicit, while full-table and stricter thresholds remain visible as sensitivity evidence.", 13, "700", "start", "#334155"),
        "</svg>",
    ]
    return "".join(output)


def category_composition():
    rows = read_csv("category_summary.csv")
    output = [
        open_svg(1100, 620),
        text(50, 50, "Pooled maintenance-intent composition", 29, "700"),
        text(50, 80, "2,533 manually classified commits with 95% Wilson intervals", 15, "400", "start", SOFT),
    ]

    base, top, max_share = 500, 130, 0.5
    x_positions = [210, 500, 790]
    bar_width = 135

    for index, row in enumerate(rows):
        share = float(row["share"])
        lower = float(row["ci_low"])
        upper = float(row["ci_high"])
        x = x_positions[index]
        y = base - (share / max_share) * (base - top)
        height = base - y
        y_low = base - (lower / max_share) * (base - top)
        y_high = base - (upper / max_share) * (base - top)
        color = COLORS[row["category"]]

        output.extend(
            [
                f'<rect x="{x}" y="{y}" width="{bar_width}" height="{height}" rx="7" fill="{color}" fill-opacity="0.78"/>',
                line(x + bar_width / 2, y_high, x + bar_width / 2, y_low, "#111827", 2),
                line(x + bar_width / 2 - 14, y_high, x + bar_width / 2 + 14, y_high, "#111827", 2),
                line(x + bar_width / 2 - 14, y_low, x + bar_width / 2 + 14, y_low, "#111827", 2),
                text(x + bar_width / 2, y - 14, f"{share*100:.1f}%", 17, "700", "middle", color),
                text(x + bar_width / 2, base + 32, row["category"].title(), 14, "700", "middle", "#334155"),
                text(x + bar_width / 2, base + 55, f'n = {row["count"]}', 12, "600", "middle", GRAY),
            ]
        )

    for value in (0, 0.1, 0.2, 0.3, 0.4, 0.5):
        y = base - (value / max_share) * (base - top)
        output.extend(
            [
                line(100, y, 1000, y),
                text(88, y + 5, f"{value*100:.0f}%", 12, "400", "end", GRAY),
            ]
        )

    output.extend(
        [
            line(100, base, 1000, base, "#334155", 1.7),
            line(100, top, 100, base, "#334155", 1.7),
            text(50, 600, "The pooled profile is a portfolio average; project-level proportions vary substantially around it.", 12, "400", "start", GRAY),
            "</svg>",
        ]
    )
    return "".join(output)


def project_heterogeneity():
    rows = read_csv("primary_project_residuals.csv")[:12]

    output = [
        open_svg(1200, 760),
        text(55, 50, "Largest project-category departures in the primary subset", 30, "700"),
        text(55, 80, "Pearson residuals for projects with n ≥ 20. Positive means more observed than expected; negative means fewer.", 15, "400", "start", SOFT),
    ]

    zero = 660
    scale = 58
    row_top = 130
    row_gap = 44

    output.append(
        line(
            zero,
            row_top - 22,
            zero,
            row_top + row_gap * (len(rows) - 1) + 24,
            "#334155",
            1.5,
        )
    )

    for index, row in enumerate(rows):
        value = float(row["pearson_residual"])
        y = row_top + index * row_gap
        x2 = zero + value * scale
        color = COLORS[row["category"]]

        output.extend(
            [
                line(zero, y, x2, y, color, 8),
                f'<circle cx="{x2}" cy="{y}" r="6" fill="{color}"/>',
                text(305, y + 5, f'{row["project"]} · {row["category"]}', 12.5, "700", "end", "#334155"),
                text(x2 + (10 if value >= 0 else -10), y + 5, f"{value:.2f}", 11.5, "700", "start" if value >= 0 else "end", color),
            ]
        )

    for value in (-5, -3, -1, 1, 3, 5):
        x = zero + value * scale
        output.extend(
            [
                line(x, row_top - 22, x, row_top + row_gap * (len(rows) - 1) + 24, "#eef2f7"),
                text(x, 700, value, 11, "400", "middle", GRAY),
            ]
        )

    output.extend(
        [
            text(660, 728, "Pearson residual", 13, "600", "middle"),
            '<rect x="875" y="112" width="250" height="104" rx="12" fill="#f8fafc" stroke="#cbd5e1"/>',
            f'<circle cx="895" cy="140" r="6" fill="{COLORS["perfective"]}"/>',
            text(912, 145, "Perfective", 12, "700"),
            f'<circle cx="895" cy="166" r="6" fill="{COLORS["corrective"]}"/>',
            text(912, 171, "Corrective", 12, "700"),
            f'<circle cx="895" cy="192" r="6" fill="{COLORS["other"]}"/>',
            text(912, 197, "Other", 12, "700"),
            text(55, 742, "Residuals explain the omnibus result and are not separate multiplicity-adjusted project tests.", 12, "400", "start", GRAY),
            "</svg>",
        ]
    )
    return "".join(output)


def sensitivity():
    rows = read_csv("heterogeneity_results.csv")

    output = [
        open_svg(1100, 620),
        text(50, 50, "Heterogeneity remains stable as small projects are removed", 29, "700"),
        text(50, 80, "Cramér's V changes little while the retained project count falls from 54 to 17.", 15, "400", "start", SOFT),
    ]

    left, right, top, bottom = 115, 1015, 145, 480
    min_v, max_v = 0.285, 0.31

    def sx(index):
        return left + index * (right - left) / (len(rows) - 1)

    def sy(value):
        return bottom - (value - min_v) / (max_v - min_v) * (bottom - top)

    for value in (0.29, 0.295, 0.30, 0.305, 0.31):
        y = sy(value)
        output.extend(
            [
                line(left, y, right, y),
                text(left - 12, y + 5, f"{value:.3f}", 12, "400", "end", GRAY),
            ]
        )

    points = " ".join(
        f"{sx(index)},{sy(float(row['cramers_v']))}"
        for index, row in enumerate(rows)
    )
    output.append(
        f'<polyline points="{points}" fill="none" stroke="{PURPLE}" stroke-width="4" '
        'stroke-linecap="round" stroke-linejoin="round"/>'
    )

    for index, row in enumerate(rows):
        x = sx(index)
        y = sy(float(row["cramers_v"]))
        output.extend(
            [
                f'<circle cx="{x}" cy="{y}" r="7" fill="#fff" stroke="{PURPLE}" stroke-width="3"/>',
                text(x, y - 13, f'{float(row["cramers_v"]):.3f}', 11.5, "700", "middle", PURPLE),
                text(x, bottom + 30, f'n ≥ {row["min_project_n"]}', 12.5, "700", "middle", "#334155"),
                text(x, bottom + 52, f'{row["projects"]} projects', 11.5, "600", "middle", GRAY),
            ]
        )

    output.extend(
        [
            line(left, bottom, right, bottom, "#334155", 1.7),
            line(left, top, left, bottom, "#334155", 1.7),
            text(50, 594, "Primary analysis: n ≥ 20, 43 projects, V = 0.302. Stricter thresholds reduce sample size without materially changing the effect estimate.", 12, "400", "start", GRAY),
            "</svg>",
        ]
    )
    return "".join(output)


def evaluation():
    output = [
        open_svg(1200, 660),
        text(55, 50, "Evidence boundary and released findings", 30, "700"),
        box(55, 100, 1090, 96, "Observed composition", ["Perfective 40.3% • Corrective 27.0% • Other 32.6% across 2,533 manually classified commits."], "#eff6ff", "#3b82f6", "#1d4ed8"),
        box(55, 220, 1090, 96, "Cross-project heterogeneity", ["Primary n ≥ 20 analysis: χ²(84)=432.452 • Cramér's V=0.302 • no expected cells below 5."], "#f0fdf4", "#22c55e", "#15803d"),
        box(55, 340, 1090, 96, "Robustness and drivers", ["V remains 0.293 to 0.305 across thresholds; Phoenix, PDFBox, Commons Math, Commons Lang, and Tez are major contributors."], "#fff7ed", "#f97316", "#9a3412"),
        box(55, 460, 1090, 96, "Claim boundary", ["Maintenance intent is not project quality, causality, requirements churn, rework cost, schedule impact, or temporal dynamics."], "#fef2f2", "#ef4444", "#991b1b"),
        text(55, 630, "Engineering interpretation: portfolio averages should not be assumed to describe each project's local maintenance profile.", 13, "700", "start", "#334155"),
        "</svg>",
    ]
    return "".join(output)


def render(out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    figures = {
        "architecture.svg": architecture(),
        "method.svg": method(),
        "category_composition.svg": category_composition(),
        "project_heterogeneity.svg": project_heterogeneity(),
        "sensitivity.svg": sensitivity(),
        "evaluation.svg": evaluation(),
    }

    for name, content in figures.items():
        ET.fromstring(content)
        (out_dir / name).write_text(content, encoding="utf-8")

    return figures


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out-dir", default=str(ROOT / "assets"))
    args = parser.parse_args()
    figures = render(Path(args.out_dir))
    print("generated_figures:", len(figures))


if __name__ == "__main__":
    main()

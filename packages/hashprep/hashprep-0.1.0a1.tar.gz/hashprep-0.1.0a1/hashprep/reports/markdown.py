import pandas as pd
import json
import yaml
import hashprep
from datetime import datetime


class MarkdownReport:
    def generate(self, summary, full=False, output_file=None, include_plots=False):
        content = "# Dataset Quality Report\n\n"
        content += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  \n"
        content += f"HashPrep Version: {hashprep.__version__}\n\n"
        content += "## Executive Summary\n"
        content += f"- Critical Issues: {summary['critical_count']}\n"
        content += f"- Warnings: {summary['warning_count']}\n"
        content += f"- Rows: {summary['summaries']['dataset_info']['rows']}\n"
        content += f"- Columns: {summary['summaries']['dataset_info']['columns']}\n\n"
        content += "## Issues Overview\n\n"
        content += (
            "| Category | Severity | Column | Description | Impact | Quick Fix |\n"
        )
        content += (
            "|----------|----------|--------|-------------|--------|-----------|\n"
        )
        for issue in summary["issues"]:
            quick_fix_inline = issue["quick_fix"].replace("\n", " ").replace("- ", "• ")
            content += f"| {issue['category']} | {issue['severity']} | {issue['column']} | {issue['description']} | {issue['impact_score']} | {quick_fix_inline} |\n"
        if full:
            content += "\n## Dataset Preview\n\n"
            content += (
                "### Head\n\n"
                + pd.DataFrame(summary["summaries"]["head"]).to_markdown(index=False)
                + "\n\n"
            )
            content += (
                "### Tail\n\n"
                + pd.DataFrame(summary["summaries"]["tail"]).to_markdown(index=False)
                + "\n\n"
            )
            content += (
                "### Sample\n\n"
                + pd.DataFrame(summary["summaries"]["sample"]).to_markdown(index=False)
                + "\n\n"
            )
            content += "## Variables\n\n"
            for col, stats in summary["summaries"]["variables"].items():
                content += f"### {col}\n\n"
                content += f"```yaml\n{yaml.safe_dump({k: v for k, v in stats.items() if k != 'plot'}, default_flow_style=False)}\n```\n"
                if include_plots and "plot" in stats:
                    content += (
                        f"![{col} Plot](data:image/png;base64,{stats['plot']})\n\n"
                    )
            content += "## Correlations\n\n"
            content += "### Numeric Correlations\n\n"
            if include_plots and "plots" in summary["summaries"].get(
                "numeric_correlations", {}
            ):
                for method in ["pearson", "spearman", "kendall"]:
                    content += f"#### {method.capitalize()}\n\n"
                    content += f"![{method.capitalize()} Correlation Heatmap](data:image/png;base64,{summary['summaries']['numeric_correlations']['plots'][method]})\n\n"
            else:
                content += (
                    "#### Pearson\n\n```json\n"
                    + json.dumps(
                        summary["summaries"]
                        .get("numeric_correlations", {})
                        .get("pearson", {}),
                        indent=2,
                    )
                    + "\n```\n"
                )
            content += "### Scatter Plots\n\n"
            scatter_data = summary["summaries"].get("scatter_pairs", {})
            if include_plots and "plots" in scatter_data:
                for pair, img_str in scatter_data["plots"].items():
                    content += f"#### {pair}\n\n"
                    content += (
                        f"![{pair} Scatter Plot](data:image/png;base64,{img_str})\n\n"
                    )
            else:
                content += "| Pair |\n|------|\n"
                for c1, c2 in scatter_data.get("pairs", []):
                    content += f"| {c1} vs {c2} |\n"
            content += (
                "### Categorical (Cramer's V)\n\n| Pair | Value |\n|------|-------|\n"
            )
            for pair, val in (
                summary["summaries"].get("categorical_correlations", {}).items()
            ):
                content += f"| {pair} | {val:.2f} |\n"
            content += "\n### Mixed\n\n| Pair | F-Stat | P-Value |\n|------|--------|---------|\n"
            for pair, stats in (
                summary["summaries"].get("mixed_correlations", {}).items()
            ):
                if "error" not in stats:
                    content += (
                        f"| {pair} | {stats['f_stat']:.2f} | {stats['p_value']:.4f} |\n"
                    )
            content += "\n## Missing Values\n\n"
            content += (
                "| Column | Count | Percentage |\n|--------|-------|------------|\n"
            )
            for col, count in summary["summaries"]["missing_values"]["count"].items():
                pct = summary["summaries"]["missing_values"]["percentage"][col]
                if count > 0:
                    content += f"| {col} | {count} | {pct} |\n"
            print("pass 6: if condition: ", summary["summaries"].keys())
            if include_plots and "plots" in summary["summaries"]:
                content += "\n### Missing Values Plots\n\n"
                plots = summary["summaries"]["plots"]
                print("pass 7: plots in markdown.py: ", plots)
                if plots.get("missing_bar"):
                    content += "#### Missing Values Count\n\n"
                    content += f"![Missing Values Bar](data:image/png;base64,{plots['missing_bar']})\n\n"
                if plots.get("missing_heatmap"):
                    content += "#### Missing Values Heatmap\n\n"
                    content += f"![Missing Values Heatmap](data:image/png;base64,{plots['missing_heatmap']})\n\n"
                if not (plots.get("missing_bar") or plots.get("missing_heatmap")):
                    content += "No missing value plots available.\n\n"
            else:
                content += "\nNo missing value plots generated (include_plots=False or no plots available).\n\n"
            content += (
                "\n## Missing Patterns\n\n```json\n"
                + json.dumps(summary["summaries"]["missing_patterns"], indent=2)
                + "\n```\n"
            )
        content += "\n## Next Steps\n- Address critical issues\n- Handle warnings\n- Re-analyze dataset\n\n---\nGenerated by HashPrep"
        if output_file:
            with open(output_file, "w") as f:
                f.write(content)
        return content

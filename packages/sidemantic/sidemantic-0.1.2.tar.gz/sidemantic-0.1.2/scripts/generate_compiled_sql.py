#!/usr/bin/env python3
# /// script
# dependencies = [
#   "sidemantic==0.1.1",
#   "sqlglot>=25.0.0",
#   "pyyaml>=6.0",
#   "pydantic>=2.0.0",
# ]
# ///

import json
from pathlib import Path

from sidemantic import Dimension, Join, Measure, Model
from sidemantic.core.semantic_graph import SemanticGraph
from sidemantic.sql.generator_v2 import SQLGenerator


def build_graph() -> tuple[SemanticGraph, SQLGenerator]:
    graph = SemanticGraph()

    orders_model = Model(
        name="orders",
        table="orders",
        primary_key="id",
        dimensions=[
            Dimension(name="status", type="categorical", expr="status"),
            Dimension(name="order_date", type="time", expr="order_date", granularity="day"),
            Dimension(name="region", type="categorical", expr="region"),
            Dimension(name="category", type="categorical", expr="category"),
        ],
        measures=[
            Measure(name="revenue", agg="sum", expr="amount"),
            Measure(name="order_count", agg="count"),
            Measure(name="avg_order_value", agg="avg", expr="amount"),
            Measure(name="cost", agg="sum", expr="cost"),
            Measure(name="profit", agg="sum", expr="profit"),
            Measure(name="returns", agg="count", filters=["status = 'returned'"]),
            Measure(name="return_rate", type="ratio", numerator="orders.returns", denominator="orders.order_count"),
            Measure(name="mtd_revenue", type="cumulative", expr="orders.revenue", grain_to_date="month"),
            Measure(name="qtd_revenue", type="cumulative", expr="orders.revenue", grain_to_date="quarter"),
            Measure(name="ytd_revenue", type="cumulative", expr="orders.revenue", grain_to_date="year"),
        ],
        joins=[Join(name="customers", type="belongs_to", foreign_key="customer_id")],
    )

    customers_model = Model(
        name="customers",
        table="customers",
        primary_key="id",
        dimensions=[
            Dimension(name="tier", type="categorical", expr="tier"),
            Dimension(name="region", type="categorical", expr="region"),
        ],
        joins=[Join(name="region_map", type="belongs_to", foreign_key="region")],
    )

    region_map_model = Model(
        name="region_map",
        table="region_map",
        primary_key="region",
        dimensions=[Dimension(name="region_group", type="categorical", expr="region_group")],
    )

    graph.add_model(orders_model)
    graph.add_model(customers_model)
    graph.add_model(region_map_model)

    generator = SQLGenerator(graph, dialect="duckdb")
    return graph, generator


def key(status: str, region: str, category: str, tier: str) -> str:
    return f"status={status}|region={region}|category={category}|tier={tier}"


def main() -> None:
    _, generator = build_graph()

    statuses = ["all", "completed", "pending", "cancelled", "shipped", "returned"]
    regions = ["all", "US", "EU", "APAC"]
    categories = ["all", "electronics", "apparel", "home"]
    tiers = ["all", "premium", "standard"]

    metrics_sel = ["revenue", "order_count", "avg_order_value", "mtd_revenue"]

    out: dict[str, str] = {}
    for s in statuses:
        for r in regions:
            for c in categories:
                for t in tiers:
                    dims = ["orders.order_date__month"]
                    if s != "all":
                        dims.append("orders.status")
                    if r != "all":
                        dims.append("orders.region")
                    if c != "all":
                        dims.append("orders.category")
                    if t != "all":
                        dims.append("customers.tier")

                    filters = []
                    if s != "all":
                        filters.append(f"orders.status = '{s}'")
                    if r != "all":
                        filters.append(f"orders.region = '{r}'")
                    if c != "all":
                        filters.append(f"orders.category = '{c}'")
                    if t != "all":
                        filters.append(f"customers.tier = '{t}'")

                    sql = generator.generate(
                        metrics=metrics_sel,
                        dimensions=dims,
                        filters=filters,
                        order_by=["orders.order_date__month"],
                        limit=200,
                    )
                    out[key(s, r, c, t)] = sql

    Path("docs/assets").mkdir(parents=True, exist_ok=True)
    Path("docs/assets/compiled_sql.json").write_text(json.dumps(out))
    print(f"Wrote docs/assets/compiled_sql.json with {len(out)} entries")


if __name__ == "__main__":
    main()


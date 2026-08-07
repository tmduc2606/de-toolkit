def data_transformations(data):
    """Apply functional transformations (filter, map, aggregate) to a dataset.

    DE reframing of functional programming patterns: given a list of records,
    filter to completed orders, project (map) to a derived "total" field, and
    aggregate a grand total via a generator expression.

    In a data engineering context, this mirrors the filter -> project ->
    aggregate pipeline common in transformation jobs.

    Args:
        data: A list of dicts with keys "quantity" and "unit_price".

    Returns:
        A dict with "valid_records", "transformed" (list of dicts with
        "item_id" and "total"), and "grand_total" (aggregate).
    """
    valid = [r for r in data if r is not None and r["quantity"] > 0]
    transformed = [
        {"item_id": r.get("item_id"), "total": r["quantity"] * r["unit_price"]}
        for r in valid
    ]
    grand_total = sum(row["total"] for row in transformed)
    return {"valid_records": valid, "transformed": transformed, "grand_total": grand_total}
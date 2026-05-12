from .extractor import extract_job

MODELS = ["gemini-2.5-flash-lite", "gemini-2.5-flash"]

def run_comparison(raw_text: str) -> dict:
    results = []
    for model in MODELS:
        try:
            out = extract_job(raw_text, model)
            results.append(out)
        except Exception as e:
            results.append({"model": model, "error": str(e)})

    return {
        "results": results,
        "summary": build_summary(results),
    }

def build_summary(results: list) -> dict:
    valid = [r for r in results if "result" in r]
    return {
        "total_cost_usd": sum(r["cost_usd"] for r in valid),
        "fastest_model": min(valid, key=lambda r: r["latency_ms"])["model"] if valid else None,
        "cheapest_model": min(valid, key=lambda r: r["cost_usd"])["model"] if valid else None,
        "model_costs": {r["model"]: r["cost_usd"] for r in valid},
        "model_latencies_ms": {r["model"]: r["latency_ms"] for r in valid},
    }
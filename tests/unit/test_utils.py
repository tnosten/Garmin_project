from src.analysis.query_duckdb_garmin import best_efforts  # Example import

def test_best_efforts():
    assert not best_efforts.empty, "Best efforts dataframe should not be empty"
    assert "best_effort" in best_efforts.columns, "Missing 'best_effort' column"
    assert "time" in best_efforts.columns, "Missing 'time' column"

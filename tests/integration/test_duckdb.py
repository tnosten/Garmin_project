import duckdb


@pytest.fixture
def setup_duckdb():
    conn = duckdb.connect(":memory:")  # In-memory DB for testing
    conn.execute("CREATE TABLE activities (activity_name STRING, fastest_split_1000 FLOAT)")
    conn.execute("INSERT INTO activities VALUES ('Morning Run', 200.5)")
    yield conn
    conn.close()

def test_query_fastest_split(setup_duckdb):
    conn = setup_duckdb
    result = conn.execute("SELECT MAX(fastest_split_1000) FROM activities").fetchone()
    assert result[0] == 200.5, "Query result is incorrect"

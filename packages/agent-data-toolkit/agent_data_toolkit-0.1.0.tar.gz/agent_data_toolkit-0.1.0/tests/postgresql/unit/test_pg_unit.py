def test_connect_and_select_one_unit(client):
    rows = client.query_rows("SELECT 1 AS ok")
    assert rows and rows[0]["ok"] == 1

import pyjsta

def test_rrep():
    res = pyjsta.rrep(["a", "b"], 3)
    assert len(res) == 6

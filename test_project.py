import project

def test_load_items(monkeypatch):
    monkeypatch.setattr(project, "FILE_NAME", "file_that_does_not_exist.json")
    assert project.load_items() == []


def test_save_items(tmp_path, monkeypatch):
    file_path = tmp_path / "test_items.json"
    monkeypatch.setattr(project, "FILE_NAME", file_path)

    items = [
        {
            "id": 1,
            "type": "lost",
            "name": "Iphone 17",
            "category": "Electronics",
            "color": "Black",
            "location": "Library",
            "date": "2026-08-31",
            "description": "Black iphone",
            "status": "open"
        }
    ]

    project.save_items(items)

    assert project.load_items() == items


def test_get_next_id():
    items = [
        {"id": 1},
        {"id": 2},
        {"id": 6},
    ]

    assert project.get_next_id(items) == 7


def test_calculate_match_score():
    lost = {
        "name": "Blue pen",
        "category": "Books & Stationery",
        "color": "Blue",
        "location": "Classroom"
    }

    found = {
        "name": "blue pen",
        "category": "Books & Stationery",
        "color": "blue",
        "location": "Classroom"
    }

    assert project.calculate_match_score(lost, found) == 4


def test_calculate_match_score_partial():
    lost = {
        "name": "Tennis racquet",
        "category": "Sports & Recreation",
        "color": "Green",
        "location": "Sports Centre"
    }

    found = {
        "name": "Badminton racquet",
        "category": "Sports & Recreation",
        "color": "blue",
        "location": "Sports Centre"
    }

    assert project.calculate_match_score(lost, found) == 2

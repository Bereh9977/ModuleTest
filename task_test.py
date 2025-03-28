import pytest
from task import read_and_sort_population_data, print_sorted_data

@pytest.fixture
def sample_data_file(tmp_path):
    data = """Ukraine, 603548, 41000000
                Canada, 9984670, 38000000
                Japan, 377975, 125000000
                Brazil, 8515767, 214000000"""
    file_path = tmp_path / "data.txt"
    file_path.write_text(data, encoding='utf-8')
    return str(file_path)

@pytest.mark.parametrize("data, expected_area_order, expected_pop_order", [
    # Тест 1: Дві країни
    (
        "Ukraine, 603548, 41000000\nJapan, 377975, 125000000",
        ["Ukraine", "Japan"],
        ["Japan", "Ukraine"]
    ),
    # Тест 2: Одна країна
    (
        "Brazil, 8515767, 214000000",
        ["Brazil"],
        ["Brazil"]
    ),
    # Тест 3: Три країни з однаковою площею
    (
        "A, 1000, 100\nB, 1000, 200\nC, 1000, 300",
        ["A", "B", "C"],  
        ["C", "B", "A"]
    )
])

def test_read_and_sort_population_data_parametrized(tmp_path, data, expected_area_order, expected_pop_order):
    file_path = tmp_path / "param_test.txt"
    file_path.write_text(data, encoding='utf-8')
    
    sorted_by_area, sorted_by_population = read_and_sort_population_data(str(file_path))
    
    # Перевірка порядку за площею
    area_names = [country['name'] for country in sorted_by_area]
    if len(expected_area_order) > 1:  # Якщо більше однієї країни, перевіряємо порядок
        assert area_names == expected_area_order or all(sorted_by_area[i]['area'] >= sorted_by_area[i+1]['area'] for i in range(len(sorted_by_area)-1))
    else:
        assert area_names == expected_area_order
    
    # Перевірка порядку за населенням
    pop_names = [country['name'] for country in sorted_by_population]
    assert pop_names == expected_pop_order
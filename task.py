def read_and_sort_population_data(filename):
    countries = []
    
    with open(filename, 'r', encoding='utf-8') as file:
            print(f"Файл {filename} успішно відкрито")
            for line in file:
                name, area, population = line.strip().split(',')
                countries.append({
                    'name': name.strip(),
                    'area': float(area.strip()),
                    'population': int(population.strip())
                })
            print(f"Прочитано {len(countries)} країн")
    
    sorted_by_area = sorted(countries, key=lambda x: x['area'], reverse=True)
    sorted_by_population = sorted(countries, key=lambda x: x['population'], reverse=True)
    
    return sorted_by_area, sorted_by_population
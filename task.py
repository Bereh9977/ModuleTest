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

def print_sorted_data(sorted_by_area, sorted_by_population):
    if sorted_by_area is None or sorted_by_population is None:
        print("Дані для виведення відсутні через помилку при читанні")
        return
    
    print("\nВідсортовано за площею (убування):")
    print("Назва країни | Площа (км²) | Населення")
    print("-" * 50)
    for country in sorted_by_area:
        print(f"{country['name']:<12} | {country['area']:>11.2f} | {country['population']:>11}")
    
    print("\nВідсортовано за населенням (убування):")
    print("Назва країни | Площа (км²) | Населення")
    print("-" * 50)
    for country in sorted_by_population:
        print(f"{country['name']:<12} | {country['area']:>11.2f} | {country['population']:>11}")

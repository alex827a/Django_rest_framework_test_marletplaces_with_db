import json
import random

def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def shuffle_reviews(data):
    all_reviews = []

    # Сбор всех отзывов в один список
    for item in data:
        for review in item['reviews']:
            all_reviews.append(review)

    # Перемешивание всех отзывов
    random.shuffle(all_reviews)

    # Распределение перемешанных отзывов обратно к товарам
    review_index = 0
    for item in data:
        num_reviews = len(item['reviews'])
        item['reviews'] = all_reviews[review_index:review_index + num_reviews]
        review_index += num_reviews
        
        # Рандомизация цены в пределах от 50 до 150
        item['price'] = round(random.uniform(50, 150), 2)

    return data

def main():
    input_file_path = 'products_and_reviews.json'
    output_file_path = 'products_and_review_mixed.json'

    data = load_json(input_file_path)
    shuffled_data = shuffle_reviews(data)
    save_json(shuffled_data, output_file_path)

if __name__ == "__main__":
    main()

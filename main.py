shopping_list={"piekarnia" : ["chleb","paczek","buleczki"],
"warzywniak":["marchew","seler","rukola","kolendra","ziemniaki"]}

total_item_count = 0
for store, items in shopping_list.items():
    items_as_str = ', '.join(items)
    print(f"Idę do {store.capitalize()}, kupuję tu następujące rzeczy: {items_as_str.title()}")
    total_item_count += len(items)
print(f"W sumie kupuję {total_item_count} produktów")
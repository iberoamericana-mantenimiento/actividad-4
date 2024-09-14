from no_numbers import NoNumbers
from all_in_lower import AllInLower
from to_list import ToList

def run(text):

    no_numbers_pipeline = NoNumbers()
    all_in_lower_pipeline = AllInLower()
    to_list_pipeline = ToList()

    text = no_numbers_pipeline.remove_numbers(text)
    print(f"Texto sin números: {text}")

    text = all_in_lower_pipeline.to_lower(text)
    print(f"Texto en minúsculas: {text}")

    text = to_list_pipeline.to_list(text)
    print(f"Texto convertido en lista: {text}")


input = input("Introduce un texto: ")
run(input)
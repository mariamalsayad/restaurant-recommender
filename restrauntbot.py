RESTAURANTS = {
    "Vonn's": {
        "cuisine": "fast food",
        "dishes": ["burgers", "cheesesteak", "nashville fried chicken"],
        "spicy": ["mild", "spicy"],
        "locations": ["vancouver"],
        "settings": ["indoors", "outdoors"],
        "note": "You MUST try their cheesesteak!",
    },
    "KFC": {
        "cuisine": "fast food",
        "dishes": ["fried chicken", "poutine"],
        "spicy": ["mild", "spicy"],
        "locations": ["vancouver", "richmond"],
        "settings": ["indoors", "outdoors"],
        "note": "Simple yet delicious fried chicken buckets.",
    },
    "Paramount": {
        "cuisine": "lebanese",
        "dishes": ["shish tawook", "mixed grill", "beef skewers", "kofta"],
        "spicy": ["mild", "spicy"],
        "locations": ["vancouver"],
        "settings": ["indoors"],
        "note": "Exceptional seasonings of Lebanese cuisine.",
    },
    "Uncle Sal's Shawarma": {
        "cuisine": "lebanese",
        "dishes": ["chicken shawarma", "beef shawarma"],
        "spicy": ["mild", "spicy"],
        "locations": ["richmond"],
        "settings": ["indoors"],
        "note": "You MUST try their chicken shawarma plate!",
    },
    "Spaghetti Factory": {
        "cuisine": "italian",
        "dishes": ["manicotti", "penne with chicken", "steamed mussels", "pesto penne", "calamari fritti"],
        "spicy": ["mild", "spicy"],
        "locations": ["vancouver", "richmond"],
        "settings": ["indoors", "outdoors"],
        "note": "Amazing spaghetti and a cozy, homely Italian dining experience.",
    },
    "Sushi Mura": {
        "cuisine": "japanese",
        "dishes": ["sushi", "seafood udon", "sashimi rolls", "shrimp tempura", "salmon gamma"],
        "spicy": ["mild", "spicy"],
        "locations": ["vancouver", "richmond"],
        "settings": ["indoors"],
        "note": "Fresh and melt-in-your-mouth sushi.",
    },
    "Karakoram": {
        "cuisine": "indian",
        "dishes": ["chicken biryani", "lamb biryani", "butter chicken", "lamb buhna", "gulabjamun"],
        "spicy": ["spicy"],
        "locations": ["vancouver"],
        "settings": ["indoors"],
        "note": "Rich flavours and spices of Indian dishes. You must try their Gulabjamun dessert!",
    },
    "Swad Indian Kitchen": {
        "cuisine": "indian",
        "dishes": ["tandoori roti", "chicken tikka", "samosa"],
        "spicy": ["spicy"],
        "locations": ["vancouver"],
        "settings": ["indoors"],
        "note": "Comfy and friendly seating with authentic Indian flavours.",
    },
}

CUISINE_OPTIONS = {
    "a": "fast food",
    "b": "lebanese",
    "c": "italian",
    "d": "japanese",
    "e": "indian",
}

SPICY_OPTIONS = {
    "a": "spicy",
    "b": "mild",
}

LOCATION_OPTIONS = {
    "a": "vancouver",
    "b": "richmond",
}

SETTING_OPTIONS = {
    "a": "outdoors",
    "b": "indoors",
}


def prompt_choice(question: str, options: dict) -> str:
   
    choices_display = "\n".join(f"  {k}) {v}" for k, v in options.items())
    while True:
        answer = input(f"{question}\n{choices_display}\n> ").strip().lower()
        if answer in options:
            return options[answer]
        valid = ", ".join(options.keys())
        print(f"  Invalid choice. Please enter one of: {valid}\n")


def prompt_dish(available_dishes: list[str]) -> str:
    """Show the available dishes and prompt until the user picks a valid one."""
    print("\nAvailable dishes:")
    for dish in available_dishes:
        print(f"  - {dish}")
    while True:
        answer = input("Enter your favourite dish from the list above:\n> ").strip().lower()
        if answer in available_dishes:
            return answer
        print("  That dish isn't on the list. Please try again.\n")


def get_dishes_for_cuisine(cuisine: str) -> list[str]:
    """Collect all unique dishes offered by restaurants of the chosen cuisine."""
    dishes = []
    for restaurant in RESTAURANTS.values():
        if restaurant["cuisine"] == cuisine:
            for dish in restaurant["dishes"]:
                if dish not in dishes:
                    dishes.append(dish)
    return dishes


def find_restaurants(cuisine: str, dish: str, spicy: str, location: str, setting: str) -> list[tuple[str, dict]]:
    """Return all restaurants that match every user preference."""
    matches = []
    for name, info in RESTAURANTS.items():
        if (
            info["cuisine"] == cuisine
            and dish in info["dishes"]
            and spicy in info["spicy"]
            and location in info["locations"]
            and setting in info["settings"]
        ):
            matches.append((name, info))
    return matches


def recommend():
    cuisine = prompt_choice(
        "What is your favourite type of cuisine?",
        CUISINE_OPTIONS,
    )

    available_dishes = get_dishes_for_cuisine(cuisine)
    if not available_dishes:
        print("Sorry, no dishes found for that cuisine. Please restart and try again.")
        return

    dish = prompt_dish(available_dishes)

    spicy = prompt_choice("How do you like your food?", SPICY_OPTIONS)
    location = prompt_choice("Which city would you like to eat in?", LOCATION_OPTIONS)
    setting = prompt_choice("Do you prefer eating indoors or outdoors?", SETTING_OPTIONS)

    matches = find_restaurants(cuisine, dish, spicy, location, setting)

    print()
    if matches:
        print(f"{'='*50}")
        print(f"  {'1 match' if len(matches) == 1 else f'{len(matches)} matches'} found!")
        print(f"{'='*50}")
        for name, info in matches:
            print(f"\n  Restaurant : {name}")
            print(f"  Tip        : {info['note']}")
        print()
    else:
        print("Sorry, no restaurant matches all your preferences.")
        print("Try adjusting your location, setting, or spice preference and run again.")


def main():
    print("=" * 50)
    print("   Welcome to the Restaurant Recommender!")
    print("=" * 50)

    while True:
        start = input("\nAnswer a few quick questions to find your ideal restaurant.\nType 'yes' to start or 'no' to exit:\n> ").strip().lower()
        if start == "yes":
            recommend()
            again = input("Would you like another recommendation? (yes/no)\n> ").strip().lower()
            if again != "yes":
                print("\nEnjoy your meal. Goodbye!")
                break
        elif start == "no":
            print("\nOk, bye!")
            break
        else:
            print("Please type 'yes' or 'no'.")


if __name__ == "__main__":
    main()
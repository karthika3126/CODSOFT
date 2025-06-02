import random
import string

def generate_password(name, food, place):
    # Remove any spaces from the name, food, and place, and convert them to lowercase
    name = name.replace(" ", "").lower()
    food = food.replace(" ", "").lower()
    place = place.replace(" ", "").lower()

    # Shuffle the characters of the name, food, and place
    shuffled_name = list(name)
    shuffled_food = list(food)
    shuffled_place = list(place)
    random.shuffle(shuffled_name)
    random.shuffle(shuffled_food)
    random.shuffle(shuffled_place)
    shuffled_name = ''.join(shuffled_name)
    shuffled_food = ''.join(shuffled_food)
    shuffled_place = ''.join(shuffled_place)

    # Define a set of special characters
    special_chars = "!@#$%^&*()_+=-{}[]|\:;<>,.?/~"

    # Choose 2 random special characters to include in the password
    random_special_chars = random.sample(special_chars, 2)

    # Calculate the maximum length of the shuffled name, food, and place
    max_length = 13 - len(random_special_chars)

    # Truncate the shuffled name, food, and place if necessary
    shuffled_name = shuffled_name[:max_length]
    shuffled_food = shuffled_food[:max_length]
    shuffled_place = shuffled_place[:max_length]

    # Create the password by combining the shuffled name, food, place, and special characters
    password = shuffled_name + shuffled_food + shuffled_place + ''.join(random_special_chars)

    return password

# Get the name, favorite food, and favorite place from the user
name = input("Enter your name: ")
food = input("Enter your favorite food: ")
place = input("Enter your favorite place: ")

# Generate the password
password = generate_password(name, food, place)
print("Your generated password is:", password)

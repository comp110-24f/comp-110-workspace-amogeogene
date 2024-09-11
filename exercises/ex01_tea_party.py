"""Planning a cozy tea party"""

__author__: str = "730766919"


def main_planner(guests: int) -> None:
    """Function is entrypoint of program and brings everything together"""
    print("A Cozy Tea Party for ", (guests), "People!")
    print("Tea Bags: ", +(tea_bags(guests)))
    print("Treats: ", (treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    "At first I was confused on the format of the concatenation"
    "I also forgot that the cost needed a $ symbol"
    "I needed to make sure the string for cost had both tea bags and treat function"


def tea_bags(people: int) -> int:
    """computing the teabags"""
    return people * 2


"I originally forgot to multiply the people by 2"
"At first I tried returning teabags for the computation"


def treats(people: int) -> int:
    """Computing the number of treats needed"""
    return int(tea_bags(people=people) * 1.5)


"I orginally forgot what a keyword argument was, so I had to relearn"
"I forgot to multiply by 1.5 at the end"


def cost(tea_count: int, treat_count: int) -> float:
    """computing the cost of the tea bags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75


"I needed a plus sign between tea_count and treat_count"
"I orginally tried returning people, but that was not in the parameters"

if __name__ == "__main__":
    main_planner(guests=int(input("How many guest are attending your tea party?")))

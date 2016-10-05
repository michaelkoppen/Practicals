#commit
def main():
    score = float(input("Enter score: "))
    returned_result = calculate_result(score)
    print(returned_result)


def calculate_result(score):
    if score < 0:
        result = "Invalid Score"
        return result
    elif score > 100:
        result = "Invalid Score"
        return result
    elif score >= 90:
        result = "Excellent"
        return result
    elif score >= 50:
        result = "Passable"
        return result
    else:
        result = "Bad"
        return result


main()
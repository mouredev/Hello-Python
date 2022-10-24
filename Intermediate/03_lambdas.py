# Clase en vídeo (19/10/22): https://www.twitch.tv/videos/1628654998

### Lambdas ###

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 4))

multiply_values = lambda first_value, second_value: first_value * second_value - 3
print(multiply_values(2, 4))

def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value

print(sum_three_values(5)(2, 4))
import copy
import random


# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []  # all colored balls will end up in this list
        for color in kwargs.items():
            for amount in range(color[1]):
                self.contents.append(color[0])

    def draw(self, draws):
        self.draw_list = []
        for _ in range(0, draws):
            try:
                random_index = random.randint(0, (len(self.contents) - 1))
                random_bal = self.contents[random_index]
                self.draw_list.append(random_bal)  # append the ball to our draw_list
                self.contents.pop(random_index)  # remove the ball from our hat
            except ValueError:  # all balls are aldready taken, return the draw_list with all balls
                return self.draw_list
        return self.draw_list  # not all balls where drawn, return the draw list


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """:param hat: A hat object containing balls that should be copied inside the function.
    :param expected_balls: An object indicating the exact group of balls to attempt to draw from the hat for the experiment.
    For example, to determine the probability of drawing 2 blue balls and 1 red ball from the hat, set expected_balls to
    {"blue":2, "red":1}.
    :param num_balls_drawn: The number of balls to draw out of the hat in each experiment.
    :param num_experiments: he number of experiments to perform.
    (The more experiments performed, the more accurate the approximate probability will be.)
    :return: The probability to draw expected_balls with num_balls_drawn"""
    probability = 0
    for experiment in range(0, num_experiments):
        draw_dict = dict()
        temp_hat = copy.deepcopy(hat)
        experiment_result = temp_hat.draw(num_balls_drawn)
        #print(experiment_result)
        for ball_color in experiment_result:
            draw_dict[ball_color] = draw_dict.get(ball_color, 0) + 1  # counts the amount of balls per color
        balls_found = True
        for ball_color in expected_balls:
            try:
                if expected_balls[ball_color] > draw_dict[ball_color]:
                    balls_found = False
            except KeyError:
                balls_found = False
        if balls_found:
            probability += 100
    probability = (probability / num_experiments) / 100
    return probability
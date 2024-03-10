from task_1 import logger


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]


@logger
def flat_generator(list_of_lists):

    for element in list_of_lists:
        for e in element:
            yield e


flat_generator(list_of_lists_1)

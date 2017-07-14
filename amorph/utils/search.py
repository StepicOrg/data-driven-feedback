from ..metrics import string_similarity


def find_closest(source, samples, metric=string_similarity):
    """
    Finds closest code to the source by finding minimum of metric
    :param source: Source code
    :param samples: Iterable of samples to search in
    :param metric: Two string arguments function measuring similarity between two codes
    :return: Closest to source sample
    """
    max_metric = None
    closest_sample = None
    for sample in samples:
        current_metric = metric(source, sample)
        if max_metric is None or current_metric > max_metric:
            max_metric = current_metric
            closest_sample = sample

    return closest_sample
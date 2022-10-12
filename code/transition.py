class Transition(object):
    """
    This class defines a set of transitions which are applied to a
    configuration to get the next configuration.
    """
    # Define set of transitions
    LEFT_ARC = 'LEFTARC'
    RIGHT_ARC = 'RIGHTARC'
    SHIFT = 'SHIFT'
    REDUCE = 'REDUCE'

    def __init__(self):
        raise ValueError('Do not construct this object!')

    @staticmethod
    def left_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """

        if not conf.buffer or not conf.stack:
            return -1

        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer.pop(0)

        if idx_wi == 0:
            return -1

        if len(filter(lambda hd: idx_wi == hd[1], conf.arcs)) > 0:
            return -1

        conf.arcs.append((idx_wj, relation, idx_wi))

    @staticmethod
    def right_arc(conf, relation):
        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        if not conf.buffer or not conf.stack:
            return -1

        # You get this one for free! Use it as an example.

        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer.pop(0)

        conf.stack.append(idx_wj)
        conf.arcs.append((idx_wi, relation, idx_wj))

    @staticmethod
    def reduce(conf):
        idx_wi = conf.stack[-1]
        idx_wj = conf.buffer.pop(0)

        if not conf.stack:
            return -1

        for bi in range(idx_wj, len(conf.sentence) + 1):
            if bi in gold_conf.heads and gold_conf.heads[bi] == idx_wi:
                return -1

        """
            :param configuration: is the current configuration
            :return : A new configuration or -1 if the pre-condition is not satisfied
        """
        conf.buffer.pop(0)

    @staticmethod
    def shift(conf):

        if not conf.buffer:
            return -1

        next_one = conf.buffer[0]
        conf.stack.append(next_one)
        conf.buffer.pop(0)
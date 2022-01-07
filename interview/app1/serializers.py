from rest_framework import serializers


class SolutionSerializer(serializers.Serializer):
    A = serializers.ListField(child=serializers.IntegerField(min_value=1, max_value=100000))
    X = serializers.IntegerField(min_value=1, max_value=100000)
    time_req = serializers.SerializerMethodField(method_name='solution')

    def solution(self, obj):
        A = obj['A']
        X = obj['X']
        if X not in A:
            return -1

        s_given_steps = set(A)
        s_con_steps = set(range(1, X + 1))
        sd = s_con_steps - s_given_steps
        if len(sd) > 0:
            return -1

        if X in A:
            # i = A.index(X)
            d = {}
            for time_sec, leaf_position in enumerate(A):
                if leaf_position not in d and leaf_position <= X:
                    d[leaf_position] = time_sec

            return max(d.values())

    def validate(self, data):
        extra = [i for i in set(data['A']) if i not in range(1, data['X']+1)]
        if len(extra) > 0:
            raise serializers.ValidationError("each element of array A is an integer within the range [1..X]")
        return data


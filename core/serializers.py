from rest_framework import serializers


class OperationSerializer(serializers.Serializer):
    operator = serializers.ChoiceField(choices=["+", "-", "*", "/"],
                                       error_messages={"invalid_choice": "Unsupported operator"})
    operand_one = serializers.IntegerField()
    operand_two = serializers.IntegerField()

    def validate(self, data):
        if data["operator"] == "/" and data["operand_two"] == 0:
            raise serializers.ValidationError("Division by zero is not allowed")
        return data


class ResultSerializer(serializers.Serializer):
    result = serializers.IntegerField()

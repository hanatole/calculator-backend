from core.serializers import OperationSerializer, ResultSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def calculate(request):
    serializer = OperationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    result = eval(
        f"{serializer.validated_data['operand_one']} {serializer.validated_data['operator']} {serializer.validated_data['operand_two']}")

    response = ResultSerializer({"result": int(result)})
    return Response(response.data, status=200)

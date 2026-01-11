from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.serializers import OperationSerializer, ResultSerializer


@api_view(["GET"])
def health_check(request):
    return Response({"status": "ok"}, status=200)


@api_view(["POST"])
def calculate(request):
    serializer = OperationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    result = eval(
        f"{serializer.validated_data['operand_one']} {serializer.validated_data['operator']} {serializer.validated_data['operand_two']}")

    response = ResultSerializer({"result": int(result)})
    return Response(response.data, status=200)

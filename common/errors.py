from rest_framework.response import Response
from rest_framework import status

class CustomResponse:
    @staticmethod
    def success(data, msg):
        return Response({
            'success': True,
            'data': data,
            'status_code': 200,
            'msg': msg
    })

    @staticmethod
    def error(data, err_code, msg):
        return Response({
            'success': False,
            'err_code': err_code,
            'msg': msg
        })
    
    
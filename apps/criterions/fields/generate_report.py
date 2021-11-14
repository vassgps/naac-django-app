# Criterion/Generate_reports.py
import os
import wget
from django.http import HttpResponse
from ..templatetags.utils import render_to_pdf
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_exempt
from django.contrib.auth.decorators import login_required
from PyPDF2 import PdfFileMerger
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import CriterionMaster
from ..serializers import ReportSerializer

# Define media URL as Global scope
media_root = settings.MEDIA_ROOT
media_url = str(settings.BASE_URL) + '/media/'
s3_status = settings.USE_S3


# Generate PDF file with all Images attached (Word/Excel/CSV Included)
def generatePdfMedia(request, **kwargs):
    criterion = kwargs.pop('criterion')
    text = kwargs.pop('text')
    filters = kwargs.pop('filters')

    object_list = CriterionMaster.objects.filter(filters).order_by('user')
    context = {'object_list': object_list, 'media_url': media_url, 's3_status': s3_status}
    if text:
        responce = render_to_pdf('criteria/text-media.html', context)
        response = HttpResponse(responce, content_type='application/pdf')
        return response
    else:
        responce = render_to_pdf('criteria/notext-media.html', context)
        response = HttpResponse(responce, content_type='application/pdf')
        return response


# Merge PDF files without Text - API
@xframe_options_exempt
def mergePdf(request, **kwargs):
    criterion = kwargs.pop('criterion')
    filters = kwargs.pop('filters')
    object_list = CriterionMaster.objects.filter(filters).order_by('user')
    pdfs = []
    # Check all files in the queryset, for getting PDF files
    for obj in object_list:
        if obj.file1:
            filename = str(obj.file1)
            if filename.lower().endswith('.pdf'):
                if s3_status:
                    pdfs.append(obj.file1.url)  # Append pdf files to the list
                else:
                    pdfs.append(obj.file1.path)
        if obj.file2:
            filename = str(obj.file2)
            if filename.lower().endswith('.pdf'):
                if s3_status:
                    pdfs.append(obj.file2.url)  # Append pdf files to the list
                else:
                    pdfs.append(obj.file2.path)
        if obj.file3:
            filename = str(obj.file3)
            if filename.lower().endswith('.pdf'):
                if s3_status:
                    pdfs.append(obj.file3.url)  # Append pdf files to the list
                else:
                    pdfs.append(obj.file3.path)

    # Merge all Pdf files in the list
    merger = PdfFileMerger()
    file_name = str(criterion) + "-result.pdf"
    if s3_status:
        for pdf in pdfs:
            temp_file = wget.download(str(pdf), media_root)
            merger.append(temp_file)
            # if os.path.exists(temp_file):
            #     os.remove(temp_file)
        merger.write(media_root + file_name)
        merger.close()
    else:
        for pdf in pdfs:
            merger.append(pdf)
        merger.write(media_root + file_name)
        merger.close()

    with open(media_root + file_name, 'rb') as pdffile:
        response = HttpResponse(pdffile.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; {file_name}'
        pdffile.close()
        os.remove(media_root + file_name)
        return response


# Testing with REST API
class ReportList(APIView):
    def get(self, request):
        # fetch all data's
        objects = CriterionMaster.objects.all()
        serializer = ReportSerializer(objects, many=True)

        # Fetch keys only
        key_dict = ReportSerializer(objects).data
        column_names = []
        fields = key_dict.keys()
        for obj in fields:
            column_names.append({"data": obj})
        # Return API response
        api_data = {'column_name': column_names, 'table_data': serializer.data}
        print(column_names)
        return Response(api_data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ReportSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

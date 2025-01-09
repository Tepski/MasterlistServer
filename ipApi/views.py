from . models import IPCategory
from . serializers import IPCategorySrlzr
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

filterList = ["ar_no", "ar_category", "area", "abnormality", "nature_of_abnormality", "affected_item"]

def check_occurence(data, list):
    data1 = [data[i] for i in filterList]
    data2 = [[x[j] for j in filterList] for x in list]
    if len(data2) == 1:
        return None
    for item in reversed(data2[:-1]):

        if data1[1:] == item[1:]:
            if item[0].count("-") == 1:
                new_id = f"{item[0]}-001"
                return new_id
            else:
                id_inc = str(int(item[0].split("-")[-1]) + 1)
                while len(id_inc) != 3:
                    id_inc = "0" + id_inc
                split_data = item[0].split("-")
                new_id = split_data[0] + "-" + split_data[1] + "-" + id_inc
                return new_id
    return None

def generate_car_no(list):
    count = 0
    for i in list:
        print(i['car_no'])
        if i["car_no"] != None:
            count += 1
        print(count)
    str_count = str(count)
    while len(str_count) != 5:
        str_count = "0" + str_count
    car_no = f"CARIPT25-{str_count}"
    return car_no

def get_non_occurence_count(items):
    list = [x['ar_no'] for x in items if x['ar_no'].count("-") == 1]

    if len(list) == 0:
        return 0

    count = int(list[-1].split("-")[1])
    print(count)
    return count + 1
        
@api_view(["GET"])
def get_values(request):
    category = IPCategory.objects.all()
    srlzr = IPCategorySrlzr(category, many=True)
    
    return Response(srlzr.data)

@api_view(["POST"])
def set_values(request):
    srlzr = IPCategorySrlzr(data=request.data)
    if srlzr.is_valid():
        srlzr.save()

        category = IPCategory.objects.all()
        cat = IPCategorySrlzr(category, many=True)

        srlzr.instance.link = f"{srlzr.instance.id}"

        if srlzr.instance.self_resolve_for_car == "FOR CAR":
            srlzr.instance.car_no = generate_car_no(cat.data)

        reoccurrence_id = check_occurence(srlzr.data, cat.data)
        if reoccurrence_id:
            srlzr.instance.ar_no = f"{reoccurrence_id}"
        else:
            str_count = str(get_non_occurence_count(cat.data))
            while len(str_count) != 5:
                str_count = "0" + str_count
            srlzr.instance.ar_no = f"ARIP25-{str_count}"

        srlzr.instance.save()

        update_instance = IPCategorySrlzr(srlzr.instance)
        return Response(update_instance.data, status=status.HTTP_201_CREATED)
    else:
        return Response(srlzr.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["DELETE"])
def delete_value(request, pk):
    try:
        data = IPCategory.objects.get(pk=pk)
    except IPCategory.DoesNotExist:
        return Response({"message": "Error deleting, does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    data.delete()
    return Response({"Message": "Item deleted Succesfully"}, status=status.HTTP_204_NO_CONTENT)

@api_view(["PUT"])
def edit_value(request, pk):
    try:
        category = IPCategory.objects.get(id=int(pk))

    except IPCategory.DoesNotExist:
        return Response({"Error": "The Category does not exist"}, status=status.HTTP_404_NOT_FOUND)
    
    srlzr = IPCategorySrlzr(category, data=request.data, partial=True)
    if srlzr.is_valid():
        srlzr.save()
        return Response(srlzr.data, status=status.HTTP_200_OK)
    return Response(srlzr.errors, status=status.HTTP_400_BAD_REQUEST)
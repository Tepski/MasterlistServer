from django.db import models
class Category(models.Model):

    intChoices = {
        "One": 1,
        "Two": 2
    }

    areaContent = ["20CY", "21MY", "CT1", "CT2", "CT3", "CT4", "OT", "PNT", "PZT", "WH", "IQC", "OQC"]
    areaChoices = {item: item for item in areaContent}

    CARContent = ["FOR CAR", "SELF RESOLVE"]
    CAR = {car: car for car in CARContent}

    statusContent = [
        "CAR CREATION",
        "UNDER REVIEW",
        "APPROVED",
        "IMPLEMENTATION",
        "VALIDATION",
        "OPEN",
        "CLOSED",
    ]
    statusChoices = {status: status for status in statusContent}

    link = models.CharField(max_length=255, blank=True)
    ar_no = models.CharField(max_length=100, blank=True)
    car_no = models.CharField(max_length=20,  blank=True, null=True)
    area = models.CharField(max_length=5, choices=areaChoices)
    ar_category = models.CharField(max_length=255)
    abnormality = models.CharField(max_length= 120)
    nature_of_abnormality = models.CharField(max_length=400, blank=True, default=None)
    affected_item = models.CharField(max_length=500, blank=True)
    level = models.CharField(max_length=3, choices=intChoices, default="One")
    created = models.CharField(max_length=10, null=True, blank=True)
    detection_process = models.CharField(max_length=500, null=True, blank=True)
    function = models.CharField(max_length=10, null=True, blank=True)
    incharge = models.CharField(max_length=255, null=True, blank=True)
    self_resolve_for_car = models.CharField(max_length=12, choices=CAR)
    status = models.CharField(max_length=14, choices=statusChoices)
    countermeasure = models.CharField(max_length=255, null=True, blank=True)
    fanout = models.BooleanField(default=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.ar_no != None:
            return self.ar_no
        return self.ar_category